# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

FortiWAN-E is a Python Flask web application that emulates WAN conditions (latency, jitter, packet loss, bandwidth limits) on Fortinet Fabric Studio Router devices via Linux `tc` (traffic control) commands. It runs as a standalone app outside Fabric Studio and communicates over its REST API.

## Running the Application

```bash
# Docker Compose (recommended)
docker compose up -d

# Direct (Debian/Ubuntu) — installs Python, venv, deps, then starts
./run.sh

# Python directly
python app.py
```

The app serves on port 5000.

There are no tests, linters, or build steps configured in this project.

## Architecture

**Single-file backend** (`app.py`, ~870 lines):
- `FabricStudioAPI` class — manages HTTPS sessions to Fabric Studio (authentication, CSRF tokens, API calls)
- `build_tc_commands()` / `_netem_params()` — generates Linux `tc netem`/`tbf` qdisc commands from WAN parameter dicts
- `_extract_devices()` / `_make_port()` — parses Fabric Studio topology API responses into device/port objects
- REST API routes under `/api/` — connect, disconnect, list fabrics, get topology, get ports, apply/clear WAN rules, presets, status, debug
- Session-based API client caching via global `api_clients` dict keyed by Flask session ID

**Frontend** (vanilla JS, no build tooling):
- `templates/index.html` — single-page layout with 5 panels (connection, fabric selection, topology, WAN controls, activity log)
- `static/js/app.js` (~600 lines) — API module, state management, topology rendering, WAN parameter sliders, preset application, demo mode logic
- `static/css/style.css` (~530 lines) — dark theme with Fortinet red accent, CSS custom properties

**Key data flow:** Browser → Flask API → `FabricStudioAPI` → Fabric Studio REST API → Router `tc` rules

## Dependencies

Python 3.11 with Flask 3.1.0, flask-cors, requests, urllib3 (see `requirements.txt`). No JavaScript dependencies or package manager.

## Fabric Studio API Integration

The `FabricStudioAPI` client handles multiple CSRF token cookie patterns and tries several endpoint variants for backward compatibility. It queries router/switch/VM port models and updates traffic control objects. All API calls use HTTPS with certificate verification disabled.

## Demo Mode vs Advanced Mode

The app has two UI modes, toggled via a switch in the header. All demo mode logic is **frontend-only** — the backend has no concept of modes.

**Demo Mode** (default):
- Automatically selects and loads the **sd-wan 7.6** fabric (fabric selection UI is hidden)
- Filters the topology to only show: **FGT-HUB1**, **FGT-HUB2**, **FGT-BR1**, **FGT-BR2**, **FGT-BR3**
- Filters ports to **port2** and **port3** only
- Renames ports in the GUI: **port2 → ISP-A**, **port3 → ISP-B** (display only, API calls use real port names)
- Hides advanced sliders (corruption, duplicates, reorder)

**Advanced Mode**:
- Full fabric selection from all available fabrics
- Shows all devices in the topology
- Shows all ports on each device
- All 7 WAN parameter sliders visible

Key constants in `app.js`:
- `DEMO_FABRIC_NAME` — fabric name to auto-load (`'sd-wan 7.6'`)
- `DEMO_ALLOWED_DEVICES` — array of device names shown in demo mode
- `DEMO_PORT_LABELS` — mapping of port names to display labels (`{ port2: 'ISP-A', port3: 'ISP-B' }`)
- `getDemoPortLabel(portName)` — returns the display label for a port (passthrough in advanced mode)

## Versioning

FortiWAN-E follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking changes to the API, data model, or configuration that require user action (e.g., changed API contract, removed features, incompatible config format)
- **MINOR** — new features or enhancements added in a backward-compatible way (e.g., new UI panels, new API endpoints, new presets)
- **PATCH** — bug fixes, styling tweaks, and small improvements that don't add new features

The version is defined as `APP_VERSION` in `app.py` and rendered in the footer via Jinja2 (`{{ version }}`).

**Every merge to the main branch must include a version bump.** Update the `APP_VERSION` constant in `app.py` according to the change type above. The version history should be traceable through git tags (e.g., `v1.2.0`).

## Documentation

**Feature changes must include documentation updates.** When implementing new features or modifying existing behavior:

1. Update **`README.md`** — feature table, usage instructions, and version badge
2. Update **`CLAUDE.md`** — architecture details, new constants/functions, and behavioral notes
3. Update **`docs/`** files if the change affects Fabric Studio API integration or user-facing workflows

This ensures documentation stays in sync with the codebase at all times.
