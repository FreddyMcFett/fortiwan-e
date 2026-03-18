#!/usr/bin/env python3
"""FortiWAN-E - Web-based WAN Emulator for Fabric Studio SD-WAN demos."""

import urllib3
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import requests as http_requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
app.secret_key = "fortiwane-secret-key-change-in-production"
CORS(app)


class FabricStudioAPI:
    """Client for Fabric Studio REST API."""

    def __init__(self, host, username="admin", password="", verify_ssl=False):
        self.base_url = f"https://{host}"
        self.verify_ssl = verify_ssl
        self.session = http_requests.Session()
        self.session.verify = verify_ssl
        self.csrf_token = None
        self.username = username
        self.password = password

    def login(self):
        """Authenticate and obtain session + CSRF tokens."""
        self.session.get(f"{self.base_url}/api/v1/session/check")
        self._update_csrf()
        resp = self.session.post(
            f"{self.base_url}/api/v1/session/open",
            json={"username": self.username, "password": self.password},
            headers=self._headers(),
        )
        resp.raise_for_status()
        data = resp.json()
        if data.get("status") == "error":
            raise Exception(f"Login failed: {data.get('errors', {})}")
        self._update_csrf()
        return data

    def _update_csrf(self):
        """Extract CSRF token from cookies."""
        for name, value in self.session.cookies.items():
            if name == "fortipoc-csrftoken":
                self.csrf_token = value
                break
            if "csrftoken" in name:
                self.csrf_token = value

    def _headers(self):
        """Build request headers with CSRF token."""
        headers = {"Referer": f"{self.base_url}/"}
        if self.csrf_token:
            headers["X-FortiPoC-CSRFToken"] = self.csrf_token
        return headers

    def get(self, endpoint, params=None):
        """GET request to API. params can be a list of tuples for repeated keys."""
        resp = self.session.get(
            f"{self.base_url}/api/v1/{endpoint}",
            params=params,
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()

    def post(self, endpoint, data=None):
        """POST request to API."""
        resp = self.session.post(
            f"{self.base_url}/api/v1/{endpoint}",
            json=data,
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()

    def patch(self, endpoint, data=None):
        """PATCH request to API."""
        resp = self.session.patch(
            f"{self.base_url}/api/v1/{endpoint}",
            json=data,
            headers=self._headers(),
        )
        resp.raise_for_status()
        return resp.json()

    def get_fabrics(self):
        """List all fabrics."""
        return self.get("model/fabric")

    def get_routers(self, fabric_id=None):
        """Get routers with ports, optionally filtered by fabric."""
        params = [
            ("related_fields", "ports"),
            ("related_fields", "ports.cable"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/router", params)

    def get_router_ports(self, router_id):
        """Get ports for a specific router, trying multiple API approaches."""
        errors = []

        # Approach 1: Query routerport model directly
        try:
            result = self.get("model/router/port", [("select", f"device={router_id}")])
            objs = result.get("object", [])
            if isinstance(objs, dict):
                objs = [objs]
            if objs:
                return result
        except Exception as e:
            errors.append(f"routerport: {e}")

        # Approach 2: Query router with related_fields=ports, extract from others
        try:
            result = self.get("model/router", [
                ("select", f"id={router_id}"),
                ("related_fields", "ports"),
            ])
            devices = _extract_devices(result, "router", "routerport")
            if devices and devices[0].get("ports"):
                return {"status": "done", "object": devices[0]["ports"]}
        except Exception as e:
            errors.append(f"router+related: {e}")

        # Nothing worked — return empty with error context
        raise Exception(f"Could not fetch ports for router {router_id}. Tried: {'; '.join(errors)}")

    def get_switches(self, fabric_id=None):
        """Get switches with ports, optionally filtered by fabric."""
        params = [
            ("related_fields", "ports"),
            ("related_fields", "ports.cable"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/switch", params)

    def get_vms(self, fabric_id=None):
        """Get VMs with ports, optionally filtered by fabric."""
        params = [
            ("related_fields", "ports"),
            ("related_fields", "ports.cable"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/vm", params)

    def get_switch_ports(self, switch_id):
        """Get ports for a specific switch."""
        try:
            result = self.get("model/switch/port", [("select", f"device={switch_id}")])
            objs = result.get("object", [])
            if isinstance(objs, dict):
                objs = [objs]
            if objs:
                return result
        except Exception:
            pass
        # Fallback: query switch with related-fields
        try:
            result = self.get("model/switch", [
                ("select", f"id={switch_id}"),
                ("related_fields", "ports"),
            ])
            devices = _extract_devices(result, "switch", "switchport")
            if devices and devices[0].get("ports"):
                return {"status": "done", "object": devices[0]["ports"]}
        except Exception:
            pass
        raise Exception(f"Could not fetch ports for switch {switch_id}")

    def get_vm_ports(self, vm_id):
        """Get ports for a specific VM."""
        try:
            result = self.get("model/vm/port", [("select", f"device={vm_id}")])
            objs = result.get("object", [])
            if isinstance(objs, dict):
                objs = [objs]
            if objs:
                return result
        except Exception:
            pass
        # Fallback: query vm with related-fields
        try:
            result = self.get("model/vm", [
                ("select", f"id={vm_id}"),
                ("related_fields", "ports"),
            ])
            devices = _extract_devices(result, "vm", "vmport")
            if devices and devices[0].get("ports"):
                return {"status": "done", "object": devices[0]["ports"]}
        except Exception:
            pass
        raise Exception(f"Could not fetch ports for VM {vm_id}")

    def update_router(self, router_id, data):
        """Update router properties via PATCH."""
        payload = {
            "object": {"id": router_id, **data},
            "update_fields": ",".join(data.keys()),
            "related_fields": [],
        }
        return self.patch(f"model/router/{router_id}", payload)

    def get_tc_for_port(self, fabric_id, device_id, port_id):
        """Get the traffic control object for a specific port.

        Uses the fabric-scoped endpoint:
        GET /api/v1/model/fabric/{fabric}/device/{device}/port/{port}/tc
        """
        try:
            result = self.get(f"model/fabric/{fabric_id}/device/{device_id}/port/{port_id}/tc")
            obj = result.get("object")
            if isinstance(obj, dict) and "id" in obj:
                return obj
            if isinstance(obj, list) and obj:
                return obj[0]
        except Exception:
            pass
        return None

    def update_tc(self, tc_id, data, fabric_id, device_id, port_id):
        """Update a traffic control object.

        Uses the fabric-scoped endpoint:
        PATCH /api/v1/model/fabric/{fabric}/device/{device}/port/{port}/tc
        """
        obj = {"id": tc_id}
        obj.update(data)
        update_fields = ",".join(data.keys())
        payload = {
            "object": obj,
            "update_fields": update_fields,
            "related_fields": [],
        }
        return self.patch(
            f"model/fabric/{fabric_id}/device/{device_id}/port/{port_id}/tc",
            payload,
        )

    def sync_tc(self, device_id, port_id):
        """Sync runtime traffic control from the model values."""
        return self.post(f"runtime/device/{device_id}/port/{port_id}/tc:sync")

    def force_tc(self, device_id, port_id):
        """Reapply traffic control on a port via the runtime endpoint."""
        return self.post(f"runtime/device/{device_id}/port/{port_id}/tc:force")


# Global API client store
api_clients = {}


def get_api_client():
    """Get or create API client from session config."""
    config = session.get("fs_config")
    if not config:
        return None
    key = f"{config['host']}:{config['username']}"
    if key not in api_clients:
        client = FabricStudioAPI(
            config["host"], config["username"], config["password"]
        )
        client.login()
        api_clients[key] = client
    return api_clients[key]


# --- TC Command Builder ---

def build_tc_commands(interface, params):
    """Build tc (traffic control) commands for WAN emulation."""
    commands = []
    commands.append(f"tc qdisc del dev {interface} root 2>/dev/null || true")

    has_netem = any(
        params.get(k)
        for k in ["delay_ms", "jitter_ms", "loss_percent", "corrupt_percent",
                   "duplicate_percent", "reorder_percent"]
    )
    has_bw = params.get("bandwidth_kbit")

    if not has_netem and not has_bw:
        return commands

    if has_netem and has_bw:
        bw = int(params["bandwidth_kbit"])
        commands.append(
            f"tc qdisc add dev {interface} root handle 1: tbf"
            f" rate {bw}kbit burst {max(bw // 8, 1)}kb latency 50ms"
        )
        netem_cmd = f"tc qdisc add dev {interface} parent 1:1 handle 10: netem"
        netem_cmd += _netem_params(params)
        commands.append(netem_cmd)
    elif has_netem:
        netem_cmd = f"tc qdisc add dev {interface} root netem"
        netem_cmd += _netem_params(params)
        commands.append(netem_cmd)
    elif has_bw:
        bw = int(params["bandwidth_kbit"])
        commands.append(
            f"tc qdisc add dev {interface} root tbf"
            f" rate {bw}kbit burst {max(bw // 8, 1)}kb latency 50ms"
        )

    return commands


def _netem_params(params):
    """Build netem parameter string."""
    parts = ""
    if params.get("delay_ms"):
        parts += f" delay {int(params['delay_ms'])}ms"
        if params.get("jitter_ms"):
            parts += f" {int(params['jitter_ms'])}ms"
            if params.get("correlation_percent"):
                parts += f" {int(params['correlation_percent'])}%"
    if params.get("loss_percent"):
        parts += f" loss {float(params['loss_percent'])}%"
    if params.get("corrupt_percent"):
        parts += f" corrupt {float(params['corrupt_percent'])}%"
    if params.get("duplicate_percent"):
        parts += f" duplicate {float(params['duplicate_percent'])}%"
    if params.get("reorder_percent"):
        parts += f" reorder {float(params['reorder_percent'])}%"
    return parts


def build_router_script(port_rules):
    """Build a complete router script with tc rules for multiple ports."""
    lines = []
    for interface, params in port_rules.items():
        cmds = build_tc_commands(interface, params)
        lines.extend(cmds)
    return "\n".join(lines)


# --- WAN Profile Presets ---

WAN_PRESETS = {
    "perfect": {
        "label": "Perfect Link",
        "delay_ms": 0, "jitter_ms": 0, "loss_percent": 0,
        "bandwidth_kbit": 0, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "broadband": {
        "label": "Broadband (Cable/DSL)",
        "delay_ms": 20, "jitter_ms": 5, "loss_percent": 0.1,
        "bandwidth_kbit": 50000, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "4g_lte": {
        "label": "4G LTE",
        "delay_ms": 50, "jitter_ms": 15, "loss_percent": 0.5,
        "bandwidth_kbit": 30000, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "3g": {
        "label": "3G Mobile",
        "delay_ms": 100, "jitter_ms": 40, "loss_percent": 2,
        "bandwidth_kbit": 5000, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "satellite": {
        "label": "Satellite",
        "delay_ms": 600, "jitter_ms": 50, "loss_percent": 1,
        "bandwidth_kbit": 10000, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "congested": {
        "label": "Congested Network",
        "delay_ms": 80, "jitter_ms": 60, "loss_percent": 5,
        "bandwidth_kbit": 2000, "corrupt_percent": 0.5,
        "duplicate_percent": 1, "reorder_percent": 2,
    },
    "mpls": {
        "label": "MPLS (Enterprise)",
        "delay_ms": 10, "jitter_ms": 2, "loss_percent": 0,
        "bandwidth_kbit": 100000, "corrupt_percent": 0,
        "duplicate_percent": 0, "reorder_percent": 0,
    },
    "degraded": {
        "label": "Degraded WAN",
        "delay_ms": 150, "jitter_ms": 80, "loss_percent": 8,
        "bandwidth_kbit": 1000, "corrupt_percent": 1,
        "duplicate_percent": 2, "reorder_percent": 5,
    },
}


# --- Routes ---

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/connect", methods=["POST"])
def connect():
    """Connect to Fabric Studio instance."""
    data = request.json
    host = data.get("host", "").strip()
    username = data.get("username", "admin").strip()
    password = data.get("password", "")

    if not host:
        return jsonify({"status": "error", "message": "Host is required"}), 400

    try:
        client = FabricStudioAPI(host, username, password)
        client.login()
        key = f"{host}:{username}"
        api_clients[key] = client
        session["fs_config"] = {
            "host": host,
            "username": username,
            "password": password,
        }
        return jsonify({"status": "ok", "message": "Connected to Fabric Studio"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


@app.route("/api/disconnect", methods=["POST"])
def disconnect():
    """Disconnect from Fabric Studio."""
    config = session.pop("fs_config", None)
    if config:
        key = f"{config['host']}:{config['username']}"
        api_clients.pop(key, None)
    return jsonify({"status": "ok"})


@app.route("/api/fabrics", methods=["GET"])
def list_fabrics():
    """List available fabrics."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401
    try:
        result = client.get_fabrics()
        fabrics = []
        objects = result.get("object", [])
        if isinstance(objects, dict):
            objects = [objects]
        for f in objects:
            fabrics.append({"id": f["id"], "name": f.get("name", f"Fabric {f['id']}")})
        return jsonify({"status": "ok", "fabrics": fabrics})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/fabric/<int:fabric_id>/topology", methods=["GET"])
def get_topology(fabric_id):
    """Get fabric topology - routers, switches, VMs and their connections."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401
    try:
        routers = client.get_routers(fabric_id)
        switches = client.get_switches(fabric_id)
        vms = client.get_vms(fabric_id)

        router_devs = _extract_devices(routers, "router", "routerport")
        switch_devs = _extract_devices(switches, "switch", "switchport")
        vm_devs = _extract_devices(vms, "vm", "vmport")

        # If routers have 0 ports, try fetching ports individually as fallback
        for dev in router_devs:
            if not dev["ports"]:
                try:
                    result = client.get_router_ports(dev["id"])
                    objs = result.get("object", [])
                    if isinstance(objs, dict):
                        objs = [objs]
                    dev["ports"] = [_make_port(p) for p in objs if isinstance(p, dict) and "id" in p]
                except Exception:
                    pass

        topology = {
            "routers": router_devs,
            "switches": switch_devs,
            "vms": vm_devs,
        }
        return jsonify({"status": "ok", "topology": topology})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/router/<int:router_id>/ports", methods=["GET"])
def get_router_ports_route(router_id):
    """Get ports for a specific router (separate call for reliability)."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401
    try:
        result = client.get_router_ports(router_id)
        ports = []
        objects = result.get("object", [])
        if isinstance(objects, dict):
            objects = [objects]
        for p in objects:
            ports.append({
                "id": p["id"],
                "name": p.get("name", p.get("nameid", f"port{p['id']}")),
                "cable": p.get("cable"),
            })
        return jsonify({"status": "ok", "ports": ports})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


def _find_port_others(others, port_model, device_type):
    """Find port data in the others section, trying multiple key patterns."""
    # Try exact model name, then common variations
    candidates = [port_model, "port", f"{device_type}_port", f"{device_type}port"]
    for key in candidates:
        if key in others and isinstance(others[key], dict) and others[key]:
            return others[key]

    # Search all others for dicts whose entries have a "device" field
    for key, val in others.items():
        if key == "global" or not isinstance(val, dict) or not val:
            continue
        first_entry = next(iter(val.values()), None)
        if isinstance(first_entry, dict) and "device" in first_entry:
            return val

    return {}


def _make_port(port_data, tc_others=None):
    """Build a port dict from raw API port data.

    ``tc_others`` is the ``others["trafficcontrol"]`` dict (keyed by TC
    object ID) so we can resolve the TC reference into an actual ID even
    when the port only carries a bare integer reference.
    """
    port = {
        "id": port_data["id"],
        "name": port_data.get("name", port_data.get("nameid", f"port{port_data['id']}")),
        "cable": port_data.get("cable"),
    }
    # Include tc (traffic control) ID if available
    tc = port_data.get("tc")
    if tc is not None:
        # tc may be an int (ID reference) or a dict (inline object)
        if isinstance(tc, dict) and "id" in tc:
            port["tc"] = tc["id"]
        elif isinstance(tc, (int, str)):
            port["tc"] = int(tc) if isinstance(tc, str) else tc
    elif tc_others:
        # Fallback: scan tc_others for a TC whose port matches this port
        for tc_id_str, tc_obj in tc_others.items():
            if isinstance(tc_obj, dict):
                tc_port = tc_obj.get("port")
                if tc_port == port_data["id"]:
                    port["tc"] = tc_obj.get("id", int(tc_id_str))
                    break
    return port


def _extract_devices(result, device_type, port_model):
    """Extract device list from API result."""
    devices = []
    objects = result.get("object", [])
    if isinstance(objects, dict):
        objects = [objects]
    others = result.get("others", {})

    port_others = _find_port_others(others, port_model, device_type)

    # Look for TC data in others — Fabric Studio stores model.trafficcontrol
    # objects under the key "trafficcontrol" in the others dict.
    tc_others = {}
    for key in ("trafficcontrol", "tc", "traffic_control"):
        if key in others and isinstance(others[key], dict):
            tc_others = others[key]
            break

    for obj in objects:
        dev = {
            "id": obj["id"],
            "name": obj.get("name", obj.get("nameid", f"{device_type}-{obj['id']}")),
            "type": device_type,
            "ports": [],
        }

        # Strategy 1: Match ports from others by parent device ID
        for port_id_str, port_data in port_others.items():
            if not isinstance(port_data, dict):
                continue
            parent_id = port_data.get("device")
            if parent_id == obj["id"]:
                dev["ports"].append(_make_port(port_data, tc_others))

        # Strategy 2: Check inline ports on the object itself
        if not dev["ports"] and "ports" in obj:
            inline_ports = obj["ports"]
            if isinstance(inline_ports, list):
                for p in inline_ports:
                    if isinstance(p, dict) and "id" in p:
                        dev["ports"].append(_make_port(p, tc_others))
                    elif isinstance(p, (int, str)):
                        # Port is just an ID — look it up in others
                        port_data = port_others.get(str(p), port_others.get(int(p) if isinstance(p, str) else p, {}))
                        if isinstance(port_data, dict) and "id" in port_data:
                            dev["ports"].append(_make_port(port_data, tc_others))
                        else:
                            dev["ports"].append({
                                "id": int(p) if isinstance(p, str) else p,
                                "name": f"port{p}",
                                "cable": None,
                            })

        devices.append(dev)
    return devices


@app.route("/api/presets", methods=["GET"])
def get_presets():
    """Get available WAN profile presets."""
    return jsonify({"status": "ok", "presets": WAN_PRESETS})


@app.route("/api/device/<device_type>/<int:device_id>/ports", methods=["GET"])
def get_device_ports_route(device_type, device_id):
    """Get ports for any device type (router, switch, vm)."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401
    try:
        if device_type == "router":
            result = client.get_router_ports(device_id)
        elif device_type == "switch":
            result = client.get_switch_ports(device_id)
        elif device_type == "vm":
            result = client.get_vm_ports(device_id)
        else:
            return jsonify({"status": "error", "message": f"Unknown device type: {device_type}"}), 400
        ports = []
        objects = result.get("object", [])
        if isinstance(objects, dict):
            objects = [objects]
        for p in objects:
            if isinstance(p, dict) and "id" in p:
                ports.append({
                    "id": p["id"],
                    "name": p.get("name", p.get("nameid", f"port{p['id']}")),
                    "cable": p.get("cable"),
                })
        return jsonify({"status": "ok", "ports": ports})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


def _resolve_tc_field_names(tc_obj):
    """Discover actual API field names from a TC object.

    Returns a dict mapping our canonical names to the real API field names.
    Always returns all 7 canonical fields — defaults to the documented
    Fabric Studio field names (delay, jitter, loss, corrupt, duplicate,
    reorder, bandwidth) and only overrides if an alternative name is found
    in *tc_obj*.

    Previous versions only included fields present in tc_obj, which caused
    loss/corrupt/duplicate/reorder to be silently dropped when the API
    omitted zero-valued fields from responses.
    """
    # Canonical names matching the documented Fabric Studio TC schema
    mapping = {
        "delay": "delay",
        "jitter": "jitter",
        "loss": "loss",
        "corrupt": "corrupt",
        "duplicate": "duplicate",
        "reorder": "reorder",
        "bandwidth": "bandwidth",
    }

    if not tc_obj:
        return mapping

    # Override with alternative field names if found in the actual TC object
    alternatives = {
        "delay": ["delay_ms"],
        "jitter": ["jitter_ms"],
        "loss": ["loss_percent", "packet_loss", "loss_pct"],
        "corrupt": ["corrupt_percent", "corruption"],
        "duplicate": ["duplicate_percent", "duplication"],
        "reorder": ["reorder_percent", "reordering"],
        "bandwidth": ["rate", "bandwidth_bps", "bw"],
    }
    for canonical, alt_names in alternatives.items():
        for alt in alt_names:
            if alt in tc_obj:
                mapping[canonical] = alt
                break

    return mapping


def _build_tc_params(params, field_names=None):
    """Convert our WAN emulation params to Fabric Studio tc model fields.

    *field_names* maps canonical names to actual API field names (as returned
    by ``_resolve_tc_field_names``).  All 7 TC fields are always included to
    ensure the API receives the complete set of impairment values.
    """
    if field_names is None:
        field_names = _resolve_tc_field_names(None)
    bandwidth_kbit = int(params.get("bandwidth_kbit", 0))

    # Map of canonical name -> (value to send)
    values = {
        "delay": int(params.get("delay_ms", 0)),
        "jitter": int(params.get("jitter_ms", 0)),
        "loss": float(params.get("loss_percent", 0)),
        "bandwidth": bandwidth_kbit * 1000,
        "corrupt": float(params.get("corrupt_percent", 0)),
        "duplicate": float(params.get("duplicate_percent", 0)),
        "reorder": float(params.get("reorder_percent", 0)),
    }

    # Only include fields that have a known API field name
    result = {}
    for canonical, value in values.items():
        if canonical in field_names:
            result[field_names[canonical]] = value
    return result


def _tc_to_ui_params(tc_obj):
    """Convert a raw TC API object back to UI param dict.

    Tries multiple possible field names to handle different API versions.
    """
    def _get(names, default=0):
        for n in names:
            if n in tc_obj:
                try:
                    return float(tc_obj[n])
                except (TypeError, ValueError):
                    pass
        return default

    bw_raw = _get(["bandwidth", "rate", "bandwidth_bps", "bw"], 0)
    return {
        "delay_ms": _get(["delay", "delay_ms"]),
        "jitter_ms": _get(["jitter", "jitter_ms"]),
        "loss_percent": _get(["loss", "loss_percent", "packet_loss", "loss_pct"]),
        "corrupt_percent": _get(["corrupt", "corrupt_percent", "corruption"]),
        "duplicate_percent": _get(["duplicate", "duplicate_percent", "duplication"]),
        "reorder_percent": _get(["reorder", "reorder_percent", "reordering"]),
        "bandwidth_kbit": int(bw_raw / 1000) if bw_raw else 0,
        "correlation_percent": 0,
    }


@app.route("/api/tc/values", methods=["POST"])
def get_tc_values():
    """Fetch current TC values for one or more ports.

    Expects JSON:
    {
        "fabric_id": 1,
        "device_id": 1,
        "ports": { "port1": { "port_id": 42, "tc_id": 7 }, ... }
    }

    Returns current TC values mapped to UI param names for each port.
    """
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    fabric_id = data.get("fabric_id")
    device_id = data.get("device_id")
    ports = data.get("ports", {})

    if not fabric_id or not device_id:
        return jsonify({"status": "error", "message": "fabric_id and device_id are required"}), 400

    results = {}
    for port_name, port_info in ports.items():
        port_id = port_info.get("port_id")
        if not port_id:
            continue
        try:
            tc_obj = client.get_tc_for_port(fabric_id, device_id, port_id)
            if tc_obj:
                results[port_name] = _tc_to_ui_params(tc_obj)
            else:
                results[port_name] = None
        except Exception:
            results[port_name] = None

    return jsonify({"status": "ok", "values": results})


@app.route("/api/apply", methods=["POST"])
def apply_wan_rules():
    """Apply WAN emulation rules to a device via the tc (traffic control) model.

    Expects JSON:
    {
        "device_id": 1,
        "device_type": "router",
        "fabric_id": 1,
        "interfaces": {
            "port1": { "delay_ms": 50, "jitter_ms": 10, ... }
        },
        "port_ids": { "port1": 42 },
        "tc_ids": { "port1": 7 }
    }
    """
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    device_id = data.get("device_id") or data.get("router_id")
    device_type = data.get("device_type", "router")
    fabric_id = data.get("fabric_id")
    interfaces = data.get("interfaces", {})
    port_ids = data.get("port_ids", {})
    tc_ids = data.get("tc_ids", {})

    if not device_id:
        return jsonify({"status": "error", "message": "device_id is required"}), 400

    if not fabric_id:
        return jsonify({"status": "error", "message": "fabric_id is required"}), 400

    results = {}
    errors = []
    for iface_name, params in interfaces.items():
        port_id = port_ids.get(iface_name)
        tc_id_hint = tc_ids.get(iface_name)

        if not port_id:
            errors.append(f"{iface_name}: no port_id provided")
            continue

        try:
            # Get the TC object (also gives us the tc_id and field names)
            tc_obj = client.get_tc_for_port(fabric_id, device_id, port_id)
            tc_id = tc_id_hint
            if tc_obj:
                tc_id = tc_obj.get("id", tc_id_hint)
            if not tc_id:
                errors.append(f"{iface_name}: no traffic control object found for port {port_id}")
                continue

            field_names = _resolve_tc_field_names(tc_obj)
            tc_params = _build_tc_params(params, field_names)
            update_result = _apply_tc_update(client, tc_id, tc_params, fabric_id, device_id, port_id)
            iface_result = {"tc_id": tc_id, "status": "ok", "applied_params": params}
            if update_result.get("sync_error"):
                iface_result["sync_error"] = update_result["sync_error"]
            results[iface_name] = iface_result
        except Exception as e:
            errors.append(f"{iface_name}: {str(e)}")

    if errors and not results:
        return jsonify({"status": "error", "message": "; ".join(errors)}), 500

    return jsonify({
        "status": "ok",
        "message": f"WAN rules applied to {device_type} {device_id}",
        "results": results,
        "errors": errors,
    })


def _apply_tc_update(client, tc_id, tc_params, fabric_id, device_id, port_id):
    """Update a TC model object, then sync the runtime to apply immediately.

    *tc_params* should already be built with the correct API field names
    (see ``_resolve_tc_field_names``).
    """
    result = client.update_tc(tc_id, tc_params, fabric_id, device_id, port_id)

    # Sync runtime from the updated model so changes take effect immediately
    sync_error = None
    try:
        client.sync_tc(device_id, port_id)
    except Exception as e:
        # sync failed — try force as fallback
        try:
            client.force_tc(device_id, port_id)
        except Exception as e2:
            sync_error = f"sync failed: {e}; force failed: {e2}"

    return {"model_result": result, "sync_error": sync_error}


@app.route("/api/clear", methods=["POST"])
def clear_wan_rules():
    """Clear all WAN emulation rules from a device by resetting tc objects."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    device_id = data.get("device_id") or data.get("router_id")
    device_type = data.get("device_type", "router")
    fabric_id = data.get("fabric_id")
    interfaces = data.get("interfaces", [])
    port_ids = data.get("port_ids", {})
    tc_ids = data.get("tc_ids", {})

    if not device_id:
        return jsonify({"status": "error", "message": "device_id is required"}), 400
    if not fabric_id:
        return jsonify({"status": "error", "message": "fabric_id is required"}), 400

    results = {}
    errors = []
    for iface_name in interfaces:
        port_id = port_ids.get(iface_name)
        tc_id_hint = tc_ids.get(iface_name)

        if not port_id:
            errors.append(f"{iface_name}: no port_id provided")
            continue

        try:
            # Get the TC object (also gives us the tc_id and field names)
            tc_obj = client.get_tc_for_port(fabric_id, device_id, port_id)
            tc_id = tc_id_hint
            if tc_obj:
                tc_id = tc_obj.get("id", tc_id_hint)
            if not tc_id:
                errors.append(f"{iface_name}: no traffic control object found for port {port_id}")
                continue

            field_names = _resolve_tc_field_names(tc_obj)
            zero_params = _build_tc_params({}, field_names)
            _apply_tc_update(client, tc_id, zero_params, fabric_id, device_id, port_id)
            results[iface_name] = {"tc_id": tc_id, "status": "ok"}
        except Exception as e:
            errors.append(f"{iface_name}: {str(e)}")

    if errors and not results:
        return jsonify({"status": "error", "message": "; ".join(errors)}), 500

    return jsonify({
        "status": "ok",
        "message": f"WAN rules cleared on {device_type} {device_id}",
        "results": results,
        "errors": errors,
    })


@app.route("/api/status", methods=["GET"])
def connection_status():
    """Check current connection status."""
    config = session.get("fs_config")
    if not config:
        return jsonify({"status": "disconnected"})
    return jsonify({
        "status": "connected",
        "host": config["host"],
        "username": config["username"],
    })


@app.route("/api/debug/raw/<path:endpoint>", methods=["GET"])
def debug_raw(endpoint):
    """Debug endpoint to see raw API responses."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401
    try:
        params = list(request.args.items(multi=True))
        result = client.get(endpoint, params if params else None)
        return jsonify(result)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
