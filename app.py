#!/usr/bin/env python3
"""FortiWAN-E - Web-based WAN Emulator for Fabric Studio SD-WAN demos."""

import json
import re
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

    def post_form(self, endpoint, form_data=None):
        """POST request with form-encoded data."""
        resp = self.session.post(
            f"{self.base_url}/api/v1/{endpoint}",
            data=form_data,
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
            ("related-fields", "ports"),
            ("related-fields", "ports.wire"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/router", params)

    def get_router_ports(self, router_id):
        """Get ports for a specific router, trying multiple API approaches."""
        errors = []

        # Approach 1: Query routerport model directly
        try:
            result = self.get("model/routerport", [("select", f"router={router_id}")])
            objs = result.get("object", [])
            if isinstance(objs, dict):
                objs = [objs]
            if objs:
                return result
        except Exception as e:
            errors.append(f"routerport: {e}")

        # Approach 2: Query router with related-fields=ports, extract from others
        try:
            result = self.get("model/router", [
                ("select", f"id={router_id}"),
                ("related-fields", "ports"),
            ])
            devices = _extract_devices(result, "router", "routerport")
            if devices and devices[0].get("ports"):
                return {"status": "done", "object": devices[0]["ports"]}
        except Exception as e:
            errors.append(f"router+related: {e}")

        # Approach 3: Try generic port model
        try:
            result = self.get("model/port", [("select", f"router={router_id}")])
            objs = result.get("object", [])
            if isinstance(objs, dict):
                objs = [objs]
            if objs:
                return result
        except Exception as e:
            errors.append(f"port: {e}")

        # Nothing worked — return empty with error context
        raise Exception(f"Could not fetch ports for router {router_id}. Tried: {'; '.join(errors)}")

    def get_switches(self, fabric_id=None):
        """Get switches with ports, optionally filtered by fabric."""
        params = [
            ("related-fields", "ports"),
            ("related-fields", "ports.wire"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/switch", params)

    def get_vms(self, fabric_id=None):
        """Get VMs with ports, optionally filtered by fabric."""
        params = [
            ("related-fields", "ports"),
            ("related-fields", "ports.wire"),
        ]
        if fabric_id:
            params.append(("select", f"fabric={fabric_id}"))
        return self.get("model/vm", params)

    def get_switch_ports(self, switch_id):
        """Get ports for a specific switch."""
        try:
            result = self.get("model/switchport", [("select", f"switch={switch_id}")])
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
                ("related-fields", "ports"),
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
            result = self.get("model/vmport", [("select", f"vm={vm_id}")])
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
                ("related-fields", "ports"),
            ])
            devices = _extract_devices(result, "vm", "vmport")
            if devices and devices[0].get("ports"):
                return {"status": "done", "object": devices[0]["ports"]}
        except Exception:
            pass
        raise Exception(f"Could not fetch ports for VM {vm_id}")

    def update_router(self, router_id, data):
        """Update router properties via form POST."""
        form = {}
        for key, value in data.items():
            form[f"object.{key}"] = value
        return self.post_form(f"model/router/{router_id}", form)

    def update_device(self, device_type, device_id, data):
        """Update any device type. Routers use form POST, others use PATCH."""
        if device_type == "router":
            form = {}
            for key, value in data.items():
                form[f"object.{key}"] = value
            return self.post_form(f"model/{device_type}/{device_id}", form)
        else:
            return self.patch(f"model/{device_type}/{device_id}", data)


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
                "wire": p.get("wire"),
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

    # Search all others for dicts whose entries reference the device_type
    for key, val in others.items():
        if key == "global" or not isinstance(val, dict) or not val:
            continue
        first_entry = next(iter(val.values()), None)
        if isinstance(first_entry, dict) and device_type in first_entry:
            return val

    return {}


def _make_port(port_data):
    """Build a port dict from raw API port data."""
    return {
        "id": port_data["id"],
        "name": port_data.get("name", port_data.get("nameid", f"port{port_data['id']}")),
        "wire": port_data.get("wire"),
    }


def _extract_devices(result, device_type, port_model):
    """Extract device list from API result."""
    devices = []
    objects = result.get("object", [])
    if isinstance(objects, dict):
        objects = [objects]
    others = result.get("others", {})

    port_others = _find_port_others(others, port_model, device_type)

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
            parent_id = port_data.get(device_type)
            if parent_id == obj["id"]:
                dev["ports"].append(_make_port(port_data))

        # Strategy 2: Check inline ports on the object itself
        if not dev["ports"] and "ports" in obj:
            inline_ports = obj["ports"]
            if isinstance(inline_ports, list):
                for p in inline_ports:
                    if isinstance(p, dict) and "id" in p:
                        dev["ports"].append(_make_port(p))
                    elif isinstance(p, (int, str)):
                        # Port is just an ID — look it up in others
                        port_data = port_others.get(str(p), port_others.get(int(p) if isinstance(p, str) else p, {}))
                        if isinstance(port_data, dict) and "id" in port_data:
                            dev["ports"].append(_make_port(port_data))
                        else:
                            dev["ports"].append({
                                "id": int(p) if isinstance(p, str) else p,
                                "name": f"port{p}",
                                "wire": None,
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
                    "wire": p.get("wire"),
                })
        return jsonify({"status": "ok", "ports": ports})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/apply", methods=["POST"])
def apply_wan_rules():
    """Apply WAN emulation rules to a device.

    Expects JSON:
    {
        "device_id": 1,
        "device_type": "router",
        "interfaces": {
            "eth0": { "delay_ms": 50, "jitter_ms": 10, ... }
        }
    }
    Also accepts legacy "router_id" field for backward compatibility.
    """
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    device_id = data.get("device_id") or data.get("router_id")
    device_type = data.get("device_type", "router")
    interfaces = data.get("interfaces", {})

    if not device_id:
        return jsonify({"status": "error", "message": "device_id is required"}), 400

    try:
        script = build_router_script(interfaces)
        result = client.update_device(device_type, device_id, {"script": script})
        return jsonify({
            "status": "ok",
            "message": f"WAN rules applied to {device_type} {device_id}",
            "script": script,
            "result": result,
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/clear", methods=["POST"])
def clear_wan_rules():
    """Clear all WAN emulation rules from a device."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    device_id = data.get("device_id") or data.get("router_id")
    device_type = data.get("device_type", "router")
    interfaces = data.get("interfaces", [])

    if not device_id:
        return jsonify({"status": "error", "message": "device_id is required"}), 400

    try:
        lines = []
        for iface in interfaces:
            lines.append(f"tc qdisc del dev {iface} root 2>/dev/null || true")
        script = "\n".join(lines)
        result = client.update_device(device_type, device_id, {"script": script})
        return jsonify({
            "status": "ok",
            "message": f"WAN rules cleared on {device_type} {device_id}",
            "script": script,
            "result": result,
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


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
