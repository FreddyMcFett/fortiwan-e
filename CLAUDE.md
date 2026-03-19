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
- `static/js/app.js` (~540 lines) — API module, state management, topology rendering, WAN parameter sliders, preset application
- `static/css/style.css` (~530 lines) — dark theme with Fortinet red accent, CSS custom properties

**Key data flow:** Browser → Flask API → `FabricStudioAPI` → Fabric Studio REST API → Router `tc` rules

## Dependencies

Python 3.11 with Flask 3.1.0, flask-cors, requests, urllib3 (see `requirements.txt`). No JavaScript dependencies or package manager.

## Fabric Studio API Integration

The `FabricStudioAPI` client handles multiple CSRF token cookie patterns and tries several endpoint variants for backward compatibility. It queries router/switch/VM port models and updates traffic control objects. All API calls use HTTPS with certificate verification disabled.

## Versioning

FortiWAN-E follows [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`):

- **MAJOR** — breaking changes to the API, data model, or configuration that require user action (e.g., changed API contract, removed features, incompatible config format)
- **MINOR** — new features or enhancements added in a backward-compatible way (e.g., new UI panels, new API endpoints, new presets)
- **PATCH** — bug fixes, styling tweaks, and small improvements that don't add new features

The version is defined as `APP_VERSION` in `app.py` and rendered in the footer via Jinja2 (`{{ version }}`).

**Every merge to the main branch must include a version bump.** Update the `APP_VERSION` constant in `app.py` according to the change type above. The version history should be traceable through git tags (e.g., `v1.1.0`).
