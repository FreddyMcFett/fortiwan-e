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
        # First request to get initial cookies
        self.session.get(f"{self.base_url}/api/v1/session/check")
        # Extract CSRF token from cookies
        self._update_csrf()
        # Login
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
            if "csrftoken" in name and not name.endswith("-csrftoken"):
                self.csrf_token = value
                break
            if name == "fortipoc-csrftoken":
                self.csrf_token = value

    def _headers(self):
        """Build request headers with CSRF token."""
        headers = {"Referer": f"{self.base_url}/"}
        if self.csrf_token:
            headers["X-FortiPoC-CSRFToken"] = self.csrf_token
        return headers

    def get(self, endpoint, params=None):
        """GET request to API."""
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

    def get_fabrics(self):
        """List all fabrics."""
        return self.get("model/fabric")

    def get_fabric_devices(self, fabric_id):
        """Get all devices in a fabric with ports."""
        return self.get(
            "model/fabric",
            {
                "select": f"id={fabric_id}",
                "related-fields": [
                    "devices",
                    "devices.ports",
                    "devices.ports.wire",
                ],
            },
        )

    def get_routers(self, fabric_id=None):
        """Get routers, optionally filtered by fabric."""
        params = {"related-fields": ["ports"]}
        if fabric_id:
            params["select"] = f"fabric={fabric_id}"
        return self.get("model/router", params)

    def get_router_ports(self, router_id):
        """Get ports for a specific router."""
        return self.get("model/routerport", {"select": f"router={router_id}"})

    def get_switches(self, fabric_id=None):
        """Get switches, optionally filtered by fabric."""
        params = {"related-fields": ["ports"]}
        if fabric_id:
            params["select"] = f"fabric={fabric_id}"
        return self.get("model/switch", params)

    def get_vms(self, fabric_id=None):
        """Get VMs, optionally filtered by fabric."""
        params = {"related-fields": ["ports"]}
        if fabric_id:
            params["select"] = f"fabric={fabric_id}"
        return self.get("model/vm", params)

    def execute_router_script(self, router_id, script):
        """Execute a script on a router via configuration update."""
        return self.post(
            f"model/router/update",
            {"id": router_id, "script": script},
        )

    def update_router(self, router_id, data):
        """Update router properties."""
        data["id"] = router_id
        return self.post("model/router/update", data)


# Global API client store (per-session in production, simplified here)
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
    """Build tc (traffic control) commands for WAN emulation.

    Uses tc qdisc with netem for latency/jitter/loss and tbf for bandwidth.
    """
    commands = []
    # Clear existing rules
    commands.append(f"tc qdisc del dev {interface} root 2>/dev/null || true")

    has_netem = any(
        params.get(k)
        for k in ["delay_ms", "jitter_ms", "loss_percent", "corrupt_percent", "duplicate_percent", "reorder_percent"]
    )
    has_bw = params.get("bandwidth_kbit")

    if not has_netem and not has_bw:
        # Just clear - no rules to apply
        return commands

    if has_netem and has_bw:
        # Chain: root htb -> netem as child
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
    """Build a complete router script with tc rules for multiple ports.

    port_rules: dict of {interface_name: params_dict}
    """
    lines = []
    for interface, params in port_rules.items():
        cmds = build_tc_commands(interface, params)
        lines.extend(cmds)
    return "\n".join(lines)


# --- WAN Profile Presets ---

WAN_PRESETS = {
    "perfect": {
        "label": "Perfect Link",
        "delay_ms": 0,
        "jitter_ms": 0,
        "loss_percent": 0,
        "bandwidth_kbit": 0,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "broadband": {
        "label": "Broadband (Cable/DSL)",
        "delay_ms": 20,
        "jitter_ms": 5,
        "loss_percent": 0.1,
        "bandwidth_kbit": 50000,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "4g_lte": {
        "label": "4G LTE",
        "delay_ms": 50,
        "jitter_ms": 15,
        "loss_percent": 0.5,
        "bandwidth_kbit": 30000,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "3g": {
        "label": "3G Mobile",
        "delay_ms": 100,
        "jitter_ms": 40,
        "loss_percent": 2,
        "bandwidth_kbit": 5000,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "satellite": {
        "label": "Satellite",
        "delay_ms": 600,
        "jitter_ms": 50,
        "loss_percent": 1,
        "bandwidth_kbit": 10000,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "congested": {
        "label": "Congested Network",
        "delay_ms": 80,
        "jitter_ms": 60,
        "loss_percent": 5,
        "bandwidth_kbit": 2000,
        "corrupt_percent": 0.5,
        "duplicate_percent": 1,
        "reorder_percent": 2,
    },
    "mpls": {
        "label": "MPLS (Enterprise)",
        "delay_ms": 10,
        "jitter_ms": 2,
        "loss_percent": 0,
        "bandwidth_kbit": 100000,
        "corrupt_percent": 0,
        "duplicate_percent": 0,
        "reorder_percent": 0,
    },
    "degraded": {
        "label": "Degraded WAN",
        "delay_ms": 150,
        "jitter_ms": 80,
        "loss_percent": 8,
        "bandwidth_kbit": 1000,
        "corrupt_percent": 1,
        "duplicate_percent": 2,
        "reorder_percent": 5,
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
        # Get all device types
        routers = client.get_routers(fabric_id)
        switches = client.get_switches(fabric_id)
        vms = client.get_vms(fabric_id)

        topology = {
            "routers": _extract_devices(routers, "router"),
            "switches": _extract_devices(switches, "switch"),
            "vms": _extract_devices(vms, "vm"),
        }
        return jsonify({"status": "ok", "topology": topology})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


def _extract_devices(result, device_type):
    """Extract device list from API result."""
    devices = []
    objects = result.get("object", [])
    if isinstance(objects, dict):
        objects = [objects]
    others = result.get("others", {})

    for obj in objects:
        dev = {
            "id": obj["id"],
            "name": obj.get("name", obj.get("nameid", f"{device_type}-{obj['id']}")),
            "type": device_type,
            "ports": [],
        }
        # Extract ports from related objects
        port_model = f"{device_type}port"
        port_others = others.get(port_model, {})
        for port_id, port_data in port_others.items():
            parent_id = port_data.get(device_type)
            if parent_id == obj["id"]:
                dev["ports"].append({
                    "id": port_data["id"],
                    "name": port_data.get("name", port_data.get("nameid", f"port{port_data['id']}")),
                    "wire": port_data.get("wire"),
                })
        devices.append(dev)
    return devices


@app.route("/api/presets", methods=["GET"])
def get_presets():
    """Get available WAN profile presets."""
    return jsonify({"status": "ok", "presets": WAN_PRESETS})


@app.route("/api/apply", methods=["POST"])
def apply_wan_rules():
    """Apply WAN emulation rules to router interfaces.

    Expects JSON:
    {
        "router_id": 1,
        "interfaces": {
            "eth0": { "delay_ms": 50, "jitter_ms": 10, ... },
            "eth1": { "delay_ms": 100, ... }
        }
    }
    """
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    router_id = data.get("router_id")
    interfaces = data.get("interfaces", {})

    if not router_id:
        return jsonify({"status": "error", "message": "router_id is required"}), 400

    try:
        script = build_router_script(interfaces)
        result = client.update_router(router_id, {"script": script})
        return jsonify({
            "status": "ok",
            "message": f"WAN rules applied to router {router_id}",
            "script": script,
            "result": result,
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/clear", methods=["POST"])
def clear_wan_rules():
    """Clear all WAN emulation rules from a router."""
    client = get_api_client()
    if not client:
        return jsonify({"status": "error", "message": "Not connected"}), 401

    data = request.json
    router_id = data.get("router_id")
    interfaces = data.get("interfaces", [])

    if not router_id:
        return jsonify({"status": "error", "message": "router_id is required"}), 400

    try:
        lines = []
        for iface in interfaces:
            lines.append(f"tc qdisc del dev {iface} root 2>/dev/null || true")
        script = "\n".join(lines)
        result = client.update_router(router_id, {"script": script})
        return jsonify({
            "status": "ok",
            "message": f"WAN rules cleared on router {router_id}",
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
