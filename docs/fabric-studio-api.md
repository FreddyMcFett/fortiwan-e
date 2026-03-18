# Fabric Studio API v2.0.6

Fabric Studio API

- **Contact:** Your local SE
- **License:** [License](https://docs.fabricstudio.net/fabric-studio/license)
- **OpenAPI Version:** 3.0.0

## Tags

- **model**: Everything about 'model' API
- **runtime**: Everything about 'runtime' API
- **session**: Everything about 'session' API
- **system**: Everything about 'system' API
- **task**: Everything about 'task' API

## Standard Response Wrapper

All API responses follow this structure:

```json
{
  "status": "done" | "error",
  "object": <response_data>,
  "errors": { "<field>": ["error message"] },
  "warnings": { "<field>": ["warning message"] },
  "rcode": 0,
  "page": { "number": 1, "total": 1, "size": 50, "count": 10 }
}
```

- `status`: `"done"` for success, `"error"` for failure
- `object`: The response payload (single object or array)
- `errors`/`warnings`: Keyed by field name, or `"global"` for general messages
- `rcode`: Return code (0 = success)
- `page`: Pagination info (present on list endpoints)

---

## API Endpoints

### SESSION Endpoints

#### `GET /api/v1/session/check`
**Verify current session status.**

**Response 200**: `class.sessionstatus` (wrapped in standard response)

---

#### `POST /api/v1/session/close`
**Close the session.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/session/open`
**Open a new session.**

**Request Body** (`application/json`):

- `username`: string **(required)**
- `password`: string **(required)**

**Response 200**: Successful operation.

---

### MODEL Endpoints

#### `GET /api/v1/model/cable`
**List cables.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given cable ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.cable` (wrapped in standard response)

---

#### `POST /api/v1/model/cable`
**Create cable.**

**Request Body** (`application/json`):

- `object`: `model.cable` (see Schemas) **(required)**
- `auto_disconnect`: boolean (default: False)
- `auto_address`: boolean
- `auto_params`: boolean
- `related_fields`: array of str

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `GET /api/v1/model/cable/{cable}`
**Detail view of cable.**

**Parameters:**

- `cable` (path, ) **(required)**: ID of the cable
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `PATCH /api/v1/model/cable/{cable}`
**Update cable.**

**Parameters:**

- `cable` (path, ) **(required)**: ID of the cable

**Request Body** (`application/json`):

- `object`: `model.cable` (see Schemas) **(required)**
- `auto_disconnect`: boolean (default: False)
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `DELETE /api/v1/model/cable/{cable}`
**Delete cable.**

**Parameters:**

- `cable` (path, ) **(required)**: ID of the cable
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `POST /api/v1/model/cable/{device1}/{device2}`
**Connect first free ports between two devices.**

**Parameters:**

- `device1` (path, ) **(required)**
- `device2` (path, ) **(required)**

**Request Body** (`application/json`):

- `auto_disconnect`: boolean (default: False)
- `auto_address`: boolean
- `auto_params`: boolean

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/debug/fabric:export`
**Save Fabrics as a ZIP archive or as a cfg.**

**Parameters:**

- `output` (query, ): Export to this file in local repository
- `fabric` (query, ): export only the fabric configuration, all include_* flags are ignored
- `include_cfg` (query, )
- `include_local_repo` (query, )
- `include_remote_repo` (query, )
- `include_licenses` (query, )
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/debug/fabric:import`
**Import Fabrics from fabric *input*, rename imported Fabric if a Fabric already
exists with same name.**

**Request Body** (`application/json`):

- `input`: string
- `rename`: boolean (default: True)
- `as`: string

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary)
- `rename`: boolean (default: True)
- `as`: string

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/debug/tc`
**Remove dangling traffic control.**

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/model/device`
**List devices.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given device ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/device/{device}`
**Detail view of device.**

**Parameters:**

- `device` (path, ) **(required)**: ID of the device
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/device/config`
**List device configs.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given deviceconfig ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.deviceconfig` (wrapped in standard response)

---

#### `POST /api/v1/model/device/config:import`
**Upload a VM config in the Fabric for VM type.**

**Request Body** (`application/json`):

- `input`: string — VM configuration file **(required)**
- `object`: `model.deviceconfig` (see Schemas) **(required)**
- `overwrite`: boolean (default: False)
- `erase_source`: boolean (default: True)

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary) — VM configuration file **(required)**
- `object`: `model.deviceconfig` (see Schemas) **(required)**
- `overwrite`: boolean (default: False)
- `erase_source`: boolean (default: True)

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `GET /api/v1/model/device/config/{deviceconfig}`
**Detail view of device config.**

**Parameters:**

- `deviceconfig` (path, ) **(required)**: ID of the deviceconfig
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `PATCH /api/v1/model/device/config/{deviceconfig}`
**Update device config.**

**Parameters:**

- `deviceconfig` (path, ) **(required)**: ID of the deviceconfig

**Request Body** (`application/json`):

- `object`: `model.deviceconfig` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `DELETE /api/v1/model/device/config/{deviceconfig}`
**Delete device config.**

**Parameters:**

- `deviceconfig` (path, ) **(required)**: ID of the deviceconfig
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `GET /api/v1/model/device/config/{deviceconfig}:export`

**Parameters:**

- `deviceconfig` (path, ) **(required)**
- `output` (query, ): Export to this file in local repository

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/device/config/{deviceconfig}/is-local`
**Verify VM config file exists locally.**

**Parameters:**

- `deviceconfig` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric`
**List fabrics.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given fabric ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.fabric` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric`
**Create a Fabric from a template.**

**Request Body** (`application/json`):

- `name`: string — the new Fabric name
- `if_exists`: string (default: abort) — What to do when a fabric with same name already exists
- `template`: integer (format: int64) — Must specify a template ID or relative path (eg: templates/myfabric.zip)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric:import`
**Create a fabric from a template file.**

**Request Body** (`application/json`):

- `input`: string **(required)**
- `name`: string
- `if_exists`: string — What to do when a fabric with same name already exists
- `delete_after`: string (default: success) — Do we delete after create
- `interactive`: boolean (default: True)

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary) **(required)**
- `name`: string
- `if_exists`: string — What to do when a fabric with same name already exists
- `delete_after`: string (default: success) — Do we delete after create
- `interactive`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}`
**Detail view of fabric.**

**Parameters:**

- `fabric` (path, ) **(required)**: ID of the fabric
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.fabric` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}`
**Update fabric.**

**Parameters:**

- `fabric` (path, ) **(required)**: ID of the fabric

**Request Body** (`application/json`):

- `object`: `model.fabric` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.fabric` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}`
**Delete fabric.**

**Parameters:**

- `fabric` (path, ) **(required)**: ID of the fabric
- `interactive` (query, )

**Response 200**: `model.fabric` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}:clone`

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `as`: string
- `interactive`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}:export`

**Parameters:**

- `fabric` (path, ) **(required)**
- `output` (query, ): Export to this file in local repository or as streamed file (REST)

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/cable`
**List cables.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given cable ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.cable` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/cable`
**Create cable.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `device1`: integer (format: int64) **(required)**
- `device1port`: integer (format: int64) **(required)**
- `device2`: integer (format: int64) **(required)**
- `device2port`: integer (format: int64) **(required)**
- `auto_disconnect`: boolean (default: False)
- `auto_address`: boolean
- `auto_params`: boolean
- `related_fields`: array of str

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/cable:connect`
**Connect first free ports between two devices.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `device1`: integer (format: int64) **(required)**
- `device2`: integer (format: int64) **(required)**
- `auto_disconnect`: boolean (default: False)
- `auto_address`: boolean
- `auto_params`: boolean

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/device/{device}/port/{port}/tc`
**Detail view of traffic control.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/device/{device}/port/{port}/tc`
**Update traffic control.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.trafficcontrol` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/device/{device}/tc`
**List traffic controls.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given trafficcontrol ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/device/config`
**List device configs.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given deviceconfig ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.deviceconfig` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/device/config/{deviceconfig}`
**Detail view of device config.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `deviceconfig` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/device/config/{deviceconfig}`
**Update device config.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `deviceconfig` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.deviceconfig` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/device/config/{deviceconfig}`
**Delete device config.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `deviceconfig` (path, ) **(required)**
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/device/config/{deviceconfig}:is-local`
**Verify VM config file exists locally.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `deviceconfig` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/host`
**Detail view of System Host.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.host` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/host`
**Update System Host.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.host` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.host` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/host/port`
**List host ports in this Fabric.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given hostport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.hostport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/host/port`
**Delete the last internal port.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/host/port/{hostport}`
**Detail view of System Port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `hostport` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/host/port/{hostport}`
**Update inner system ports connection to the Fabric.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `hostport` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.hostport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/host/port/redirect`
**List port redirects.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given portredirect ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.portredirect` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/host/port/redirect`
**Create port redirect.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/host/port/redirect/{portredirect}`
**Detail view of port redirect.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `portredirect` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/host/port/redirect/{portredirect}`
**Update port redirect.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `portredirect` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/host/port/redirect/{portredirect}`
**Delete port redirect.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `portredirect` (path, ) **(required)**
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/host/port(/{hostport})?`
**Create a new host internal port, name and index are automatic.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `hostport` (path, ) **(required)**

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/install/policy`

**Parameters:**

- `fabric` (path, ) **(required)**

**Response 200**: `model.installpolicy` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/install/policy`

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `install_policy`: `model.installpolicy` (see Schemas) **(required)**

**Response 200**: `model.installpolicy` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/layout`

**Parameters:**

- `fabric` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/fabric/{fabric}/layout`

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `layout`: list **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/layout/gui`

**Parameters:**

- `fabric` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/fabric/{fabric}/layout/gui`

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `layout`: object **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/network`
**List networks.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given network ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.network` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/network`
**Create network.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.network` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `model.network` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/network/{network}`
**Detail view of network.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `network` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.network` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/network/{network}`
**Update network.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `network` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.network` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.network` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/network/{network}`
**Delete network.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `network` (path, ) **(required)**
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.network` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/router`
**List routers.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given router ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.router` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/router`
**Create router.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.router` (see Schemas)
- `ports_count`: integer (format: int64) (default: 10)
- `related_fields`: array of str

**Response 200**: `model.router` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/router/{router}`
**Detail view of router.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.router` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/router/{router}`
**Update router.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.router` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.router` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/router/{router}`
**Delete router.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**
- `interactive` (query, )

**Response 200**: `model.router` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/router/{router}/port`
**List router ports.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given routerport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.routerport` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/router/{router}/port`

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**

**Request Body** (`application/json`):

- `routerport`: `model.routerport` (see Schemas)

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/router/{router}/port`
**Delete the last port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/router/{router}/port/{routerport}`
**Detail view of router port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**
- `routerport` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/router/{router}/port/{routerport}`
**Update router port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `router` (path, ) **(required)**
- `routerport` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.routerport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/switch`
**List Switches.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switch ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switch` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/switch`
**Create switch.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.switch` (see Schemas)
- `ports_count`: integer (format: int64) (default: 10)
- `related_fields`: array of str

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/switch/{switch}`
**Detail view of switch.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/switch/{switch}`
**Update switch.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.switch` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/switch/{switch}`
**Delete switch.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**
- `interactive` (query, )

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/switch/{switch}/port`
**List switch ports.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switchport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switchport` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/switch/{switch}/port`

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**

**Request Body** (`application/json`):

- `switchport`: `model.switchport` (see Schemas)

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/switch/{switch}/port`
**Delete the last port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/switch/{switch}/port/{switchport}`
**Detail view of switch port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**
- `switchport` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/switch/{switch}/port/{switchport}`
**Update switch port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `switch` (path, ) **(required)**
- `switchport` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.switchport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm`
**List VMs.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vm ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vm` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/vm`
**Create a new VM object.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vm` (see Schemas) **(required)**
- `ports_count`: integer (format: int64)
- `auto_connect`: boolean
- `related_fields`: array of str

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}`
**Detail view of vm.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}`
**Update vm.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vm` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}`
**Delete vm.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `interactive` (query, )

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/access`
**List vm accesss.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmaccess ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/vm/{vm}/access`
**Create vm access.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmaccess` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/fabric/{fabric}/vm/{vm}/access:order`

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `accesses`: array of model.vmaccess **(required)**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/access/{vmaccess}`
**Detail view of vm access.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmaccess` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}/access/{vmaccess}`
**Update vm access.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmaccess` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmaccess` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}/access/{vmaccess}`
**Delete vm access.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmaccess` (path, ) **(required)**
- `interactive` (query, )
- `yes` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/disk`
**List vm disks.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmdisk ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vmdisk` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/vm/{vm}/disk`
**Add an extra disk to the VM.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `capacity`: integer (format: int64) — MB size by default **(required)**

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}/disk`
**Remove last extra disk from the VM.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/disk/{vmdisk}`
**Detail view of vm disk.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmdisk` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}/disk/{vmdisk}`
**Update vm disk.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmdisk` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmdisk` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/license`
**Detail view of vm license.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmlicense` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}/license`
**Update vm license.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmlicense` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmlicense` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}/license`
**Update vm license.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Response 200**: `model.vmlicense` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/vm/{vm}/license:release`

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/parameters`
**Detail view of vm parameters.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmparameters` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}/parameters`
**Update vm parameters.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmparameters` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmparameters` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}/parameters`
**Update vm parameters.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Response 200**: `model.vmparameters` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/port`
**List vm ports.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vmport` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/{fabric}/vm/{vm}/port`
**Create port as the new latest port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `vmport`: `model.vmport` (see Schemas)

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/{fabric}/vm/{vm}/port`
**Delete the last port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/{fabric}/vm/{vm}/port/{vmport}`
**Detail view of vm port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmport` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/fabric/{fabric}/vm/{vm}/port/{vmport}`
**Update vm port.**

**Parameters:**

- `fabric` (path, ) **(required)**
- `vm` (path, ) **(required)**
- `vmport` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/fabric/batch`
**Batch delete Fabrics.**

**Parameters:**

- `interactive` (query, )
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter

**Response 200**: array of `model.fabric` (wrapped in standard response)

---

#### `POST /api/v1/model/fabric/documentation/{fabric}:download`

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `active`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/fabric/remote:import`

**Request Body** (`application/json`):

- `address`: string **(required)**
- `fabric`: integer (format: int64) (default: 0)
- `interactive`: boolean (default: True)
- `ssh_password`: string
- `ssh_port`: integer (format: int64) (default: 22)
- `home_firmwares`: boolean (default: True)
- `home_templates`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/model/fabric/sanity(/{fabric})?`

**Parameters:**

- `fabric` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/host`
**List System Hosts.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given host ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.host` (wrapped in standard response)

---

#### `GET /api/v1/model/host/{host}`
**Detail view of System Host.**

**Parameters:**

- `host` (path, ) **(required)**: ID of the host
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.host` (wrapped in standard response)

---

#### `PATCH /api/v1/model/host/{host}`
**Update System Host.**

**Parameters:**

- `host` (path, ) **(required)**: ID of the host

**Request Body** (`application/json`):

- `object`: `model.host` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.host` (wrapped in standard response)

---

#### `POST /api/v1/model/host/{host}:sync`
**Synchronize with available System Host ports.**

**Parameters:**

- `host` (path, ) **(required)**

**Request Body** (`application/json`):

- `drop`: boolean (default: False) — drop extra ports even if connected

**Response 200**: array (wrapped in standard response)

---

#### `POST /api/v1/model/host/{host}/port`
**Create a new host internal port, name and index are automatic.**

**Parameters:**

- `host` (path, ) **(required)**

**Request Body** (`application/json`):

- `hostport`: `model.hostport` (see Schemas)

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/host/{host}/port`
**Delete the last internal port.**

**Parameters:**

- `host` (path, ) **(required)**

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/host/{host}/port/redirect`
**List port redirects.**

**Parameters:**

- `host` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given portredirect ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.portredirect` (wrapped in standard response)

---

#### `POST /api/v1/model/host/{host}/port/redirect`
**Create port redirect.**

**Parameters:**

- `host` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `GET /api/v1/model/host/{host}/port/redirect/{portredirect}`
**Detail view of port redirect.**

**Parameters:**

- `host` (path, ) **(required)**
- `portredirect` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `PATCH /api/v1/model/host/{host}/port/redirect/{portredirect}`
**Update port redirect.**

**Parameters:**

- `host` (path, ) **(required)**
- `portredirect` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `DELETE /api/v1/model/host/{host}/port/redirect/{portredirect}`
**Delete port redirect.**

**Parameters:**

- `host` (path, ) **(required)**
- `portredirect` (path, ) **(required)**
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `GET /api/v1/model/host/port`
**List System Ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given hostport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/host/port/{hostport}`
**Detail view of System Port.**

**Parameters:**

- `hostport` (path, ) **(required)**: ID of the hostport
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/host/port/{hostport}`
**Update inner system ports connection to the Fabric.**

**Parameters:**

- `hostport` (path, ) **(required)**: ID of the hostport

**Request Body** (`application/json`):

- `object`: `model.hostport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.hostport` (wrapped in standard response)

---

#### `GET /api/v1/model/network`
**List networks.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given network ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.network` (wrapped in standard response)

---

#### `POST /api/v1/model/network`
**Create network.**

**Request Body** (`application/json`):

- `object`: `model.network` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `model.network` (wrapped in standard response)

---

#### `GET /api/v1/model/network/{network}`
**Detail view of network.**

**Parameters:**

- `network` (path, ) **(required)**: ID of the network
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.network` (wrapped in standard response)

---

#### `PATCH /api/v1/model/network/{network}`
**Update network.**

**Parameters:**

- `network` (path, ) **(required)**: ID of the network

**Request Body** (`application/json`):

- `object`: `model.network` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.network` (wrapped in standard response)

---

#### `DELETE /api/v1/model/network/{network}`
**Delete network.**

**Parameters:**

- `network` (path, ) **(required)**: ID of the network
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.network` (wrapped in standard response)

---

#### `GET /api/v1/model/object/detail`
**Get detail view of any *model* object with *id* ``ID``. The deepest
subclass is returned.**

**Parameters:**

- `model` (query, ) **(required)**
- `ids` (query, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/object/diff`
**Compare "model" and "runtime" *model* object with *id* ID for
difference.**

**Parameters:**

- `model` (query, ) **(required)**
- `id` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/port`
**List ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given port ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/port/{port}`
**Detail view of port.**

**Parameters:**

- `port` (path, ) **(required)**: ID of the port
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/port/redirect`
**List port redirects.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given portredirect ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.portredirect` (wrapped in standard response)

---

#### `POST /api/v1/model/port/redirect`
**Create port redirect.**

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `GET /api/v1/model/port/redirect/{portredirect}`
**Detail view of port redirect.**

**Parameters:**

- `portredirect` (path, ) **(required)**: ID of the portredirect
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `PATCH /api/v1/model/port/redirect/{portredirect}`
**Update port redirect.**

**Parameters:**

- `portredirect` (path, ) **(required)**: ID of the portredirect

**Request Body** (`application/json`):

- `object`: `model.portredirect` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `DELETE /api/v1/model/port/redirect/{portredirect}`
**Delete port redirect.**

**Parameters:**

- `portredirect` (path, ) **(required)**: ID of the portredirect
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `model.portredirect` (wrapped in standard response)

---

#### `GET /api/v1/model/router`
**List routers.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given router ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.router` (wrapped in standard response)

---

#### `POST /api/v1/model/router`
**Create router.**

**Request Body** (`application/json`):

- `object`: `model.router` (see Schemas) **(required)**
- `ports_count`: integer (format: int64) (default: 10)
- `related_fields`: array of str

**Response 200**: `model.router` (wrapped in standard response)

---

#### `GET /api/v1/model/router/{router}`
**Detail view of router.**

**Parameters:**

- `router` (path, ) **(required)**: ID of the router
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.router` (wrapped in standard response)

---

#### `PATCH /api/v1/model/router/{router}`
**Update router.**

**Parameters:**

- `router` (path, ) **(required)**: ID of the router

**Request Body** (`application/json`):

- `object`: `model.router` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.router` (wrapped in standard response)

---

#### `DELETE /api/v1/model/router/{router}`
**Delete router.**

**Parameters:**

- `router` (path, ) **(required)**: ID of the router
- `interactive` (query, )

**Response 200**: `model.router` (wrapped in standard response)

---

#### `POST /api/v1/model/router/{router}/port`

**Parameters:**

- `router` (path, ) **(required)**

**Request Body** (`application/json`):

- `routerport`: `model.routerport` (see Schemas)

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/router/{router}/port`
**Delete the last port.**

**Parameters:**

- `router` (path, ) **(required)**

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `GET /api/v1/model/router/port`
**List router ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given routerport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.routerport` (wrapped in standard response)

---

#### `GET /api/v1/model/router/port/{routerport}`
**Detail view of router port.**

**Parameters:**

- `routerport` (path, ) **(required)**: ID of the routerport
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/router/port/{routerport}`
**Update router port.**

**Parameters:**

- `routerport` (path, ) **(required)**: ID of the routerport

**Request Body** (`application/json`):

- `object`: `model.routerport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.routerport` (wrapped in standard response)

---

#### `GET /api/v1/model/switch`
**List Switches.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switch ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switch` (wrapped in standard response)

---

#### `POST /api/v1/model/switch`
**Create switch.**

**Request Body** (`application/json`):

- `object`: `model.switch` (see Schemas) **(required)**
- `ports_count`: integer (format: int64) (default: 10)
- `related_fields`: array of str

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `GET /api/v1/model/switch/{switch}`
**Detail view of switch.**

**Parameters:**

- `switch` (path, ) **(required)**: ID of the switch
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `PATCH /api/v1/model/switch/{switch}`
**Update switch.**

**Parameters:**

- `switch` (path, ) **(required)**: ID of the switch

**Request Body** (`application/json`):

- `object`: `model.switch` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `DELETE /api/v1/model/switch/{switch}`
**Delete switch.**

**Parameters:**

- `switch` (path, ) **(required)**: ID of the switch
- `interactive` (query, )

**Response 200**: `model.switch` (wrapped in standard response)

---

#### `POST /api/v1/model/switch/{switch}/port`

**Parameters:**

- `switch` (path, ) **(required)**

**Request Body** (`application/json`):

- `switchport`: `model.switchport` (see Schemas)

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/switch/{switch}/port`
**Delete the last port.**

**Parameters:**

- `switch` (path, ) **(required)**

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `GET /api/v1/model/switch/local-port`
**List switch local ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switchlocalport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switchlocalport` (wrapped in standard response)

---

#### `GET /api/v1/model/switch/local-port/{switchlocalport}`
**Detail view of switch local port.**

**Parameters:**

- `switchlocalport` (path, ) **(required)**: ID of the switchlocalport
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.switchlocalport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/switch/local-port/{switchlocalport}`
**Update switch local port.**

**Parameters:**

- `switchlocalport` (path, ) **(required)**: ID of the switchlocalport

**Request Body** (`application/json`):

- `object`: `model.switchlocalport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.switchlocalport` (wrapped in standard response)

---

#### `GET /api/v1/model/switch/port`
**List switch ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switchport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switchport` (wrapped in standard response)

---

#### `GET /api/v1/model/switch/port/{switchport}`
**Detail view of switch port.**

**Parameters:**

- `switchport` (path, ) **(required)**: ID of the switchport
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/switch/port/{switchport}`
**Update switch port.**

**Parameters:**

- `switchport` (path, ) **(required)**: ID of the switchport

**Request Body** (`application/json`):

- `object`: `model.switchport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.switchport` (wrapped in standard response)

---

#### `GET /api/v1/model/tc`
**List traffic controls.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given trafficcontrol ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/model/tc/{trafficcontrol}`
**Detail view of traffic control.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**: ID of the trafficcontrol
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `PATCH /api/v1/model/tc/{trafficcontrol}`
**Update traffic control.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**: ID of the trafficcontrol

**Request Body** (`application/json`):

- `object`: `model.trafficcontrol` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/model/vm`
**List VMs.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vm ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vm` (wrapped in standard response)

---

#### `POST /api/v1/model/vm`
**Create a new VM object.**

**Request Body** (`application/json`):

- `object`: `model.vm` (see Schemas) **(required)**
- `ports_count`: integer (format: int64)
- `auto_connect`: boolean
- `related_fields`: array of str

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/{vm}`
**Detail view of vm.**

**Parameters:**

- `vm` (path, ) **(required)**: ID of the vm
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/{vm}`
**Update vm.**

**Parameters:**

- `vm` (path, ) **(required)**: ID of the vm

**Request Body** (`application/json`):

- `object`: `model.vm` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}`
**Delete vm.**

**Parameters:**

- `vm` (path, ) **(required)**: ID of the vm
- `interactive` (query, )

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `POST /api/v1/model/vm/{vm}:clone`

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `related_fields`: array of str

**Response 200**: `model.vm` (wrapped in standard response)

---

#### `POST /api/v1/model/vm/{vm}/disk`
**Add an extra disk to the VM.**

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `capacity`: integer (format: int64) — MB size by default **(required)**

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}/disk`
**Remove last extra disk from the VM.**

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/{vm}/install/after`
**View install after constraints.**

**Parameters:**

- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.installafter` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/{vm}/install/after`
**Update install after constraints.**

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `after`: array of model.vm **(required)**

**Response 200**: `model.installafter` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}/install/after`
**Remove all install after constraints.**

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/vm/{vm}/license`
**Detail view of vm license.**

**Parameters:**

- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmlicense` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/{vm}/license`
**Update vm license.**

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmlicense` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmlicense` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}/license`
**Reset license to default values.**

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/vm/{vm}/license:release`

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/vm/{vm}/parameters`
**Detail view of vm parameters.**

**Parameters:**

- `vm` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmparameters` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/{vm}/parameters`
**Update vm parameters.**

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.vmparameters` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmparameters` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}/parameters`
**Reset parameters to default values.**

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/vm/{vm}/port`
**Create port as the new latest port.**

**Parameters:**

- `vm` (path, ) **(required)**

**Request Body** (`application/json`):

- `vmport`: `model.vmport` (see Schemas)

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `DELETE /api/v1/model/vm/{vm}/port`
**Delete the last port.**

**Parameters:**

- `vm` (path, ) **(required)**

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/access`
**List vm accesss.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmaccess ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `POST /api/v1/model/vm/access`
**Create vm access.**

**Request Body** (`application/json`):

- `object`: `model.vmaccess` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: Successful operation.

---

#### `POST /api/v1/model/vm/access:order`

**Request Body** (`application/json`):

- `accesses`: array of model.vmaccess **(required)**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/model/vm/access/{vmaccess}`
**Detail view of vm access.**

**Parameters:**

- `vmaccess` (path, ) **(required)**: ID of the vmaccess
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/model/vm/access/{vmaccess}`
**Update vm access.**

**Parameters:**

- `vmaccess` (path, ) **(required)**: ID of the vmaccess

**Request Body** (`application/json`):

- `object`: `model.vmaccess` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/model/vm/access/{vmaccess}`
**Delete vm access.**

**Parameters:**

- `vmaccess` (path, ) **(required)**: ID of the vmaccess
- `interactive` (query, )
- `yes` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/model/vm/disk`
**List vm disks.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmdisk ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vmdisk` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/disk/{vmdisk}`
**Detail view of vm disk.**

**Parameters:**

- `vmdisk` (path, ) **(required)**: ID of the vmdisk
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/disk/{vmdisk}`
**Update vm disk.**

**Parameters:**

- `vmdisk` (path, ) **(required)**: ID of the vmdisk

**Request Body** (`application/json`):

- `object`: `model.vmdisk` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmdisk` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/port`
**List vm ports.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vmport ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vmport` (wrapped in standard response)

---

#### `GET /api/v1/model/vm/port/{vmport}`
**Detail view of vm port.**

**Parameters:**

- `vmport` (path, ) **(required)**: ID of the vmport
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.vmport` (wrapped in standard response)

---

#### `PATCH /api/v1/model/vm/port/{vmport}`
**Update vm port.**

**Parameters:**

- `vmport` (path, ) **(required)**: ID of the vmport

**Request Body** (`application/json`):

- `object`: `model.vmport` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.vmport` (wrapped in standard response)

---

### RUNTIME Endpoints

#### `GET /api/v1/runtime/cable`
**List cables.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given cable ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.cable` (wrapped in standard response)

---

#### `GET /api/v1/runtime/cable/{cable}`
**Detail view of cable.**

**Parameters:**

- `cable` (path, ) **(required)**: ID of the cable
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.cable` (wrapped in standard response)

---

#### `POST /api/v1/runtime/cable/{cable}:break`
**Break the cable but do not remove it.**

**Parameters:**

- `cable` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/cable/{cable}:repair`
**Repair a broken cable.**

**Parameters:**

- `cable` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/config`
**List device configs.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given deviceconfig ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.deviceconfig` (wrapped in standard response)

---

#### `GET /api/v1/runtime/config/{deviceconfig}`
**Detail view of device config.**

**Parameters:**

- `deviceconfig` (path, ) **(required)**: ID of the deviceconfig
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `GET /api/v1/runtime/device`
**List all "runtime" devices objects.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given device ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/device/{device}`
**Return detail view of a device, to be used during runtime to
interact with the Fabric from a device script (REST call).**

**Parameters:**

- `device` (path, ) **(required)**: ID of the device
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}`
**Install a clean device.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "model" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `power_on`: boolean (default: True) — do not power on
- `post_boot`: boolean (default: True) — do post boot preparation
- `timeout`: integer (format: int64) — inactivity timeout in second to abort
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/device/{device}`
**Uninstall the device and delete (by default) the object from the
"runtime" environment DB.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `delete` (query, ): delete or not the object

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}:power-off`
**Power off a device instance, data may be lost and disk corrupted.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}:power-on`
**Power-on the device instance and perform post boot preparation.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort
- `post_boot`: boolean (default: True)
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}:shutdown`
**Shutdown a device. You can force a power off if shutdown didn't
complete before timeout.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) (default: 30) — timeout in seconds before aborting or forcing power off
- `power_off`: boolean (default: False) — power off if shutdown doesn't complete before timeout is reached

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}:synchronize`
**Synchronize the "runtime" device object and instance with the
    "model" object if possible.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/cables`
**Connect all cables to the device instance, peer device instances
    must exist.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/device/{device}/cables`
**Disconnect all cables from the device instance.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/config:backup`
**Perform a device instance configuration backup.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `filename`: string **(required)**
- `overwrite`: boolean (default: False)
- `as_default`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/config:restore`
**Restore the device instance original configuration.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/config/{config}:restore`
**Restore the specified configuration for the device instance.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `config` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/license`
**Install the default device's license.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, unspecified default wait

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/license:wait`
**Waiting for device license to be validated.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/license/{license}`
**Install the specified device's license.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `license` (path, ) **(required)**: Use this specific license

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, None default wait

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/device/{device}/port`
**List device instance ports.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/device/{device}/port/{port}`
**Show port detail.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/device/{device}/port/{port}/tc`
**Detail view of traffic control.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `POST /api/v1/runtime/device/{device}/port/{port}/tc`
**Update traffic control.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Request Body** (`application/json`):

- `object`: `model.trafficcontrol` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `POST /api/v1/runtime/device/{device}/port/{port}/tc:force`
**Reapply traffic control.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/port/{port}/tc:stop`
**Disable traffic control by adjusting the values.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/{device}/port/{port}/tc:sync`
**Reset traffic control with values from the model.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/device/{device}/status`
**Return the device instance status.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)

**Response 200**: `class.devicestatus` (wrapped in standard response)

---

#### `GET /api/v1/runtime/device/{device}/tc`
**List traffic controls.**

**Parameters:**

- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given trafficcontrol ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/runtime/device/cable/{device}/{port}`
**View state of cable attached to the VM port.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/cable/{device}/{port}:break`
**Break the cable attach to the VM port but do not remove it.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/device/cable/{device}/{port}:repair`
**Repair the broken cable attached to the VM port.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/{port}/{device}/device/port`

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/{trafficcontrol}`

**Parameters:**

- `trafficcontrol` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/cables`
**Any cable interfaces in "cables" group.**

**Parameters:**

- `cable` (query, )

**Response 200**: array of `class.systeminterface` (wrapped in standard response)

---

#### `GET /api/v1/runtime/diagnose/host/firewall(/{router})?`

**Parameters:**

- `router` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/host/reverse-proxy`

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/host/sysctl`

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/diagnose/interfaces(/{router})?`
**Any interfaces in "fabric" group.**

**Parameters:**

- `router` (path, ) **(required)**
- `ifname` (query, )

**Response 200**: array of `class.systeminterface` (wrapped in standard response)

---

#### `GET /api/v1/runtime/diagnose/router/firewall/{router}`

**Parameters:**

- `router` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/device/{device}/port/{port}:down`
**Bring device instance *port* down.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/device/{device}/port/{port}:up`
**Bring device instance *port* up.**

**Parameters:**

- `device` (path, ) **(required)**: A device's "runtime" object id (CLI accepts name and nameid too)
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/host/{device}/port/{port}:down`
**Bring device instance *port* down.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/host/{device}/port/{port}:up`
**Bring device instance *port* up.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/router/{device}/port/{port}:down`
**Bring device instance *port* down.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/router/{device}/port/{port}:up`
**Bring device instance *port* up.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/switch/{device}/port/{port}:down`
**Bring device instance *port* down.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/switch/{device}/port/{port}:up`
**Bring device instance *port* up.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/vm/{device}/port/{port}:down`
**Bring device instance *port* down.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/expert/vm/{device}/port/{port}:up`
**Bring device instance *port* up.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/fabric`
**Current running Fabric detail.**

**Parameters:**

- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.fabric` (wrapped in standard response)

---

#### `POST /api/v1/runtime/fabric`
**Power-on all Fabric VM in the runtime environment.**

**Request Body** (`application/json`):

- `vms_tasks`: boolean (default: True) — power-on VMs in separate tasks (True) or not (False)
- `on_boot`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/fabric`
**Uninstall Fabric from runtime environment and reseting all systems.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/fabric:synchronize`
**Synchronize fabric parameters.**

**Request Body** (`application/json`):

- `environment`: `model.deviceconfig` (see Schemas)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/fabric/{fabric}`
**Install a Fabric in the runtime environment.**

**Parameters:**

- `fabric` (path, ) **(required)**

**Request Body** (`application/json`):

- `environment`: `model.deviceconfig` (see Schemas)
- `power_on_vms`: boolean (default: True) — power on (True) or do not power on (False) VMs
- `install_vms`: boolean (default: True) — install (True) or do not install VMs (False)
- `install_vms_tasks`: boolean (default: True) — install VMs in separate tasks (True) or not (False)
- `doc_download`: boolean (default: True) — download documentation

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/fabric/documentation:download`

**Request Body** (`application/json`):

- `interactive`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/fabric/license`
**Notify license server we are still alive.**

**Request Body** (`application/json`):

- `mode`: string (default: alive)
- `quiet`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/host`
**Returns the runtime host definition.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given host ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.host` (wrapped in standard response)

---

#### `GET /api/v1/runtime/host/{device}`
**Return detail view of a device, to be used during runtime to
interact with the Fabric from a device script (REST call).**

**Parameters:**

- `device` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}`
**Install a clean device.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `power_on`: boolean (default: True) — do not power on
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not
- `post_boot`: boolean (default: True) — do post boot preparation
- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/host/{device}`
**Uninstall the device and delete (by default) the object from the
"runtime" environment DB.**

**Parameters:**

- `device` (path, ) **(required)**
- `delete` (query, ): delete or not the object

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}:power-off`
**Power off a device instance, data may be lost and disk corrupted.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}:power-on`
**Power-on the device instance and perform post boot preparation.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort
- `post_boot`: boolean (default: True)
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}:shutdown`
**Shutdown a device. You can force a power off if shutdown didn't
complete before timeout.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) (default: 30) — timeout in seconds before aborting or forcing power off
- `power_off`: boolean (default: False) — power off if shutdown doesn't complete before timeout is reached

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}:synchronize`
**Synchronize the "runtime" device object and instance with the
    "model" object if possible.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/cables`
**Connect all cables to the device instance, peer device instances
    must exist.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/host/{device}/cables`
**Disconnect all cables from the device instance.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/config:backup`
**Perform a device instance configuration backup.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `filename`: string **(required)**
- `overwrite`: boolean (default: False)
- `as_default`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/config:restore`
**Restore the device instance original configuration.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/config/{config}:restore`
**Restore the specified configuration for the device instance.**

**Parameters:**

- `device` (path, ) **(required)**
- `config` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/license`
**Install the default device's license.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, unspecified default wait

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/license:wait`
**Waiting for device license to be validated.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/{device}/license/{license}`
**Install the specified device's license.**

**Parameters:**

- `device` (path, ) **(required)**
- `license` (path, ) **(required)**: Use this specific license

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, None default wait

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/host/{device}/port`
**List device instance ports.**

**Parameters:**

- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/host/{device}/port/{port}`
**Show port detail.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/host/{device}/status`
**Return the device instance status.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: `class.devicestatus` (wrapped in standard response)

---

#### `GET /api/v1/runtime/host/cable/{device}/{port}`
**View state of cable attached to the host port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/cable/{device}/{port}:break`
**Break the cable attach to the host port but do not remove it.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/host/cable/{device}/{port}:repair`
**Repair the broken cable attached to the host port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/license`
**List licenses.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given license ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `license.license` (wrapped in standard response)

---

#### `GET /api/v1/runtime/router`
**List all "runtime" routers objects.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given router ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.router` (wrapped in standard response)

---

#### `GET /api/v1/runtime/router/{device}`
**Return detail view of a device, to be used during runtime to
interact with the Fabric from a device script (REST call).**

**Parameters:**

- `device` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}`
**Install a clean device.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `power_on`: boolean (default: True) — do not power on
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not
- `post_boot`: boolean (default: True) — do post boot preparation
- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/router/{device}`
**Uninstall the device and delete (by default) the object from the
"runtime" environment DB.**

**Parameters:**

- `device` (path, ) **(required)**
- `delete` (query, ): delete or not the object

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}:power-off`
**Power off a device instance, data may be lost and disk corrupted.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}:power-on`
**Power-on the device instance and perform post boot preparation.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort
- `post_boot`: boolean (default: True)
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}:shutdown`
**Shutdown a device. You can force a power off if shutdown didn't
complete before timeout.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) (default: 30) — timeout in seconds before aborting or forcing power off
- `power_off`: boolean (default: False) — power off if shutdown doesn't complete before timeout is reached

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}:synchronize`
**Synchronize the "runtime" device object and instance with the
    "model" object if possible.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/cables`
**Connect all cables to the device instance, peer device instances
    must exist.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/router/{device}/cables`
**Disconnect all cables from the device instance.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/config:backup`
**Perform a device instance configuration backup.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `filename`: string **(required)**
- `overwrite`: boolean (default: False)
- `as_default`: boolean (default: False)

**Response 200**: `model.deviceconfig` (wrapped in standard response)

---

#### `POST /api/v1/runtime/router/{device}/config:restore`
**Restore the device instance original configuration.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/config/{config}:restore`
**Restore the specified configuration for the device instance.**

**Parameters:**

- `device` (path, ) **(required)**
- `config` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/license`
**Install the default device's license.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, unspecified default wait

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/license:wait`
**Waiting for device license to be validated.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/{device}/license/{license}`
**Install the specified device's license.**

**Parameters:**

- `device` (path, ) **(required)**
- `license` (path, ) **(required)**: Use this specific license

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, None default wait

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/router/{device}/port`
**List device instance ports.**

**Parameters:**

- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/router/{device}/port/{port}`
**Show port detail.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/router/{device}/status`
**Return the device instance status.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: `class.devicestatus` (wrapped in standard response)

---

#### `GET /api/v1/runtime/router/cable/{device}/{port}`
**View state of cable attached to the router port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/cable/{device}/{port}:break`
**Break the cable attach to the router port but do not remove it.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/router/cable/{device}/{port}:repair`
**Repair the broken cable attached to the router port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/switch`
**List all "runtime" switches objects.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given switch ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.switch` (wrapped in standard response)

---

#### `GET /api/v1/runtime/switch/{device}`
**Return detail view of a device, to be used during runtime to
interact with the Fabric from a device script (REST call).**

**Parameters:**

- `device` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}`
**Install a clean device.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `power_on`: boolean (default: True) — do not power on
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not
- `post_boot`: boolean (default: True) — do post boot preparation
- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/switch/{device}`
**Uninstall the device and delete (by default) the object from the
"runtime" environment DB.**

**Parameters:**

- `device` (path, ) **(required)**
- `delete` (query, ): delete or not the object

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}:power-off`
**Power off a device instance, data may be lost and disk corrupted.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}:power-on`
**Power-on the device instance and perform post boot preparation.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort
- `post_boot`: boolean (default: True)
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}:shutdown`
**Shutdown a device. You can force a power off if shutdown didn't
complete before timeout.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) (default: 30) — timeout in seconds before aborting or forcing power off
- `power_off`: boolean (default: False) — power off if shutdown doesn't complete before timeout is reached

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}:synchronize`
**Synchronize the "runtime" device object and instance with the
    "model" object if possible.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/cables`
**Connect all cables to the device instance, peer device instances
    must exist.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/switch/{device}/cables`
**Disconnect all cables from the device instance.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/config:backup`
**Perform a device instance configuration backup.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `filename`: string **(required)**
- `overwrite`: boolean (default: False)
- `as_default`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/config:restore`
**Restore the device instance original configuration.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/config/{config}:restore`
**Restore the specified configuration for the device instance.**

**Parameters:**

- `device` (path, ) **(required)**
- `config` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/license`
**Install the default device's license.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, unspecified default wait

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/license:wait`
**Waiting for device license to be validated.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/{device}/license/{license}`
**Install the specified device's license.**

**Parameters:**

- `device` (path, ) **(required)**
- `license` (path, ) **(required)**: Use this specific license

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, None default wait

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/switch/{device}/port`
**List device instance ports.**

**Parameters:**

- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/switch/{device}/port/{port}`
**Show port detail.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/switch/{device}/status`
**Return the device instance status.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: `class.devicestatus` (wrapped in standard response)

---

#### `GET /api/v1/runtime/switch/cable/{device}/{port}`
**View state of cable attached to the switch port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/cable/{device}/{port}:break`
**Break the cable attach to the switch port but do not remove it.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/switch/cable/{device}/{port}:repair`
**Repair the broken cable attached to the switch port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/tc`
**List traffic controls.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given trafficcontrol ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `DELETE /api/v1/runtime/tc`
**Cleanup dangling traffic control.**

**Response 200**: array of `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/runtime/tc/{trafficcontrol}`
**Detail view of traffic control.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**: ID of the trafficcontrol
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `PATCH /api/v1/runtime/tc/{trafficcontrol}`
**Update traffic control.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**: ID of the trafficcontrol

**Request Body** (`application/json`):

- `object`: `model.trafficcontrol` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `POST /api/v1/runtime/tc/{trafficcontrol}:force`
**Reapply traffic control.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `POST /api/v1/runtime/tc/{trafficcontrol}:stop`
**Disable traffic control by adjusting the values.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `POST /api/v1/runtime/tc/{trafficcontrol}:sync`
**Reset traffic control with values from the model.**

**Parameters:**

- `trafficcontrol` (path, ) **(required)**

**Response 200**: `model.trafficcontrol` (wrapped in standard response)

---

#### `GET /api/v1/runtime/vm`
**List all "runtime" VMs objects.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given vm ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `model.vm` (wrapped in standard response)

---

#### `GET /api/v1/runtime/vm/{device}`
**Return detail view of a device, to be used during runtime to
interact with the Fabric from a device script (REST call).**

**Parameters:**

- `device` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}`
**Install a clean device.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `power_on`: boolean (default: True) — do not power on
- `license`: boolean (default: True) — install the license or not
- `configuration`: boolean (default: True) — restore configuration or not
- `post_boot`: boolean (default: True) — do post boot preparation
- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/vm/{device}`
**Uninstall the device and delete (by default) the object from the
"runtime" environment DB.**

**Parameters:**

- `device` (path, ) **(required)**
- `delete` (query, ): delete or not the object

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}:export`

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `name`: string **(required)**
- `overwrite`: boolean (default: False)
- `interactive`: boolean (default: True)
- `diff`: boolean (default: False)
- `refresh`: boolean (default: True)
- `switch`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}:power-off`
**Power off a device instance, data may be lost and disk corrupted.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}:power-on`
**Power-on the device instance and perform post boot preparation.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `configuration`: boolean (default: True) — restore configuration or not
- `license`: boolean (default: True) — install the license or not
- `post_boot`: boolean (default: True)
- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}:shutdown`
**Shutdown a device. You can force a power off if shutdown didn't
complete before timeout.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) (default: 30) — timeout in seconds before aborting or forcing power off
- `power_off`: boolean (default: False) — power off if shutdown doesn't complete before timeout is reached

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}:synchronize`
**Synchronize the "runtime" device object and instance with the
    "model" object if possible.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/cables`
**Connect all cables to the device instance, peer device instances
    must exist.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/runtime/vm/{device}/cables`
**Disconnect all cables from the device instance.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/config:backup`
**Perform a device instance configuration backup.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `filename`: string **(required)**
- `overwrite`: boolean (default: False)
- `as_default`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/config:restore`
**Restore the device instance original configuration.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/config/{config}:restore`
**Restore the specified configuration for the device instance.**

**Parameters:**

- `device` (path, ) **(required)**
- `config` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/license`
**Install the default device's license.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, unspecified default wait

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/license:wait`
**Waiting for device license to be validated.**

**Parameters:**

- `device` (path, ) **(required)**

**Request Body** (`application/json`):

- `timeout`: integer (format: int64) — inactivity timeout in second to abort

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/{device}/license/{license}`
**Install the specified device's license.**

**Parameters:**

- `device` (path, ) **(required)**
- `license` (path, ) **(required)**: Use this specific license

**Request Body** (`application/json`):

- `reinstall`: boolean (default: False)
- `refresh`: boolean (default: True)
- `wait`: integer (format: int64) — wait timeout for license validation, 0 wait forever, None default wait

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/vm/{device}/port`
**List device instance ports.**

**Parameters:**

- `device` (path, ) **(required)**
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/runtime/vm/{device}/port/{port}`
**Show port detail.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `GET /api/v1/runtime/vm/{device}/status`
**Return the device instance status.**

**Parameters:**

- `device` (path, ) **(required)**

**Response 200**: `class.devicestatus` (wrapped in standard response)

---

#### `GET /api/v1/runtime/vm/cable/{device}/{port}`
**View state of cable attached to the VM port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/cable/{device}/{port}:break`
**Break the cable attach to the VM port but do not remove it.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/runtime/vm/cable/{device}/{port}:repair`
**Repair the broken cable attached to the VM port.**

**Parameters:**

- `device` (path, ) **(required)**
- `port` (path, ) **(required)**

**Response 200**: Successful operation.

---

### SYSTEM Endpoints

#### `GET /api/v1/system/account`
**Get registration user information.**

**Response 200**: `users.userprofile` (wrapped in standard response)

---

#### `POST /api/v1/system/account`
**Register the Fabric Studio on the registration server.**

**Request Body** (`application/json`):

- `mode`: string **(required)**
- `identity`: string **(required)**
- `password`: string — cleartext password
- `interactive`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `DELETE /api/v1/system/account`
**Unregister the Fabric Studio.**

**Parameters:**

- `interactive` (query, )

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/account:refresh`
**Refresh the Fabric Studio registration.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `force`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/account/permissions`
**Return current user permissions list.**

**Parameters:**

- `inactive` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/account/ssh/keys`
**Show all keys.**

**Response 200**: array (wrapped in standard response)

---

#### `POST /api/v1/system/account/ssh/keys:add`
**Add a public key to the authorized keys.**

**Request Body** (`application/json`):

- `key`: string **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/account/ssh/keys:del`
**Delete all keys matching *key*, *key* can be:**

**Request Body** (`application/json`):

- `key`: string **(required)**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/system/certificate/local/ca`
**List ca certificates.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given cacertificate ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `certificates.cacertificate` (wrapped in standard response)

---

#### `POST /api/v1/system/certificate/local/ca:import`
**Import a CA certificate.**

**Request Body** (`application/json`):

- `pem`: string — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `name`: string

**Request Body** (`multipart/form-data`):

- `pem`: string (format: binary) — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `name`: string

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/certificate/local/ca/{cacertificate}`
**Detail view of ca certificate.**

**Parameters:**

- `cacertificate` (path, ) **(required)**: ID of the cacertificate
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `certificates.cacertificate` (wrapped in standard response)

---

#### `DELETE /api/v1/system/certificate/local/ca/{cacertificate}`
**Delete ca certificate.**

**Parameters:**

- `cacertificate` (path, ) **(required)**: ID of the cacertificate
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `certificates.cacertificate` (wrapped in standard response)

---

#### `GET /api/v1/system/db/devices/list`
**Supported devices.**

**Response 200**: array of `class.devicetype` (wrapped in standard response)

---

#### `GET /api/v1/system/db/schema`
**List models.**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/system/db/schema/{model}`
**Dump *model* schema.**

**Parameters:**

- `model` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/debug/kernel/printk`
**Return current kernel printk levels.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/debug/kernel/printk`
**Change the kernel printk levels.**

**Request Body** (`application/json`):

- `current`: integer (format: int64) **(required)**
- `default`: integer (format: int64) **(required)**
- `minimum`: integer (format: int64) **(required)**
- `boot_time_default`: integer (format: int64) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/diagnose/date`
**Return current UTC datetime as ISO 8601 string.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/diagnose/nogroup`
**Any interfaces in "nogroup" group.**

**Response 200**: array of `class.systeminterface` (wrapped in standard response)

---

#### `GET /api/v1/system/diagnose/user/cwd`
**Return current working directory.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/diagnose/user/ip`
**Return current user connection IP if it can be determined else
"MISSING".**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/diagnose/vm/factory`
**List known VM type.**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/system/disclaimer`
**Show disclaimer.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/disk/data:extend`
**Extend the data disk.**

**Request Body** (`application/json`):

- `size`: integer (format: int64) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/disk/detail`
**Disk details.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/disk/extend`
**Extend VG.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/disk/system:extend`
**Extend the system partition.**

**Request Body** (`application/json`):

- `size`: integer (format: int64) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/disk/system:retry`
**Complete system partition resizing.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/execute:factoryreset`
**Reset system to factory settings and reboot.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `reboot`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/execute:login`
**Run login session.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/execute:reboot`
**Reboot the system.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/execute:shutdown`
**Shutdown the system.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/execute:upgrade`
**Upgrade the product.**

**Request Body** (`application/json`):

- `channel`: string — Upgrade channel, conflicts with "version" option
- `version`: Tag
- `upgrade_script_source`: UrlInfo
- `upgrade_repository_source`: UrlInfo
- `force`: boolean (default: False) — Force the upgrade
- `interactive`: boolean (default: True) — Interactive upgrade or not
- `dangerous`: boolean (default: False) — Dangerous upgrade with Fabric running and no reboot

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/execute/date:sync`
**Force date synchronization.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/expert/server/zone`
**List server zones.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given serverzone ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `repository.serverzone` (wrapped in standard response)

---

#### `POST /api/v1/system/expert/server/zone`
**Create server zone.**

**Request Body** (`application/json`):

- `object`: `repository.serverzone` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `repository.serverzone` (wrapped in standard response)

---

#### `GET /api/v1/system/expert/server/zone/{serverzone}`
**Detail view of server zone.**

**Parameters:**

- `serverzone` (path, ) **(required)**: ID of the serverzone
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `repository.serverzone` (wrapped in standard response)

---

#### `PATCH /api/v1/system/expert/server/zone/{serverzone}`
**Update server zone.**

**Parameters:**

- `serverzone` (path, ) **(required)**: ID of the serverzone

**Request Body** (`application/json`):

- `object`: `repository.serverzone` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `repository.serverzone` (wrapped in standard response)

---

#### `DELETE /api/v1/system/expert/server/zone/{serverzone}`
**Delete server zone.**

**Parameters:**

- `serverzone` (path, ) **(required)**: ID of the serverzone
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `repository.serverzone` (wrapped in standard response)

---

#### `GET /api/v1/system/firewall/address`
**List firewall addresss.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given firewalladdress ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `system.firewalladdress` (wrapped in standard response)

---

#### `POST /api/v1/system/firewall/address`
**Create firewall address.**

**Request Body** (`application/json`):

- `object`: `system.firewalladdress` (see Schemas) **(required)**
- `force`: boolean (default: False)
- `related_fields`: array of str

**Response 200**: `system.firewalladdress` (wrapped in standard response)

---

#### `DELETE /api/v1/system/firewall/address`
**Flush all firewall addresses.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/firewall/address/{firewalladdress}`
**Detail view of firewall address.**

**Parameters:**

- `firewalladdress` (path, ) **(required)**: ID of the firewalladdress
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `system.firewalladdress` (wrapped in standard response)

---

#### `PATCH /api/v1/system/firewall/address/{firewalladdress}`
**Update firewall address.**

**Parameters:**

- `firewalladdress` (path, ) **(required)**: ID of the firewalladdress

**Request Body** (`application/json`):

- `object`: `system.firewalladdress` (see Schemas) **(required)**
- `force`: boolean (default: False)
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `system.firewalladdress` (wrapped in standard response)

---

#### `DELETE /api/v1/system/firewall/address/{firewalladdress}`
**Delete firewall address.**

**Parameters:**

- `firewalladdress` (path, ) **(required)**: ID of the firewalladdress
- `force` (query, )
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `system.firewalladdress` (wrapped in standard response)

---

#### `GET /api/v1/system/forticloud/account`
**Get FortiCloud account registration information.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/forticloud/account`
**Set FortiCloud API user credentials.**

**Request Body** (`application/json`):

- `apiId`: string **(required)**
- `password`: string
- `interactive`: boolean (default: True)
- `yes`: boolean (default: False)
- `accountId`: integer (format: int64)
- `refresh`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `DELETE /api/v1/system/forticloud/account`
**Clear FortiCloud API user credentials.**

**Parameters:**

- `interactive` (query, )

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/forticloud/account:upload`
**Configure FortiCloud credentials from the API credentials file generated
by https://support.fortinet.com/ site.**

**Request Body** (`application/json`):

- `file`: string **(required)**
- `accountId`: integer (format: int64)
- `interactive`: boolean (default: True)
- `yes`: boolean (default: False)
- `password`: string

**Request Body** (`multipart/form-data`):

- `file`: string (format: binary) **(required)**
- `accountId`: integer (format: int64)
- `interactive`: boolean (default: True)
- `yes`: boolean (default: False)
- `password`: string

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/forticloud/account/disclaimer`
**Return the FortiCloud API usage disclaimer.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/forticloud/account/token`
**Return token refresh time.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/forticloud/account/token:renew`
**Renew the API access token.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `force`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/hostname`
**Get system hostname.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/hostname`
**Set system hostname.**

**Request Body** (`application/json`):

- `hostname`: string **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/information`
**System detailed information.**

**Response 200**: `class.systeminformation` (wrapped in standard response)

---

#### `GET /api/v1/system/interfaces/mgmt`
**Get management interface configuration.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/interfaces/mgmt`
**Configure mangement interface.**

**Request Body** (`application/json`):

- `object`: SystemInterfaceConfig **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/interfaces/mgmt/public-address`
**Return public address by questionning opendns (default), google or
cloudfare.**

**Parameters:**

- `ipv` (query, )
- `operator` (query, )
- `ns` (query, )

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/kernel/grub/flush`
**Flush all custom grub configruation.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/kernel/hugepages:free`
**Return free hugepages count.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/kernel/hugepages/get`
**Return configured hugepages count.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/kernel/hugepages/set`
**Define hugepages count to reserve on next boot.**

**Request Body** (`application/json`):

- `count`: integer (format: int64) **(required)**
- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license`
**List VM licenses.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given license ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `license.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license:import`
**Upload a VM licence.**

**Request Body** (`application/json`):

- `input`: string **(required)**
- `license`: `license.license` (see Schemas)
- `erase_source`: boolean (default: True)

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary) **(required)**
- `license`: `license.license` (see Schemas)
- `erase_source`: boolean (default: True)

**Response 200**: `license.license` (wrapped in standard response)

---

#### `GET /api/v1/system/license/{license}`
**Detail view of a VM license.**

**Parameters:**

- `license` (path, ) **(required)**: ID of the license
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `license.license` (wrapped in standard response)

---

#### `PATCH /api/v1/system/license/{license}`
**Update VM licenses meta information.**

**Parameters:**

- `license` (path, ) **(required)**: ID of the license

**Request Body** (`application/json`):

- `object`: `license.license` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `license.license` (wrapped in standard response)

---

#### `DELETE /api/v1/system/license/{license}`
**Delete VM licenses.**

**Parameters:**

- `license` (path, ) **(required)**: ID of the license
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `license.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license/{license}:release`
**Release a license.**

**Parameters:**

- `license` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/api/flow/info`
**Return flow of calls information.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/api/license`
**Download an assets license LIC file.**

**Parameters:**

- `serialNumber` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/api/product:detail`
**An assets product detail (see official assets API documentation).**

**Parameters:**

- `serialNumber` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/api/product:list`
**List assets products matching serialNumber (see official assets API
documentation).**

**Parameters:**

- `serialNumber` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/assets/api/product:refresh`
**Refresh assets products information.**

**Request Body** (`application/json`):

- `serialNumber`: string

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/fp-type`
**List FPTypes.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given fptype ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `assets.fptype` (wrapped in standard response)

---

#### `POST /api/v1/system/license/assets/fp-type`
**Create FPType.**

**Request Body** (`application/json`):

- `object`: `assets.fptype` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `assets.fptype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/assets/fp-type/{fptype}`
**Detail view of FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `assets.fptype` (wrapped in standard response)

---

#### `PATCH /api/v1/system/license/assets/fp-type/{fptype}`
**Update FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype

**Request Body** (`application/json`):

- `object`: `assets.fptype` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `assets.fptype` (wrapped in standard response)

---

#### `DELETE /api/v1/system/license/assets/fp-type/{fptype}`
**Delete FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `assets.fptype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/assets/license`
**List licenses.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given license ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `assets.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license/assets/license:download`
**Download .lic files from the FortiCloud server.**

**Request Body** (`application/json`):

- `save`: boolean (default: False)
- `serial_number`: string

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/assets/license:refresh`
**Download licenses information from the FortiCloud server.**

**Request Body** (`application/json`):

- `serial_number`: string

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/assets/license/{license}`
**Detail view of license.**

**Parameters:**

- `license` (path, ) **(required)**: ID of the license
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `assets.license` (wrapped in standard response)

---

#### `GET /api/v1/system/license/client/request/group`
**Get the license group.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/request/group`
**Set the license group.**

**Request Body** (`application/json`):

- `group`: string **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/client/request/supported`
**Get the supported license classes to request licenses.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/request/supported`
**Set the supported license classes to request licenses.**

**Request Body** (`application/json`):

- `class`: array of str **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/client/server`
**Return remote license server use.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/server:disable`
**Disable use of remote license server.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/server:enable`
**Enable use of remote license server.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/client/server/legacy`
**Return remote license server legacy flag.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/server/legacy:disable`
**Set remote license server is NOT legacy.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/server/legacy:enable`
**Set remote license server is legacy.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/client/server/url`
**Return the remote license server URL.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/client/server/url`
**Set the remote license server URL.**

**Request Body** (`application/json`):

- `server`: UrlInfo **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/config`
**List configs.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given config ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.config` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/config:refresh`
**Refresh FortiFlex Config information for current FortiFlex API
account.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/config/{config}`
**Detail view of config.**

**Parameters:**

- `config` (path, ) **(required)**: ID of the config
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.config` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/fp-type`
**List FPTypes.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given fptype ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.fptype` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/fp-type`
**Create FPType.**

**Request Body** (`application/json`):

- `object`: `flexvm.fptype` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `flexvm.fptype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/fp-type/{fptype}`
**Detail view of FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.fptype` (wrapped in standard response)

---

#### `PATCH /api/v1/system/license/flex/fp-type/{fptype}`
**Update FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype

**Request Body** (`application/json`):

- `object`: `flexvm.fptype` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `flexvm.fptype` (wrapped in standard response)

---

#### `DELETE /api/v1/system/license/flex/fp-type/{fptype}`
**Delete FPType.**

**Parameters:**

- `fptype` (path, ) **(required)**: ID of the fptype
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `flexvm.fptype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/license`
**List licenses.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given license ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/license:reactivate`
**To reactivate all known licenses.**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/flex/license:refresh`
**Download and refresh licenses from the FortiFlex server.**

**Request Body** (`application/json`):

- `type`: string **(required)**
- `save`: boolean (default: False)
- `serial_number`: string
- `select`: string
- `interactive`: boolean (default: True)

**Response 200**: array of `flexvm.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/license:stop`
**To stop all known licenses.**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/flex/license:transfer`
**Transfer license(s) between two accounts.**

**Request Body** (`application/json`):

- `targetAccountId`: integer (format: int64) **(required)**
- `serials`: array of str **(required)**
- `targetConfigId`: integer (format: int64)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/license/{license}`
**Detail view of license.**

**Parameters:**

- `license` (path, ) **(required)**: ID of the license
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.license` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/license/{license}:reactivate`
**To reactivate specific license.**

**Parameters:**

- `license` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/flex/license/{license}:stop`
**To stop specific license.**

**Parameters:**

- `license` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/pool`
**List pools.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given pool ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.pool` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/pool`
**Enable config for the device *type*.**

**Request Body** (`application/json`):

- `type`: string **(required)**
- `config`: integer (format: int64)
- `refresh`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/system/license/flex/pool`
**Disable pool for the device *type*.**

**Parameters:**

- `type` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/pool/{pool}`
**Detail view of pool.**

**Parameters:**

- `pool` (path, ) **(required)**: ID of the pool
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.pool` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/pool/{pool}:generate`
**Generate new FortiFlex VM license in selected pool.**

**Parameters:**

- `pool` (path, ) **(required)**

**Request Body** (`application/json`):

- `count`: integer (format: int64) **(required)**
- `save`: boolean (default: False)

**Response 200**: array of `flexvm.license` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/product`
**List product types.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given producttype ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.producttype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/product/{producttype}`
**Detail view of product type.**

**Parameters:**

- `producttype` (path, ) **(required)**: ID of the producttype
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.producttype` (wrapped in standard response)

---

#### `PATCH /api/v1/system/license/flex/product/{producttype}`
**Update product type.**

**Parameters:**

- `producttype` (path, ) **(required)**: ID of the producttype

**Request Body** (`application/json`):

- `object`: `flexvm.producttype` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `flexvm.producttype` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/program`
**List programs.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given program ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `flexvm.program` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/program:refresh`
**Refresh FortiFlex Program information for current FortiFlex API
account.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/flex/program/{program}`
**Detail view of program.**

**Parameters:**

- `program` (path, ) **(required)**: ID of the program
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `flexvm.program` (wrapped in standard response)

---

#### `GET /api/v1/system/license/flex/settings`
**Return license manager configuration for FortiFlex.**

**Response 200**: `class.flexvmsettings` (wrapped in standard response)

---

#### `POST /api/v1/system/license/flex/settings`
**Set license manager configuration for FortiFlex.**

**Request Body** (`application/json`):

- `settings`: FlexVMSettings **(required)**

**Response 200**: `class.flexvmsettings` (wrapped in standard response)

---

#### `POST /api/v1/system/license/server`
**LabSetup only command. Do NOT use.**

**Request Body** (`application/json`):

- `server`: UrlInfo **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/legacy`
**LabSetup only command. Do NOT use.**

**Request Body** (`application/json`):

- `state`: boolean **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/server/service`
**Return service state for remote client.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/service:disable`
**Disable service for remote client.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/service:enable`
**Enable service for remote client.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/server/service/local`
**Return service state for local client.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/service/local:disable`
**Disable service for local client.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/service/local:enable`
**Enable service for local client.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/license/server/supported`
**Get the supported license classes to serve licenses.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/license/server/supported`
**Set the supported license classes to serve licenses.**

**Request Body** (`application/json`):

- `class`: array of str **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/log`
**List api calls.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given apicall ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `log.apicall` (wrapped in standard response)

---

#### `DELETE /api/v1/system/log:purge`
**Delete all API call logs.**

**Parameters:**

- `yes` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/log/{apicall}`
**Detail view of api call.**

**Parameters:**

- `apicall` (path, ) **(required)**: ID of the apicall
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `log.apicall` (wrapped in standard response)

---

#### `GET /api/v1/system/mgmt/interface`
****Deprecated call, use 'system interfaces mgmt get' instead****

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/mgmt/interface`
****Deprecated call, use 'system interfaces mgmt set' instead****

**Request Body** (`application/json`):

- `object`: SystemInterfaceConfig **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/mgmt/interface/public/address`
****Deprecated call, use 'system interfaces mgmt public-address' instead****

**Parameters:**

- `ipv` (query, )
- `operator` (query, )
- `ns` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/openapi`
**List available OpenAPI definition created during upgrade.**

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/system/openapi/{version}`
**Get the *version* OpenAPI definition if available.**

**Parameters:**

- `version` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/parameter`
**List parameters.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given parameter ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `system.parameter` (wrapped in standard response)

---

#### `POST /api/v1/system/parameter`
**Create parameter.**

**Request Body** (`application/json`):

- `object`: `system.parameter` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `system.parameter` (wrapped in standard response)

---

#### `GET /api/v1/system/parameter/{parameter}`
**Detail view of parameter.**

**Parameters:**

- `parameter` (path, ) **(required)**: ID of the parameter
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `system.parameter` (wrapped in standard response)

---

#### `PATCH /api/v1/system/parameter/{parameter}`
**Update parameter.**

**Parameters:**

- `parameter` (path, ) **(required)**: ID of the parameter

**Request Body** (`application/json`):

- `object`: `system.parameter` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `system.parameter` (wrapped in standard response)

---

#### `DELETE /api/v1/system/parameter/{parameter}`
**Delete parameter.**

**Parameters:**

- `parameter` (path, ) **(required)**: ID of the parameter
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `system.parameter` (wrapped in standard response)

---

#### `GET /api/v1/system/preferences`
**Return system preferences.**

**Response 200**: `class.systempreferences` (wrapped in standard response)

---

#### `PATCH /api/v1/system/preferences`
**Set system preferencies.**

**Request Body** (`application/json`):

- `preferences`: SystemPreferences **(required)**

**Response 200**: `class.systempreferences` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/firmware`
**List firmwares available in repositories.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given syncfirmware ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `repository.firmware` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/firmware/{firmware}`
**Detail view of sync firmware.**

**Parameters:**

- `firmware` (path, ) **(required)**: ID of the syncfirmware
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `repository.firmware` (wrapped in standard response)

---

#### `DELETE /api/v1/system/repository/firmware/{firmware}`
**Remove downloaded firmware from remote repositories cache or
delete it from home repository.**

**Parameters:**

- `firmware` (path, ) **(required)**
- `interactive` (query, )
- `db_delete` (query, )

**Response 200**: `repository.firmware` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/firmware/{firmware}:download`
****NYI** Launch a task to download a firmware to the
repositories cache.**

**Parameters:**

- `firmware` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/firmware/{firmware}:extract`
****NYI** Launch a task to extract firmware archive content from the
repositories cache.**

**Parameters:**

- `firmware` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/firmware/{firmware}:resolve`
**Trigger parent diff resolution and return state.**

**Parameters:**

- `firmware` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/repository/home`
**Detail view of repository.**

**Parameters:**

- `related_fields` (query, ): Extra fields to dump

**Response 200**: `repository.repository` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/home:deploy`
**Deploy local repository structure if required.**

**Request Body** (`application/json`):

- `rebuild`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/home:purge`
**Purge home repository backingstore of unused or obsolete firmwares.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `in_model`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/home:refresh`
**Refresh local repository with new firmwares and templates.**

**Request Body** (`application/json`):

- `dry_run`: boolean (default: False) — simulate meta generation
- `database`: boolean (default: True) — refresh or not information in Fabric Studio database
- `filename`: string

**Request Body** (`multipart/form-data`):

- `dry_run`: boolean (default: False) — simulate meta generation
- `database`: boolean (default: True) — refresh or not information in Fabric Studio database
- `filename`: string (format: binary)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/home/firmware`
**List home repository firmwares by filenames.**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/system/repository/home/firmware`
**Erase a home repository firmware by filename.**

**Parameters:**

- `name` (query, ) **(required)**
- `interactive` (query, )

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/home/firmware:import`
**Import a firmware in the home repository.**

**Request Body** (`application/json`):

- `input`: string **(required)**
- `if_exists`: string (default: abort) — What to do when a template with same name already exists in the home repository

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary) **(required)**
- `if_exists`: string (default: abort) — What to do when a template with same name already exists in the home repository

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/home/firmware/package`
**Package a custom splited firmware as a zip archive.**

**Request Body** (`application/json`):

- `name`: string **(required)**
- `output_dir`: string
- `overwrite`: boolean (default: False)
- `interactive`: boolean (default: True)

**Request Body** (`multipart/form-data`):

- `name`: string **(required)**
- `output_dir`: string (format: binary)
- `overwrite`: boolean (default: False)
- `interactive`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/home/template`
**List home repository fabric templates by filenames.**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/system/repository/home/template`
**Erase a home repository fabric template by filename.**

**Parameters:**

- `name` (query, ) **(required)**
- `interactive` (query, )

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/home/template:import`
**Import a fabric template in the home repository.**

**Request Body** (`application/json`):

- `input`: string **(required)**
- `if_exists`: string (default: rename) — What to do when a template with same name already exists in the home repository

**Request Body** (`multipart/form-data`):

- `input`: string (format: binary) **(required)**
- `if_exists`: string (default: rename) — What to do when a template with same name already exists in the home repository

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/repository/remote`
**List Repositories.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given repository ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `repository.repository` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/remote`
**Create repository.**

**Request Body** (`application/json`):

- `object`: `repository.repository` (see Schemas) **(required)**
- `related_fields`: array of str

**Response 200**: `repository.repository` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/remote:purge`
**Cleanup repository cache from unused firmwares.**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)
- `in_model`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/repository/remote:refresh-all`
**Refresh all remote repositories**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/remote/{repository}`
**Detail view of repository.**

**Parameters:**

- `repository` (path, ) **(required)**: ID of the repository
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `repository.repository` (wrapped in standard response)

---

#### `PATCH /api/v1/system/repository/remote/{repository}`
**Update repository.**

**Parameters:**

- `repository` (path, ) **(required)**: ID of the repository

**Request Body** (`application/json`):

- `object`: `repository.repository` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `repository.repository` (wrapped in standard response)

---

#### `DELETE /api/v1/system/repository/remote/{repository}`
**Delete repository.**

**Parameters:**

- `repository` (path, ) **(required)**: ID of the repository
- `interactive` (query, )
- `yes` (query, )

**Response 200**: `repository.repository` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/remote/{repository}:refresh`
**Refresh list of firmwares and pocs available from a remote repository.**

**Parameters:**

- `repository` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/template`
**List Fabric templates available in repositories.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given template ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `repository.template` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/template/{template}`
**Detail view of template.**

**Parameters:**

- `template` (path, ) **(required)**: ID of the template
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `repository.template` (wrapped in standard response)

---

#### `DELETE /api/v1/system/repository/template/{template}`
**Remove downloaded Fabric template from remote repositories
cache or delete it from home or system repository.**

**Parameters:**

- `template` (path, ) **(required)**
- `interactive` (query, )

**Response 200**: `repository.template` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/template/{template}:documentation`
**Download the template documentation.**

**Parameters:**

- `template` (path, ) **(required)**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/template/{template}:download`
**Download a Fabric template from remote repository to the repositories
cache.**

**Parameters:**

- `template` (path, ) **(required)**

**Request Body** (`application/json`):

- `force`: boolean (default: False)
- `interactive`: boolean (default: True)
- `prefetch_documentation`: boolean (default: False)
- `prefetch_firmware`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `POST /api/v1/system/repository/template/{template}:firmware`
**Download firmwares used by the template.**

**Parameters:**

- `template` (path, ) **(required)**

**Request Body** (`application/json`):

- `interactive`: boolean (default: True)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `GET /api/v1/system/repository/template/{template}/layout`
**Return template topology layout.**

**Parameters:**

- `template` (path, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/samba/account:disable`
**Disable admin user.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/samba/account:enable`
**Enable admin user.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/samba/account/password`
**Change password and enable (default) samba access for admin.**

**Request Body** (`application/json`):

- `password`: string **(required)**
- `enable`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/samba/configuration`
**Return SAMBA configuration.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/samba/services:start`
**Start smb and nmb services.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/samba/services:stop`
**Stop smb and nmb services.**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/security/preferences`
**Return security preferences.**

**Response 200**: `class.securitypreferences` (wrapped in standard response)

---

#### `PATCH /api/v1/system/security/preferences`
**Define security preferences.**

**Request Body** (`application/json`):

- `preferences`: SecurityPreferences **(required)**

**Response 200**: `class.securitypreferences` (wrapped in standard response)

---

#### `GET /api/v1/system/template`
**List available system templates.**

**Response 200**: array of `repository.template` (wrapped in standard response)

---

#### `POST /api/v1/system/template`
**Create a system template from a Fabric.**

**Request Body** (`application/json`):

- `fabric`: integer (format: int64) **(required)**
- `name`: string
- `interactive`: boolean (default: True)
- `overwrite`: boolean (default: False)

**Response 200**: `runtime.runtimetask` (wrapped in standard response)

---

#### `PATCH /api/v1/system/template/{template}`
**Rename a system template.**

**Parameters:**

- `template` (path, ) **(required)**: Specify template file name

**Request Body** (`application/json`):

- `name`: string **(required)**

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/system/template/{template}`
**Delete a system template.**

**Parameters:**

- `template` (path, ) **(required)**: Specify template file name

**Response 200**: `repository.template` (wrapped in standard response)

---

#### `GET /api/v1/system/upgrade/channel`
**Get the current upgrade channel.**

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/system/upgrade/channel`
**Change the default upgrade channel.**

**Request Body** (`application/json`):

- `channel`: string **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/user`
**List users.**

**Parameters:**

- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `limit` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given user ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array of `auth.user` (wrapped in standard response)

---

#### `GET /api/v1/system/user/{user}`
**Detail view of user.**

**Parameters:**

- `user` (path, ) **(required)**: ID of the user
- `related_fields` (query, ): Extra fields to dump

**Response 200**: `auth.user` (wrapped in standard response)

---

#### `PATCH /api/v1/system/user/{user}`
**Update user.**

**Parameters:**

- `user` (path, ) **(required)**: ID of the user

**Request Body** (`application/json`):

- `object`: `auth.user` (see Schemas) **(required)**
- `update_fields`: string
- `related_fields`: array of str

**Response 200**: `auth.user` (wrapped in standard response)

---

#### `POST /api/v1/system/user/password/{user}`
**Change user password.**

**Parameters:**

- `user` (path, ) **(required)**

**Request Body** (`application/json`):

- `current_password`: string
- `new_password`: string **(required)**
- `encrypted`: boolean (default: False)

**Response 200**: `auth.user` (wrapped in standard response)

---

#### `DELETE /api/v1/system/user/password/{user}`
**Disable a user password.**

**Parameters:**

- `user` (path, ) **(required)**
- `current_password` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/version`
**Get product version.**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/webserver/async/daemon`
**API call to manage gunicorn daemon. Daemon information are
extracted from *context._.settings.GUNICORN* (default).**

**Request Body** (`application/json`):

- `action`: string **(required)**
- `reload`: boolean (default: False) — start gunicorn with "--reload"
- `reload_engine`: string (default: auto) — gunicorn reload engine
- `kill`: boolean (default: False) — kill master daemon with SIGKILL when normal stop fails
- `django_debug`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/certificate`
**List available webserver certificates.**

**Response 200**: array (wrapped in standard response)

---

#### `DELETE /api/v1/system/webserver/https/certificate`
**Delete a webserver certificate.**

**Parameters:**

- `fqdn` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/webserver/https/certificate:import`
**Upload a webserver certificate.**

**Request Body** (`application/json`):

- `fqdn`: string **(required)**
- `crt`: string — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `key`: string — A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST **(required)**
- `overwrite`: boolean (default: False)

**Request Body** (`multipart/form-data`):

- `fqdn`: string **(required)**
- `crt`: string (format: binary) — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `key`: string (format: binary) — A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST **(required)**
- `overwrite`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/certificate/current`
**Current webserver certificate.**

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/system/webserver/https/certificate/current`
**Change webserver certificate.**

**Request Body** (`application/json`):

- `fqdn`: string **(required)**
- `force`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/certificate/source`
**Return URL of the webserver certificate archive source.**

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/system/webserver/https/certificate/source`
**Set URL to the webserver certificate archive source.**

**Request Body** (`application/json`):

- `url`: UrlInfo **(required)**
- `key`: string
- `crt`: string

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/webserver/https/certificate/source:refresh`
**Retrieve the webserver certificate archive from source and install it.**

**Request Body** (`application/json`):

- `restart`: boolean (default: True)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/certificates`
****Deprecated call, use 'webserver https certificate list' instead****

**Response 200**: array (wrapped in standard response)

---

#### `DELETE /api/v1/system/webserver/https/certificates`
****Deprecated call, use 'webserver https certificate delete' instead****

**Parameters:**

- `fqdn` (query, ) **(required)**

**Response 200**: Successful operation.

---

#### `POST /api/v1/system/webserver/https/certificates:import`
****Deprecated call, use 'webserver https certificate import' instead****

**Request Body** (`application/json`):

- `fqdn`: string **(required)**
- `crt`: string — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `key`: string — A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST **(required)**
- `overwrite`: boolean (default: False)

**Request Body** (`multipart/form-data`):

- `fqdn`: string **(required)**
- `crt`: string (format: binary) — A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST **(required)**
- `key`: string (format: binary) — A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST **(required)**
- `overwrite`: boolean (default: False)

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/port`
**The webserver HTTPS listening port.**

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/system/webserver/https/port`
**Change the webserver HTTPS listening port.**

**Request Body** (`application/json`):

- `port`: integer (format: int64) **(required)**

**Response 200**: Successful operation.

---

#### `GET /api/v1/system/webserver/https/redirect`
**Tell if webserver listen to HTTP port (80) and does a redirect to HTTPS.**

**Response 200**: Successful operation.

---

#### `PATCH /api/v1/system/webserver/https/redirect`
**Enable or disable listening on HTTP port (80) and doing a redirect to
HTTPS.**

**Request Body** (`application/json`):

- `state`: string **(required)**

**Response 200**: Successful operation.

---

### TASK Endpoints

#### `GET /api/v1/task`
**List tasks.**

**Parameters:**

- `running` (query, )
- `limit` (query, )
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given task ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `DELETE /api/v1/task`
**Stop all running tasks.**

**Parameters:**

- `timeout` (query, ): If 0 use SIGKILL else use SIGTERM and wait for timeout before doing a SGIKILL if necessary

**Response 200**: array (wrapped in standard response)

---

#### `POST /api/v1/task:purge`
**Purge system and old fabric tasks log.**

**Request Body** (`application/json`):

- `yes`: boolean (default: False)

**Response 200**: array of `number` (wrapped in standard response)

---

#### `POST /api/v1/task:refresh-all`

**Request Body** (`application/json`):

- `wait_launch`: boolean (default: True)

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/task/{task}`
**Show a running task status.**

**Parameters:**

- `task` (path, ) **(required)**
- `refresh` (query, )
- `related_fields` (query, ): Extra fields to dump

**Response 200**: Successful operation.

---

#### `DELETE /api/v1/task/{task}`
**Stop a running task.**

**Parameters:**

- `task` (path, ) **(required)**
- `timeout` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/task/{task}:log`
**Get a task log.**

**Parameters:**

- `task` (path, ) **(required)**
- `offset` (query, )
- `file` (query, )

**Response 200**: Successful operation.

---

#### `GET /api/v1/task/device`
**List tasks.**

**Parameters:**

- `device_id` (query, )
- `running` (query, )
- `limit` (query, )
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given task ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

#### `GET /api/v1/task/fabric`
**List tasks.**

**Parameters:**

- `fabric_id` (query, )
- `running` (query, )
- `limit` (query, )
- `select` (query, ): A DB filter
- `exclude` (query, ): A DB filter
- `order_by` (query, ): List of fields separated by a comma
- `startIndex` (query, )
- `endIndex` (query, )
- `page` (query, )
- `page_of` (query, ): Get page of given task ID
- `related_fields` (query, ): Extra fields to dump

**Response 200**: array (wrapped in standard response)

---

## Component Schemas

### `assets.fptype`

A Fabric Studio product type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `__model` | string | No | (default: `assets.fptype`; read-only) |

### `assets.license`

License(id, license, api_username, registrationDate, description, isDecommissioned, productModel, productModelEoR, productModelEoS, partner, expirationDate, licenseNumber, licenseSKU, licenseType, nb_cpu, fp_type)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `license` | integer | Yes | "license.license" object ID. |
| `api_username` | string | Yes |  |
| `registrationDate` | string | Yes | (format: date-time) |
| `description` | string | No |  |
| `isDecommissioned` | boolean | Yes |  |
| `productModel` | string | Yes |  |
| `productModelEoR` | string | No | (format: date-time) |
| `productModelEoS` | string | No | (format: date-time) |
| `partner` | string | No |  |
| `expirationDate` | string | No | (format: date-time) |
| `licenseNumber` | string | No |  |
| `licenseSKU` | string | No |  |
| `licenseType` | string | No |  |
| `nb_cpu` | integer | No | (default: `1`) |
| `fp_type` | integer | Yes | "assets.fptype" object ID. |
| `__model` | string | No | (default: `assets.license`; read-only) |

### `auth.user`


    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `last_login` | string | No | (format: date-time) |
| `username` | string | Yes | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. |
| `first_name` | string | No |  |
| `last_name` | string | No |  |
| `email` | string | No |  |
| `date_joined` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `__model` | string | No | (default: `auth.user`; read-only) |

### `certificates.cacertificate`

CACertificate(id, name, internal_name, not_after, subject, issuer, fingerprint, readonly, pem)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `internal_name` | string | Yes | (read-only) |
| `not_after` | string | Yes | (read-only; format: date-time) |
| `subject` | string | Yes | (read-only) |
| `issuer` | string | Yes | (read-only) |
| `fingerprint` | string | Yes | (read-only) |
| `readonly` | boolean | No | (default: `False`; read-only) |
| `pem` | string | Yes |  |
| `__model` | string | No | (default: `certificates.cacertificate`; read-only) |

### `class.addressinfo`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `family` | string | No |  |
| `local` | string | No |  |
| `prefixlen` | integer | No |  |
| `broadcast` | string | No |  |
| `scope` | string | No |  |
| `label` | string | No |  |
| `valid_life_time` | integer | No |  |
| `preferred_life_time` | integer | No |  |
| `__model` | string | No | (default: `class.addressinfo`; read-only) |

### `class.assetsaccount`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | string | No |  |
| `reftime` | integer | No |  |
| `refresh_token_time` | integer | No |  |
| `__model` | string | No | (default: `class.assetsaccount`; read-only) |

### `class.consolepreferences`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `vnc_public_allowed` | string | No |  |
| `spice_public_allowed` | string | No |  |
| `public_password` | string | No |  |
| `__model` | string | No | (default: `class.consolepreferences`; read-only) |

### `class.devicestatus`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `status` | string | No |  |
| `reason` | string | No |  |
| `__model` | string | No | (default: `class.devicestatus`; read-only) |

### `class.devicetype`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `order` | integer | No |  |
| `name` | string | No |  |
| `prefix` | string | No |  |
| `family` | string | No |  |
| `type` | string | No |  |
| `__model` | string | No | (default: `class.devicetype`; read-only) |

### `class.diskthresholds`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `system` | integer | No |  |
| `data` | integer | No |  |
| `__model` | string | No | (default: `class.diskthresholds`; read-only) |

### `class.flexvmaccount`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | string | No |  |
| `reftime` | integer | No |  |
| `refresh_token_time` | integer | No |  |
| `__model` | string | No | (default: `class.flexvmaccount`; read-only) |

### `class.flexvmautocreate`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | No |  |
| `max` | integer | No |  |
| `min` | integer | No |  |
| `__model` | string | No | (default: `class.flexvmautocreate`; read-only) |

### `class.flexvmsettings`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `auto_create` | `class.flexvmautocreate` | No |  |
| `supported_types` | string | No |  |
| `known_only` | boolean | No |  |
| `stop_on_release` | boolean | No |  |
| `__model` | string | No | (default: `class.flexvmsettings`; read-only) |

### `class.forticloudaccount`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `username` | string | No |  |
| `flexvm` | `class.flexvmaccount` | No |  |
| `assets` | `class.assetsaccount` | No |  |
| `__model` | string | No | (default: `class.forticloudaccount`; read-only) |

### `class.hugepages`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `available` | integer | No | (default: `0`) |
| `configured` | integer | No | (default: `0`) |
| `configured_on_boot` | integer | No | (default: `0`) |
| `free` | integer | No |  |
| `__model` | string | No | (default: `class.hugepages`; read-only) |

### `class.license`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `client` | `class.licenseclient` | No |  |
| `server` | `class.licenseserver` | No |  |
| `__model` | string | No | (default: `class.license`; read-only) |

### `class.licenseclient`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `server_url` | string | No |  |
| `legacy` | boolean | No |  |
| `group` | string | No |  |
| `supported` | array of string | No |  |
| `__model` | string | No | (default: `class.licenseclient`; read-only) |

### `class.licenseserver`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `enabled` | boolean | No |  |
| `local_enabled` | boolean | No |  |
| `supported` | array of string | No |  |
| `__model` | string | No | (default: `class.licenseserver`; read-only) |

### `class.lxcpreferences`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `dev_loop_allowed` | string | No |  |
| `dev_loop_max` | integer | No |  |
| `__model` | string | No | (default: `class.lxcpreferences`; read-only) |

### `class.monitoringmessage`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `message_version` | string | No | (default: `v1`) |
| `cpu_count` | integer | No |  |
| `type` | string | No | (default: `monitoring.runtime`) |
| `timestamp` | string | No | (format: date-time) |
| `is_resources_mounted` | boolean | No |  |
| `is_nested_enabled` | boolean | No |  |
| `is_swap_enabled` | boolean | No |  |
| `devices` | string | No |  |
| `zombies` | string | No |  |
| `fabric` | integer | No |  |
| `system` | string | No |  |
| `upgrades` | string | No |  |
| `reachables` | string | No |  |
| `hostname` | string | No |  |
| `information` | `class.systeminformation` | No |  |
| `hugepages` | `class.hugepages` | No |  |
| `thresholds` | `class.thresholds` | No |  |
| `license` | `class.license` | No |  |
| `__model` | string | No | (default: `class.monitoringmessage`; read-only) |

### `class.originalinformation`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | string | No |  |
| `size` | integer | No |  |
| `hexdigest` | string | No |  |
| `__model` | string | No | (default: `class.originalinformation`; read-only) |

### `class.otxorgconfiguration`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `xorg` | boolean | No |  |
| `xfreerdp_args` | string | No |  |
| `xfreerdp` | boolean | No |  |
| `xscreensaver_params` | `class.otxscreensaver` | No |  |
| `__model` | string | No | (default: `class.otxorgconfiguration`; read-only) |

### `class.otxscreensaver`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `timeout` | string | No |  |
| `lockTimeout` | string | No |  |
| `title` | string | No |  |
| `__model` | string | No | (default: `class.otxscreensaver`; read-only) |

### `class.passwordpreferences`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `minimum_length` | integer | No |  |
| `common_check` | string | No |  |
| `numeric_check` | string | No |  |
| `similarity_check` | string | No |  |
| `complexity_check` | string | No |  |
| `__model` | string | No | (default: `class.passwordpreferences`; read-only) |

### `class.securitypreferences`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `console` | `class.consolepreferences` | No |  |
| `password` | `class.passwordpreferences` | No |  |
| `lxc` | `class.lxcpreferences` | No |  |
| `ssh_public_allowed` | string | No |  |
| `http_public_allowed` | string | No |  |
| `https_public_allowed` | string | No |  |
| `custom_rules_allowed` | string | No |  |
| `web_session_age` | integer | No | Close all sessions on update |
| `cli_session_timeout` | integer | No | Active sessions are not affected |
| `__model` | string | No | (default: `class.securitypreferences`; read-only) |

### `class.sessionstatus`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `authenticated` | boolean | No |  |
| `username` | oneOf | No |  |
| `disclaimer` | string | No |  |
| `__model` | string | No | (default: `class.sessionstatus`; read-only) |

### `class.systeminformation`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `version` | string | No |  |
| `serial_number` | string | No |  |
| `uptime` | number | No |  |
| `frontend_version` | string | No |  |
| `__model` | string | No | (default: `class.systeminformation`; read-only) |

### `class.systeminterface`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `ifindex` | integer | No |  |
| `ifname` | string | No |  |
| `flags` | array of string | No |  |
| `mtu` | integer | No |  |
| `qdisc` | string | No |  |
| `operstate` | string | No |  |
| `group` | string | No |  |
| `txqlen` | integer | No |  |
| `link_type` | string | No |  |
| `address` | string | No |  |
| `broadcast` | string | No |  |
| `addr_info` | array of `class.addressinfo` | No |  |
| `__model` | string | No | (default: `class.systeminterface`; read-only) |

### `class.systeminterfaceconfig`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `mode` | string | No |  |
| `ipv4addr` | string | No | (default: ``) |
| `ipv4netmask` | string | No | (default: ``) |
| `ipv4gateway` | string | No | (default: ``) |
| `dns_primary` | string | No | (default: ``) |
| `dns_secondary` | string | No | (default: ``) |
| `ssh_port` | integer | No | (default: `22`) |
| `__model` | string | No | (default: `class.systeminterfaceconfig`; read-only) |

### `class.systempreferences`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `auto_connect` | boolean | No |  |
| `auto_address` | boolean | No |  |
| `auto_params` | boolean | No |  |
| `template` | string | No |  |
| `auto_resources_extend` | boolean | No |  |
| `server_zone` | string | No |  |
| `__model` | string | No | (default: `class.systempreferences`; read-only) |

### `class.thresholds`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `disks` | `class.diskthresholds` | No |  |
| `__model` | string | No | (default: `class.thresholds`; read-only) |

### `flexvm.config`

Configuration of a product for a program serial number.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `program` | integer | Yes | "flexvm.program" object ID. |
| `productType` | integer | Yes | "flexvm.producttype" object ID. |
| `status` | string | Yes |  |
| `__model` | string | No | (default: `flexvm.config`; read-only) |

### `flexvm.configparameter`

A config parameter and its value.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `config` | integer | Yes | "flexvm.config" object ID. |
| `parameter` | integer | Yes | "flexvm.parameter" object ID. |
| `value` | string | Yes |  |
| `__model` | string | No | (default: `flexvm.configparameter`; read-only) |

### `flexvm.fptype`

A Fabric Studio product type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `products` | integer | No |  |
| `__model` | string | No | (default: `flexvm.fptype`; read-only) |

### `flexvm.license`

A FortiFlex VM License.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `license` | integer | Yes | "license.license" object ID. |
| `config` | integer | No | "flexvm.config" object ID. |
| `not_before` | string | Yes | (format: date-time) |
| `status` | string | Yes |  |
| `tokenStatus` | string | Yes |  |
| `description` | string | No | (default: ``) |
| `__model` | string | No | (default: `flexvm.license`; read-only) |

### `flexvm.parameter`

A config parameter.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `__model` | string | No | (default: `flexvm.parameter`; read-only) |

### `flexvm.pool`

Select for a product which program serial number/config to look for
licenses.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `fp_type` | integer | Yes | "flexvm.fptype" object ID. |
| `config` | integer | Yes | "flexvm.config" object ID. |
| `__model` | string | No | (default: `flexvm.pool`; read-only) |

### `flexvm.producttype`

A FortiFlex VM product augmented with the Fabric product type.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `__model` | string | No | (default: `flexvm.producttype`; read-only) |

### `flexvm.program`

Program(id, accountId, serialNumber, startDate, endDate, hasSupportCoverage, api_username)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `accountId` | integer | Yes |  |
| `serialNumber` | string | Yes |  |
| `startDate` | string | Yes | (format: date-time) |
| `endDate` | string | Yes | (format: date-time) |
| `hasSupportCoverage` | boolean | Yes |  |
| `api_username` | string | Yes |  |
| `__model` | string | No | (default: `flexvm.program`; read-only) |

### `history.block`

Block(id, script, start_date, direction, offset, length)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `script` | integer | Yes | "history.script" object ID. |
| `start_date` | string | Yes | (format: date-time) |
| `direction` | string | Yes |  |
| `offset` | integer | Yes |  |
| `length` | integer | Yes |  |
| `__model` | string | No | (default: `history.block`; read-only) |

### `history.script`

Script(id, session, name, start_date, end_date, result, next_offset)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `session` | integer | Yes | "history.session" object ID. |
| `name` | string | Yes |  |
| `start_date` | string | Yes | (format: date-time) |
| `end_date` | string | No | (format: date-time) |
| `result` | string | No |  |
| `next_offset` | integer | Yes |  |
| `__model` | string | No | (default: `history.script`; read-only) |

### `history.session`

Session(id, vm, task, start_date, next_offset)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `vm` | integer | Yes | "model.vm" object ID. |
| `task` | string | Yes | "model.devicetask" object ID. |
| `start_date` | string | Yes | (format: date-time) |
| `next_offset` | integer | Yes |  |
| `__model` | string | No | (default: `history.session`; read-only) |

### `license.client`

Client(id, uuid, address, last_heartbeat, owner)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `uuid` | string | No | Client UUID. |
| `address` | string | No | Fabric Studio client public address using the license. (format: ipv4) |
| `last_heartbeat` | string | No | last time owner have been seen online. (default: `func:django.utils.timezone.now`; format: date-time) |
| `owner` | string | No | (default: ``) |
| `__model` | string | No | (default: `license.client`; read-only) |

### `license.license`

A Fortinet product license.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No | (read-only) |
| `mime_types` | string | No | (default: ``) |
| `id` | integer | No | "license.license" object ID |
| `max_cpu` | integer | No | Maximum number of CPU supported by the license. (default: `1`) |
| `vm_type` | string | No | The type of the license for Fabric Studio. |
| `subtype` | string | No | Extra license supported (ex: carrier). (default: ``) |
| `lic_type` | string | No | Type as it appears in the "lic" file. (read-only) |
| `vm_uuid` | string | No | VM UUID associated to the license, overrides the VM UUID defined in the Fabric. |
| `mgmt_addr` | string | No | IP Address associated to the license. (format: ipv4) |
| `mgmt_hwaddr` | string | No | Port hardware address associated to the license. |
| `from_server` | string | No | If received from a server the server address, blank for local. (read-only) |
| `chksum` | string | No | Internal chksum (without space and new line) to detect duplicated. |
| `not_after` | string | No | license expiration date if available. (format: date-time) |
| `group` | string | No | license group. (default: ``) |
| `enable` | boolean | No | (default: `True`) |
| `valid_until` | string | No | can't be used after this date, only when from a server. (format: date-time) |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `license.license`; read-only) |

### `license.served`

A license on a license server.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `license` | integer | Yes | "license.license" object ID. |
| `owner` | integer | Yes | "license.client" object ID. |
| `valid_until` | string | No | can be reused after this date. (format: date-time) |
| `registered_at` | string | No | date when license is assigned to the owner. (format: date-time) |
| `vm_nameid` | string | No | (default: ``) |
| `vm_id` | integer | No | (default: `0`) |
| `__model` | string | No | (default: `license.served`; read-only) |

### `log.apicall`

APICall(id, user, timestamp, command, arguments)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `user` | integer | No | "auth.user" object ID. |
| `timestamp` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `command` | string | Yes |  |
| `arguments` | string | Yes |  |
| `__model` | string | No | (default: `log.apicall`; read-only) |

### `model.cable`

A cable connects two ports together.

    Internally implemented with an OpenVSWicth and a copy openflow
    rule.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `conn1` | integer | Yes | Port connected to one end of the cable. "model.port" object ID. |
| `conn2` | integer | Yes | Port connected to other end of the cable. "model.port" object ID. |
| `hwaddr` | string | No | Internal hardware address used to manage the cable. Automatically filled by the API. |
| `description` | string | No | (default: ``) |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `__model` | string | No | (default: `model.cable`; read-only) |

### `model.defaultvmaccess`

DefaultVmAccess(id, vm, type, name, redirect, mode, path, fqdn, dport, fport, fport_idx, _order, vmaccess_ptr)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `vm` | integer | Yes | "model.vm" object ID. |
| `type` | string | Yes |  |
| `name` | string | Yes |  |
| `redirect` | integer | No | Use redirection rule, exclusive with fport and fport_idx. "model.portredirect" object ID. |
| `mode` | string | No | (default: `PRIVATE`) |
| `path` | string | No | Only for HTTP/HTTPS. (default: ``) |
| `fqdn` | string | No | Only for HTTP/HTTPS. (default: ``) |
| `dport` | integer | No | Destination port when is not default one. (default: `0`) |
| `fport` | integer | No | Source port, use 0 to use default one, exclusive with fport_idx and redirect. (default: `0`) |
| `fport_idx` | integer | No | Source port index, use 0 to user default one, exclusive with fport and redirect. (default: `0`) |
| `_order` | integer | Yes |  |
| `id` | integer | No | "model.defaultvmaccess" object ID |
| `__model` | string | No | (default: `model.defaultvmaccess`; read-only) |

### `model.deviceconfig`

DeviceConfig(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr, fabric, fabricstorage_ptr, vm_type, method)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `local_name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `fabric` | integer | No | "model.fabric" object ID. |
| `id` | integer | No | "model.deviceconfig" object ID |
| `vm_type` | string | Yes |  |
| `method` | string | No | Method to restore a VM configuration. (default: `RESTORE`) |
| `size` | string | No | (read-only) |
| `export_name` | string | No | (read-only) |
| `__model` | string | No | (default: `model.deviceconfig`; read-only) |

### `model.fabric`

A Fabric represents multiple devices interconnected all together by
different virtual networks and connections.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes | The name of the fabric. |
| `description` | string | No | A short description of the fabric. (default: ``) |
| `timeout` | integer | No | Communication timeout in seconds with a device. (default: `180`) |
| `version` | string | No | (default: `0.0.0`) |
| `maintainer` | string | No |  |
| `export_date` | string | No | (default: `func:django.utils.timezone.now`; read-only; format: date-time) |
| `create_date` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `docurl` | string | No | An URL to a zip archive with the fabric documentation. |
| `revert_mode` | string | No | How to use device's snapshots on fabric/devices install. (default: `SCR`) |
| `vm_hwaddr_prefix` | string | No | Default OUI to generate device's port hardware addresses. Automatically filled by the API. |
| `rt_hwaddr_prefix` | string | No | Default OUI to generate router's port hardware addresses. Automatically filled by the API. |
| `sw_hwaddr_prefix` | string | No | Default OUI to generate switches's port hardware addresses. Automatically filled by the API. |
| `override_pair_hwaddr_prefix` | string | No | Internal peer virtual port OUI. Automatically managed. (default: ``) |
| `override_router_pair_hwaddr_prefix` | string | No | Internal peer router port OUI. Automatically managed. (default: ``) |
| `password` | string | Yes | Default account password to use when default is not working, automatically changed on supported device. |
| `http_password` | string | No | Default HTTP password to use when default is not working, use *password* value if empty. (default: ``) |
| `console_password` | string | No | Graphical console access password. (default: ``) |
| `poweron_all_on_boot` | boolean | No | Power-on all devices on Fabric Studio boot. (default: `False`) |
| `runtime` | string | No | Return the runtime fabric if it exists. (read-only) |
| `pair_hwaddr_prefix` | string | No | (read-only) |
| `__model` | string | No | (default: `model.fabric`; read-only) |

### `model.fabricdocstatus`

FabricDocStatus(id, fabric, status)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `fabric` | integer | Yes | "model.fabric" object ID. |
| `status` | string | No | (default: `NONE`) |
| `__model` | string | No | (default: `model.fabricdocstatus`; read-only) |

### `model.fabricstorage`

Storage directory for a Fabric related files.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `id` | integer | No | "model.fabricstorage" object ID |
| `fabric` | integer | No | "model.fabric" object ID. |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `model.fabricstorage`; read-only) |

### `model.host`

Inner Fabric view of the Fabric host system.

This device allows to attach host system's ports to other devices
through the :py:class:`HostPort`.

The host is unique by Fabric and is automatically created with the
Fabric.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fabric` | integer | Yes | the fabric. "model.fabric" object ID. |
| `nameid` | string | No | Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the API. (read-only) |
| `name` | string | Yes | The device name. |
| `description` | string | No | A device description. (default: ``) |
| `auto_address_network` | integer | No | To automatically assign an address to the peer port when connecting a cable. "model.network" object ID. |
| `config` | integer | No | The configuration to load on the device. "model.deviceconfig" object ID. |
| `id` | integer | No | "model.host" object ID |
| `ipv4dns` | string | No | The main nameserver address, system one if empty. (format: ipv4) |
| `__model` | string | No | (default: `model.host`; read-only) |

### `model.hostport`

The host system's port exposed to the Fabric.

Automatically created with a Fabric and mirror a
:py:class:`fortipoc.core.django.system.models.Port` port.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | No | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `device` | integer | Yes | "model.device" object ID. |
| `id` | integer | No | "model.hostport" object ID |
| `ipv4addr` | string | No | (format: ipv4) |
| `ipv4netmask` | string | No | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `egress_nat` | boolean | No | Masquerade egress traffic. (default: `False`) |
| `ingress_nat` | boolean | No | Masquerade ingress traffic. (default: `False`) |
| `forwarding` | boolean | No | (default: `True`) |
| `dhcp_service` | boolean | No | Enable dhcp server (only for internal ports). (default: `False`) |
| `external` | integer | No | The external host port, only managed by the API. "system.port" object ID. |
| `peer` | oneOf | No |  |
| `cable` | oneOf | No |  |
| `pair_hwaddr` | oneOf | No |  |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `type` | string | No | (read-only) |
| `__model` | string | No | (default: `model.hostport`; read-only) |

### `model.installafter`

Track list of devices that must be started prior to the device.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `vm` | integer | Yes | The VM to be started after all other listed VM. "model.vm" object ID. |
| `after` | integer | No | The list of all VM to be installed before the VM. |
| `__model` | string | No | (default: `model.installafter`; read-only) |

### `model.installpolicy`

InstallPolicy(id, mode, fabric, max_queue)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `mode` | string | No | (default: `PAR`) |
| `fabric` | integer | Yes | "model.fabric" object ID. |
| `max_queue` | integer | No | (default: `0`) |
| `__model` | string | No | (default: `model.installpolicy`; read-only) |

### `model.network`

To help managing networks defined in a Fabric and assigning addresses
    to devices ports.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `fabric` | integer | Yes | The fabric. "model.fabric" object ID. |
| `name` | string | Yes | Name of the network. |
| `description` | string | No | (default: ``) |
| `ipv4network` | string | Yes | Network subnet. (format: ipv4) |
| `ipv4netmask` | string | Yes | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `ipv4gateway` | string | No | Default gateway for this network. (format: ipv4) |
| `ipv4dns1` | string | No | First nameserver address for this network. (format: ipv4) |
| `ipv4dns2` | string | No | Second nameserver address for this network. (format: ipv4) |
| `__model` | string | No | (default: `model.network`; read-only) |

### `model.portredirect`

PortRedirect(id, device, name, from_port, to_addr, to_port, snat, socktype, description, enabled)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `device` | integer | Yes | "model.host" object ID. |
| `name` | string | Yes |  |
| `from_port` | integer | Yes |  |
| `to_addr` | string | Yes | (format: ipv4) |
| `to_port` | integer | Yes |  |
| `snat` | boolean | No | Use *to_addr* as source. (default: `True`) |
| `socktype` | string | No | (default: `TCP`) |
| `description` | string | No | (default: ``) |
| `enabled` | boolean | No | (default: `True`) |
| `__model` | string | No | (default: `model.portredirect`; read-only) |

### `model.router`

A router is used to connect multiple ports from different networks.

    A router can define a default route.

    A router runs dnsmasq, tftp and ftp daemons.

    Internally a router is managed in a dedicated netns to isolate
    traffic.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fabric` | integer | Yes | the fabric. "model.fabric" object ID. |
| `nameid` | string | No | Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the API. |
| `name` | string | Yes | The device name. |
| `description` | string | No | A device description. (default: ``) |
| `auto_address_network` | integer | No | To automatically assign an address to the peer port when connecting a cable. "model.network" object ID. |
| `config` | integer | No | The configuration to load on the device. "model.deviceconfig" object ID. |
| `id` | integer | No | "model.router" object ID |
| `auto_params_network` | integer | No | Use this network default gateway and DNS'. "model.network" object ID. |
| `ipv4gateway` | string | No | The router's default gateway. (format: ipv4) |
| `ipv4dns` | string | No | The router nameserver address, none if empty. (format: ipv4) |
| `ports` | string | No | All device's ports. (read-only) |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `vm_type` | string | No | The VM type. (read-only) |
| `__model` | string | No | (default: `model.router`; read-only) |

### `model.routerport`

A router's port.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | No | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `device` | integer | Yes | "model.device" object ID. |
| `id` | integer | No | "model.routerport" object ID |
| `ipv4addr` | string | No | (format: ipv4) |
| `ipv4netmask` | string | No | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `mgmt` | boolean | No | (default: `False`) |
| `addrmode` | string | No | (default: `STA`) |
| `auto_config` | boolean | No | Address is configured by the Fabric Studio. (default: `True`) |
| `egress_nat` | boolean | No | Masquerade egress traffic. (default: `False`) |
| `ingress_nat` | boolean | No | Masquerade ingress traffic. (default: `False`) |
| `dhcp_service` | boolean | No | Enable dhcp server. (default: `False`) |
| `mtu` | integer | No | Force MTU of the interface, use 0 for system default. (default: `0`) |
| `peer` | oneOf | No |  |
| `cable` | oneOf | No |  |
| `pair_hwaddr` | oneOf | No |  |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `__model` | string | No | (default: `model.routerport`; read-only) |

### `model.runtimedhcpentry`

RuntimeDHCPEntry(id, router, port_id, nameid, hwaddr, ipv4addr, ipv4gateway, ipv4dns1, ipv4dns2, options)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `router` | integer | Yes | "model.device" object ID. |
| `port_id` | integer | Yes |  |
| `nameid` | string | Yes |  |
| `hwaddr` | string | Yes |  |
| `ipv4addr` | string | Yes | (format: ipv4) |
| `ipv4gateway` | string | No | (format: ipv4) |
| `ipv4dns1` | string | No | (format: ipv4) |
| `ipv4dns2` | string | No | (format: ipv4) |
| `options` | string | No | Options in TOML format. (default: ``) |
| `__model` | string | No | (default: `model.runtimedhcpentry`; read-only) |

### `model.switch`

A switch is used to connect multiple ports.

    Internally a router is managed by an OpenVSwitch bridge.
    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fabric` | integer | Yes | the fabric. "model.fabric" object ID. |
| `nameid` | string | No | Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the API. |
| `name` | string | Yes | The device name. |
| `description` | string | No | A device description. (default: ``) |
| `auto_address_network` | integer | No | To automatically assign an address to the peer port when connecting a cable. "model.network" object ID. |
| `config` | integer | No | The configuration to load on the device. "model.deviceconfig" object ID. |
| `id` | integer | No | "model.switch" object ID |
| `mgmt` | boolean | No | Is it a management switch or not. (default: `False`) |
| `ports` | string | No | All device's ports. (read-only) |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `vm_type` | string | No | The VM type. (read-only) |
| `__model` | string | No | (default: `model.switch`; read-only) |

### `model.switchlocalport`

Internal. The default port created with the switch.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | No | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `device` | integer | Yes | "model.device" object ID. |
| `id` | integer | No | "model.switchlocalport" object ID |
| `ipv4addr` | string | No | (format: ipv4) |
| `ipv4netmask` | string | No | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `peer` | oneOf | No |  |
| `cable` | oneOf | No |  |
| `pair_hwaddr` | string | No | A Switch Local Port has no pair hwaddr, always return None. (read-only) |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `__model` | string | No | (default: `model.switchlocalport`; read-only) |

### `model.switchport`

A switch port.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | No | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `device` | integer | Yes | "model.device" object ID. |
| `id` | integer | No | "model.switchport" object ID |
| `vlan` | integer | No | Port native VLAN. (default: `0`) |
| `trunk` | string | No | Comma separated list of VLANs or VLAN ranges. (default: ``) |
| `mode` | string | No | (default: `default`) |
| `peer` | oneOf | No |  |
| `cable` | oneOf | No |  |
| `pair_hwaddr` | string | No | A Switch Port has no pair hwaddr, always return None. (read-only) |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `__model` | string | No | (default: `model.switchport`; read-only) |

### `model.trafficcontrol`

Ingress traffic control for a port.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `port` | integer | No | "model.port" object ID. (read-only) |
| `delay` | integer | No | Delay in ms. (default: `0`) |
| `jitter` | integer | No | Jitter in ms. (default: `0`) |
| `corrupt` | number | No | (default: `0`) |
| `duplicate` | number | No | (default: `0`) |
| `reorder` | number | No | Requires delay. (default: `0`) |
| `loss` | number | No | (default: `0`) |
| `bandwidth` | integer | No | in bps, 0 is no bandwidth limit, minimum is 8. (default: `0`) |
| `bucket_size` | integer | No | bucket size in bytes. (default: `15000`) |
| `override` | boolean | No | (default: `False`; read-only) |
| `__model` | string | No | (default: `model.trafficcontrol`; read-only) |

### `model.vm`

Represent a device running in a virtual machine (either KVM or LXC).

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fabric` | integer | Yes | the fabric. "model.fabric" object ID. |
| `nameid` | string | No | Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the API. |
| `name` | string | Yes | The device name. |
| `description` | string | No | A device description. (default: ``) |
| `auto_address_network` | integer | No | To automatically assign an address to the peer port when connecting a cable. "model.network" object ID. |
| `config` | integer | No | The configuration to load on the device. "model.deviceconfig" object ID. |
| `id` | integer | No | "model.vm" object ID |
| `auto_params_network` | integer | No | Use this network default gateway and DNS'. "model.network" object ID. |
| `firmware` | integer | Yes | The firmware to run on this VM. "repository.firmware" object ID. |
| `ipv4gateway` | string | No | The default gateway to configure on this VM. (format: ipv4) |
| `ipv4dns1` | string | No | The primary nameserver to configure on this VM. (format: ipv4) |
| `ipv4dns2` | string | No | The secondary nameserver to configure on this VM. (format: ipv4) |
| `poweron_on_install` | boolean | No | Should the device be powered on during the Fabric installation. (default: `True`) |
| `poweron_on_boot` | boolean | No | Should the device be powered on after the Fabric Studio boot. (default: `False`) |
| `uuid` | string | No | VM UUID, automatically generated if empty. |
| `port_idx` | integer | Yes | Port forwarding index for automatic forwarding rules, automatically generated if null. |
| `timeout` | integer | No | When 0 use Fabric global timeout. (default: `0`) |
| `password` | string | No | Default account password to use when default is not working, automatically changed on supported device. Supersed Fabric password if not empty. (default: ``) |
| `http_password` | string | No | Default HTTP account password to use when default is not working. Supersed Fabric HTTP password if not empty. (default: ``) |
| `console_password` | string | No | Graphical console access password. Supersed Fabric console password if not empty. (default: ``) |
| `ports` | array of integer | No |  |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `vm_type` | string | No | The VM type. (read-only) |
| `mgmt_port` | integer | No | Return management port. (read-only) |
| `__model` | string | No | (default: `model.vm`; read-only) |

### `model.vmaccess`

VmAccess(id, vm, type, name, redirect, mode, path, fqdn, dport, fport, fport_idx, _order)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `vm` | integer | Yes | "model.vm" object ID. |
| `type` | string | Yes |  |
| `name` | string | Yes |  |
| `redirect` | integer | No | Use redirection rule, exclusive with fport and fport_idx. "model.portredirect" object ID. |
| `mode` | string | No | (default: `PRIVATE`) |
| `path` | string | No | Only for HTTP/HTTPS. (default: ``) |
| `fqdn` | string | No | Only for HTTP/HTTPS. (default: ``) |
| `dport` | integer | No | Destination port when is not default one. (default: `0`) |
| `fport` | integer | No | Source port, use 0 to use default one, exclusive with fport_idx and redirect. (default: `0`) |
| `fport_idx` | integer | No | Source port index, use 0 to user default one, exclusive with fport and redirect. (default: `0`) |
| `_order` | integer | Yes |  |
| `__model` | string | No | (default: `model.vmaccess`; read-only) |

### `model.vmdisk`

Represent a Vm disk.

Disk are declared or not in the meta.

When disks are not *extra* disks:

* A static disk is listed in the meta with a *declared* size of 0, it's a disk
  from the firmware. It can be extended: *capacity* >= *declared*. If
  *capacity* < *declared*, the capacity is ignored. By default *capacity* is 0.

* A dynamic disk is listed in the meta with a *declared* size > 0, it's not a
  disk from the firmware, it's created empty. It can be extended or shrinked: 0
  < *capacity*. By default *capacity* is set to *declared* value.

When disks are *extra* disks:

* A manually added disk in the DB with a *declared* size of 0, the *capacity* >
  0. The disk is created empty.

* A static disk, result of a firmware backup, the *declared* size > 0 but it's
  a disk from the firmware. It can be extended: *capacity* >= *declared*. If
  *capacity* < *declared*, the capacity is ignored.

All sizes are in MB.

+-------------+----------+-------+----------------------------------+
| declared    | capacity | extra |                                  |
| (from meta) | (DB)     |       |                                  |
+-------------+----------+-------+----------------------------------+
| 0           | >= 0     | False | static disk, build from firmware |
| 0           | > 0      | True  | extra disk, manually added       |
| > 0         | > 0      | False | dynamic disk, empty on build     |
| > 0         | > 0      | True  | extra disk, build from firmware  |
+-------------+----------+-------+----------------------------------+

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `vm` | integer | Yes | "model.vm" object ID. |
| `declared` | integer | Yes | size in MB: declared in the meta. |
| `capacity` | integer | Yes | expected disk size in MB for VM. |
| `name` | string | No | (default: ``; read-only) |
| `physical` | integer | No | Static disk physical size in the firmware archive if available. (default: `0`; read-only) |
| `extra` | boolean | No | Extra disk. (default: `False`) |
| `_order` | integer | Yes |  |
| `__model` | string | No | (default: `model.vmdisk`; read-only) |

### `model.vmlicense`

Link a VM to a license. This is a weak reference, so if license is
removed we can still know which license it was linked to.

A license can only be associated to one VM in a Fabric. But the license
can be associated to multiple VMs in multiple Fabric.

*serial_number* is always synchronized on save if a license is present
(*license*) and *serial_number* or *license* must be updated
(update_fields).

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `serial_number` | string | No | (default: ``) |
| `vm` | integer | No | "model.vm" object ID. |
| `license` | integer | No | "license.license" object ID. |
| `mode` | string | No | Method to select a license for the VM. (default: `AUTO`) |
| `served` | integer | No | "license.license" object ID. (read-only) |
| `supported` | string | No | Supported licenses type NONE, FLEX or LIC separated by comma, when empty use meta default. (default: ``) |
| `__model` | string | No | (default: `model.vmlicense`; read-only) |

### `model.vmparameters`

:py:class:`VmParameters` are used to override the default meta
values.

Override is a XML file, possible syntax::

  <override>
    <!-- delete a node or attrib based on xpath -->
    <action type="delete" path="XPATH" attrib="NAME|"/>
    <!-- set the atrtibute *attrib* or the node text if empty to TEXT -->
    <action type="set" path="XPATH" attrib="NAME|">TEXT</action>
    <!-- set text or attrib ... -->
    <action type="text">
      <domain><vcpu>10</vcpu></domain>
    </action>
    <action type="attrib">
      <domain><vcpu placement="dynamic"/></domain>
    </action>
  </override>

Problem: this syntax requires to repeat multiple time the same tree/xpath ...

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `vm` | integer | Yes | "model.vm" object ID. |
| `as_version` | string | No | Handle the firmware as this specific version. (default: ``) |
| `memory` | integer | No | VM memory size, when 0 use default value from meta. (default: `0`) |
| `cpu_count` | integer | No | Number of CPU, when 0 use default value from meta. (default: `0`) |
| `cpu_model` | string | No | Override CPU model, CPU mode must be set accordingly. (default: ``) |
| `cpu_mode` | string | No | (default: `DECLARED`) |
| `cpu_set` | string | No | comma separated list of CPUs number or CPUs range. (default: ``) |
| `video` | string | No | Override video driver, when empty use default value from meta. (default: ``) |
| `hugepages` | boolean | No | Use 1GB hugepages if available. (default: `False`) |
| `boot_menu_time` | integer | No | (default: `0`) |
| `override` | string | No | XML to update libvirt VM XML definition. |
| `install_license` | string | No | Install the license before the configuration or not, when undefined use meta default. (default: `FIRMWARE`) |
| `validate_license_wait` | integer | No | not set: default value, 0: infinite wait, time in seconds, negative: no wait. |
| `meta_patch` | string | No | (default: ``) |
| `expert` | string | No | Expert parameters in TOML format. (default: ``) |
| `use_firmware_uuid` | boolean | No | Use VM UUID stored in the firmware meta, for custom firmware it can be required if disk are encrytpted using the VM UUID. (default: `False`) |
| `__model` | string | No | (default: `model.vmparameters`; read-only) |

### `model.vmport`

A VM port.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | No | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `device` | integer | Yes | "model.device" object ID. |
| `id` | integer | No | "model.vmport" object ID |
| `ipv4addr` | string | No | (format: ipv4) |
| `ipv4netmask` | string | No | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `mgmt` | boolean | No | (default: `False`) |
| `addrmode` | string | No | (default: `STA`) |
| `auto_config` | boolean | No | Address is configured by the Fabric Studio. (default: `True`) |
| `dhcp_server` | integer | No | Native router that offers the address or empty if it's another device. "model.device" object ID. |
| `network` | integer | No | To configure gateway and nameserver served by the native DHCP service. "model.network" object ID. |
| `copy_hwaddr_from_peer` | boolean | No | Override HW address with the external System Host port peer on runtime. (default: `False`) |
| `mtu` | integer | No | Force MTU of the interface, use 0 for system default. (default: `0`) |
| `license_ip` | boolean | No | License is bound to this port IP. (default: `False`) |
| `peer` | oneOf | No |  |
| `cable` | oneOf | No |  |
| `pair_hwaddr` | oneOf | No |  |
| `runtime` | integer | No | Return the runtime element if it exists. (read-only) |
| `__model` | string | No | (default: `model.vmport`; read-only) |

### `model.vmstorage`

Storage to store files related to a VM.

    Storage is destroyed with the VM.
    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `id` | integer | No | "model.vmstorage" object ID |
| `vm` | integer | Yes | "model.vm" object ID. |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `model.vmstorage`; read-only) |

### `repository.firmware`

VM firmware.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | string | Yes |  |
| `hexdigest` | string | Yes |  |
| `size` | integer | Yes |  |
| `expiration` | string | No |  |
| `repository` | integer | Yes | "repository.repository" object ID. |
| `meta_hexdigest` | string | Yes | Checksum of the file meta information. |
| `status` | string | No | Status of the file. (default: `remote`) |
| `id` | integer | No | "repository.firmware" object ID |
| `vm_type` | string | No | (default: `BASIC`) |
| `major` | integer | No | (default: `0`) |
| `minor` | integer | No | (default: `0`) |
| `patch` | integer | No | (default: `0`) |
| `revision` | integer | No | (default: `0`) |
| `build` | integer | No | (default: `0`) |
| `version_s` | string | No | (default: ``) |
| `added_at` | string | No | Date when firmware information has been added locally. (format: date-time) |
| `diff_from` | integer | No | "repository.firmware" object ID. (read-only) |
| `is_diff` | boolean | No | Is the firmware a diff snapshot firmware. (default: `False`; read-only) |
| `original_detail` | string | No | Return original firmware details. (read-only) |
| `backup_state` | string | No | (read-only) |
| `__model` | string | No | (default: `repository.firmware`; read-only) |

### `repository.remotefile`

A file coming from a remote repository.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `file` | integer | Yes | "repository.repositoryfile" object ID. |
| `__model` | string | No | (default: `repository.remotefile`; read-only) |

### `repository.repository`

A repository that contains firmwares and Fabrics.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes | name of the repository. |
| `source` | string | Yes | Repository location. |
| `date` | string | No | repository update date. (format: date-time) |
| `active` | boolean | No | active repository. (default: `True`) |
| `chksum` | boolean | No | validate checksum of files. (default: `True`) |
| `signed` | boolean | No | repository is signed by a SSL certificate. (default: `False`) |
| `split` | boolean | No | allow split directory. (default: `False`) |
| `description` | string | No | (default: ``) |
| `sync` | string | No | repository last synchronization date. (format: date-time) |
| `cli` | boolean | No | added by CLI. (default: `False`) |
| `reg` | boolean | No | added by registration. (default: `False`) |
| `hide` | boolean | No | hide repository. (default: `False`) |
| `client_pem` | string | No |  |
| `client_key` | string | No |  |
| `private_ca` | integer | No | "certificates.cacertificate" object ID. |
| `__model` | string | No | (default: `repository.repository`; read-only) |

### `repository.repositoryfile`

A file stored in a repository.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `path` | string | Yes |  |
| `hexdigest` | string | Yes |  |
| `size` | integer | Yes |  |
| `expiration` | string | No |  |
| `repository` | integer | Yes | "repository.repository" object ID. |
| `meta_hexdigest` | string | Yes | Checksum of the file meta information. |
| `status` | string | No | Status of the file. (default: `remote`) |
| `__model` | string | No | (default: `repository.repositoryfile`; read-only) |

### `repository.serverzone`

ServerZone(id, zone, hostname, cname)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `zone` | string | Yes |  |
| `hostname` | string | Yes |  |
| `cname` | string | Yes |  |
| `__model` | string | No | (default: `repository.serverzone`; read-only) |

### `repository.template`

A Fabric template.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `path` | string | Yes |  |
| `hexdigest` | string | Yes |  |
| `size` | integer | Yes |  |
| `expiration` | string | No |  |
| `repository` | integer | Yes | "repository.repository" object ID. |
| `meta_hexdigest` | string | Yes | Checksum of the file meta information. |
| `status` | string | No | Status of the file. (default: `remote`) |
| `id` | integer | No | "repository.template" object ID |
| `name` | string | No |  |
| `docurl` | string | No |  |
| `description` | string | No | (default: ``) |
| `create_date` | string | No | (default: `1945-11-13T00:00:00Z`; format: date-time) |
| `export_date` | string | No | (default: `1945-11-13T00:00:00Z`; format: date-time) |
| `maintainer` | string | No |  |
| `version` | string | No | (default: `0.0.0`) |
| `__model` | string | No | (default: `repository.template`; read-only) |

### `runtime.fabricparameters`

Env.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `fabric` | string | Yes | "runtime.fabric" object ID. |
| `environment` | integer | No | "model.deviceconfig" object ID. |
| `__model` | string | No | (default: `runtime.fabricparameters`; read-only) |

### `runtime.runtimetask`

A global task related to the runtime.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `related_obj` | integer | No | "task.taskobject" object ID. |
| `author` | integer | No | "auth.user" object ID. |
| `name` | string | Yes | Task name. |
| `created_date` | string | No | Task Creation date. (default: `func:django.utils.timezone.now`; format: date-time) |
| `launched_date` | string | No | Task launched date. (format: date-time) |
| `returned_date` | string | No | Task returned date. (format: date-time) |
| `returncode` | integer | No | Task command return code. |
| `signal` | integer | No | Task command exited on this signal. |
| `monitor_pid` | integer | No | PID of monitoring process. (default: `0`) |
| `monitor_error` | string | No | error returned by the monitoring process. (default: ``) |
| `parent` | integer | No | "task.task" object ID. |
| `id` | integer | No | "runtime.runtimetask" object ID |
| `__model` | string | No | (default: `runtime.runtimetask`; read-only) |

### `runtime.vmstatus`

Information about a VM.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `last_modified` | string | No | (format: date-time) |
| `created` | string | No | (format: date-time) |
| `powered` | boolean | No | Is the VM power-on or not. (default: `False`) |
| `pre_boot_prepared` | boolean | No | Is the VM been pre configured. (default: `False`) |
| `post_boot_prepared` | boolean | No | Is the VM been post configured. (default: `False`) |
| `licensed` | boolean | No | Is the VM been licensed. (default: `False`) |
| `vm` | integer | Yes | "model.vm" object ID. |
| `__model` | string | No | (default: `runtime.vmstatus`; read-only) |

### `sessions.session`


    Django provides full support for anonymous sessions. The session
    framework lets you store and retrieve arbitrary data on a
    per-site-visitor basis. It stores data on the server side and
    abstracts the sending and receiving of cookies. Cookies contain a
    session ID -- not the data itself.

    The Django sessions framework is entirely cookie-based. It does
    not fall back to putting session IDs in URLs. This is an intentional
    design decision. Not only does that behavior make URLs ugly, it makes
    your site vulnerable to session-ID theft via the "Referer" header.

    For complete documentation on using Sessions in your code, consult
    the sessions documentation that is shipped with Django (also available
    on the Django web site).
    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `session_key` | string | Yes |  |
| `session_data` | string | Yes |  |
| `expire_date` | string | Yes | (format: date-time) |
| `__model` | string | No | (default: `sessions.session`; read-only) |

### `storage.pstorage`

PStorage(id, parent, created_at, modified_at, name, local_name, mime_types)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `parent` | integer | No | "storage.pstorage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `storage.pstorage`; read-only) |

### `storage.storage`

Storage(id, parent, created_at, modified_at, name, local_name, mime_types)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `storage.storage`; read-only) |

### `system.firewalladdress`

Address that can access the Fabric Studio.

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `ipaddr` | string | Yes |  |
| `policy` | string | Yes |  |
| `enabled` | boolean | No | (default: `True`) |
| `__model` | string | No | (default: `system.firewalladdress`; read-only) |

### `system.kernelmodule`

KernelModule(id, name, policy)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes |  |
| `policy` | string | Yes |  |
| `__model` | string | No | (default: `system.kernelmodule`; read-only) |

### `system.parameter`

A simple key/value pair associated to a user.

    A parameter can only be changed by it's owner.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `owner` | integer | No | "auth.user" object ID. |
| `name` | string | Yes |  |
| `value` | string | No |  |
| `__model` | string | No | (default: `system.parameter`; read-only) |

### `system.port`

A system port attached to a physical interface.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `name` | string | Yes | Interface name. |
| `index` | integer | No | (default: `0`) |
| `hwaddr` | string | Yes | Device side port hardware address. Automatically filled by the API. |
| `override_pair_hwaddr` | string | No | Internal peer virtual port hardware address. Automatically managed. (default: ``) |
| `ipv4addr` | string | No | (format: ipv4) |
| `ipv4netmask` | string | No | Network mask as cidr or quad-dotted notation. (format: ipv4) |
| `mgmt` | boolean | No | (default: `False`) |
| `addrmode` | string | No | (default: `STA`) |
| `sysname` | string | Yes | Interface name. |
| `missing` | boolean | No | True is the interface does not exists. (default: `True`) |
| `status` | string | No | (default: `Enabled`) |
| `__model` | string | No | (default: `system.port`; read-only) |

### `task.acktask`

AckTask(id, task, user, ack_date)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `task` | integer | Yes | "task.task" object ID. |
| `user` | integer | Yes | "auth.user" object ID. |
| `ack_date` | string | No | Task Acknowledge date. (default: `func:django.utils.timezone.now`; format: date-time) |
| `__model` | string | No | (default: `task.acktask`; read-only) |

### `task.task`

A task tracks an asynchronous process monitored by a *monitor*
process.

The :py:attr:`returncode` is the command exit code, it should be
betwwen 0 and 255. On normal termination it's normally 0 (but it
doesn't mean that the task was successful.)

There are 3 negative values to represent internal task management
errors:

:QUEUEERROR = -1: the task manager fails to queue the task (task
    conflict, storage error, ...)
:FAILED = -2: the task manager fails to retrieve task status (monitor
    has died, database objects are missing,...)
:SIGNALED = -3: the task has finished on a signal, you can find the
    signal value in :py:attr:`signal`.

All the task's information are stored in a log storage directory:

:cmdline: the execute command line for the task
:stdout: the stdout and stderr of the task command
:watched.pid: the task PID
:monitor.pid: PID of the monitor process
:monitor.log: the stdout and stderr of the monitor
:result.json: the result produced by the task if any
:status.json: the status of the task generated by the monitor

In case of task conflicts, the conflicting task IDs are stored as a
list in the *result.json* file.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `related_obj` | integer | No | "task.taskobject" object ID. |
| `author` | integer | No | "auth.user" object ID. |
| `name` | string | Yes | Task name. |
| `created_date` | string | No | Task Creation date. (default: `func:django.utils.timezone.now`; format: date-time) |
| `launched_date` | string | No | Task launched date. (format: date-time) |
| `returned_date` | string | No | Task returned date. (format: date-time) |
| `returncode` | integer | No | Task command return code. |
| `signal` | integer | No | Task command exited on this signal. |
| `monitor_pid` | integer | No | PID of monitoring process. (default: `0`) |
| `monitor_error` | string | No | error returned by the monitoring process. (default: ``) |
| `parent` | integer | No | "task.task" object ID. |
| `__model` | string | No | (default: `task.task`; read-only) |

### `task.taskobject`

TaskObject(id, obj_model, obj_pk, obj_parent, obj_name)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `obj_model` | string | No |  |
| `obj_pk` | integer | No | (default: `0`) |
| `obj_parent` | integer | No | "task.taskobject" object ID. |
| `obj_name` | string | No |  |
| `__model` | string | No | (default: `task.taskobject`; read-only) |

### `task.taskstorage`

TaskStorage(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr, task)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `id` | integer | No | "task.taskstorage" object ID |
| `task` | integer | No | "task.task" object ID. |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `task.taskstorage`; read-only) |

### `users.userprofile`

UserProfile(id, user, authmode, timezone, regmode, identity, email, title, uuid, status, expiration, update_date, is_empty_pam_password)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `user` | integer | Yes | "auth.user" object ID. |
| `authmode` | string | No | (default: `LOC`) |
| `timezone` | string | No | (default: ``) |
| `regmode` | string | No | (default: `fndn`) |
| `identity` | string | No |  |
| `email` | string | No | (default: ``) |
| `title` | string | No |  |
| `uuid` | string | No |  |
| `status` | string | No | (default: `FAILED`) |
| `expiration` | string | No | (format: date-time) |
| `update_date` | string | No | (format: date-time) |
| `is_empty_pam_password` | boolean | No | (default: `True`) |
| `__model` | string | No | (default: `users.userprofile`; read-only) |

### `visual.devicenode`

Define a node over a device, by default the image used is the device
vm_type.

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fabric` | integer | Yes | "model.fabric" object ID. |
| `name` | string | Yes |  |
| `nameid` | string | Yes |  |
| `level` | integer | No | (default: `-1`) |
| `image` | integer | No | "visual.nodeimage" object ID. |
| `vm_type` | string | No | (default: ``) |
| `id` | integer | No | "visual.devicenode" object ID |
| `device` | integer | Yes | "model.device" object ID. |
| `__model` | string | No | (default: `visual.devicenode`; read-only) |

### `visual.edge`

Edge(id, nameid, node_from, node_to)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `nameid` | string | Yes |  |
| `node_from` | integer | Yes | "visual.node" object ID. |
| `node_to` | integer | Yes | "visual.node" object ID. |
| `__model` | string | No | (default: `visual.edge`; read-only) |

### `visual.node`

Represent a graphical object on the topology.

If the object is an image, it can be a custom image stored as a NodeImage or a
device vm_type to use standard images.

To define a node over a device, use a DeviceNode.

:param fabric: the fabric
:param name: name of the node
:param level: define the layer level

    

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | integer | No |  |
| `fabric` | integer | Yes | "model.fabric" object ID. |
| `name` | string | Yes |  |
| `nameid` | string | Yes |  |
| `level` | integer | No | (default: `-1`) |
| `image` | integer | No | "visual.nodeimage" object ID. |
| `vm_type` | string | No | (default: ``) |
| `__model` | string | No | (default: `visual.node`; read-only) |

### `visual.nodeimage`

NodeImage(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr, fabric, fabricstorage_ptr)

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `parent` | integer | No | "storage.storage" object ID. |
| `created_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `modified_at` | string | No | (default: `func:django.utils.timezone.now`; format: date-time) |
| `name` | string | No |  |
| `mime_types` | string | No | (default: ``) |
| `fabric` | integer | No | "model.fabric" object ID. |
| `id` | integer | No | "visual.nodeimage" object ID |
| `size` | string | No | (read-only) |
| `__model` | string | No | (default: `visual.nodeimage`; read-only) |
