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
- `debug_log()` — in-memory debug log buffer (`DEBUG_LOG_BUFFER`, deque of 2000 entries) with structured entries (timestamp, level, category, message, details)
- `/api/debug/logs` — GET returns debug logs filtered by `?minutes=N`, DELETE clears the buffer
- Session-based API client caching via global `api_clients` dict keyed by Flask session ID

**Frontend** (vanilla JS, no build tooling):
- `templates/index.html` — single-page layout with 5 panels (connection, fabric selection, topology, WAN controls, activity log) + debug panel overlay
- `static/js/app.js` (~1100 lines) — API module, `DebugLog` system, state management, topology rendering, WAN parameter sliders, preset application, demo mode logic
- `static/css/style.css` (~850 lines) — dark theme with Fortinet red accent, CSS custom properties, debug panel styles

**Key data flow:** Browser → Flask API → `FabricStudioAPI` → Fabric Studio REST API → Router `tc` rules

## Dependencies

Python 3.11 with Flask 3.1.0, flask-cors, requests, urllib3 (see `requirements.txt`). No JavaScript dependencies or package manager.

## Fabric Studio API Integration

The `FabricStudioAPI` client handles multiple CSRF token cookie patterns and tries several endpoint variants for backward compatibility. It queries router/switch/VM port models and updates traffic control objects. All API calls use HTTPS with certificate verification disabled.

## Demo Mode vs Advanced Mode

The app has two UI modes, toggled via a switch in the header. All demo mode logic is **frontend-only** — the backend has no concept of modes.

**Demo Mode** (default):
- Connection panel is locked down: studio instance is shown as static text (not a dropdown), host and username are readonly; only the password field is editable
- Only shows **Studio 01** (`studio-01.mp-cloud.lab`) and auto-selects it; "Add Studio" button is hidden
- Automatically selects and loads the **sd-wan 7.6** fabric (fabric selection UI is hidden)
- Filters the topology to only show: **FGT-HUB1**, **FGT-HUB2**, **FGT-BR1**, **FGT-BR2**, **FGT-BR3**
- Filters ports to **port2** and **port3** only
- Renames ports in the GUI: **port2 → ISP-A**, **port3 → ISP-B** (display only, API calls use real port names)
- Displays custom SVG icons: **server rack** icon for HUB devices, **office building** icon for BR devices (replaces the generic VM badge)
- Hides device type label ("VM") and port count — shows "Hub" or "Branch" role label instead
- Hides advanced sliders (corruption, duplicates, reorder)

**Advanced Mode**:
- All studios visible, custom studios can be added
- Full fabric selection from all available fabrics
- Shows all devices in the topology
- Shows all ports on each device
- All 7 WAN parameter sliders visible

Key constants in `app.js`:
- `DEMO_FABRIC_NAME` — fabric name to auto-load (`'sd-wan-7.6'`); matching normalizes hyphens, spaces, dots, and underscores
- `DEMO_STUDIO_HOST` — studio host to show in demo mode (`'studio-01.mp-cloud.lab'`)
- `DEMO_STUDIO_LABEL` — display label for the demo studio (`'Studio 01'`)
- `DEMO_USERNAME` — hardcoded username in demo mode (`'admin'`)
- `DEMO_ALLOWED_DEVICES` — array of device names shown in demo mode
- `DEMO_PORT_LABELS` — mapping of port names to display labels (`{ port2: 'ISP-A', port3: 'ISP-B' }`)
- `getDemoPortLabel(portName)` — returns the display label for a port (passthrough in advanced mode)
- `getDemoDeviceIcon(deviceName)` — returns inline SVG icon (server rack for HUB, office building for BR)
- `applyDemoConnectionMode(isDemoMode)` — locks/unlocks the connection panel fields based on mode

## Debug Console

The app includes a built-in debug console accessible via the **Debug** button in the header. It captures detailed logs from both frontend and backend for troubleshooting.

**Backend** (`app.py`):
- `debug_log(level, category, message, details)` — adds structured entries to `DEBUG_LOG_BUFFER` (deque, max 2000 entries)
- All `FabricStudioAPI` methods (`get`, `post`, `patch`, `login`) log requests, responses, and errors
- Connect/disconnect and TC apply/clear routes log key operations
- `GET /api/debug/logs?minutes=N` — returns logs within the specified time range
- `DELETE /api/debug/logs` — clears the backend log buffer

**Frontend** (`app.js`):
- `DebugLog` object — manages frontend log entries (max 5000) with `add()`, `getFilteredLogs()`, `renderDebugPanel()`
- All `API.request()` calls are automatically logged with method, URL, status, and duration
- `addLog()` (activity log) entries are also captured in the debug log
- Connection state changes are logged

**Debug Console UI** (`/debug` route, `templates/debug.html`):
- Opens in a **separate browser tab** via the header Debug button (not an inline overlay)
- Standalone page at `/debug` with its own self-contained JS — no dependency on `app.js`
- Fetches backend logs only (via `GET /api/debug/logs`) — no frontend log mixing or feedback loops
- Time range filter: 5 min, 15 min (default), 1 hour, 4 hours, 1 day
- **Refresh** button — manually re-fetches logs (no auto-polling to avoid noise)
- **Copy** button — copies all filtered logs as JSON to clipboard
- **Export** button — downloads a `.json` file with logs and user agent
- Status bar shows entry count and last refresh time
- Each log entry shows: timestamp, source badge (BE), category, level, message, and expandable details
- Color-coded levels: blue (info), gray (debug), yellow (warn), red (error)
- Error and warn entries have colored left border for visibility

**Disconnect button** is located in the header next to the connection status badge (not in the connection form).

## Clear All

The **Clear All** button appears in the WAN Emulation panel header (next to the panel title). It clears every WAN rule from every device in the loaded fabric topology with a single click. Works in both Demo and Advanced modes:

- In **Demo Mode**, it iterates only over `DEMO_ALLOWED_DEVICES` and their demo-filtered ports (port2/port3)
- In **Advanced Mode**, it iterates over all devices (routers, switches, VMs) and all their ports

Implementation: `handleClearAll()` in `app.js` loops through `state.topology` devices, builds the full interfaces/port_ids/tc_ids payload per device, and calls `API.clear()` for each. It also resets `state.appliedParams` for cleared devices and re-renders the emulator panel if the currently selected device was affected.

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
