# Fabric Studio API Documentation

> **Source:** `studio-01.mp-cloud.lab/help/api.html`
> **Product:** Fabric Studio (FortiPoC)
> **Copyright:** 2016–2026 Fortinet, Inc.

---

## Table of Contents

1. [API Overview](#1-api-overview)
2. [5.1 API Tutorial](#51-api-tutorial)
   - [5.1.1 Introduction](#511-introduction)
   - [5.1.2 Session and CSRF](#512-session-and-csrf)
   - [5.1.3 API Call Request](#513-api-call-request)
   - [5.1.4 API Call Result](#514-api-call-result)
   - [5.1.5 Filtering Expressions](#515-filtering-expressions)
   - [5.1.6 Related Fields Option](#516-related-fields-option)
   - [5.1.7 WebSockets](#517-websockets)
3. [5.2 CLI Reference](#52-cli-reference)
   - [CLI General Commands](#cli-general-commands)
   - [DEBUG Commands](#debug-commands)
   - [MODEL Commands](#model-commands)
   - [RUNTIME Commands](#runtime-commands)
   - [SYSTEM Commands](#system-commands)
   - [TASK Commands](#task-commands)
4. [5.4 OAuth2 Authorization Grants](#54-oauth2-authorization-grants)
   - [5.4.1 Client Credential](#541-client-credential)
   - [5.4.2 Authorization Code](#542-authorization-code)

---

## 1. API Overview

Fabric Studio exposes two API interfaces:

- **REST-like HTTP API** — accessible via session/CSRF cookies or OAuth2 Bearer token
- **CLI API** — available via the built-in command-line interface

See [5.1 API Tutorial](#51-api-tutorial) for authentication requirements. Full REST endpoint reference is in the OpenAPI documentation (`/help/openapi.html`).

---

## 5.1 API Tutorial

### 5.1.1 Introduction

The REST API supports two authentication methods:

**Cookie-based authentication** uses three cookies unique per Fabric Studio instance:

| Cookie | Description |
|--------|-------------|
| `fortipoc-sessionid-<UUID>` | Session cookie, unique to the Fabric Studio instance |
| `fortipoc-csrftoken-<UUID>` | CSRF cookie, unique to the Fabric Studio instance |
| `fortipoc-csrftoken` | Copy of the CSRF cookie readable by frontend JavaScript |

**Token-based authentication** uses OAuth2 Authorization Grants. See [Section 5.4](#54-oauth2-authorization-grants).

---

### 5.1.2 Session and CSRF

#### Shell Template

> **Note:** This shell template is the base for all REST examples in this documentation. Download: `/_static/scripts/rest.sh`

The `rest` shell function:
- Manages the cookie jar (`~/fortipoc.jar`)
- Reads the CSRF token from cookies
- Injects `X-FortiPoC-CSRFToken` on POST/PUT/DELETE requests
- Uses `curl -k` (skip SSL verification — remove `-k` if you have a valid certificate)

**Setup:**
```sh
# Set your FortiPoC instance address
ADDR=<your-fortipoc-address>

# Source the rest.sh script
source rest.sh
```

**Usage examples:**
```sh
# Get initial cookies (CSRF token) and check session state
rest -f https://${ADDR}/api/v1/session/check

# Login using Form
rest -f https://${ADDR}/api/v1/session/open \
  -d username=admin \
  -d password=<password>

# Login using JSON
rest -f https://${ADDR}/api/v1/session/open \
  -H 'Content-Type: application/json' \
  --data-raw '{"username": "admin", "password": "<password>"}'
```

#### JavaScript

A frontend JavaScript client must extract the CSRF token from the `fortipoc-csrftoken` cookie and pass it as the `X-FortiPoC-CSRFToken` request header.

```js
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
```

> **Note:** In FortiOS, the CSRF token cookie is set as `Secure` and cannot be read from JavaScript. The cookie name is `csrftoken` and the header name is `x-csrftoken`.

---

### 5.1.3 API Call Request

Both CLI and REST API share a common call mechanism.

#### Object Instance

When an argument must be a model instance, pass it as a JSON object:

```json
{
  "__model": "MODEL",
  "id": <integer>,
  "native_field1": value1,
  "native_field2": value2,
  ...
}
```

**Fields:**

| Field | Description |
|-------|-------------|
| `__model` | Model string identifier, e.g. `model.vm`. Optional when the API call only accepts one model. |
| `id` | Internal database ID. **Do not specify on `create`**. Not required on `update` (ID is in the URL/command). |
| `native_field*` | Object's native fields. Optional fields use their defaults if omitted. |

> **Warning:** Using an existing `id` on `create` will fail if that ID already exists.
> **Note:** Unknown and read-only fields are silently ignored by the server.

#### CLI

Pass a model instance as a JSON string:

```sh
# Create a VM
# model vm create '{"name": "FGT1", "firmware": 1}'

# View help for a command
# model fabric list --help
```

**Common list options:**

| Option | Type | Description |
|--------|------|-------------|
| `--select FILTER` | filter | Select elements matching expression |
| `--exclude FILTER` | filter | Exclude elements matching expression |
| `--order-by ORDER_BY` | tuple | Comma-separated list of fields |
| `--limit LIMIT` | int | Max number of results |
| `--page PAGE` | int | Page number |
| `--page-of ID` | int | Get page containing this object ID |
| `--related-fields FIELDS` | str* | Extra fields to dump |

**Example:**
```sh
# cli json enable
# model fabric list --select 'name="Test Fabric"' \
    --related-fields devices devices.ports devices.ports.wire
```

#### GET Query

For read-only calls (e.g., `fabric list`), pass arguments as URL-encoded GET parameters.

> **Warning:** Parameters must be properly URL-encoded.

**Python encoding helper:**
```sh
$ python3 -c "import sys, urllib.parse; print(urllib.parse.urlencode({...}))"
```

**Example:**
```sh
$ rest https://${ADDR}/api/v1/model/fabric -G \
  -d 'select=name=Test+Fabric+1' \
  -d 'related-fields=devices'
```

#### POST Query

Most API calls support both JSON and Form POST encoding. **JSON is preferred.**

**JSON POST:**
```sh
# Create a Fabric from default template
rest https://${ADDR}/api/v1/model/fabric \
  -H 'Content-Type: application/json' \
  --data-raw '{"name": "MyFabric"}'

# Create a Fabric from alternate template (explicit POST)
rest https://${ADDR}/api/v1/model/fabric -X POST \
  -H 'Content-Type: application/json' \
  --data-raw '{"template": "alternate", "name": "MyFabric"}'
```

**Form POST:**

Supports `application/x-www-form-urlencoded` and `multipart/form-data`.
Use `multipart/form-data` when an argument uses a `Path` type (file upload).

Each argument is a key/value pair. For object arguments, use `ARGNAME.FIELD` notation:

```sh
# Create a VM via form
$ rest https://${ADDR}/api/v1/model/vm \
  -F 'object.name=FGT' \
  -F 'object.fabric=1' \
  -F 'object.firmware=2'

# Upload a file
$ rest https://${ADDR}/api/v1/model/fabric:import \
  -F 'input=@my.fabric'
```

---

### 5.1.4 API Call Result

When using CLI JSON output (`--json`) or HTTP REST, most API calls return an `APIResult` object.

#### APIResult Structure

```json
{
  "status": "done" | "error",
  "object": VALUE,
  "errors": {
    "MSG_KEY": "ERROR_MSG",
    ...
  },
  "warnings": {
    "MSG_KEY": "WARNING_MSG",
    ...
  },
  "rcode": RETURN_CODE,
  "page": {
    "number": <current page>,
    "total": <total pages>,
    "count": <total elements>
  },
  "others": {
    "global": ANY,
    "MODEL": {
      "OBJECT_ID": VALUE,
      ...
    }
  }
}
```

**Status values (`API_STATUS`):**

| Value | Meaning |
|-------|---------|
| `"error"` | Call failed |
| `"done"` | Call succeeded (may still include warnings, e.g. missing firmware) |

**Object structure (`OBJECT`):**

```json
{
  "__model": "MODEL",
  "id": <integer>,
  "native_field1": VALUE,
  "native_field2": VALUE,
  ...,
  "extra_field1": VALUE,
  "return": {
    "status": "done" | "error",
    "action": "add" | "del" | "upd" | "keep",
    "errors": { "MSG_KEY": "ERROR_MSG" },
    "warnings": { "MSG_KEY": "WARNING_MSG" }
  }
}
```

**Object status (`OBJ_STATUS`):**

| Value | Meaning |
|-------|---------|
| `"done"` | Object operation succeeded |
| `"error"` | Object operation failed |

**Error key (`MSG_KEY`):**

| Value | Meaning |
|-------|---------|
| `"global"` | General error on the object call |
| `FIELD_NAME` | Error on a specific native field |

> **Note:** Extra fields are dynamic attributes or property values computed at runtime, not part of the base object model.

---

### 5.1.5 Filtering Expressions

Two filter modes are available:

| Mode | Description |
|------|-------------|
| `--select EXPR` | Select elements matching the expression |
| `--exclude EXPR` | Exclude elements matching the expression |

The `select` is applied first, then `exclude` is applied to the result.

#### Expression Syntax

A filter expression contains: `KEY OPERATOR [CAST] VALUE`

- **Keys:** field name, e.g. `name`
- **Operators:** `=`, `<`, `<=`, `>=`, `>`
- **Optional cast:** `int`, `bool`
- **Values:** the value to match, e.g. `Fabric`

**Type inference (no cast needed for):**

| Type | Examples |
|------|---------|
| Boolean | `active=True` or `active=1`, `active=False` or `active=0` |
| Integer | `timeout=300` |

**Explicit cast:**

```
(bool)True   (bool)False
(int)VALUE
```

**Logical operators:**

| Operator | Meaning |
|----------|---------|
| `\|` | OR |
| `&` | AND |
| `(...)` | Grouping |

**Examples:**
```sh
# Simple equality
name=Fabric

# OR + AND with grouping
name=Fabric|name=Test & timeout>=300 & password=fortinet

# Value with spaces — use quotes
name="Test Fabric"

# CLI — escape or single-quote the expression
# model fabric list --select 'name="Test Fabric"'

# Negative match — use --exclude
# model fabric list --exclude 'name="Test Fabric"'
```

#### Default Lookup

Some CLI commands have an implicit default key (e.g., `model fabric list` uses `name.contains`):

```sh
# model fabric list --select '"Test Fabric"'
```

> **Warning:** Default lookup only works in the CLI, not in REST.

#### Field Lookups (Django QuerySet Syntax)

Fabric Studio uses Django-style double-underscore (`__`) or dot (`.`) notation for field lookups.

| Lookup | Alias | Description |
|--------|-------|-------------|
| `FIELD__contains=VALUE` | `FIELD.contains=VALUE` | String field contains VALUE |
| `FIELD__gt=VALUE` | `FIELD.gt=VALUE` | Numeric field greater than VALUE |
| `FIELD__gte=VALUE` | `FIELD.gte=VALUE` | Numeric field ≥ VALUE |
| `FIELD__lte=VALUE` | `FIELD.lte=VALUE` | Numeric field ≤ VALUE |
| `FIELD__isnull=BOOL` | `FIELD.isnull=BOOL` | Field is null or not null |

**Comparison operator aliases:**

| Notation | Equivalent |
|----------|-----------|
| `NAME<VALUE` | `NAME.lt=VALUE` |
| `NAME<=VALUE` | `NAME.lte=VALUE` |
| `NAME>=VALUE` | `NAME.gte=VALUE` |
| `NAME>VALUE` | `NAME.gt=VALUE` |

**Chained field lookups** (traverse relationships):

```sh
$ fpcli model device list --select 'fabric.name="Test Fabric"'
```

> **Warning:** Chained lookups do not work for dynamically computed read-only fields.

---

### 5.1.6 Related Fields Option

The `--related-fields` option retrieves extra fields such as computed values or reverse-relationship data.

**Without `--related-fields`:**
```sh
# cli json enable
# model fabric list
```
```json
{
  "status": "done",
  "object": {
    "name": "Test Fabric",
    "description": "",
    "timeout": 180,
    "revert_mode": "SCR",
    "hwaddr_prefix": "02:09:0F",
    "password": "fortinet",
    ...
  }
}
```

**With `--related-fields devices`** (reverse relationship):
```sh
# model fabric list --related-fields devices
```
```json
{
  "status": "done",
  "object": {
    "name": "Test Fabric",
    ...,
    "devices": [
      {
        "nameid": "sw000",
        "name": "sw1",
        "description": null,
        "__model": "model.switch",
        "id": ...
      }
    ]
  }
}
```

**With `--related-fields fabric`** (forward reference expansion):
```sh
# model device list --related-fields fabric --select name=sw1
```
```json
{
  "status": "done",
  "object": {
    "fabric": {
      "name": "Test Fabric",
      "timeout": 180,
      "revert_mode": "SCR",
      "__model": "model.fabric",
      "id": ...
    },
    "nameid": "sw000",
    "name": "sw1",
    ...
  }
}
```

---

### 5.1.7 WebSockets

#### `/api/ws/events`

Connect to this WebSocket endpoint to receive real-time notifications from Fabric Studio in JSON format.

**Base message structure:**
```json
{
  "type": "STRING",
  "timestamp": TIMESTAMP,
  "KEY": VALUE,
  ...
}
```

#### Monitoring Event

```json
{
  "type": "monitoring.runtime",
  "timestamp": <seconds since epoch>,
  ...
}
```

#### Task Events

**New task:**
```json
{
  "type": "task",
  "action": "new",
  "task": TASK_ID,
  "parent": PARENT_TASK_ID,
  "id": null,
  "model": null,
  "name": "STRING",
  "timestamp": "<ISO UTC timestamp>",
  "pid": MONITORING_TASK_PID
}
```

**Task return:**
```json
{
  "type": "task",
  "action": "return",
  "task": TASK_ID,
  "parent": PARENT_TASK_ID,
  "id": null,
  "model": null,
  "name": "STRING",
  "timestamp": "<ISO UTC timestamp>",
  "pid": TASK_PID
}
```

#### Log Event

```json
{
  "type": "log",
  "id": OBJECT_ID,
  "model": "OBJECT_MODEL",
  "task": TASK_ID,
  "level": "print",
  "message": "STRING",
  "timestamp": "<ISO UTC timestamp>",
  "linenb": LINE_NUMBER,
  "pid": TASK_PID
}
```

---

## 5.2 CLI Reference

All CLI commands follow this pattern: `NAMESPACE SUBCOMMAND [OPTIONS] [ARGS]`

**Top-level namespaces:**

| Namespace | Description |
|-----------|-------------|
| `cli` | CLI session settings |
| `debug` | Django debugging utilities |
| `model` | Manage the Fabric topology model (desired state) |
| `runtime` | Interact with running/installed objects (actual state) |
| `system` | System administration |
| `task` | Task management |

---

### CLI General Commands

```
cli [-h] [{restart,prefix,ctx,verbose,debug,fork,terminal,settings,json}]
```

| Subcommand | Description |
|------------|-------------|
| `restart` | Restart the CLI session |
| `prefix` | Manage command-line prefix options |
| `ctx` | Show execution context |
| `verbose` | Manage verbose level |
| `debug` | Manage debug flag |
| `fork` | Propagate debug/verbose flags on command fork |
| `terminal` | Manage the terminal (resize, reset) |
| `settings` | View execution settings |
| `json` | Toggle JSON output mode |

#### `cli json <STATE>`
```
cli json [-h] <STATE>
STATE: 'enable' | 'disable'
```
Toggle JSON output. Required before using CLI output programmatically.

#### `cli ctx get`
```
cli ctx get [-h]
```
Get current execution context.

#### `cli debug [<STATE>]`
```
cli debug [-h] [<STATE>]
STATE: 'enable' | 'disable'
Return: str | None
```

#### `cli fork [<STATE>]`
```
cli fork [-h] [<STATE>]
STATE: 'enable' | 'disable'
Return: str
```
Propagate debug and verbose flags on command fork.

#### `cli prefix set [<ARGS> ...]`
```
cli prefix set [-h] [<ARGS> ...]
```
Define prefix options added before every command.

#### `cli prefix get`
```
cli prefix get [-h]
```

#### `cli verbose set <LEVEL>`
```
cli verbose set [-h] <LEVEL>
LEVEL: int
```

#### `cli terminal resize`
```
cli terminal resize [-h]
```
Resize serial terminal to match real columns and rows. **Warning:** may break paste.

#### `cli terminal reset`
```
cli terminal reset [-h]
```
Restart TTY console.

#### `cli settings get <NAME>`
```
cli settings get [-h] <NAME>
```

#### `cli restart`
```
cli restart [-h]
```

---

### DEBUG Commands

```
debug [-h] [{django,whoami}]
```

| Subcommand | Description |
|------------|-------------|
| `django` | Django debugging |
| `whoami` | Show current authenticated user |

#### `debug whoami`
```
debug whoami [-h]
```

#### `debug django urls [OPTIONS] [<PREFIX>] [<RESOLVER>]`
```
debug django urls [-h] [--file FILE] [--app-names APP_NAMES] [<PREFIX>] [<RESOLVER>]
```
Flatten all URLs from the Django URL resolver.

---

### MODEL Commands

The `model` namespace manages **desired-state** objects — the topology definition before deployment.

```
model [-h] [{fabric,host,network,port,switch,router,cable,vm,device,tc,debug,object,diagnose}]
```

All model commands follow a common CRUD pattern:

| Operation | Signature | Description |
|-----------|-----------|-------------|
| `list` | `model <OBJ> list [--select FILTER] [--exclude FILTER] [--order-by FIELDS] [--limit INT] [--page INT] [--page-of ID] [--related-fields FIELDS]` | List objects with optional filtering and pagination |
| `detail` | `model <OBJ> detail [--related-fields FIELDS] <ID>` | Get full detail of one object |
| `create` | `model <OBJ> create [--related-fields FIELDS] <OBJECT_JSON>` | Create a new object |
| `update` | `model <OBJ> update [--update-fields FIELDS] [--related-fields FIELDS] <ID> <OBJECT_JSON>` | Update an existing object |
| `delete` | `model <OBJ> delete [--interactive] [--yes] <ID>` | Delete an object |

---

#### model cable

```
model cable [-h] [{list,detail,create,delete,update,connect}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model cable list [FILTER_OPTS]` | List cables. Returns `list[model.cable]\|page[model.cable]` |
| `detail` | `model cable detail [--related-fields ...] <cable>` | Detail view. Returns `model.cable` |
| `create` | `model cable create [--auto-disconnect\|--no-auto-disconnect] [--auto-address\|--no-auto-address] [--auto-params\|--no-auto-params] [--related-fields ...] <cable>` | Create cable. Returns `model.cable` |
| `update` | `model cable update [--auto-disconnect] [--update-fields ...] [--related-fields ...] <cable> <OBJECT>` | Update cable. Returns `model.cable` |
| `delete` | `model cable delete [--interactive] [--yes] <cable>` | Delete cable. Returns `model.cable` |
| `connect` | `model cable connect [--auto-disconnect] [--auto-address] [--auto-params] <DEVICE1> <DEVICE2>` | Connect first free ports between two devices. For native switches, missing ports are auto-created. |

---

#### model debug

```
model debug [-h] [{tc,reader,fabric}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `fabric export` | `model debug fabric export [--fabric] [--include-cfg] [--include-local-repo] [--include-remote-repo] [--include-licenses] [FILTER_OPTS] [<OUTPUT>]` | Save Fabrics as ZIP archive or cfg. Returns `optional[IOBase]` |
| `fabric import` | `model debug fabric import [--rename\|--no-rename] [--as AS] [<INPUT>]` | Import Fabrics from fabric input. Returns `list[*]` |
| `reader` | `model debug reader [<INPUT>]` | Reader output of fabric import. Returns `list[*]` |
| `tc cleanup` | `model debug tc cleanup` | Remove dangling traffic control. Returns `list[model.trafficcontrol]\|page[model.trafficcontrol]` |

---

#### model device

```
model device [-h] [{config,list,detail}]
```

**Device sub-commands:**

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model device list [FILTER_OPTS]` | List devices. Returns `list[model.device]\|page[model.device]` |
| `detail` | `model device detail [--related-fields ...] <device>` | Detail view. Returns `model.device` |
| `config list` | `model device config list [FILTER_OPTS]` | List device configs. Returns `list[model.deviceconfig]\|page[model.deviceconfig]` |
| `config detail` | `model device config detail [--related-fields ...] <deviceconfig>` | Detail view. Returns `model.deviceconfig` |
| `config create` | `model device config create` | (via form or JSON) |
| `config update` | `model device config update [--update-fields ...] [--related-fields ...] <deviceconfig> <OBJECT>` | Returns `model.deviceconfig` |
| `config delete` | `model device config delete [--interactive] [--yes] <deviceconfig>` | Returns `model.deviceconfig` |
| `config export` | `model device config export <DEVICECONFIG> [<OUTPUT>]` | Returns `optional[IOBase]` |
| `config import` | `model device config import [--overwrite] [--erase-source] <INPUT> <OBJECT>` | Upload VM config. Returns `model.deviceconfig` |
| `config is-local` | `model device config is-local <DEVICECONFIG>` | Verify VM config file exists locally. Returns `Path` |

---

#### model diagnose

```
model diagnose [-h] [{fabric}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `fabric storage config` | `model diagnose fabric storage config <FABRIC>` | Print `ls -al` of the fabric config storage |

---

#### model fabric

```
model fabric [-h] [{clone,sanity,export,import,remote,documentation,list,detail,layout,create,delete,update,batch,install,host,network,switch,router,cable,device}]
```

**Core operations:**

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model fabric list [FILTER_OPTS]` | List fabrics. Returns `list[model.fabric]\|page[model.fabric]` |
| `detail` | `model fabric detail [--related-fields ...] <fabric>` | Detail view. Returns `model.fabric` |
| `create` | `model fabric create [--related-fields ...] <fabric>` | Create from template. Returns `model.fabric` |
| `update` | `model fabric update [--update-fields ...] [--related-fields ...] <fabric> <OBJECT>` | Update fabric. Returns `model.fabric` |
| `delete` | `model fabric delete [--interactive] [--yes] <fabric>` | Delete fabric. Returns `model.fabric` |
| `clone` | `model fabric clone ...` | Clone a fabric |
| `export` | `model fabric export [OUTPUT]` | Export fabric. Returns `optional[IOBase]` |
| `import` | `model fabric import [--rename] [--as AS] [<INPUT>]` | Create fabric from template file. Deletes template on success by default. |
| `batch delete` | `model fabric batch delete [FILTER_OPTS]` | Batch delete Fabrics. Returns `list[model.fabric]` |
| `sanity check` | `model fabric sanity check <FABRIC>` | Returns `dict` |
| `layout get` | `model fabric layout get <FABRIC>` | Returns `list` |
| `layout set` | `model fabric layout set <FABRIC> <LAYOUT>` | |
| `layout gui get` | `model fabric layout gui get <FABRIC>` | Returns `dict` |
| `layout gui set` | `model fabric layout gui set <FABRIC> <LAYOUT>` | |

**Remote import:**

| Command | Description |
|---------|-------------|
| `remote import fabric-studio` | Import from another Fabric Studio |
| `remote import fortipoc` | Import from FortiPoC |

**Documentation:**

| Command | Description |
|---------|-------------|
| `documentation download` | Download fabric documentation. Returns `str` |

**Fabric-scoped cable:**

| Command | Description |
|---------|-------------|
| `fabric cable list <FABRIC> [FILTER_OPTS]` | List cables in fabric. Returns `list[model.cable]\|page[model.cable]` |
| `fabric cable create <FABRIC> <cable>` | Create cable in fabric |
| `fabric cable connect <FABRIC> <DEVICE1> <DEVICE2>` | Connect first free ports |

**Fabric-scoped device config:**

| Command | Description |
|---------|-------------|
| `fabric device config list <FABRIC> [FILTER_OPTS]` | List device configs |
| `fabric device config detail <FABRIC> <deviceconfig>` | Detail view |
| `fabric device config update <FABRIC> <deviceconfig> <OBJECT>` | Update |
| `fabric device config delete <FABRIC> <deviceconfig>` | Delete |
| `fabric device config is-local <FABRIC> <DEVICECONFIG>` | Verify local existence |

**Fabric-scoped device port traffic control:**

| Command | Description |
|---------|-------------|
| `fabric device port tc detail <FABRIC> <DEVICE> <PORT> <tc>` | Detail view of traffic control |
| `fabric device port tc update <FABRIC> <DEVICE> <PORT> <tc> <OBJECT>` | Update traffic control |
| `fabric device tc list <FABRIC> <DEVICE> [FILTER_OPTS]` | List traffic controls |

**Fabric-scoped host:**

| Command | Description |
|---------|-------------|
| `fabric host detail <FABRIC> <host>` | Detail view of System Host |
| `fabric host update <FABRIC> <host> <OBJECT>` | Update System Host |
| `fabric host sync <FABRIC> <host> [--drop]` | Synchronize with available System Host ports |
| `fabric host port list <FABRIC> <host> [FILTER_OPTS]` | List host ports |
| `fabric host port detail <FABRIC> <hostport>` | Detail view |
| `fabric host port create <FABRIC> <HOST> [<HOSTPORT>]` | Create new host internal port |
| `fabric host port delete <FABRIC> <HOST>` | Delete last internal port |
| `fabric host port update <FABRIC> <hostport> <OBJECT>` | Update inner system port connection |
| `fabric host port redirect list <FABRIC> <HOST> [FILTER_OPTS]` | List port redirects |
| `fabric host port redirect create <FABRIC> <HOST> <portredirect>` | Create port redirect |
| `fabric host port redirect detail <FABRIC> <HOST> <PORTREDIRECT>` | Detail view |
| `fabric host port redirect update <FABRIC> <HOST> <PORTREDIRECT> <OBJECT>` | Update |
| `fabric host port redirect delete <FABRIC> <HOST> <PORTREDIRECT>` | Delete |

**Fabric-scoped network:**

| Command | Description |
|---------|-------------|
| `fabric network list <FABRIC> [FILTER_OPTS]` | List networks |
| `fabric network detail <FABRIC> <network>` | Detail view |
| `fabric network create <FABRIC> <network>` | Create network |
| `fabric network update <FABRIC> <network> <OBJECT>` | Update |
| `fabric network delete <FABRIC> <network>` | Delete |

**Fabric-scoped router:**

| Command | Description |
|---------|-------------|
| `fabric router list <FABRIC> [FILTER_OPTS]` | List routers |
| `fabric router detail <FABRIC> <router>` | Detail view |
| `fabric router create <FABRIC> <router>` | Create router |
| `fabric router update <FABRIC> <router> <OBJECT>` | Update |
| `fabric router delete <FABRIC> <router>` | Delete |
| `fabric router port list <FABRIC> <ROUTER> [FILTER_OPTS]` | List router ports |
| `fabric router port detail <FABRIC> <routerport>` | Detail view |
| `fabric router port create <FABRIC> <ROUTER> [<ROUTERPORT>]` | Create port |
| `fabric router port delete <FABRIC> <ROUTER>` | Delete last port |
| `fabric router port update <FABRIC> <routerport> <OBJECT>` | Update |

**Fabric-scoped switch:**

| Command | Description |
|---------|-------------|
| `fabric switch list <FABRIC> [FILTER_OPTS]` | List switches |
| `fabric switch detail <FABRIC> <switch>` | Detail view |
| `fabric switch create <FABRIC> <switch>` | Create switch |
| `fabric switch update <FABRIC> <switch> <OBJECT>` | Update |
| `fabric switch delete <FABRIC> <switch>` | Delete |
| `fabric switch port list <FABRIC> <SWITCH> [FILTER_OPTS]` | List switch ports |
| `fabric switch port detail <FABRIC> <switchport>` | Detail view |
| `fabric switch port create <FABRIC> <SWITCH> [<SWITCHPORT>]` | Create port |
| `fabric switch port delete <FABRIC> <SWITCH>` | Delete last port |
| `fabric switch port update <FABRIC> <switchport> <OBJECT>` | Update |

**Fabric-scoped VM:**

| Command | Description |
|---------|-------------|
| `fabric vm list <FABRIC> [FILTER_OPTS]` | List VMs |
| `fabric vm detail <FABRIC> <vm>` | Detail view |
| `fabric vm create <FABRIC> <vm>` | Create VM. Mandatory fields: `fabric` ID, `firmware` ID |
| `fabric vm update <FABRIC> <vm> <OBJECT>` | Update VM |
| `fabric vm delete <FABRIC> <vm>` | Delete VM |
| `fabric vm clone <FABRIC> <vm>` | Clone VM |
| `fabric vm port list` | List VM ports |
| `fabric vm port detail` | Detail |
| `fabric vm port create <FABRIC> <VM>` | Create port as new latest port |
| `fabric vm port delete <FABRIC> <VM>` | Delete last port |
| `fabric vm port update` | Update VM port |
| `fabric vm disk list` | List VM disks |
| `fabric vm disk detail` | Detail |
| `fabric vm disk create <FABRIC> <VM>` | Add extra disk |
| `fabric vm disk delete <FABRIC> <VM>` | Remove last extra disk |
| `fabric vm disk update` | Update VM disk |
| `fabric vm access list` | List VM accesses |
| `fabric vm access detail` | Detail |
| `fabric vm access create` | Create VM access |
| `fabric vm access update` | Update |
| `fabric vm access delete` | Delete |
| `fabric vm access order` | Reorder VM accesses |
| `fabric vm license detail` | Detail view of VM license |
| `fabric vm license update` | Update VM license |
| `fabric vm license reset` | Reset to default values |
| `fabric vm license release` | Release VM license |
| `fabric vm parameters detail` | Detail view of VM parameters |
| `fabric vm parameters update` | Update VM parameters |
| `fabric vm parameters reset` | Reset parameters to defaults |
| `fabric install policy detail` | View install policy |
| `fabric install policy update` | Update install policy |

---

#### model host

```
model host [-h] [{list,detail,update,sync,port}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model host list [FILTER_OPTS]` | List System Hosts. Returns `list[model.host]\|page[model.host]` |
| `detail` | `model host detail [--related-fields ...] <host>` | Detail view. Returns `model.host` |
| `update` | `model host update [--update-fields ...] [--related-fields ...] <host> <OBJECT>` | Update System Host. Returns `model.host` |
| `sync` | `model host sync [--drop\|--no-drop] <HOST>` | Synchronize with available System Host ports. `--drop`: drop extra ports even if connected |
| `port list` | `model host port list [FILTER_OPTS]` | List System Ports. Returns `list[model.hostport]\|page[model.hostport]` |
| `port detail` | `model host port detail [--related-fields ...] <hostport>` | Detail view. Returns `model.hostport` |
| `port create` | `model host port create <HOST> [<HOSTPORT>]` | Create new host internal port (name and index are automatic). Returns `model.hostport` |
| `port delete` | `model host port delete <HOST>` | Delete last internal port. Returns `model.hostport` |
| `port update` | `model host port update [--update-fields ...] [--related-fields ...] <hostport> <OBJECT>` | Update inner system port connection. Returns `model.hostport` |
| `port redirect list` | `model host port redirect list [FILTER_OPTS] <HOST>` | List port redirects. Returns `list[model.portredirect]\|page[model.portredirect]` |
| `port redirect detail` | `model host port redirect detail [--related-fields ...] <HOST> <PORTREDIRECT>` | Detail view. Returns `model.portredirect` |
| `port redirect create` | `model host port redirect create [--related-fields ...] <HOST> <portredirect>` | Create port redirect. Returns `model.portredirect` |
| `port redirect update` | `model host port redirect update [--update-fields ...] [--related-fields ...] <HOST> <PORTREDIRECT> <OBJECT>` | Update. Returns `model.portredirect` |
| `port redirect delete` | `model host port redirect delete [--interactive] [--yes] <HOST> <PORTREDIRECT>` | Delete. Returns `model.portredirect` |

---

#### model network

```
model network [-h] [{list,detail,create,delete,update}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model network list [FILTER_OPTS]` | List networks. Returns `list[model.network]\|page[model.network]` |
| `detail` | `model network detail [--related-fields ...] <network>` | Detail view. Returns `model.network` |
| `create` | `model network create [--related-fields ...] <network>` | Create network. Returns `model.network` |
| `update` | `model network update [--update-fields ...] [--related-fields ...] <network> <OBJECT>` | Update network. Returns `model.network` |
| `delete` | `model network delete [--interactive] [--yes] <network>` | Delete network. Returns `model.network` |

---

#### model object

```
model object [-h] [{diff,detail}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `detail` | `model object detail [--related-fields ...] <MODEL> <IDS> [<IDS> ...]` | Get detail view of any object by model + ID(s). The deepest subclass is returned. Returns `list[*]` |
| `diff` | `model object diff <MODEL> <ID>` | Compare "model" (desired) vs "runtime" (actual) state. Returns `dict` |

**`model object diff` response structure:**

```json
{
  "model": { ... },    // desired state object (or null)
  "runtime": { ... }, // actual state object (or null)
  "diff": {
    "FIELD_NAME": "install" | "uninstall" | "synchronize"
  }
}
```

**Apply methods:**

| Method | Meaning |
|--------|---------|
| `install` | Object must be installed |
| `uninstall` | Object must be uninstalled |
| `synchronize` | Object can be synchronized without uninstall/install cycle |

For `model.fabric`, the `diff.devices` key contains device status by ID:

| Status | Meaning |
|--------|---------|
| `added` | Device is in "model" but not yet in "runtime" |
| `removed` | Device is in "runtime" but no longer in "model" |
| `modified` | Device differs between "model" and "runtime" |

**Specific diff algorithms** are implemented for: `model.fabric`, `model.host`, `model.switch`, `model.router`, `model.vm`. All others use a generic algorithm.

---

#### model port

```
model port [-h] [{redirect,list,detail}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model port list [FILTER_OPTS]` | List ports. Returns `list[model.port]\|page[model.port]` |
| `detail` | `model port detail [--related-fields ...] <port>` | Detail view. Returns `model.port` |
| `redirect list` | `model port redirect list [FILTER_OPTS]` | List port redirects. Returns `list[model.portredirect]\|page[model.portredirect]` |
| `redirect detail` | `model port redirect detail [--related-fields ...] <portredirect>` | Detail view. Returns `model.portredirect` |
| `redirect create` | `model port redirect create [--related-fields ...] <portredirect>` | Create. Returns `model.portredirect` |
| `redirect update` | `model port redirect update [--update-fields ...] [--related-fields ...] <portredirect> <OBJECT>` | Update. Returns `model.portredirect` |
| `redirect delete` | `model port redirect delete [--interactive] [--yes] <portredirect>` | Delete. Returns `model.portredirect` |

---

#### model router

```
model router [-h] [{list,detail,create,delete,update,port}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model router list [FILTER_OPTS]` | Returns `list[model.router]\|page[model.router]` |
| `detail` | `model router detail [--related-fields ...] <router>` | Returns `model.router` |
| `create` | `model router create [--ports-count INT] [--related-fields ...] <router>` | Returns `model.router` |
| `update` | `model router update [--update-fields ...] [--related-fields ...] <router> <OBJECT>` | Returns `model.router` |
| `delete` | `model router delete [--interactive] <router>` | Returns `model.router` |
| `port list` | `model router port list [FILTER_OPTS]` | Returns `list[model.routerport]\|page[model.routerport]` |
| `port detail` | `model router port detail [--related-fields ...] <routerport>` | Returns `model.routerport` |
| `port create` | `model router port create <ROUTER> [<ROUTERPORT>]` | Returns `model.routerport` |
| `port delete` | `model router port delete <ROUTER>` | Delete last port. Returns `model.routerport` |
| `port update` | `model router port update [--update-fields ...] [--related-fields ...] <routerport> <OBJECT>` | Returns `model.routerport` |

---

#### model switch

```
model switch [-h] [{list,detail,create,delete,update,port,local-port}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model switch list [FILTER_OPTS]` | Returns `list[model.switch]\|page[model.switch]` |
| `detail` | `model switch detail [--related-fields ...] <switch>` | Returns `model.switch` |
| `create` | `model switch create [--ports-count INT] [--related-fields ...] <switch>` | Returns `model.switch` |
| `update` | `model switch update [--update-fields ...] [--related-fields ...] <switch> <OBJECT>` | Returns `model.switch` |
| `delete` | `model switch delete [--interactive] <switch>` | Returns `model.switch` |
| `port list` | `model switch port list [FILTER_OPTS]` | Returns `list[model.switchport]\|page[model.switchport]` |
| `port detail` | `model switch port detail [--related-fields ...] <switchport>` | Returns `model.switchport` |
| `port create` | `model switch port create <SWITCH> [<SWITCHPORT>]` | Returns `model.switchport` |
| `port delete` | `model switch port delete <SWITCH>` | Delete last port. Returns `model.switchport` |
| `port update` | `model switch port update [--update-fields ...] [--related-fields ...] <switchport> <OBJECT>` | Returns `model.switchport` |
| `local-port list` | `model switch local-port list [FILTER_OPTS]` | Returns `list[model.switchlocalport]\|page[model.switchlocalport]` |
| `local-port detail` | `model switch local-port detail [--related-fields ...] <switchlocalport>` | Returns `model.switchlocalport` |
| `local-port update` | `model switch local-port update [--update-fields ...] [--related-fields ...] <switchlocalport> <OBJECT>` | Returns `model.switchlocalport` |

---

#### model tc (Traffic Control)

```
model tc [-h] [{list,detail,update}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model tc list [FILTER_OPTS]` | List traffic controls. Returns `list[model.trafficcontrol]\|page[model.trafficcontrol]` |
| `detail` | `model tc detail [--related-fields ...] <trafficcontrol>` | Detail view. Returns `model.trafficcontrol` |
| `update` | `model tc update [--update-fields ...] [--related-fields ...] <trafficcontrol> <OBJECT>` | Update traffic control. Returns `model.trafficcontrol` |

---

#### model vm

```
model vm [-h] [{list,detail,meta,create,delete,update,history,clone,port,disk,access,install,parameters,license}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `model vm list [FILTER_OPTS]` | List VMs. Returns `list[model.vm]\|page[model.vm]` |
| `detail` | `model vm detail [--related-fields ...] <vm>` | Detail view. Returns `model.vm` |
| `create` | `model vm create [--related-fields ...] <vm>` | Create VM. Mandatory: `fabric` ID + `firmware` ID. Returns created VM and ports. Returns `model.vm` |
| `update` | `model vm update [--update-fields ...] [--related-fields ...] <vm> <OBJECT>` | Returns `model.vm` |
| `delete` | `model vm delete [--interactive] [--yes] <vm>` | Returns `model.vm` |
| `clone` | `model vm clone <vm>` | Returns `model.vm` |
| `meta` | `model vm meta <VM> [<XPATH>]` | Return firmware meta XML or selected node(s) via XPath |
| `history` | `model vm history <vm>` | View VM history |
| `port list` | `model vm port list [FILTER_OPTS]` | Returns `list[model.vmport]\|page[model.vmport]` |
| `port detail` | `model vm port detail [--related-fields ...] <vmport>` | Returns `model.vmport` |
| `port create` | `model vm port create <VM>` | Create port as the new latest port. Returns `model.vmport` |
| `port delete` | `model vm port delete <VM>` | Delete last port. Returns `model.vmport` |
| `port update` | `model vm port update [--update-fields ...] [--related-fields ...] <vmport> <OBJECT>` | Returns `model.vmport` |
| `disk list` | `model vm disk list [FILTER_OPTS]` | Returns `list[model.vmdisk]\|page[model.vmdisk]` |
| `disk detail` | `model vm disk detail [--related-fields ...] <vmdisk>` | Returns `model.vmdisk` |
| `disk create` | `model vm disk create <VM>` | Add extra disk. Returns `model.vmdisk` |
| `disk delete` | `model vm disk delete <VM>` | Remove last extra disk. Returns `model.vmdisk` |
| `disk update` | `model vm disk update [--update-fields ...] [--related-fields ...] <vmdisk> <OBJECT>` | Returns `model.vmdisk` |
| `access list` | `model vm access list [FILTER_OPTS]` | Returns `list[model.vmaccess]\|page[model.vmaccess]` |
| `access detail` | `model vm access detail [--related-fields ...] <vmaccess>` | Returns `model.vmaccess` |
| `access create` | `model vm access create [--related-fields ...] <vmaccess>` | Returns `model.vmaccess` |
| `access update` | `model vm access update [--update-fields ...] [--related-fields ...] <vmaccess> <OBJECT>` | Returns `model.vmaccess` |
| `access delete` | `model vm access delete [--interactive] [--yes] <vmaccess>` | Returns `model.vmaccess` |
| `access order` | `model vm access order <VM> <ORDER>` | Reorder VM accesses. Returns `list[model.vmaccess]` |
| `license detail` | `model vm license detail <vm>` | Returns `model.vmlicense` |
| `license update` | `model vm license update <vm> <OBJECT>` | Returns `model.vmlicense` |
| `license reset` | `model vm license reset <vm>` | Reset license to default values |
| `license release` | `model vm license release <vm>` | Release VM license |
| `parameters detail` | `model vm parameters detail <vm>` | Returns `model.vmparameters` |
| `parameters update` | `model vm parameters update <vm> <OBJECT>` | Returns `model.vmparameters` |
| `parameters reset` | `model vm parameters reset <vm>` | Reset parameters to default values |
| `install after detail` | `model vm install after detail <vm>` | View install after constraints. Returns `model.installafter` |
| `install after update` | `model vm install after update <vm> <OBJECT>` | Update install after constraints |
| `install after reset` | `model vm install after reset <vm>` | Remove all install after constraints |

---

### RUNTIME Commands

The `runtime` namespace interacts with **actual running state** — installed/deployed objects.

```
runtime [-h] [{license,fabric,device,vm,expert,config,switch,router,host,cable,diagnose,tc}]
```

Runtime mirrors the model namespace structure but operates on live objects. Key differences:
- `runtime` has **no create/delete** for most objects (topology is defined in `model`)
- `runtime` adds **operational commands** (start, stop, install, console, etc.)

**Top-level runtime namespaces:**

| Namespace | Description |
|-----------|-------------|
| `runtime cable` | Manage running cables (list, detail, break, repair) |
| `runtime config` | List/detail device configs |
| `runtime device` | Manage running devices |
| `runtime diagnose` | Runtime diagnostics |
| `runtime expert` | Expert/advanced runtime operations |
| `runtime fabric` | Manage installed fabrics |
| `runtime host` | Manage system hosts at runtime |
| `runtime license` | Runtime license management |
| `runtime router` | Manage running routers |
| `runtime switch` | Manage running switches |
| `runtime tc` | Manage traffic control at runtime |
| `runtime vm` | Manage running VMs |

#### runtime cable

```
runtime cable [-h] [{list,detail,break,repair}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `runtime cable list [FILTER_OPTS]` | Returns `list[runtime.cable]\|page[runtime.cable]` |
| `detail` | `runtime cable detail [--related-fields ...] <cable>` | Returns `model.cable` |
| `break` | `runtime cable break <CABLE>` | Break cable without removing it. Ports set **down** on Fabric Studio side. |
| `repair` | `runtime cable repair <CABLE>` | Repair broken cable. Ports set **up** on Fabric Studio side. |

#### runtime config

```
runtime config [-h] [{list,detail}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `runtime config list [FILTER_OPTS]` | List device configs. Returns `list[model.deviceconfig]\|page[model.deviceconfig]` |
| `detail` | `runtime config detail [--related-fields ...] <deviceconfig>` | Returns `model.deviceconfig` |

---

### SYSTEM Commands

```
system [-h] [{account,certificate,db,debug,diagnose,disclaimer,disk,execute,expert,firewall,forticloud,hostname,information,interfaces,kernel,license,log,mgmt,monitoring,oauth2,openapi,ot,parameter,preferences,repository,samba,security,support,template,upgrade,user,version,webserver}]
```

**System sub-namespaces:**

| Namespace | Description |
|-----------|-------------|
| `system account` | User account management |
| `system certificate` | Manage certificates |
| `system db` | Database operations |
| `system debug` | System debug utilities |
| `system diagnose` | System diagnostics |
| `system disclaimer` | Show disclaimer. Returns `str` |
| `system disk` | Disk management |
| `system execute` | Execute general system commands |
| `system expert` | Expert/advanced system operations |
| `system firewall` | Firewall management |
| `system forticloud` | FortiCloud integration |
| `system hostname` | Hostname management |
| `system information` | System detailed information. Returns `SystemInformation` |
| `system interfaces` | Fabric Studio network interfaces |
| `system kernel` | Kernel management |
| `system license` | Manage local licenses and server license |
| `system log` | Log management |
| `system mgmt` | Management interface operations |
| `system monitoring` | Monitoring management |
| `system oauth2` | OAuth2 application management |
| `system openapi` | OpenAPI spec management |
| `system ot` | OT operations |
| `system parameter` | System parameter management |
| `system preferences` | Preferences management |
| `system repository` | Repository management |
| `system samba` | Samba share management |
| `system security` | Security management |
| `system support` | Support utilities |
| `system template` | Template management |
| `system upgrade` | System upgrade |
| `system user` | User management |
| `system version` | Get product version. Returns `Tag` |
| `system webserver` | Web server management |

---

### TASK Commands

```
task [-h] [{detail,device,fabric,kill,kill-all,list,log,purge,queue,refresh-all,wait}]
```

| Command | Signature | Description |
|---------|-----------|-------------|
| `list` | `task list` | List all tasks. Returns `list[task.task]` |
| `detail` | `task detail <TASK_ID>` | Show a running task status |
| `log` | `task log <TASK_ID>` | Get task log. Returns `IOBase` |
| `kill` | `task kill <TASK_ID>` | Stop a running task |
| `kill-all` | `task kill-all` | Stop all running tasks. Returns `list[task.task]` |
| `purge` | `task purge` | Purge system and old fabric task logs. Always keeps current installed fabric logs. Returns `list[int]` |
| `queue` | `task queue <TASK_INSTANCE>` | Queue a new task. Returns `task.task` |
| `refresh-all` | `task refresh-all` | Returns `list[task.task]` |
| `wait` | `task wait <TASK_ID>` | Wait for a task to complete |
| `device` | `task device ...` | Device-related task management |
| `fabric` | `task fabric ...` | Fabric-related task management |

---

## 5.4 OAuth2 Authorization Grants

> Based on [Django OAuth Toolkit](https://django-oauth-toolkit.readthedocs.io/) and [RFC6749](https://tools.ietf.org/html/rfc6749#section-1.3).

Two supported grant types:

| Grant Type | Use Case |
|------------|----------|
| **Client Credential** | Machine-to-machine (M2M), server-side automation |
| **Authorization Code** | Web/mobile apps, third-party integrations |

> **Warning:** All examples use `curl -k` due to Fabric Studio's default self-signed certificate. **Do NOT use `-k` in production.**

---

### 5.4.1 Client Credential

Suitable for machine-to-machine authentication. The access token is automatically associated to the application user.

#### Step 1: Create Application and Credential

**Via CLI:**
```sh
$ system oauth2 application default create service-worker
# Output: base64-encoded CREDENTIAL string
CREDENTIAL=<base64_credential>
```

**Via Web Interface:**
1. Navigate to `/oauth2/applications/register/`
2. Fill the form:
   - **Client type:** Confidential
   - **Authorization grant type:** Client credentials
   - **Algorithm:** HMAC with SHA-2 256
3. Note the **Client ID** and **Client Secret**

**Create base64 credential:**
```python
import base64
client_id = "${ID}"
secret = "${SECRET}"
credential = "{0}:{1}".format(client_id, secret)
credential_enc = base64.b64encode(credential.encode("utf-8")).decode("utf-8")
print(f'CREDENTIAL={credential_enc}')
```

```sh
# Store as environment variable
CREDENTIAL=<base64_encoded_id:secret>
```

#### Step 2: Get Access Token

```sh
curl -k -X POST \
  -H "Authorization: Basic ${CREDENTIAL}" \
  -H "Cache-Control: no-cache" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  "https://${FABRIC_HOST}/oauth2/token/"
```

**Response:**
```json
{
  "access_token": "GYeR7cpPFRYSMN3paSkB7utwdoYDUT",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write"
}
```

#### Step 3: Use the Access Token

```sh
BEARER=<access_token>
curl -k -X GET \
  -H "Authorization: Bearer ${BEARER}" \
  "https://${FABRIC_HOST}/api/v1/model/fabric"
```

---

### 5.4.2 Authorization Code

Best suited for web/mobile apps. Uses PKCE (Proof Key for Code Exchange) for security.

> **Warning:** You have **1 minute** to complete the authorization code validation after user approval.

#### Step 1: Register Application

1. Navigate to `/oauth2/applications/register/`
2. Fill the form:
   - **Client type:** Confidential
   - **Authorization grant type:** Authorization code
   - **Redirect URIs:** `http://127.0.0.1:8000/noexist/callback`
   - **Algorithm:** HMAC with SHA-2 256
3. Store the **Client ID** and **Client Secret**

```sh
FABRIC_HOST=<your-fabric-studio-address>
ID=<client_id>
SECRET=<client_secret>
```

#### Step 2: Generate PKCE Code Challenge

```python
import random, string, base64, hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for _ in range(random.randint(43, 128)))
code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
code_challenge = hashlib.sha256(code_verifier).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').rstrip('=')

print(f'CODE_VERIFIER={code_verifier.decode("utf-8")}')
print(f'CODE_CHALLENGE={code_challenge}')
```

```sh
CODE_VERIFIER=<generated_verifier>
CODE_CHALLENGE=<generated_challenge>
```

#### Step 3: Get Authorization Code

Open this URL in a browser:

```
https://${FABRIC_HOST}/oauth2/authorize/?response_type=code&code_challenge=${CODE_CHALLENGE}&code_challenge_method=S256&client_id=${ID}&redirect_uri=http://127.0.0.1:8000/noexist/callback
```

**Parameters:**

| Parameter | Value |
|-----------|-------|
| `response_type` | `code` |
| `code_challenge` | Your generated challenge |
| `code_challenge_method` | `S256` |
| `client_id` | Your application's client ID |
| `redirect_uri` | `http://127.0.0.1:8000/noexist/callback` |

After authorizing, you'll be redirected to (expect a 404/unreachable page):
```
http://127.0.0.1:8000/noexist/callback?code=<AUTHORIZATION_CODE>
```

```sh
CODE=<extracted_authorization_code>
```

#### Step 4: Exchange Code for Access Token

```sh
curl -k -X POST \
  -H "Cache-Control: no-cache" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  "https://${FABRIC_HOST}/oauth2/token/" \
  -d "client_id=${ID}" \
  -d "client_secret=${SECRET}" \
  -d "code=${CODE}" \
  -d "code_verifier=${CODE_VERIFIER}" \
  -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
  -d "grant_type=authorization_code"
```

**Response:**
```json
{
  "access_token": "AAZe4twJZWlmRYRjnU5pDCpWTLfZLM",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "HNvDQjjsnvDySaK0miwG4lttJEl9yD"
}
```

#### Step 5: Use the Access Token

```sh
BEARER=<access_token>
curl -k -X GET \
  -H "Authorization: Bearer ${BEARER}" \
  "https://${FABRIC_HOST}/api/v1/model/fabric"
```

#### Python Script (Full Flow Automation)

Download: `/_static/rest.py`

This script automates the entire Authorization Code flow:
1. Opens browser for application registration
2. Generates PKCE code verifier and challenge
3. Starts a local callback server on `127.0.0.1:8000`
4. Opens browser for authorization
5. Captures the authorization code via callback
6. Exchanges code for access token
7. Tests the access token against `/api/v1/model/fabric`

---

## Appendix: Common Patterns

### Pagination

All `list` commands support pagination:

```sh
# Get page 2 with 10 items per page
model fabric list --limit 10 --page 2

# Get the page that contains fabric with ID 42
model fabric list --page-of 42
```

### JSON Output Mode

Always enable JSON output before scripting CLI results:

```sh
# cli json enable
```

### Common `--update-fields` Usage

When updating, use `--update-fields` to specify which fields to update (comma-separated):

```sh
model fabric update 1 '{"name": "new-name", "timeout": 300}' --update-fields name,timeout
```

### Base URL for REST API

All REST endpoints are prefixed with:
```
https://<FABRIC_HOST>/api/v1/
```

### Session Check (REST)

```sh
rest -f https://${ADDR}/api/v1/session/check
```
