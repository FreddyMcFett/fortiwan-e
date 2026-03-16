# Fabric Studio User Guide

> **Important:** For Fortinet employees and allowed partners use only.

---

## Table of Contents

1. [Overview](#1-overview)
   - 1.1 Why Fabric Studio
   - 1.2 Terminology
2. [Getting Started](#2-getting-started)
   - 2.1 Registration with license key
   - 2.2 First steps
3. [Security Policy](#3-security-policy)
4. [Constraints](#4-constraints)
5. [API](#5-api)
6. [Working with Licenses](#6-working-with-licenses)
7. [Device Configuration](#7-device-configuration)
8. [Supported Devices](#8-supported-devices)
9. [Windows](#9-windows)
10. [Expert](#10-expert)
11. [Troubleshooting](#11-troubleshooting)
12. [FortiPoC Backward Compatibility](#12-fortipoc-backward-compatibility)
13. [Known Issues](#13-known-issues)

---

## 1. Overview

### 1.1. Why Fabric Studio

Fabric Studio is an internal Fortinet tool to create simple or complex network topology using the different Fortinet products. The core engine has been designed:

- for incremental creation/destruction of devices while a fabric is running
- for direct connection between ports of VMs
- to expose the API as a REST-like HTTP protocol and CLI commands with same behavior using Neutrino for frontend.

### 1.2. Terminology

- **fabric**: a fabric is a group of VM interconnected together by virtual networks *(a PoC in FortiPoC)*
- **template**: when you export a fabric it creates a template of this fabric. A template can be stored in a repository (in templates directory) or exchanged between users *(fpoc file in FortiPoC)*
- **firmware**: firmwares are the files that contains the disks used to start a VM or a LXC. Firmwares are stored in a repository (in firmwares directory). *(image(s) in FortiPoC)*
- **home repository**: a repository on your Fabric Studio where you can put new firmwares and shared templates *(the local repository in FortiPoC)*
- **system repository**: a repository on your Fabric Studio to manage local fabric templates used to create a fabric from scratch with a minimal topology
- **vm**: a LXC container or KVM virtual machine
- **router**: a simple router provided by Fabric Studio
- **switch**: a simple software switch provided by Fabric Studio *(a network in FortiPoC was a mixin of a switch and a router; a switch with a connection to the host internal port stays the closest representation in Fabric Studio)*
- **host**: represents the Fabric Studio and its external ports to let your fabric access devices outside the Fabric Studio and its internal ports that make the link between your fabric and internet

---

## 2. Getting Started

### 2.1. Registration with license key

In order to register your Fabric Studio you need a registration token generated from the Registration Server.

> **Warning:** The registration using the FNDN account is limited to partners.

In the repositories assigned to your token, when you used the default properties, you should have `fortinet (2.0)`, `third-party (2.0)`, `beta (2.0)`. If not please contact Fabric Studio Support Team.

Copy the "Token+Secret" string — it's your license key.

### 2.2. First steps

1. Login to Fabric Studio with `admin` username and no password *(it's highly recommended to change the default password when your Fabric Studio is exposed to internet)*
2. Go to **System/Registration**
3. Register the Fabric Studio with your license key
4. Go to **Fabric Workspaces**
5. Select **Create/Fabric**
6. Enter a name for your fabric or keep the default one
7. In the topology view, move mouse hover the top icon then click on the "FortiGate"
8. Click on the **Install** button on top bar buttons next to your fabric name

---

## 3. Security Policy

With Fabric Studio 2.0.1.interim.139 the default password security policy is strengthened, applies to all passwords and introduces new complexity constraints.

With Fabric Studio 2.0.0.interim.109 the default security policy has changed: the global configuration prevents access to fabric devices by default, user must explicitly open the access and port forwarding rules.

### 3.1. Password Security Policy

> **Warning:** By disabling or weakening the password policy, you increase your risk of being compromised when exposed to public internet and threats.

> **Important:** The policy doesn't apply to fabric when created from a template. You MUST verify passwords of the fabric if the Fabric Studio is exposed to internet, especially with old fabric templates, FortiPoC PoC.

#### 3.1.1. "admin" password

> **Important:** You must change the "admin" password on first CLI or GUI login.

You can only execute the following commands through SSH when the "admin" password is the default password:
- `system user password change`: to change the password
- `system account ssh keys add`: to add a SSH key and disable the "admin" default password

#### 3.1.2. Minimum length

The default minimum length is 8. To change:

```
system security preferences set '{"password": {"minimum_length": MIN_LENGTH}}'
```

#### 3.1.3. Common check

Validates the password against a default database of common passwords. Enabled by default.

To disable:
```
system security preferences set '{"password": {"common_check": "no"}}'
```

#### 3.1.4. Numeric check

Validates the password is not a number. Enabled by default.

To disable:
```
system security preferences set '{"password": {"numeric_check": "no"}}'
```

#### 3.1.5. Similarity check

Validates the password is not similar to a user attribute (e.g. identical to the username). Enabled by default.

To disable:
```
system security preferences set '{"password": {"similarity_check": "no"}}'
```

#### 3.1.6. Complexity check

Validates the password has at least three (3) of: one lower alpha, one upper alpha, one number, one special character. Enabled by default.

To disable:
```
system security preferences set '{"password": {"complexity_check": "no"}}'
```

### 3.2. System Host custom port redirection rules

Disabled by default. To enable:

```
system security preferences set '{"custom_rules_allowed": "yes"}'
```

> **Warning:** Ensure exposed ports are not vulnerable and you have taken necessary measures to protect from internet threats.

### 3.3. SSH access to device

By default SSH device access is in "PRIVATE" (Admin & Guest) mode — you MUST be logged in to Fabric Studio web frontend to have SSH access.

To expose SSH to internet:
```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
system security preferences set '{"ssh_public_allowed": "yes"}'
```

### 3.4. HTTPS access to device

By default HTTPS device access is in "PRIVATE" mode.

To expose HTTPS to internet:
```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
system security preferences set '{"https_public_allowed": "yes"}'
```

### 3.5. HTTP access to device

> **Warning:** HTTP access is only present for legacy compatibility. It is deprecated and planned to be removed in Fabric Studio 2.1. Do NOT expose HTTP to public internet.

To expose HTTP to internet:
```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
system security preferences set '{"http_public_allowed": "yes"}'
```

### 3.6. VNC and SPICE

By default VNC and SPICE are in "PRIVATE" mode.

To expose VNC/SPICE to internet:
```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
system security preferences set '{"console": {"spice_public_allowed": "yes", "vnc_public_allowed": "yes"}}'
model fabric update <FABRIC_ID> '{"console_password": <STRONG_PASSWORD>}'
```

Or per VM:
```
model vm update <VM_ID> '{"console_password": <STRONG_PASSWORD>}'
```

> **Warning:** VNC protocol limits password to 8 characters. If longer, it is truncated and Fabric Studio prevents public access by default.

#### 3.6.1. Without a password

If no display password is defined, VNC and SPICE are always at least "PRIVATE". To return to default:
```
system security preferences set '{"console": {"public_password": "required"}}'
```

#### 3.6.2. Forcing public binding

**Any password** (designed for bastion use cases only):
```
system security preferences set '{"console": {"public_password": "optional"}}'
```

**VNC Truncated password**:
```
system security preferences set '{"console": {"public_password": "truncated"}}'
```

### 3.7. Trusted and blocked addresses

Manage trusted/blocked IPv4 and IPv6 addresses using `system firewall address ...` commands:

- Default policy when no addresses created: **accept**
- Policy is **drop** if at least one enabled trusted address (policy="TRUSTED")
- Blocked addresses (policy="BLOCKED") are always processed first

Fabric Studio does a sanity check on create/update/delete when address matches current user connection address. To bypass: pass `force=true` option.

> **Note:** Fabric Studio always accepts: icmp protocol, any input traffic from non-management interfaces, and already established connections.

### 3.8. Fabric Studio Session duration

#### 3.8.1. Web Session

Default: 1 hour. To change:
```
system security preferences set '{"web_session_age": AGE_IN_SECONDS}'
```

#### 3.8.2. CLI Session

Default: 15 minutes of inactivity. To change:
```
system security preferences set '{"cli_session_timeout": TIMEOUT_IN_SECONDS}'
```

### 3.9. Fabric Studio License Server

A Fabric Studio client accessing a License Server by IP doesn't verify the CN but the SSL certificate must be the default self-signed certificate or a valid (e.g. letsencrypt) certificate.

> **Warning:** Using Fabric Studio License Server IP is only allowed for isolated labs. On the internet, install a valid SSL certificate and use FQDN.

#### 3.9.1. Deploying on cloud

When deployed on cloud, it's highly recommended to:
- Configure cloud firewall to only allow access from known management addresses
- Fabric Studio clients should be on the same VPC and use internal private IP of the License Server

---

## 4. Constraints

### 4.1. Limitations

Per fabric limits:
- 1000 VMs
- 224 total VM ports (max 9999 ports per VM, based on "portDDDD" naming)
- 224 total switch ports (max 9999 per switch) — **a switch counts as 1 port**
- 224 total router ports (max 9999 per router)
- 224 wires

### 4.2. OUI and HWADDR

Default OUIs:
- VM ports: `02:09:0F`
- VM pair virtual ethernet port: `F2:09:0F`
- Host system ports: `BE:09:0F`
- Host internal ports: `02:09:0F`
- Switches and switch ports: `CE:09:0F`
- Router ports: `DE:09:0F`
- Router ports pair: `FE:09:0F`
- Wires: `EE:09:0F`

For Host internal ports, HWADDR starts at FF:FF:01 (e.g. for int1: `02:09:0F:FF:FF:01`)

### 4.3. Reserved ports

| Port Range | Usage |
|-----------|-------|
| 10000-10999 | Reserved |
| 11000-11999 | SSH port redirection to VM |
| 12000-12999 | HTTP port redirection to VM |
| 13000-13999 | HTTPS reverse proxy port to VM |
| 14000-14999 | VM VNC console |
| 15000-15999 | VM SPICE console |
| 16000-16999 | HTTPS2HTTP reverse proxy port to VM |
| 17000-19999 | Reserved |

---

## 5. API

You can use the API through CLI or REST-like.

### 5.1. API Tutorial

#### 5.1.1. Introduction

REST-like works with both cookie-based (session and CSRF cookies + CSRF token) and API token (see OAuth2 Authorization Grants).

Cookies:
- `fortipoc-sessionid-<UUID>`: session cookie unique by Fabric Studio instance
- `fortipoc-csrftoken-<UUID>`: CSRF cookie unique by Fabric Studio instance
- `fortipoc-csrftoken`: a copy of the CSRF cookie; to be read by the frontend

#### 5.1.2. Session and CSRF

**Shell template** (base for all REST examples):

```sh
#!/bin/sh
# this file MUST be sourced
# your FortiPoC instance management address
if [ -z "${ADDR}" ]; then
  ADDR=FORTIPOC_ADDR
fi

# your cookie jar
COOKIE_JAR=${HOME}/fortipoc.jar

# if you have a valid SSL certificate remove the "-k" option
CURL="curl -k -c ${COOKIE_JAR}"

get_token() {
  awk '$6 == "fortipoc-csrftoken" { print $7 }' ${COOKIE_JAR}
}

rest() {
  if [ "${ADDR}" = "FORTIPOC_ADDR" ]; then
    echo 'ERROR: must specify your FortiPoC address in "ADDR" variable' >&2
    return 1
  fi
  local CSRF_TOKEN="$(get_token)"
  if [ -z "${CSRF_TOKEN}" ]; then
    ${CURL} -b ${COOKIE_JAR} -H "Referer: https://${ADDR}/" "$@"
  else
    ${CURL} -b ${COOKIE_JAR} -H "Referer: https://${ADDR}/" -H "X-FortiPoC-CSRFToken: ${CSRF_TOKEN}" "$@"
  fi
}

# Examples:
# rest -f https://${ADDR}/api/v1/session/check
# rest -f https://${ADDR}/api/v1/session/open -d username=admin -d password=
# or using JSON:
# rest -f https://${ADDR}/api/v1/session/open -H 'Content-Type: application/json' --data-raw '{"username": "admin", "password": ""}'
```

**JavaScript** — A frontend Javascript must extract the CSRF Token from the `fortipoc-csrftoken` cookie and place it on REST request as `X-FortiPoC-CSRFToken` HTTP header.

#### 5.1.3. API call request

**Object instance** — When an argument must be a model instance, pass as JSON:
```json
{
  "__model": "MODEL",
  "id": ID,
  "native_field1": value1,
  "native_field2": value2
}
```

- `__model`: optional when API call only accepts one model
- `id`: internal DB ID; do not specify on create; not required on update
- Omitted optional fields get default values on create; are left unchanged on update
- Unknown and read-only fields are ignored by the server

**CLI example**:
```
# model vm create '{"name": "FGT1", "firmware": 1}'
```

**GET QUERY** — For read-only API calls, pass arguments as GET parameters:
```
$ rest https://${ADDR}/api/v1/model/fabric -G \
  -d 'select=name=Test+Fabric+1' \
  -d 'related-fields=devices' \
  -d 'related-fields=devices.ports' \
  -d 'related-fields=devices.ports.wire'
```

**POST QUERY (JSON)**:
```
rest https://${ADDR}/api/v1/model/fabric \
  -H 'Content-Type: application/json' \
  --data-raw '{"name": "Test Fabric 1"}'
```

**POST QUERY (Form)**:
```
$ rest https://${ADDR}/api/v1/model/vm \
  -F 'object.name=FGT' \
  -F 'object.fabric=1' \
  -F 'object.firmware=1'

# Upload file:
$ rest https://${ADDR}/api/v1/model/fabric:import -F 'input=@my.fabric'
```

#### 5.1.4. API call result

```json
{
  "status": "error|done",
  "object": VALUE,
  "errors": {"MSG_KEY": ["ERROR_MSG"]},
  "warnings": {"MSG_KEY": ["WARNING_MSG"]},
  "rcode": 0,
  "page": {
    "number": "current page",
    "total": "total pages",
    "count": "total elements"
  },
  "others": {
    "global": [],
    "MODEL": {"ID": OBJECT}
  }
}
```

#### 5.1.5. Filtering expression

Two modes: `select` (include matching) and `exclude` (exclude matching). Select runs first.

Syntax: `KEY OPERATOR [CAST] VALUE`

Supported operators: `=`, `<`, `<=`, `>=`, `>`

Logical operators: `|` (OR), `&` (AND), `()` (grouping)

Examples:
```
# Name filter
model fabric list --select 'name="Test Fabric"'

# Complex filter
(name=Fabric|name=Test)&timeout>=300&password=fortinet

# Negative match (use exclude)
model fabric list --exclude 'name="Test Fabric"'

# Default lookup (CLI only)
model fabric list --select '"Test Fabric"'
```

**Field lookups** (Django QuerySet syntax, `__` replaced by `.`):
- `FIELD.contains=VALUE`
- `FIELD.gt=VALUE` (also gte, lt, lte)
- `FIELD.isnull=BOOL`
- Chain fields: `model device list --select 'fabric.name="Test Fabric"'`

#### 5.1.6. Related fields option

Used to retrieve extra fields or dive into referenced object details:

```
# List all devices of a fabric
cli json enable
model fabric list --related-fields devices

# Dump device's fabric detail
cli json enable
model device list --related-fields fabric --select name=sw1
```

#### 5.1.7. Websockets

Endpoint: `/api/ws/events`

**Monitoring event**:
```json
{"type": "monitoring.runtime", "timestamp": SECONDS_SINCE_EPOCH}
```

**Task events**:
```json
{"type": "task", "action": "new|return", "task": TASK_ID, "parent": PARENT_TASK_ID, "name": STRING, "timestamp": ISO_UTC, "pid": PID}
```

**Log events**:
```json
{"type": "log", "id": OBJECT_ID, "model": MODEL, "task": TASK_ID, "level": "print", "message": STRING, "timestamp": ISO_UTC, "linenb": LINE_NUMBER, "pid": PID}
```

### 5.2. CLI

CLI API commands available under: `DEBUG`, `MODEL`, `RUNTIME`, `SYSTEM`, `TASK`

**Fabric Studio Objects Model** (partial list):
- `model.cable`, `model.device`, `model.deviceconfig`, `model.fabric`, `model.host`, `model.hostport`
- `model.network`, `model.port`, `model.portredirect`, `model.router`, `model.routerport`
- `model.switch`, `model.switchport`, `model.vm`, `model.vmaccess`, `model.vmdisk`
- `model.vmlicense`, `model.vmparameters`, `model.vmport`, `model.vmstorage`
- `repository.firmware`, `repository.repository`, `repository.template`
- `runtime.runtimetask`, `runtime.vmstatus`
- `system.firewalladdress`, `system.parameter`

### 5.3. OpenAPI documentation

Available at: `/openapi/` on your Fabric Studio instance.

### 5.4. OAuth2 Authorization Grants

> **Warning:** All examples use `-k` option (self-signed cert). Install valid SSL certificate in production.

#### 5.4.1. Client Credential

Suitable for machine-to-machine authentication. The access token is automatically associated to the application user.

**Using CLI** (generate application and get CREDENTIAL):
```
$ system oauth2 application default create service-worker
```

**Store credential**:
```
CREDENTIAL=<base64_encoded_client_id:client_secret>
```

**Get access token**:
```
curl -k -X POST \
  -H "Authorization: Basic ${CREDENTIAL}" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  "https://${FABRIC_HOST}/oauth2/token/" \
  -d "grant_type=client_credentials"
```

Response:
```json
{"access_token": "TOKEN", "expires_in": 36000, "token_type": "Bearer", "scope": "read write"}
```

**Test API access**:
```
curl -k -X GET -H "Authorization: Bearer ${BEARER}" "https://${FABRIC_HOST}/api/v1/model/fabric"
```

#### 5.4.2. Authorization Code

> **Warning:** You have only one minute to validate the authorization code.

Best for web and mobile apps. Uses PKCE (Proof Key for Code Exchange).

**Generate code challenge**:
```python
import random, string, base64, hashlib
code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
code_challenge = hashlib.sha256(code_verifier).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').rstrip('=')
```

**Authorization URL**:
```
https://${FABRIC_HOST}/oauth2/authorize/?response_type=code&code_challenge=${CODE_CHALLENGE}&code_challenge_method=S256&client_id=${ID}&redirect_uri=http://127.0.0.1:8000/noexist/callback
```

**Get access token**:
```
curl -k -X POST -H "Content-Type: application/x-www-form-urlencoded" \
  "https://${FABRIC_HOST}/oauth2/token/" \
  -d "client_id=${ID}" -d "client_secret=${SECRET}" \
  -d "code=${CODE}" -d "code_verifier=${CODE_VERIFIER}" \
  -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
  -d "grant_type=authorization_code"
```

---

## 6. Working with Licenses

### 6.1. License Sources

#### 6.1.1. BYOL (Bring Your Own License)

Fabric Studio supports both `.lic` files and Flex-VM licenses.

Import via GUI (Repositories/Home:Licenses) or CLI:
```
scp FGVM00000000.lic admin@FABRIC_STUDIO_IP:
ssh admin@FABRIC_STUDIO_IP system license import FGVM00000000.lic
```

By default the copied license file is removed when the operation completes.

#### 6.1.2. License Server

Licenses can be retrieved from a Fabric Studio, FortiPoC, or labsetup license server.

> **Warning:** A Fabric Studio CANNOT be a license server for a FortiPoC.

**Configuring server**:
```
system license server service enable
```

**Configuring client (for Fabric Studio License Server)**:
```
system license client server url set https://FS_LICSRV/license/
```

> **Warning:** DON'T FORGET the `/license/` path.

SSL validation: FQDN = strict validation; IP = CA chain validation only (accepts default self-signed cert).

Set license group:
```
system license client request group set wkshop1
```

**For FortiPoC or LabSetup License Server**:
```
system license client server url set https://LICSRV/
system license client server legacy enable
```

### 6.2. Configuring device's license

> **Important:** The UUID attached to a license supersedes the VM's UUID defined in the Fabric.

#### 6.2.1. Linking license

Modes:
- **Automatic**: if device supports license, Fabric Studio must apply one (error if not)
- **Custom**: manually select the license to use
- **None**: no license installed

#### 6.2.2. Exporting a Fabric

License contents are never exported. Only the license serial number is exported in custom mode.

#### 6.2.3. License meta information

When importing a license, VM UUID is computed as: `uuid.uuid5(uuid.NAMESPACE_DNS, license.stem.upper())`

Default `mgmt_addr` values:
- FortiManager: `10.0.0.1`
- FortiSandbox: `10.0.0.1`

To set custom mgmt_addr:
```
system license update FMVMMLTM23002931 '{"mgmt_addr": "192.168.1.128"}'
```

#### 6.2.4. Devices with license key

For devices using a license key (e.g. FAD CM), create a license file:
```
-----BEGIN <MODEL> LICENSE-----
THE_KEY
-----END <MODEL> LICENSE-----
```

The MODEL must use spaces replaced by underscore (e.g. `FortiADC_CM`).

### 6.3. FortiFlex licenses

Fabric Studio supports the FortiFlex API to manage licenses.

> **Important:** Only standalone or License Server Fabric Studio should configure FortiFlex. A FortiFlex API user CANNOT be shared between multiple Fabric Studio instances.

#### 6.3.1. Prerequisites

ITF the post-paid FortiFlex FC-10-ELAVS-221-02-DD and activate it.

API User permissions must include:
- Asset Management: "Read & Write" for Asset Maintenance and Entitlement Management
- FortiFlex: enable access with "Read/Write" access type

#### 6.3.2. Credentials

```
system forticloud account set <API ID> [--password <Password>] [--accountId <Account_ID>]
```

> **Warning:** When using a Sub-OU API user, you MUST provide the account ID.

Refresh programs/configs after updating user on support.fortinet.com:
```
system license flex program refresh
system license flex config refresh
```

Remove credentials:
```
system forticloud account reset
```

#### 6.3.3. Configuration

Activate license type in a program:
```
system license flex pool set <TYPE> [--config <CONFIG_ID>]
```

Refresh available licenses:
```
system license flex license refresh *
```

Generate new licenses:
```
system license flex pool generate <POOL> <COUNT>
```

**Standalone** — Auto-create if pool exhausted (default enabled):
```
system license flex settings auto-create set disable|enable
```

#### 6.3.4. Duplicating FortiFlex VM configuration

```
ssh admin@<FS1> -- -j system license flex config export > config.json
scp config.json admin@<FS2>:
ssh admin@<FS2> system license flex config import config.json
```

#### 6.3.5. License auto stop

Fabric Studio tries to stop licenses when released (on fabric uninstall).

> **Important:** It's not guaranteed that licenses are effectively stopped. Users MUST verify and track point consumption.

For workshops:
```
# Disable auto stop
system license flex settings set '{"stop_on_release": false}'

# Reactivate all licenses before workshop
system license flex license reactivate all

# After workshop: stop all and re-enable
system license flex license stop all
system license flex settings set '{"stop_on_release": true}'
```

### 6.4. Organisation OU and Sub-OU

#### 6.4.1. Enabling feature

ITF a FC-15-CLDPS-219-02-DD and activate it. Enable Organization for your corporate account at:
https://support.fortinet.com/cred/#/sec/my-account/account-preferences

#### 6.4.2. Create organization

1. Note your account ID (from upper right user dropdown)
2. Create a Sub-OU (recommended: use hostname of license server)
3. Create a new member account in the Sub-OU
4. Logout

> **Warning:** Note the account ID for each member — required for FortiFlex API calls and can't be retrieved via API.

#### 6.4.3. Create your IAM user

In IAM, add IAM user with corporate email. Set permissions:
- Type: Organization
- Scope: Top level Organization
- Profile: SysAdmin

#### 6.4.4. Create API user

Login using IAM login (account ID, username, corporate password). Select Sub-OU member. Create permission profile and API user.

#### 6.4.5. Moving licenses between (Sub-)OU

Switch to the OU account (not user account) to move licenses between (Sub-)OUs.

---

## 7. Device Configuration

### 7.1. Fortinet products

Configuration sequence:
1. Fabric Studio uses serial console CLI to configure management port (static IP)
2. Uses SSH CLI to configure default route (using system host as next hop) and nameserver
3. Installs license (if any) via SSH CLI and waits for reboot
4. Waits for license validation if possible
5. Completes configuration: ports, default route, nameserver via SSH CLI or by restoring configuration

> **Important:** If configuration is encrypted, Fabric Studio uses password `fortinet`.

Three configuration methods:
- **Restore method**: full configuration — Fabric Studio restores via TFTP, FTP, etc.
- **Restore-Append method**: snippets — Fabric Studio backups config, appends snippet, restores
- **Script method**: snippets — Fabric Studio executes line by line via SSH

**Script method directives** (no preceding spaces):
- `#!confirm:<REGEXP>`: changes awaited prompt to send next command
- `#!reboot:[<REGEXP>]`: must be last line; waits for reboot after SSH disconnect

**Example (FortiMail gateway to transparent mode)**:
```
config system global
  set operation-mode transparent
  set hostname FML-t
end
#!confirm:Do you want to continue\? \(y/n\)
y
#!reboot:
```

#### 7.1.1. FortiGate VDOM

Fabric Studio can backup/restore configuration or install license with VDOMs enabled.

**HA mode** — Configure HA for port1 as management interface:
```
config system ha
  set ha-mgmt-status enable
  config ha-mgmt-interfaces
    edit 1
      set interface port1
    next
  end
end
```

**ZTP** — Warning: ZTP should only be achieved using port1. After static IP and license installation:
```
execute factoryreset keepvmlicense
```

#### 7.1.2. FortiManager License .LIC file

Default mgmt address: `10.0.0.1`. To set a different address:
```
system license update FMVMMLTM23002931 '{"mgmt_addr": "192.168.1.128"}'
```

For encrypted configuration: Fabric Studio uses `fortinet` as password.

To specify a version (for interim/special builds):
```
model vm parameters update VM_ID '{"as_version": "v7.4.2"}'
```

#### 7.1.3. FortiAnalyzer

Same as FortiManager for .LIC file and encrypted configuration.

### 7.2. Native devices

> **Warning:** Script configuration is EXPERIMENTAL.

#### 7.2.1. System Host Script

Allowed commands:
- `sysctl net.ipv4.XYZ=...`
- `sysctl net.ipv6.XYZ=...`
- `ip ...` (except `ip netns`)
- `tc ...`

#### 7.2.2. Router Script

Same as System Host plus:
- `nft ...`

#### 7.2.3. Switch Script

Allowed commands:
- `ovs-ofctl <COMMAND> ${SWITCH} ...` (no options starting with `-`)

**VLAN Modes**:
- **default**: (VLAN Unaware) allow any tagged/untagged packets
- **access**: packet is in Native VLAN; must NOT have 802.1Q header with nonzero VLAN ID
- **trunk**: VLAN from 802.1Q header or VLAN 0 if no header; Tagged VLANs are valid (empty = all valid)
- **native-tagged**: same as trunk but untagged packet VLAN from Native VLAN
- **native-untagged**: same as trunk but on out, Native VLAN is stripped

### 7.3. Third-party Linux devices

Fabric Studio supports Linux devices (LXC, Light Ubuntu VM, etc.) with post-installation, backup, and restore configuration.

The default `/fabric/init` script handles these actions. A second copy at `/fabric.init` is created for updates.

#### 7.3.1. Backup

> **Warning:** Backup only works when VM is powered on.

Process:
1. Fabric Studio calls `/fabric/init prepare` (script must copy files to backup under `/fabric`)
2. Generates `tar.gz` named `/.fabric_backup` with `/fabric` directory content
3. Retrieves file via SFTP

#### 7.3.2. Restore

Three timing options:

**Install** (fresh VM):
- Config file extracted to VM root directory before power-on
- Post-installation script executed as last SystemD service target

**Online** (VM running):
- Restore method: SFTP copy → extract → call `/fabric/init restore`
- Script method: SFTP copy to `/fabric.script` → call `/fabric/init script`

**Offline** (VM not running):
- Restore method: extract to root dir + create `/.ftnt/restore_on_boot` marker
- Script method: copy to root dir as `/fabric.script` + create `/.ftnt/script_on_boot` marker

#### 7.3.3. Post-Installation

On first boot: `/fabric/init install` is called. In `/.ftnt`:
- `postinst.<PID>.log`: post-installation logs
- `postinst.log`: symlink to latest log
- `postinst_done`: marker created on successful completion

### 7.4. Network

#### 7.4.1. DHCP

**Served by a VM**:
- Client VM port: set Addressing mode to DHCP; leave Native DHCP Server empty
- Default gateway in Network Parameters is only used when in same subnet as a Fabric Studio controlled port

**Served by a Native Device**:
- Client VM port: set Addressing mode to DHCP with mandatory Address and Mask
- Select which native device is the DHCP Server in the "Native DHCP Server" field
- If client's VM default gateway is in same subnet as the DHCP-handled port, gateway is included in DHCP lease

For a different gateway per port:
```
model vm port update PORT_ID '{"network": NETWORK_ID}'
```

**Extra DHCP options** (expert VM parameters, TOML format):
```
model vm parameters update VM_ID '{"expert": "[dhcp.port1]\n\"option:240\" = \"10.254.254.1\"\n\"option:241\" = \"etlab.net\"\n"}'
```

---

## 8. Supported Devices

### 8.1. Fortinet products

| Product | License F | License L | Backup B | Restore R | Restore-Append A | Script S |
|---------|-----------|-----------|----------|-----------|-----------------|---------|
| FortiADC | CLI | TFTP (NT) | TFTP | TFTP | TFTP (NT) | |
| FortiAnalyzer 7.4.2+ | CLI | CLI (NT) | FTP | FTP | NO (NT) | |
| FortiGate | CLI | TFTP (NT) | TFTP | TFTP | TFTP (NT) | |
| FortiManager 7.4.2+ | CLI | CLI (NT) | FTP | FTP | NO (NT) | |
| FortiMail | CLI | TFTP (NT) | TFTP | TFTP | TFTP (NT) | |
| FortiProxy | CLI (NT) | TFTP | TFTP | TFTP | TFTP (NT) | |
| FortiWeb | CLI | TFTP (NT) | TFTP | TFTP | TFTP (NT) | |
| FortiSOAR | SSH | SFTP/SSH | SFTP/SSH | SFTP/SSH | NO (NT) | |

Legend: NT = not tested, NO = not supported, HTTP = REST API, FTP = FTP transfer, TFTP = TFTP transfer, CLI = CLI on serial/SSH, SSH = CLI via SSH

#### 8.1.7. FortiClient EMS

> **Important:** Experimental and limited support. Must use DHCP to configure management port.

#### 8.1.13. FortiGate

> Upgrading: `.out` upgrade doesn't work due to Fabric Studio reverse proxy. Upgrade from FortiGuard works.

#### 8.1.26. FortiSOAR

> **Important:** FortiSOAR only supports one NIC (port1) and it must be in DHCP.

#### 8.1.28. FortiSwitch

> **Important:** License not required in standalone mode. FortiLink managed requires FortiSwitch license (ITF: LIC-FS24VM-INT). Use FSW_24VM-v7 image.

#### 8.1.29. FortiSwitch-NMS

> **Warning:** Serial console and display are automatically logged in by FortiSwitch-NMS — DO NOT PUBLICLY EXPOSE these to the internet!

### 8.2. Third-party devices

#### 8.2.1. ISO firmware

Live image ISOs don't use a persistent disk — Fabric Studio CAN'T configure, backup/restore, or execute postinst scripts. All must use DHCP.

#### 8.2.2. Debian-Lubuntu

Light Ubuntu installation with openssh-server. Supports LVM root filesystem for logical volume disk extension.

#### 8.2.3. VyOS LACP

To support LACP on VyOS, interface type must be e1000. Change from virtio:
```
model vm parameters update VM_ID '{"meta_patch": "<update node=\"./hypervisor/devices/interface/model\"><attribute name=\"type\" value=\"e1000\"/></update>"}'
```

### 8.3. Deep nested VMs

FortiDeceptor and FortiSandbox need to run VMs, creating Level 3 VMs:
- L0: Hypervisor (VMWare, GCP, ...)
- L1: Fabric Studio
- L2: FortiDeceptor, FortiSandbox
- L3: VMs

> **Warning:** Such depth is experimental and may not work or have poor performance.

---

## 9. Windows

### 9.1. Installation

Official images from Microsoft: Windows 10, Windows 10 Enterprise, Windows 11, Windows 11 Enterprise, Windows Server 2022.

> **Warning:** It's your responsibility to conform to Microsoft license and policies.

Default meta template uses e1000 network driver and sata disk. For virtIO, download driver ISO from Fedora.

#### 9.1.1. Copying ISO image

ISO filename must begin (case insensitive) with "windows" or "win" followed by a number and a dash/underscore:
```
Win10_22H2_EnglishInternational_x64v1.iso
Win11_23H2_EnglishInternational_x64v2.iso
windows-server-2022.iso
```

Copy to home repository:
```
scp Win11_23H2_EnglishInternational_x64v2.iso admin@FS_IP:firmwares/
```

Refresh home repository:
```
system repository home refresh
```

#### 9.1.2. Creating the Fabric

1. Define new Fabric
2. Add Windows device (select ISO if multiple)
3. Configure Windows ethernet port in DHCP
4. Configure Windows default gateway and DNS

#### 9.1.3. Installing Windows

```
runtime fabric install fabric
```

The Windows installation requires pressing a key to start. If on EFI shell, type `reset` to get that option.

#### 9.1.4. Installing with virtIO driver

1. Power off Windows device
2. Attach virtIO driver ISO:
```
runtime vm cdrom attach WINDOWS virtio-win-0.1.240.iso
```
3. Power on Windows device
4. When choosing hard disk, use **Load Driver** → select Red Hat VirtIO SCSI controller driver for your Windows version

#### 9.1.5. Exporting the Windows device disk

> **Warning:** With recent Windows, remove network adapter(s) from Device Manager before shutdown to ensure correct MAC on next boot.

```
runtime vm export WINDOWS windows-install
```

> **Warning:** When re-exporting, do NOT reuse the current disk name.

### 9.2. Timezone

Fabric Studio exposes system clock as UTC. Windows supposes system clock is in selected timezone. To fix, tell Fabric Studio to expose a timezoned clock.

#### 9.2.1. Add clock node

If no clock node exists in meta:
```
model vm parameters update 32 '{"meta_patch": "<insert node=\"./hypervisor\"><clock offset=\"timezone\" timezone=\"Europe/Paris\"/></insert>"}'
```

#### 9.2.2. Update clock node

If clock node already exists:
```
model vm parameters update 32 '{"meta_patch": "<update node=\"./hypervisor/clock\"><attribute name=\"offset\" value=\"timezone\"/><attribute name=\"timezone\" value=\"Europe/Paris\"/></update>"}'
```

---

## 10. Expert

### 10.1. Backup as Firmware: creating snapshot

Backup a VM disk to create a firmware in the home repository. Useful for products where configuration backup/restore isn't possible (e.g. Windows).

> **Warning:** You must shutdown the VM before exporting disks.

Checksum note: The empty checksum (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`) is always used for home directory firmware archives.

#### 10.1.1. Standalone snapshot firmware (default)

Merges runtime VM disks with original standalone firmware disks:
```
runtime vm export VM_ID_OR_NAMEID FIRMWARE_NAME
```

#### 10.1.2. Diff snapshot firmware

Extracts only the delta between runtime VM disks and original standalone firmware:
```
runtime vm export --diff VM_ID_OR_NAMEID FIRMWARE_NAME
```

> **Warning:** A diff snapshot firmware is FULLY DEPENDENT on the original standalone firmware.

#### 10.1.3. Tracked information

In (root) "model" XML node attributes:
- `is_pre_boot_prepared="<True or False>"`
- `is_licensed="SERIAL_NUMBER"`
- `is_post_boot_prepared="<True or False>"`

For diff firmware, the `model/diff_from` node tracks the original standalone firmware.

#### 10.1.4. Publishing to a repository

Package the snapshot firmware:
```
system repository home package <FIRMWARE_NAME>
```

Creates `<FIRMWARE_NAME>.zip` next to the split directory.

#### 10.1.5. Original standalone firmware resolution

`backup_state` values:
- `STANDALONE`: not a diff firmware
- `UNRESOLVED`: no original firmware found
- `RESOLVED`: original firmware found
- `FALLBACK`: not found, but one with same name is used

To query:
```
cli json enable
system repository firmware detail 809 --related-fields backup_state
```

To force resolution:
```
system repository firmware resolve ID
```

### 10.2. Extending disks

> **Note:** On boot, Fabric Studio adds available free space to data disk by default.

Disable auto extend:
```
system preferences set '{"auto_resources_extend": false}'
```

Add space options:
1. Extend existing disk: `qemu-img resize /path/to/FS_DOMAIN.qcow2 512G`
2. Add extra disk to VM definition

Then run:
```
system disk extend
```

> **Important:** Free space on firmware disk must be greater than 32GB, otherwise Fabric Studio will not extend the VG.

#### 10.2.1. Data disk

```
system disk data extend <SIZE>
```

#### 10.2.2. System disk

```
system disk system extend <SIZE>
```

(Size example: `32GiB` or `32GB`; use `0` for 100% of free space)

### 10.3. MTU Policy

Fabric Studio uses higher MTU for hypervisor virtual network to never fragment packets.

| Device | Guest MTU | Hypervisor MTU |
|--------|-----------|----------------|
| LXC VM | Configured or default if 0 | 65535 (max for VETH) |
| KVM VM | Default | 65521 (max for TUN/TAP) |
| Native Router | Configured MTU or 1500 if 0 | 65535 (max for VETH) |
| Host | 1500 (always default) | 1500 |
| Native Switch | 65535 (OpenVSwitch may reduce) | N/A |
| Cables | Follow Native Switch policy | N/A |

### 10.4. Meta files

#### 10.4.1. Templates

Meta templates describe one or more meta models for device firmware. They use filename pattern matching to identify firmwares.

**Pattern matching** uses Python regular expressions with extended match group syntax:
- `(%device%...)`: explicit named match group
- `{{version}}`, `{{build}}`: automatically replaced with complex expressions

**Meta model version matching** uses `<match>` nodes with expressions:
```xml
<match>version.major GT 6</match>
<match>version GTE 6.0.0.0.215</match>
<core>version GTE 1.0</core>
```

**Version Match Syntax** (EBNF, case insensitive):
- `VERSION`: full version (e.g. 1.2.3.4)
- `VERSION.MAJOR`: only major
- `VERSION:MINOR`: version up to minor
- Operators: `=`/`EQ`, `>`/`GT`, `>=`/`GTE`, `<`/`LT`, `<=`/`LTE`, `!=`/`NE`
- Logical: `|`/`OR`, `&`/`AND`

**Inherit** to avoid cloning full model trees:
```xml
<model name="FMG642">
  <inherit name="FMG62">
    <replace node="./detection/firmware/match">
      <match>version GT 7</match>
    </replace>
  </inherit>
</model>
```

**License Detection** (two modes):
1. ID mode: checks first line of license for `-----BEGIN <WORD> ... LICENSE-----`
2. Filename mode: matches `fname` regular expression

**License Installation** declaration:
```xml
<license install="first">
  <auto supported="LIC,FLEX">version GE 7.2</auto>
  <auto supported="LIC">version GT 0</auto>
</license>
```

**Debian image partitions** (specify root partition):
```xml
<mount type="part" part="p2">/</mount>
<!-- or for LVM: -->
<mount type="lvm" group="lubuntu" logical="root">/</mount>
```

#### 10.4.2. Patching

Meta patching syntax used by inheritance mechanism and VM `meta_patch` parameters.

Patching actions (execution order: delete → replace → insert → append → prepend → update):

**delete** — remove all matching nodes:
```xml
<delete node="XPATH"/>
```

**replace** — replace matching children:
```xml
<replace node="XPATH"><NEW_NODES/></replace>
```

**insert** — insert new children into node:
```xml
<insert node="XPATH"><NEW_NODES/></insert>
```

**append** — append after last matching node:
```xml
<append node="XPATH"><NEW_NODES/></append>
```

**prepend** — prepend before first matching node:
```xml
<prepend node="XPATH"><NEW_NODES/></prepend>
```

**update** — update node attributes:
```xml
<update node="XPATH">
  <attribute name="ATTR" value="NEW_VALUE"/>
  <attribute name="ATTR_TO_REMOVE"/>
</update>
```

> **Note:** Use `&quot;` for double quotes in XPath values.

### 10.5. VM Hooks

VM hooks allow extra steps during installation. Configured via "expert" VM parameter (TOML syntax):
```
model vmparameters update VM_ID '{"expert": "[section]\nkey=value\n..."}'
```

#### 10.5.1. Post boot configuration hooks

```toml
[post-boot-hooks]
pre-sleep=5
post-sleep=10
```

#### 10.5.2. License installation hooks

```toml
[license-hooks]
pre-sleep=5
post-sleep=10
```

### 10.6. Baremetal

#### 10.6.1. Native

Dump Fabric Studio disk to physical disk. 

> **Important:** Serial console connection to physical host is highly recommended.

Fabric Studio uses kernel interface detection order to link to its interfaces. To link a Fabric Studio interface to a system interface:
```
system expert interface link <NAME> <SYSNAME>
```

To list interfaces:
```
system interfaces list
```

Example:
```
system expert interface link mgmt1 ens13
```

Then reboot, or force changes:
```
system interfaces ports uninstall
system interfaces sync
system interfaces mgmt restart --uninstall
system interfaces ports up
```

#### 10.6.2. Docker

> **Warning:** STRICTLY LIMITED to a reduced audience for Fortinet office/datacenter labs only. NOT to be shared outside Fortinet.

Requirements:
- Expose all Linux capabilities (recommended)
- Use unique `FS_SYSTEM_UUID` per instance (avoid registration/license troubles)
- Use a volume per instance mounted at `/opt/ftnt/resources`
- Load kernel modules before any instance: `modprobe openvswitch nbd`

> **Warning:** Firmwares requiring disk patching don't work in docker (e.g. FortiSOAR, debian-lubuntu).

Example:
```
docker volume create instance-01-volume
docker create \
  --name instance-01 \
  -ti --privileged \
  -e FS_SYSTEM_UUID=03000200-0400-0500-0006-000700080009 \
  --tmpfs /run --tmpfs /run/lock \
  --mount source=instance-01-volume,target=/opt/ftnt/resources \
  fortinet/fabric-studio
docker start instance-01
```

---

## 11. Troubleshooting

### 11.1. Fabric Studio logs

Access from home repository shell:
```
system repository home shell
cd log/
ls -la service/
ls -la system/
```

Locations:
- `~/log/service/fortipoc`: Fabric Studio service logs
- `~/log/service/nginx`: nginx logs
- `~/log/system/`: operating system logs

### 11.2. SystemD Journal logs

```
system repository home shell
journalctl -D log/system/journal -u fortipoc.service -b 0
```

### 11.3. Sniff packets

Use `runtime diagnose tcpdump` with device name/nameid/ID and port name/ID:
```
runtime diagnose tcpdump LXC eth0
runtime diagnose tcpdump mgmtsw port2
runtime diagnose tcpdump mgmtsw port1
runtime diagnose tcpdump host int1
```

For Fabric Studio ports:
```
system diagnose tcpdump mgmt1
```

### 11.4. Not enough space

See section 10.2 (Extending disks).

### 11.5. Failing SCP

If SCP fails before changing the default password:
```
scp: Received message too long 1500476704
scp: Ensure the remote shell produces no output for non-interactive sessions.
```

Solution: Change the default `admin` password first.

---

## 12. FortiPoC Backward Compatibility

You should be able to import any FortiPoC PoC definitions.

**Limitations:**
- All configuration files are imported as full configuration using the "Restore" method. Manually update those that are snippets to use "Append-Restore" (the method used by FortiPoC). You can try "Script" method, but it's not guaranteed for all devices.
- The "copymac" introduced in FortiPoC 1.8.20 is converted to copy hwaddr from peer — verify the peer port is the right port.

---

## 13. Known Issues

*(No issues documented at this time.)*

---

*Documentation extracted from Fabric Studio User Guide at https://studio-01.mp-cloud.lab/help/*
