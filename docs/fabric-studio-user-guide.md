# Fabric Studio User Guide

> **Important:** For Fortinet employees and allowed partners use only.

---

## Table of Contents

- [1. Overview](#1-overview)
  - [1.1. Why Fabric Studio](#11-why-fabric-studio)
  - [1.2. Terminology](#12-terminology)
- [2. Getting started](#2-getting-started)
  - [2.1. Registration with license key](#21-registration-with-license-key)
  - [2.2. First steps](#22-first-steps)
- [3. Security Policy](#3-security-policy)
  - [3.1. Password Security Policy](#31-password-security-policy)
  - [3.2. System Host custom port redirection rules](#32-system-host-custom-port-redirection-rules)
  - [3.3. SSH access to device](#33-ssh-access-to-device)
  - [3.4. HTTPS access to device](#34-https-access-to-device)
  - [3.5. HTTP access to device](#35-http-access-to-device)
  - [3.6. VNC and SPICE](#36-vnc-and-spice)
  - [3.7. Trusted and blocked addresses](#37-trusted-and-blocked-addresses)
  - [3.8. Fabric Studio Session duration](#38-fabric-studio-session-duration)
  - [3.9. Fabric Studio License Server](#39-fabric-studio-license-server)
- [4. Constraints](#4-constraints)
  - [4.1. Limitations](#41-limitations)
  - [4.2. OUI and HWADDR](#42-oui-and-hwaddr)
  - [4.3. Reserved ports](#43-reserved-ports)
- [5. API](#5-api)
  - [5.1. API Tutorial](#51-api-tutorial)
  - [Shell](#shell)
  - [Javascript](#javascript)
  - [Object instance](#object-instance)
  - [CLI](#cli)
  - [GET QUERY](#get-query)
  - [POST QUERY](#post-query)
  - [Default lookup](#default-lookup)
  - [Field lookups](#field-lookups)
  - [/api/ws/events](#apiwsevents)
  - [5.2. CLI](#52-cli)
- [General options](#general-options)
  - [cli ctx ](#cli-ctx)
  - [cli debug ](#cli-debug)
  - [cli fork ](#cli-fork)
  - [cli json ](#cli-json)
  - [cli prefix ](#cli-prefix)
  - [cli restart ](#cli-restart)
  - [cli settings ](#cli-settings)
  - [cli terminal ](#cli-terminal)
  - [cli verbose ](#cli-verbose)
- [General options](#general-options)
  - [debug django ](#debug-django)
  - [debug whoami ](#debug-whoami)
- [General options](#general-options)
  - [model cable ](#model-cable)
  - [model debug ](#model-debug)
  - [model device ](#model-device)
  - [model diagnose ](#model-diagnose)
  - [model fabric ](#model-fabric)
  - [model host ](#model-host)
  - [model network ](#model-network)
  - [model object ](#model-object)
  - [model port ](#model-port)
  - [model router ](#model-router)
  - [model switch ](#model-switch)
  - [model tc ](#model-tc)
  - [model vm ](#model-vm)
- [General options](#general-options)
  - [runtime cable ](#runtime-cable)
  - [runtime config ](#runtime-config)
  - [runtime device ](#runtime-device)
  - [runtime diagnose ](#runtime-diagnose)
  - [runtime expert ](#runtime-expert)
  - [runtime fabric ](#runtime-fabric)
  - [runtime host ](#runtime-host)
  - [runtime license ](#runtime-license)
  - [runtime router ](#runtime-router)
  - [runtime switch ](#runtime-switch)
  - [runtime tc ](#runtime-tc)
  - [runtime vm ](#runtime-vm)
- [General options](#general-options)
  - [system account ](#system-account)
  - [system certificate ](#system-certificate)
  - [system db ](#system-db)
  - [system debug ](#system-debug)
  - [system diagnose ](#system-diagnose)
  - [system disclaimer ](#system-disclaimer)
  - [system disk ](#system-disk)
  - [system execute ](#system-execute)
  - [system expert ](#system-expert)
  - [system firewall ](#system-firewall)
  - [system forticloud ](#system-forticloud)
  - [system hostname ](#system-hostname)
  - [system information ](#system-information)
  - [system interfaces ](#system-interfaces)
  - [system kernel ](#system-kernel)
  - [system license ](#system-license)
  - [system log ](#system-log)
  - [system mgmt ](#system-mgmt)
  - [system monitoring ](#system-monitoring)
  - [system oauth2 ](#system-oauth2)
  - [system openapi ](#system-openapi)
  - [system ot ](#system-ot)
  - [system parameter ](#system-parameter)
  - [system preferences ](#system-preferences)
  - [system repository ](#system-repository)
  - [system samba ](#system-samba)
  - [system security ](#system-security)
  - [system support ](#system-support)
  - [system template ](#system-template)
  - [system upgrade ](#system-upgrade)
  - [system user ](#system-user)
  - [system version ](#system-version)
  - [system webserver ](#system-webserver)
- [General options](#general-options)
  - [task detail ](#task-detail)
  - [task device ](#task-device)
  - [task fabric ](#task-fabric)
  - [task kill ](#task-kill)
  - [task kill-all ](#task-kill-all)
  - [task list ](#task-list)
  - [task log ](#task-log)
  - [task purge ](#task-purge)
  - [task queue ](#task-queue)
  - [task refresh-all ](#task-refresh-all)
  - [task wait ](#task-wait)
- [admin.logentry  model](#adminlogentry-model)
- [assets.fptype  model](#assetsfptype-model)
- [assets.license  model](#assetslicense-model)
- [auth.group  model](#authgroup-model)
- [auth.permission  model](#authpermission-model)
- [auth.user  model](#authuser-model)
- [certificates.cacertificate  model](#certificatescacertificate-model)
- [contenttypes.contenttype  model](#contenttypescontenttype-model)
- [flexvm.config  model](#flexvmconfig-model)
- [flexvm.configparameter  model](#flexvmconfigparameter-model)
- [flexvm.fptype  model](#flexvmfptype-model)
- [flexvm.license  model](#flexvmlicense-model)
- [flexvm.parameter  model](#flexvmparameter-model)
- [flexvm.pool  model](#flexvmpool-model)
- [flexvm.producttype  model](#flexvmproducttype-model)
- [flexvm.program  model](#flexvmprogram-model)
- [history.block  model](#historyblock-model)
- [history.script  model](#historyscript-model)
- [history.session  model](#historysession-model)
- [license.client  model](#licenseclient-model)
- [license.license  model](#licenselicense-model)
- [license.served  model](#licenseserved-model)
- [log.apicall  model](#logapicall-model)
- [model.cable  model](#modelcable-model)
- [model.defaultvmaccess  model](#modeldefaultvmaccess-model)
- [model.device  model](#modeldevice-model)
- [model.deviceconfig  model](#modeldeviceconfig-model)
- [model.fabric  model](#modelfabric-model)
- [model.fabricdocstatus  model](#modelfabricdocstatus-model)
- [model.fabricstorage  model](#modelfabricstorage-model)
- [model.host  model](#modelhost-model)
- [model.hostport  model](#modelhostport-model)
- [model.installafter  model](#modelinstallafter-model)
- [model.installpolicy  model](#modelinstallpolicy-model)
- [model.network  model](#modelnetwork-model)
- [model.port  model](#modelport-model)
- [model.portredirect  model](#modelportredirect-model)
- [model.router  model](#modelrouter-model)
- [model.routerport  model](#modelrouterport-model)
- [model.runtimedhcpentry  model](#modelruntimedhcpentry-model)
- [model.switch  model](#modelswitch-model)
- [model.switchlocalport  model](#modelswitchlocalport-model)
- [model.switchport  model](#modelswitchport-model)
- [model.trafficcontrol  model](#modeltrafficcontrol-model)
- [model.vm  model](#modelvm-model)
- [model.vmaccess  model](#modelvmaccess-model)
- [model.vmdisk  model](#modelvmdisk-model)
- [model.vmlicense  model](#modelvmlicense-model)
- [model.vmparameters  model](#modelvmparameters-model)
- [model.vmport  model](#modelvmport-model)
- [model.vmstorage  model](#modelvmstorage-model)
- [oauth2_provider.accesstoken  model](#oauth2_provideraccesstoken-model)
- [oauth2_provider.application  model](#oauth2_providerapplication-model)
- [oauth2_provider.grant  model](#oauth2_providergrant-model)
- [oauth2_provider.idtoken  model](#oauth2_provideridtoken-model)
- [oauth2_provider.refreshtoken  model](#oauth2_providerrefreshtoken-model)
- [repository.firmware  model](#repositoryfirmware-model)
- [repository.remotefile  model](#repositoryremotefile-model)
- [repository.repository  model](#repositoryrepository-model)
- [repository.repositoryfile  model](#repositoryrepositoryfile-model)
- [repository.serverzone  model](#repositoryserverzone-model)
- [repository.template  model](#repositorytemplate-model)
- [runtime.fabricparameters  model](#runtimefabricparameters-model)
- [runtime.runtimetask  model](#runtimeruntimetask-model)
- [runtime.vmstatus  model](#runtimevmstatus-model)
- [sessions.session  model](#sessionssession-model)
- [storage.pstorage  model](#storagepstorage-model)
- [storage.storage  model](#storagestorage-model)
- [system.firewalladdress  model](#systemfirewalladdress-model)
- [system.kernelmodule  model](#systemkernelmodule-model)
- [system.parameter  model](#systemparameter-model)
- [system.port  model](#systemport-model)
- [task.acktask  model](#taskacktask-model)
- [task.task  model](#tasktask-model)
- [task.taskobject  model](#tasktaskobject-model)
- [task.taskstorage  model](#tasktaskstorage-model)
- [users.userprofile  model](#usersuserprofile-model)
- [visual.devicenode  model](#visualdevicenode-model)
- [visual.edge  model](#visualedge-model)
- [visual.node  model](#visualnode-model)
- [visual.nodeimage  model](#visualnodeimage-model)
  - [5.3. OpenAPI documentation](#53-openapi-documentation)
  - [5.4. OAuth2 Authorization Grants](#54-oauth2-authorization-grants)
  - [Application and credential](#application-and-credential)
  - [Get access token](#get-access-token)
  - [Test API access](#test-api-access)
  - [Register application](#register-application)
  - [Create code challenge](#create-code-challenge)
  - [Authorization code](#authorization-code)
  - [Get access token](#get-access-token)
  - [Test API access](#test-api-access)
  - [Python script example](#python-script-example)
- [6. Working with licenses](#6-working-with-licenses)
  - [6.1. License Sources](#61-license-sources)
  - [Configuring server](#configuring-server)
  - [Configuring client](#configuring-client)
  - [6.2. Configuring device’s license](#62-configuring-devices-license)
  - [Automatic](#automatic)
  - [Custom](#custom)
  - [None](#none)
  - [6.3. FortiFlex licenses](#63-fortiflex-licenses)
  - [API User](#api-user)
  - [Standalone](#standalone)
  - [License Server](#license-server)
  - [6.4. Organisation OU and Sub-OU](#64-organisation-ou-and-sub-ou)
- [7. Device configuration](#7-device-configuration)
  - [7.1. Fortinet products](#71-fortinet-products)
  - [7.2. Native devices](#72-native-devices)
  - [7.3. Third-party Linux devices](#73-third-party-linux-devices)
  - [7.4. Network](#74-network)
- [8. Supported Devices](#8-supported-devices)
  - [8.1. Fortinet products](#81-fortinet-products)
  - [8.2. Third-party devices](#82-third-party-devices)
  - [8.3. Deep nested VMs](#83-deep-nested-vms)
- [9. Windows](#9-windows)
  - [9.1. Installation](#91-installation)
  - [9.2. Timezone](#92-timezone)
- [10. Expert](#10-expert)
  - [10.1. Backup as Firmware: creating snapshot](#101-backup-as-firmware-creating-snapshot)
  - [10.2. Extending disks](#102-extending-disks)
  - [10.3. MTU Policy](#103-mtu-policy)
  - [LXC](#lxc)
  - [KVM](#kvm)
  - [10.4. Meta files](#104-meta-files)
  - [Filename pattern matching](#filename-pattern-matching)
  - [Meta model version matching](#meta-model-version-matching)
  - [Core model version matching](#core-model-version-matching)
  - [Evolution](#evolution)
  - [Version Match Syntax](#version-match-syntax)
  - [Inherit](#inherit)
  - [Firmware meta](#firmware-meta)
  - [License Detection](#license-detection)
  - [License Installation](#license-installation)
  - [Debian image partitions](#debian-image-partitions)
  - [10.5. VM Hooks](#105-vm-hooks)
  - [10.6. Baremetal](#106-baremetal)
  - [Interfaces](#interfaces)
- [11. Troubleshooting](#11-troubleshooting)
  - [11.1. Fabric Studio logs](#111-fabric-studio-logs)
  - [11.2. SystemD Journal logs](#112-systemd-journal-logs)
  - [11.3. Sniff packets](#113-sniff-packets)
  - [11.4. Not enough space](#114-not-enough-space)
  - [11.5. Failing SCP](#115-failing-scp)
- [12. FortiPoC backward compatibility](#12-fortipoc-backward-compatibility)
- [13. Known Issues](#13-known-issues)

---

## 1. Overview

### 1.1. Why Fabric Studio

Fabric Studio is an internal Fortinet tool to create simple or complex network topology using the
different Fortinet products.
The core engine has been designed:
for incremental creation/destruction of devices while a fabric [1] is running
for direct connection between ports of VMs
to expose the API as a REST-like HTTP protocol and CLI commands with same behavior
using Neutrino for frontend.

### 1.2. Terminology

fabric:
a fabric is a group of VM interconnected together by virtual networks [1]
template:
when you export a fabric it creates a template of this fabric. A template can be stored in a repository
(in templates  directory) or exchanged between users [2]
firmware:
firmwares are the files that contains the disks used to start a VM or a LXC. Firmwares are stored in a
repository (in firmwares  directory). [3]
home repository:
a repository on your Fabric Studio where you can put new firmwares and shared templates [4]
system repository:
a repository on your Fabric Studio to manage local fabric templates used to create a fabric from
scratch with a minimal topology
vm:
a LXC container or KVM virtual machine
router:
a simple router provided by Fabric Studio
switch:
a simple software switch provided by Fabric Studio [5]
host:
represents the Fabric Studio and its external ports to let your fabric access devices outside the
Fabric Studio and its internal ports that make the link between your fabric and internet
[1] (1,2)
a PoC in FortiPoC
[2]
fpoc file in FortiPoC
[3]
image(s) in FortiPoC
[4]
the local repository in FortiPoC
[5]
a network in FortiPoC was a mixin of a switch and a router, a switch with a connection to the host
internal port stays the closest representation in Fabric Studio

## 2. Getting started

### 2.1. Registration with license key

In order to register your Fabric Studio you need a registration token generated from the Registration
Server.

> **Warning**
> The registration using the FNDN account is limited to partners.
> In the repositories assigned to your token, when you used the default properties, you should have
> fortinet (2.0), third-party (2.0), beta (2.0), if not please contact Fabric Studio Support Team.
> Copy the “Token+Secret” string, it’s your license key.

### 2.2. First steps

login to Fabric Studio with admin username and no password [1]
go to “System/Registration”
register the Fabric Studio with your license key
go to “Fabric Workspaces”
select “Create/Fabric”
enter a name for your fabric or keep the default one
in the topology view, move mouse hover the top icon then click on the “FortiGate”
click on the “Install” button on top bar buttons next to your fabric name
[1]
it’s highly recommended to change the default password when your Fabric Studio is exposed to
internet

## 3. Security Policy

With Fabric Studio 2.0.1.interim.139 the default password security policy is strengthened, applies to
all passwords and introduces new complexity constraint (see Complexity check).
With Fabric Studio 2.0.0.interim.109 the default security policy has changed: the global configuration
prevents access to fabric devices by default, user must explicitly open the access and port
forwarding rules.

### 3.1. Password Security Policy

> **Warning**
> By disabling or weakening the password policy, you increase your risk of being compromised when
> exposed to public internet and threats. You may expose the company to loss of trust and bad
> reputation.

> **Important**
> The policy doesn’t apply to fabric when created from a template. You MUST verify passwords of the
> fabric if the Fabric Studio is exposed to internet, especially with old fabric templates, FortiPoC PoC.

#### 3.1.1. “admin” password

> **Important**
> You must change the “admin” password on first CLI or GUI login.
> You can only execute the following commands through SSH when the “admin” password is the
> default password:
> system user password change:
> to change the password
> system account ssh keys add:
> to add a SSH key and disable the “admin” default password

#### 3.1.2. Minimum length

The default minimum length is 8.
To change the value:

```
system security preferences set '{"password": {"minimum_length": MIN_LENGTH}}
```

#### 3.1.3. Common check

Validate the password against a default database of common password.

> **Note**
> This validation is enabled by default.
> To disable the validation:

```
system security preferences set '{"password": {"common_check": "no"}}'
```

#### 3.1.4. Numeric check

Validate the password is not a number.

> **Note**
> This validation is enabled by default.
> To disable the validation:

```
system security preferences set '{"password": {"numeric_check": "no"}}'
```

#### 3.1.5. Similarity check

Validate the password is not similar to a user attribute (eg: identical to the username).

> **Note**
> This validation is enabled by default.
> To disable the validation:

```
system security preferences set '{"password": {"similarity_check": "no"}}'
```

#### 3.1.6. Complexity check

Validate the password has at least three (3) of the following:
one (1) lower alpha
one (1) upper alpha
one (1) number
one (1) special character

> **Note**
> This validation is enabled by default.
> To disable the validation:

```
system security preferences set '{"password": {"complexity_check": "no"}}'
```

### 3.2. System Host custom port redirection rules

The System Host custom port redirection rules are disabled by default.
To enable them:

```
system security preferences set '{"custom_rules_allowed": "yes"}'
```

> **Warning**
> You must ensure the exposed ports are not vulnerable and that you have taken all necessary
> measures to protect from internet threats. Not complying may expose the company to loss of trust
> and bad reputation.

> **Important**
> The system security parameter has direct effect.

### 3.3. SSH access to device

Fabric Studio relies on a port redirection to expose a SSH device access.
By default the SSH device access is in a “PRIVATE” (Admin & Guest) mode, it means that you MUST
be logged in to Fabric Studio web frontend to have access to the device using the SSH web frontend.
The port redirection rule is disabled.
To expose the SSH device access to internet, you must comply with:
the device SSH access must be “PUBLIC” (Any):

```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
```

the Fabric Studio must allow public SSH access:

```
system security preferences set '{"ssh_public_allowed": "yes"}'
```

> **Important**
> The system security parameter has direct effect.

> **Warning**
> You MUST ensure the exposed devices are using strong passwords and that you have taken all
> necessary measures to protect from internet threats. Not complying may expose the company to loss
> of trust and bad reputation.

> **Important**
> Enabling public access also exposes the SSH web frontend to public access.

### 3.4. HTTPS access to device

Fabric Studio relies on a reverse proxy to expose HTTPS device access.
By default the HTTPS device access is in a “PRIVATE” (Admin & Guest) mode, it means that you
MUST be logged in to Fabric Studio web frontend to have access to the devices using the dedicated
port.
To expose the HTTPS device access to internet, you must comply with:
the device HTTPS access must be “PUBLIC”:

```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
```

the Fabric Studio must allow public HTTPS access:

```
system security preferences set '{"https_public_allowed": "yes"}'
```

> **Important**
> The system security parameter has direct effect.

> **Warning**
> You MUST ensure the exposed devices are using strong passwords and that you have taken all
> necessary measures to protect from internet threats. Not complying may expose the company to loss
> of trust and bad reputation.

### 3.5. HTTP access to device

> **Warning**
> HTTP access is only present for legacy compatibility, such access is deprecated and planned to be
> removed in Fabric Studio 2.1 (in worst case or before if imposed for security reason). You SHOULD
> NOT expose HTTP access to public internet and threats. Doing so may expose the company to loss
> of trust and bad reputation.
> Fabric Studio relies on a port redirection to expose a HTTP device access.

> **Note**
> Fabric Studio can’t use the reverse proxy for cookies security reasons.
> By default the HTTP device access is in a “PRIVATE” (Admin & Guest) mode, you have no way to
> access the device using HTTP except by using a device running in your fabric. The port redirection
> rule is disabled.
> To expose the HTTP device access to internet, you must comply with:
> the device HTTP access must be “PUBLIC” (Any):

```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
```

the Fabric Studio must allow public HTTP access:

```
system security preferences set '{"http_public_allowed": "yes"}'
```

> **Important**
> The system security parameter has direct effect.

### 3.6. VNC and SPICE

Fabric Studio protects the accesses to VNC and SPICE using firewall rules.
By default, the VNC and SPICE screen displays are in a “PRIVATE” (Admin & Guest), you can only
access them using the VNC or SPICE web frontends that require to be logged in to Fabric Studio.
To expose the VNC or SPICE access to internet you must comply with:
the device VNC or SPICE access must be “PUBLIC” (Any):

```
model vm access update <ACCESS_ID> '{"mode": "PUBLIC"}'
```

the Fabric Studio must allow public VNC or SPICE accesses:

```
system security preferences set '{"console": {"spice_public_allowed": "yes",
```

> **Important**
> The system security parameters have direct effect.
> you must define a “display password” in your fabric, eg:

```
model fabric update <FABRIC_ID> '{"console_password": <STRONG_PASSWORD>}'
```

Or define the “display password” by VM using the web interface (VM Advanced) or CLI:

```
model vm update <VM_ID> '{"console_password": <STRONG_PASSWORD>}'
```

> **Warning**
> VNC protocol limits password to 8 characters. If the fabric defines a longer password, it is truncated
> and Fabric Studio acts like the password is empty and prevents public access by default (see Forcing
> public binding for overriding options).

> **Warning**
> You MUST ensure the access is protected using strong passwords and that you have taken all
> necessary measures to protect from internet threats. Not complying may expose the company to loss
> of trust and bad reputation.

> **Note**
> If you are logged in to the Fabric Studio web frontend, you don’t need to enter the password when
> using the VNC or SPICE web frontends.

#### 3.6.1. Without a password

By default, if the fabric or VM don’t define a “display password” (or it is too long for VNC), VNC and
SPICE accesses are always at least “PRIVATE” (Admin & Guest) whatever the fabric defines and
you MUST be logged in to the Fabric Studio web frontend in order to use the VNC or SPICE web
frontends.
To return to default security preference:

```
system security preferences set '{"console": {"public_password": "required"}}
```

#### 3.6.2. Forcing public binding

#### Any password

> **Warning**
> This feature is designed for user using a frontend service (eg: a bastion) to control access to the
> Fabric Studio devices. DO NOT activate this if your Fabric Studio is exposed to public internet and
> threats. Not complying may expose the company to loss of trust and bad reputation.
> You can allow VNC and SPICE public access without a “display password” or a VNC truncated
> password (you should prefer VNC Truncated password solution in this last case):

```
system security preferences set '{"console": {"public_password": "optional"}}
```

#### VNC Truncated password

> **Warning**
> You MUST verify that truncated password is strong enough. Not complying may expose the company
> to loss of trust and bad reputation.

> **Note**
> Fabric Studio verifies that the truncated password follows the system password policy, if not the
> public access is not allowed in this mode.
> You can allow VNC public access with a truncated password:

```
system security preferences set '{"console": {"public_password": "truncated"}
```

### 3.7. Trusted and blocked addresses

You can define a list of trusted or blocked IPv4 and IPv6 network addresses for the management
interface (mgmt1) using the system firewall address ...  commands:
the default policy when no firewall addresses are created is accept
the policy is drop if you have at least one enabled trusted address ( policy="TRUSTED" )
the blocked addresses ( policy="BLOCKED" ) are always processed first
Fabric Studio implements a sanity check on create, update and delete when the address matches
current user connection address:
create: on creating a BLOCKED address
delete: on deleting a TRUSTED address if no other TRUSTED enabled addresses match
update:
enabling a disabled BLOCKED address
disabling a enabled TRUSTED address if no other TRUSTED enabled addresses match
To bypass the sanity check, you must pass the force=true  option.

> **Warning**
> The sanity check doesn’t work when you use the web frontend CLI.

> **Note**
> Fabric Studio always accepts:
> icmp protocol
> any input traffic from all others interfaces than management interface (mgmt1)
> any already established connection: if you block your own address, current (SSH) connection will
> persist

### 3.8. Fabric Studio Session duration

#### 3.8.1. Web Session

By default a web session is valid for 1 hour.
You can change the duration with:

```
system security preferences set '{"web_session_age": AGE_IN_SECONDS}'
```

#### 3.8.2. CLI Session

By default a CLI session timeouts after 15 minutes of inactivity.
You can change the inactivity timeout with:

```
system security preferences set '{"cli_session_timeout": TIMEOUT_IN_SECONDS}
```

### 3.9. Fabric Studio License Server

A Fabric Studio client can access a Fabric Studio License Server by the IP, the client doesn’t verify
the “CN” because it can’t match an IP, but the SSL certificate must be the default self-signed
certificate or a valid (eg: letsencrypt) certificate (see Configuring client - For a Fabric Studio License
Server).

> **Warning**
> Using the Fabric Studio License Server IP on your Fabric Studio client is only allowed for isolated
> labs and MUST NOT be used by a server on Internet. In this case you must install a valid SSL
> certificate (eg: letsencrypt) on your Fabric Studio License Server and configure the Fabric Studio
> client to access the license server using the corresponding FQDN.

#### 3.9.1. Deploying on cloud

When a Fabric Studio License Server is deployed on cloud, it’s highly recommended:
to configure the cloud firewall to only allow access from internet to the Fabric Studio License Server
for known management addresses
the Fabric Studio clients must be deployed on same VPC network and use the internal private IP of
the Fabric Studio License Server because of the first point

## 4. Constraints

### 4.1. Limitations

Outside any hardware and resources availability, the limitations by fabrics are:
1000 VMs
\(2^{24}\) total VM ports, with at most 9999 ports by VM (based on “portDDDD” naming convention).
\(2^{24}\) total switches ports with at most 9999 ports by switch (based on “portDDDD” naming
convention).

> **Warning**
> a switch counts itself as 1 port
> \(2^{24}\) total routers ports with at most 9999 ports by router (based on “portDDDD” naming
> convention).
> \(2^{24}\) wires

### 4.2. OUI and HWADDR

Defaults OUIs are:
for VMs ports: 02:09:0F
for VMs pair virtual ethernet port: F2:09:0F
for Host system ports: BE:09:0F
for Host internal ports: 02:09:0F
for switches and switches ports: CE:09:0F
for routers ports: DE:09:0F
for routers ports pair: FE:09:0F
for wires: EE:09:0F
For Host internal ports, HWADDR starts at FF:FF:01 , eg: for int1 02:09:0F:FF:FF:01

### 4.3. Reserved ports

10000-10999:
reserved
11000-11999:
used for SSH port redirection to Vm
12000-12999:
used for HTTP port redirection to Vm
13000-13999:
used for HTTPS reverse proxy port to Vm
14000-14999:
used by Vm VNC console
15000-15999:
used by Vm SPICE console
16000-16999:
used for HTTPS2HTTP reverse proxy port to Vm
17000-19999:
reserved

## 5. API

You can use the API through CLI or REST-like.
See API Tutorial for requirements.

### 5.1. API Tutorial

#### 5.1.1. Introduction

You can use the API through CLI or REST-like.
REST-like works with both cookie based (session and CSRF cookies + CSRF token) and API token
(see OAuth2 Authorization Grants).
When using cookies you have:
fortipoc-sessionid-<UUID>:
the session cookie unique by Fabric Studio instance
fortipoc-csrftoken-<UUID>:
the CSRF cookie unique by Fabric Studio instance
fortipoc-csrftoken:
a copie of the CSRF cookie; to be read by the frontend and ignored by the server. This cookie allows
simple extraction as the name is guessable

#### 5.1.2. Session and CSRF

### Shell

> **Note**
> this template is the base for all REST examples using shell in this documentation (download).

```
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
echo 'ERROR: must specify your FortiPoC address in "ADDR" variable' >
return 1
fi
local CSRF_TOKEN="$(get_token)"
if [ -z "${CSRF_TOKEN}" ]; then
${CURL} \
-b ${COOKIE_JAR} \
-H "Referer: https://${ADDR}/" \
"$@"
else
${CURL} \
-b ${COOKIE_JAR} \
-H "Referer: https://${ADDR}/" \
-H "X-FortiPoC-CSRFToken: ${CSRF_TOKEN}" \
"$@"
fi
}
cat <<EOF
Do not forget to define the ADDR variable with your FortiPoC address:
ADDR=${ADDR}
Examples:
  # get initial cookies (CSRF token) and check session state
  rest -f https://\${ADDR}/api/v1/session/check
  # login using Form
  rest -f https://\${ADDR}/api/v1/session/open \
      -d username=admin \
      -d password=
  # or using JSON
  rest -f https://\${ADDR}/api/v1/session/open \
       -H 'Content-Type: application/json' \
       --data-raw '{"username": "admin", "password": ""}'
EOF
```

### Javascript

A frontend Javascript must extract the CSRF Token from the fortipoc-csrftoken  cookie and place it
on REST request as X-FortiPoC-CSRFToken  HTTP header.
Template code (from https://docs.djangoproject.com/en/3.2/ref/csrf/):

```
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('fortipoc-csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-FortiPoC-CSRFToken", csrftoken);
        }
    }
});
```

> **Important**
> In FortiOS the CSRF token cookie is defined as Secure and so can’t be read from javascript. But
> even if we didn’t identify how it’s done, captures show that the cookie (csrftoken) value and header
> (x-csrftoken) value are the same.

#### 5.1.3. API call request

The CLI and REST API use common mechanism during the call.
For call details see CLI or OpenAPI documentation.

### Object instance

When an argument must be a model instance, it must be passed as a JSON object:

```
OBJECT := {
"__model": MODEL,
"id": ID,
"native_field1": value1,
"native_field2": value2,
...
}
```

Fields:
__model:
the object model string identifier, e.g.: model.vm

> **Note**
> When an API call only accepts one model, the __model is optional.
> id:
> the internal ID of the model instance in the database. It should not
> be specified on create. On update call it is not required as the ID is already specified in the command
> or the path.

> **Warning**
> Using a id value during a create call fails if another instance already exists for this id value.
> native_field*:
> the object instance’s native fields. You can omit optional fields, they will be assigned their default
> value during create. During an update the omitted fields are left unchanged.

> **Note**
> Unknown and read-only fields are ignored by the server.

### CLI

When using CLI you can pass the model instance as a JSON object string, e.g.:

```
# model vm create '{"name": "FGT1", "firmare": 1}'
```

To pass extra API call parameters, see the command help, e.g.:

```
# model fabric list --help
usage: model fabric list [-h] [--select FILTER] [--exclude FILTER]
       [--order-by ORDER_BY] [--limit LIMIT] [--page PAGE] [--page-of PAGE_OF
       [--related-fields [RELATED_FIELDS ...]]
List fabrics
optional arguments:
--help, -h            show this help message and exit
--select FILTER{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY
--limit LIMIT{int}
--page PAGE{int}
--page-of fabric{int}    Get page of given id
--related-fields RELATED_FIELDS{*}{str}
                        Extra fields to dump
```

Call example:

```
# cli json enable
# model fabric list --select 'name="Test Fabric"' \
--related-fields devices devices.ports devices.ports.wire
```

### GET QUERY

For read-only API calls (like fabric list ), you must pass arguments as GET parameters in the
URL.

> **Warning**
> Parameters must be properly encoded.
> Encoding key and values with python example:

```
$ python3 -c "import sys, urllib.parse; print(urllib.parse.urlencode({sys.std
select
name=Test Fabric 1
EOF
```

Result:

```
select=name%3DTest+Fabric+1
```

Example:

```
$ rest https://${ADDR}/api/v1/model/fabric -G \
      -d 'select=name=Test+Fabric+1' \
      -d 'related-fields=devices' \
      -d 'related-fields=devices.ports' \
      -d 'related-fields=devices.ports.wire'
```

### POST QUERY

Most API calls support both the JSON and Form POST payload encoding.
User should prefer the JSON to the Form format. But if you need to pass files to API call, you can
only use the Form format.

#### JSON

When calling an API, arguments must be in the POST payload as a JSON object with the call
argument name or options as keys.
Example to create a Fabric from default template, POST to api/v1/model/fabric :

```
rest https://${ADDR}/api/v1/model/fabric \
     -H 'Content-Type: application/json' \
     --data-raw '{"name": "Test Fabric 1"}'
```

Example to create a Fabric from alternate template, POST to api/v1/model/fabric :

```
rest https://${ADDR}/api/v1/model/fabric -X POST \
     -H 'Content-Type: application/json' \
     --data-raw '{"name": "Test Fabric 2", "template": "ZTNA"}'
```

#### Form

Both application/x-www-form-urlencoded  and multipart/form-data  are supported.
If an API call uses a Path  object as an argument you must use the multipart/form-data .
With form, each argument is a key/value pair.
The key is the argument name (e.g.: select ). But for objects, each element of the object must be
passed using a special key format:

```
ARGNAME.FIELD
```

> **Note**
> When an API call only accepts one model, it can be omited.
> Example:

```
$ rest https://${ADDR}/api/v1/model/vm \
      -F 'object.name=FGT' \
      -F 'object.fabric=1' \
      -F 'object.firmware=1'
```

To upload a file use the @  syntax:

```
$ rest https://${ADDR}/api/v1/model/fabric:import \
      -F 'input=@my.fabric'
```

#### 5.1.4. API call result

When using the CLI JSON output format ( --json ) or an HTTP REST request, most API calls return
an APIResult  except those generating a file (e.g.: exporting the Fabrics).
APIResult  structure is:

```
APIResult := {
"status": API_STATUS,
"object": VALUE,
"errors": {MSG_KEY: [ERROR_MSG, ...], ...}
"warnings": {MSG_KEY: [WARNING_MSG, ...], ...}
"rcode": RETURN_CODE,
"page": { # optional, only if object is a list returned by page
"number": current page number,
"total": total number of pages,
"count": total number of elements
  },
"others": { # optional, only if the call has side effect on other objects
"global": [ ANY ], # optional
    MODEL: {
      ID: OBJECT,
...
    },
...
  }
}
VALUE := OBJECT | JSON_VALUE
API_STATUS := "error" | "done"
ERROR := an error message
WARNING := a warning message, call can succeed but returns some
           warnings (like a missing firmware)
RCODE := the API call return code, 0 by default
OBJECT := {
"__model": MODEL,
"id": ID,
"native_field1": VALUE,
"native_field2": VALUE,
...
"extra_field1": VALUE | OBJECT,
...
"return": { # optional
"status": OBJ_STATUS,
"action": "add" | "del" | "upd" | "keep", # optional
"errors": {MSG_KEY: [ERROR_MSG, ...],  ...},
"warnings": {MSG_KEY: [WARNING_MSG, ...], ...},
   }
}
JSON_VALUE := see JSON native values
OBJ_STATUS := "done" | "error"
MSG_KEY := "global" general error of the object/call | OBJECT's
           native field name
ERROR_MSG := an error string
WARNING_MSG := a warning string
```

Extra fields are not part of the object model but can be a dynamic attribute or property value at the
time of the call, like device’s ports.

#### 5.1.5. Filtering expression

You have two filtering expression mode:
the select  to select elements matching the expression
the exclude  to exclude elements matching the expresssion
The select  is executed first then the exclude  applies on the result.
A filtering expression is composed of one or more keys, operators, cast and value groups:
the key is the field name you want to use to filter, e.g.: name
supported operators are = , < , <= , >= , >
an optional cast ( int , bool )
then the value you want to match, e.g.: Fabric
Some fields type can be infered and accept string representation:
boolean: True  (or 1 ) and False  (or 0 ), e.g.: active=True  or active=1
integer: the integer string representation, eg: timeout=300
If expressions require an explicit cast:
boolean: use (bool)True  or (bool)False
integer: use (int)VALUE
Example to find the Fabric named Fabric , the filter is name=Fabric .
You can also use logical operator |  for OR, &  for AND and parentheses ()  for grouping.
For example to search Fabrics named “Fabric” or “Test” and timeout value is greater than or equal to
300 seconds and that are using “fortinet” for password:

```
(name=Fabric|name=Test)&timeout>=300&password=fortinet
```

If value contains spaces or one of these special characters "()|&=<> , you must enclose the value
between " , e.g.:

```
name="Test Fabric"
```

If you pass it on the command line, you must escape it or enclose the whole expression between ' ,
e.g.:

```
# model fabric list --select 'name="Test Fabric"'
```

If you want to do a negative match ( != ), you must use the exclude  filter. Example to search all
Fabrics that are not named Test Fabric :

```
# model fabric list --exclude 'name="Test Fabric"'
```

### Default lookup

Some API commands have an implicit default key to search value, for instance the “model fabric list”
default key is name.contains , so to get all Fabrics that have “Test Fabric” in their name, you can
directly write:

```
# model fabric list --select '"Test Fabric"'
```

> **Warning**
> The default lookup only works for CLI commands but not REST.

### Field lookups

Fabric Studio uses a modified Django QuerySet syntax for the filed lookups function where the
double underscore __  from Django is replaced by the dot . .
Here is a small extract, refers to Django documentation for more
(https://docs.djangoproject.com/en/5.1/ref/models/querysets/#field-lookups):
FIELD__contains=VALUE:
find object where string FIELD contains the VALUE value
FIELD__gt=VALUE:
find object where numeral FIELD is greater than VALUE, other suffix are gte , lt , lte
FIELD__isnull=BOOL:
find object where the FIELD reference key is null or not null
With the dot notation:
FIELD__contains=VALUE:
can be written as FIELDS.contains=VALUE
FIELD__gt=VALUE:
can be written as FIELD.gt=VALUE
FIELD__insnull=VALUE:
can be written as FIELD.isnull=BOOL
With the QuerySet syntax, you can also chain the objects fields, e.g. to search devices that are part
of the fabric named “Test Fabric”:

```
$ fpcli model device list --select 'fabric.name="Test Fabric"'
```

> **Warning**
> This doesn’t work for some read-only fields that are dynamically computed values.
> The numerical comparison operators accepted notation are:
> NAME<VALUE :
> can be written as NAME.lt=VALUE
> NAME<=VALUE :
> can be written as NAME.lte=VALUE
> NAME>=VALUE :
> can be written as NAME.gte=VALUE
> NAME>VALUE :
> can be written as NAME.gt=VALUE

#### 5.1.6. Related fields option

The related-fields  option is used to retrieve extra fields (e.g. some read-only computed values or
reverse relationship like all the devices of a fabric) or dive into details of a referenced object about
extra fields (e.g. the detail of the device’s fabric).
For instance you can list all the devices of a fabric by specifying the devices  reverse relationship as
the related field.
Without:

```
# cli json enable
# model fabric list
{
"status": "done",
"object": [
      {
"name": "Test Fabric",
"description": "",
"timeout": 180,
"docurl": "",
"revert_mode": "SCR",
"hwaddr_prefix": "02:09:0F",
"override_pair_hwaddr_prefix": "",
"password": "fortinet",
...
```

With:

```
# cli json enable
# model fabric list --related-fields devices
{
"status": "done",
"object": [
      {
"name": "Test Fabric",
"description": "",
"timeout": 180,
"docurl": "",
"revert_mode": "SCR",
"hwaddr_prefix": "02:09:0F",
"override_pair_hwaddr_prefix": "",
"password": "fortinet",
"devices": [
              {
"fabric": 4,
"nameid": "sw000",
"name": "sw1",
"description": null,
"__model": "model.switch",
"id": 9
              },
...
```

Or you can dump the device’s fabric detail with the “fabric” reference key field.
Without:

```
# cli json enable
# model device list --select name=sw1
{
"status": "done",
"object": [
      {
"fabric": 4,
"nameid": "sw000",
"name": "sw1",
...
```

With:

```
# cli json enable
# model device list --related-fields fabric --select name=sw1
{
"status": "done",
"object": [
      {
"fabric": {
"name": "Test Fabric",
"description": "",
"timeout": 180,
"docurl": "",
"revert_mode": "SCR",
"hwaddr_prefix": "02:09:0F",
"override_pair_hwaddr_prefix": "",
"password": "fortinet",
"__model": "model.fabric",
"id": 4
          },
"nameid": "sw000",
"name": "sw1",
...
```

#### 5.1.7. Websockets

### /api/ws/events

The WebSocket to get notifications from Fabric Studio in JSON format:

```
{
"type": STRING,
"timestamp": TIMESTAMP,
   KEY: VALUE,
...
}
```

#### Monitoring

```
{
"type": "monitoring.runtime",
"timestamp": SECOND since epoch TIMESTAMP,
...
}
```

#### Task

```
{
"type": "task",
"action": "new",
"task": TASK_ID,
"parent": PARENT_TASK_ID or null,
"id": null,
"model": null,
"name": STRING
"timestamp": ISO formatted UTC TIMESTAMP STRING,
"pid": MONITORING_TASK_PID
}
{
"type": "task",
"action": "return",
"task": TASK_ID,
"parent": PARENT_TASK_ID or null,
"id": null,
"model": null,
"name": STRING
"timestamp": ISO formatted UTC TIMESTAMP STRING,
"pid": TASK_PID
}
```

#### Log

```
{
"type": "log",
"id":  OBJECT_ID,
"model": OBJECT MODEL,
"task": TASK_ID
"level": "print"
"message": STRING
"timestamp": ISO formatted UTC TIMESTAMP STRING,
"linenb": LINE  NUMBER
"pid": TASK_PID
}
```

### 5.2. CLI

CLI API

#### 5.2.1. CLI

# CLI

## General options

```
cli [-h] [{restart,prefix,ctx,verbose,debug,fork,terminal,settings,json}]
```

Positional arguments:
[{restart,prefix,ctx,verbose,debug,fork,terminal,settings,json}]
restart
Restart CLI.
prefix
Manage command line options.
ctx
Execution context.
verbose
debug
Manage debug flag.
fork
Propage debug and verbose flags on command fork.
terminal
Manage terminal.
settings
Execution settings.
json
Manage JSON output format.
Optional arguments:
--help, -h
show this help message and exit

### cli ctx 

```
cli ctx [-h] [{get}]
```

Execution context.
Positional arguments:
[{get}]
get
Get current context.
Optional arguments:
--help, -h
show this help message and exit

#### cli ctx get 

```
cli ctx get [-h]
```

Get current context.
Optional arguments:
--help, -h
show this help message and exit

### cli debug 

```
cli debug [-h] [<STATE>]
```

Manage debug flag.
Return: str | None
Positional arguments:
STATE{str} ('enable', 'disable')
Optional arguments:
--help, -h
show this help message and exit

### cli fork 

```
cli fork [-h] [<STATE>]
```

Propage debug and verbose flags on command fork.
Return: str
Positional arguments:
STATE{str} ('enable', 'disable')
Optional arguments:
--help, -h
show this help message and exit

### cli json 

```
cli json [-h] <STATE>
```

Manage JSON output format.
Positional arguments:
STATE{str} ('enable', 'disable')
Optional arguments:
--help, -h
show this help message and exit

### cli prefix 

```
cli prefix [-h] [{set,get}]
```

Manage command line options.
Positional arguments:
[{set,get}]
set
Define prefix options to add before the command.
get
Get prefix options added before command.
Optional arguments:
--help, -h
show this help message and exit

#### cli prefix get 

```
cli prefix get [-h]
```

Get prefix options added before command.
Optional arguments:
--help, -h
show this help message and exit

#### cli prefix set 

```
cli prefix set [-h] [<ARGS> ...]
```

Define prefix options to add before the command.
Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

### cli restart 

```
cli restart [-h]
```

Restart CLI.
Optional arguments:
--help, -h
show this help message and exit

### cli settings 

```
cli settings [-h] [{get}]
```

Execution settings.
Positional arguments:
[{get}]
get
Optional arguments:
--help, -h
show this help message and exit

#### cli settings get 

```
cli settings get [-h] <NAME>
```

Positional arguments:
NAME
Optional arguments:
--help, -h
show this help message and exit

### cli terminal 

```
cli terminal [-h] [{resize,reset}]
```

Manage terminal.
Positional arguments:
[{resize,reset}]
resize
Resize serial terminal to match real columns and row.
reset
Restart TTY console.
Optional arguments:
--help, -h
show this help message and exit

#### cli terminal reset 

```
cli terminal reset [-h]
```

Restart TTY console.
Optional arguments:
--help, -h
show this help message and exit

#### cli terminal resize 

```
cli terminal resize [-h]
```

Resize serial terminal to match real columns and row.

> **Warning**
> may break paste
> Optional arguments:
> --help, -h
> show this help message and exit

### cli verbose 

```
cli verbose [-h] [{set}]
```

Return: int
Positional arguments:
[{set}]
set
Optional arguments:
--help, -h
show this help message and exit

#### cli verbose set 

```
cli verbose set [-h] <LEVEL>
```

Positional arguments:
LEVEL{int}
Optional arguments:
--help, -h
show this help message and exit

# DEBUG

## General options

```
debug [-h] [{django,whoami}]
```

Positional arguments:
[{django,whoami}]
django
Django debugging
whoami
Tell which user you are.
Optional arguments:
--help, -h
show this help message and exit

### debug django 

```
debug django [-h] [{urls}]
```

Django debugging
Positional arguments:
[{urls}]
urls
Flatten all urls from the resolver.
Optional arguments:
--help, -h
show this help message and exit

#### debug django urls 

```
debug django urls [-h] [--file FILE] [--app-names APP_NAMES] [<PREFIX>]
[<RESOLVER>]
```

Flatten all urls from the resolver.
Positional arguments:
PREFIX
RESOLVER
Optional arguments:
--help, -h
show this help message and exit
--file FILE
--app-names APP_NAMES

### debug whoami 

```
debug whoami [-h]
```

Tell which user you are.
Optional arguments:
--help, -h
show this help message and exit

# MODEL

## General options

```
model [-h]
[{fabric,host,network,port,switch,router,cable,vm,device,tc,debug,object,diag
```

Positional arguments:
[{fabric,host,network,port,switch,router,cable,vm,device,tc,debug,object,diagnose}]
fabric
host
network
port
switch
router
cable
vm
device
tc
debug
object
diagnose
Optional arguments:
--help, -h
show this help message and exit

### model cable 

```
model cable [-h] [{list,detail,create,delete,update,connect}]
```

Positional arguments:
[{list,detail,create,delete,update,connect}]
list
List cables.
detail
Detail view of cable.
create
Create cable.
delete
Delete cable.
update
Update cable.
connect
Connect first free ports between two devices.
Optional arguments:
--help, -h
show this help message and exit

#### model cable connect 

```
model cable connect [-h] [--auto-disconnect] [--no-auto-disconnect]
[--auto-address] [--no-auto-address] [--auto-params] [--no-auto-params]
<DEVICE1> <DEVICE2>
```

Connect first free ports between two devices.
For native switch, missing ports are automatically created.
Positional arguments:
DEVICE1{Device}
DEVICE2{Device}
Optional arguments:
--help, -h
show this help message and exit
--auto-disconnect
--no-auto-disconnect
(default)
--auto-address
--no-auto-address
--auto-params
--no-auto-params

#### model cable create 

```
model cable create [-h] [--auto-disconnect] [--no-auto-disconnect]
[--auto-address] [--no-auto-address] [--auto-params] [--no-auto-params]
[--related-fields [RELATED_FIELDS ...]] <cable>
```

Create cable.
Return: model.cable model
Positional arguments:
cable{Cable}
cable object
Optional arguments:
--help, -h
show this help message and exit
--auto-disconnect
--no-auto-disconnect
(default)
--auto-address
--no-auto-address
--auto-params
--no-auto-params
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model cable delete 

```
model cable delete [-h] [--interactive] [--no-interactive] [--yes] [--no-yes]
<cable>
```

Delete cable.
Return: model.cable model
Positional arguments:
cable{Cable}
ID of the cable
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model cable detail 

```
model cable detail [-h] [--related-fields [RELATED_FIELDS ...]] <cable>
```

Detail view of cable.
Return: model.cable model
Positional arguments:
cable{Cable}
ID of the cable
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model cable list 

```
model cable list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of cable]
[--related-fields [RELATED_FIELDS ...]]
```

List cables.
Return: (list[model.cable]|page[model.cable])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of cable{int}
Get page of given cable ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model cable update 

```
model cable update [-h] [--auto-disconnect] [--no-auto-disconnect]
[--update-fields UPDATE_FIELDS] [--related-fields [RELATED_FIELDS ...]]
<cable> <OBJECT>
```

Update cable.
Return: model.cable model
Positional arguments:
cable{Cable}
ID of the cable
OBJECT{Cable}
cable object
Optional arguments:
--help, -h
show this help message and exit
--auto-disconnect
--no-auto-disconnect
(default)
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model debug 

```
model debug [-h] [{tc,reader,fabric}]
```

Positional arguments:
[{tc,reader,fabric}]
tc
reader
Reader ouput of fabric import.
fabric
Optional arguments:
--help, -h
show this help message and exit

#### model debug fabric export 

```
model debug fabric export [-h] [--fabric] [--no-fabric] [--include-cfg]
[--no-include-cfg] [--include-local-repo] [--no-include-local-repo]
[--include-remote-repo] [--no-include-remote-repo] [--include-licenses]
[--no-include-licenses] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--related-fields [RELATED_FIELDS ...]] [<OUTPUT>]
```

Save Fabrics as a ZIP archive or as a cfg.
Return: optional[IOBase]
Positional arguments:
OUTPUT{Path}
Export to this file in local repository
Optional arguments:
--help, -h
show this help message and exit
--fabric
export only the fabric configuration, all include_* flags are ignored
--no-fabric
export only the fabric configuration, all include_* flags are ignored (default)
--include-cfg
(default)
--no-include-cfg
--include-local-repo
--no-include-local-repo
(default)
--include-remote-repo
--no-include-remote-repo
(default)
--include-licenses
--no-include-licenses
(default)
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model debug fabric import 

```
model debug fabric import [-h] [--rename] [--no-rename] [--as AS] [<INPUT>]
```

Import Fabrics from fabric input, rename imported Fabric if a Fabric already exists with same name.
Return: list[*]
Positional arguments:
INPUT{Path}
Optional arguments:
--help, -h
show this help message and exit
--rename
(default)
--no-rename
--as AS{str}

#### model debug reader 

```
model debug reader [-h] [<INPUT>]
```

Reader ouput of fabric import.
Return: list[*]
Positional arguments:
INPUT{Path}
Optional arguments:
--help, -h
show this help message and exit

#### model debug tc cleanup 

```
model debug tc cleanup [-h]
```

Remove dangling traffic control.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Optional arguments:
--help, -h
show this help message and exit

### model device 

```
model device [-h] [{config,list,detail}]
```

Positional arguments:
[{config,list,detail}]
config
list
List devices.
detail
Detail view of device.
Optional arguments:
--help, -h
show this help message and exit

#### model device config delete 

```
model device config delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <deviceconfig>
```

Delete device config.
Return: model.deviceconfig model
Positional arguments:
deviceconfig{DeviceConfig}
ID of the deviceconfig
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model device config detail 

```
model device config detail [-h] [--related-fields [RELATED_FIELDS ...]]
<deviceconfig>
```

Detail view of device config.
Return: model.deviceconfig model
Positional arguments:
deviceconfig{DeviceConfig}
ID of the deviceconfig
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model device config export 

```
model device config export [-h] <DEVICECONFIG> [<OUTPUT>]
```

Return: optional[IOBase]
Positional arguments:
DEVICECONFIG{DeviceConfig}
OUTPUT{Path}
Export to this file in local repository
Optional arguments:
--help, -h
show this help message and exit

#### model device config import 

```
model device config import [-h] [--overwrite] [--no-overwrite]
[--erase-source] [--no-erase-source] <INPUT> <OBJECT>
```

Upload a VM config in the Fabric for VM type.
Return: model.deviceconfig model
Positional arguments:
INPUT{Path}
VM configuration file
OBJECT{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--erase-source
(default)
--no-erase-source

#### model device config is-local 

```
model device config is-local [-h] <DEVICECONFIG>
```

Verify VM config file exists locally.
Return: Path
Positional arguments:
DEVICECONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### model device config list 

```
model device config list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of deviceconfig]
[--related-fields [RELATED_FIELDS ...]]
```

List device configs.
Return: (list[model.deviceconfig]|page[model.deviceconfig])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of deviceconfig{int}
Get page of given deviceconfig ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model device config update 

```
model device config update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <deviceconfig> <OBJECT>
```

Update device config.
Return: model.deviceconfig model
Positional arguments:
deviceconfig{DeviceConfig}
ID of the deviceconfig
OBJECT{DeviceConfig}
deviceconfig object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model device detail 

```
model device detail [-h] [--related-fields [RELATED_FIELDS ...]] <device>
```

Detail view of device.
Return: model.device model
Positional arguments:
device{Device}
ID of the device
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model device list 

```
model device list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of device]
[--related-fields [RELATED_FIELDS ...]]
```

List devices.
Return: (list[model.device]|page[model.device])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of device{int}
Get page of given device ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model diagnose 

```
model diagnose [-h] [{fabric}]
```

Positional arguments:
[{fabric}]
fabric
Optional arguments:
--help, -h
show this help message and exit

#### model diagnose fabric storage config 

```
model diagnose fabric storage config [-h] <FABRIC>
```

Print “ls -al” of the fabric config storage.
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

### model fabric 

```
model fabric [-h]
[{clone,sanity,export,import,remote,documentation,list,detail,layout,create,d
```

Positional arguments:
[{clone,sanity,export,import,remote,documentation,list,detail,layout,create,delete,update,batch,install,hos
clone
sanity
export
import
Create a fabric from a template file.
remote
documentation
list
List fabrics.
detail
Detail view of fabric.
layout
create
Create a Fabric from a template.
delete
Delete fabric.
update
Update fabric.
batch
install
host
network
switch
router
cable
vm
device
Optional arguments:
--help, -h
show this help message and exit

#### model fabric batch delete 

```
model fabric batch delete [-h] [--interactive] [--no-interactive]
[--select SELECT] [--exclude EXCLUDE]
```

Batch delete Fabrics.
Return: list[model.fabric]
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--select SELECT{filter}
--exclude EXCLUDE{filter}

#### model fabric cable connect 

```
model fabric cable connect [-h] [--auto-disconnect] [--no-auto-disconnect]
[--auto-address] [--no-auto-address] [--auto-params] [--no-auto-params]
<FABRIC> <DEVICE1> <DEVICE2>
```

Connect first free ports between two devices.
For native switch, missing ports are automatically created.
Positional arguments:
FABRIC{Fabric}
DEVICE1{Device}
DEVICE2{Device}
Optional arguments:
--help, -h
show this help message and exit
--auto-disconnect
--no-auto-disconnect
(default)
--auto-address
--no-auto-address
--auto-params
--no-auto-params

#### model fabric cable create 

```
model fabric cable create [-h] [--auto-disconnect] [--no-auto-disconnect]
[--auto-address] [--no-auto-address] [--auto-params] [--no-auto-params]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <DEVICE1> <DEVICE1PORT>
<DEVICE2> <DEVICE2PORT>
```

Create cable.
Return: model.cable model
Positional arguments:
FABRIC{Fabric}
DEVICE1{Device}
DEVICE1PORT{Port}
DEVICE2{Device}
DEVICE2PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--auto-disconnect
--no-auto-disconnect
(default)
--auto-address
--no-auto-address
--auto-params
--no-auto-params
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric cable list 

```
model fabric cable list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of cable]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List cables.
Return: (list[model.cable]|page[model.cable])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of cable{int}
Get page of given cable ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric clone 

```
model fabric clone [-h] [--interactive] [--no-interactive] <FABRIC> [<AS>]
```

Return: runtime.runtimetask model if not ‘interactive’
Result: list[*]
Positional arguments:
FABRIC{Fabric}
AS{str}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model fabric create 

```
model fabric create [-h] [--if-exists IF_EXISTS] [--template TEMPLATE]
[<NAME>]
```

Create a Fabric from a template.
Return: runtime.runtimetask model
Result: model.fabric model
Positional arguments:
NAME{str}
the new Fabric name
Optional arguments:
--help, -h
show this help message and exit
--if-exists{str} ('abort', 'rename')
What to do when a fabric with same name already exists
Default: abort .
--template TEMPLATE{Template}
Must specify a template ID or relative path (eg: templates/myfabric.zip)

#### model fabric delete 

```
model fabric delete [-h] [--interactive] [--no-interactive] <fabric>
```

Delete fabric.
Return: model.fabric model
Positional arguments:
fabric{Fabric}
ID of the fabric
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model fabric detail 

```
model fabric detail [-h] [--related-fields [RELATED_FIELDS ...]] <fabric>
```

Detail view of fabric.
Return: model.fabric model
Positional arguments:
fabric{Fabric}
ID of the fabric
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device config delete 

```
model fabric device config delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <FABRIC> <DEVICECONFIG>
```

Delete device config.
Return: model.deviceconfig model
Positional arguments:
FABRIC{Fabric}
DEVICECONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model fabric device config detail 

```
model fabric device config detail [-h] [--related-fields [RELATED_FIELDS ...]
<FABRIC> <DEVICECONFIG>
```

Detail view of device config.
Return: model.deviceconfig model
Positional arguments:
FABRIC{Fabric}
DEVICECONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device config is-local 

```
model fabric device config is-local [-h] <FABRIC> <DEVICECONFIG>
```

Verify VM config file exists locally.
Return: Path
Positional arguments:
FABRIC{Fabric}
DEVICECONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric device config list 

```
model fabric device config list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of deviceconfig]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List device configs.
Return: (list[model.deviceconfig]|page[model.deviceconfig])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of deviceconfig{int}
Get page of given deviceconfig ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device config update 

```
model fabric device config update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <DEVICECONFIG> <OBJECT>
```

Update device config.
Return: model.deviceconfig model
Positional arguments:
FABRIC{Fabric}
DEVICECONFIG{DeviceConfig}
OBJECT{DeviceConfig}
deviceconfig object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device port tc detail 

```
model fabric device port tc detail [-h]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <DEVICE> <PORT>
```

Detail view of traffic control.
Return: model.trafficcontrol model
Positional arguments:
FABRIC{Fabric}
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device port tc update 

```
model fabric device port tc update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <DEVICE> <PORT> <OBJECT>
```

Update traffic control.
Return: model.trafficcontrol model
Positional arguments:
FABRIC{Fabric}
DEVICE{Device}
PORT{Port}
OBJECT{TrafficControl}
trafficcontrol object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric device tc list 

```
model fabric device tc list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of trafficcontrol]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <DEVICE>
```

List traffic controls.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Positional arguments:
FABRIC{Fabric}
DEVICE{Device}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of trafficcontrol{int}
Get page of given trafficcontrol ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric documentation download 

```
model fabric documentation download [-h] [--interactive] [--no-interactive]
[--active] [--no-active] <FABRIC>
```

Return: task.task model if not ‘interactive’
Result: str
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--active
--no-active
(default)

#### model fabric export 

```
model fabric export [-h] <FABRIC> [<OUTPUT>]
```

Return: optional[IOBase]
Positional arguments:
FABRIC{Fabric}
OUTPUT{Path}
Export to this file in local repository or as streamed file (REST)
Optional arguments:
--help, -h
show this help message and exit

#### model fabric host detail 

```
model fabric host detail [-h] [--related-fields [RELATED_FIELDS ...]] <FABRIC
```

Detail view of System Host.
Return: model.host model
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port create 

```
model fabric host port create [-h] <FABRIC> [<HOSTPORT>]
```

Create a new host internal port, name and index are automatic.
Return: model.hostport model
Positional arguments:
FABRIC{Fabric}
HOSTPORT{HostPort}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric host port delete 

```
model fabric host port delete [-h] <FABRIC>
```

Delete the last internal port.
Return: model.hostport model
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric host port detail 

```
model fabric host port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <HOSTPORT>
```

Detail view of System Port.
Return: model.hostport model
Positional arguments:
FABRIC{Fabric}
HOSTPORT{HostPort}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port list 

```
model fabric host port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of hostport]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List host ports in this Fabric.
Return: (list[model.hostport]|page[model.hostport])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of hostport{int}
Get page of given hostport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port redirect create 

```
model fabric host port redirect create [-h]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <portredirect>
```

Create port redirect.
Return: model.portredirect model
Positional arguments:
FABRIC{Fabric}
portredirect{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port redirect delete 

```
model fabric host port redirect delete [-h] [--interactive] [--no-interactive
[--yes] [--no-yes] <FABRIC> <PORTREDIRECT>
```

Delete port redirect.
Return: model.portredirect model
Positional arguments:
FABRIC{Fabric}
PORTREDIRECT{PortRedirect}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model fabric host port redirect detail 

```
model fabric host port redirect detail [-h]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <PORTREDIRECT>
```

Detail view of port redirect.
Return: model.portredirect model
Positional arguments:
FABRIC{Fabric}
PORTREDIRECT{PortRedirect}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port redirect list 

```
model fabric host port redirect list [-h] [--select SELECT]
[--exclude EXCLUDE] [--order-by [ORDER_BY ...]] [--startIndex STARTINDEX]
[--endIndex ENDINDEX] [--limit LIMIT] [--page PAGE] [--page-of portredirect]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List port redirects.
Return: (list[model.portredirect]|page[model.portredirect])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of portredirect{int}
Get page of given portredirect ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port redirect update 

```
model fabric host port redirect update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <PORTREDIRECT> <OBJECT>
```

Update port redirect.
Return: model.portredirect model
Positional arguments:
FABRIC{Fabric}
PORTREDIRECT{PortRedirect}
OBJECT{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host port update 

```
model fabric host port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <HOSTPORT> <OBJECT>
```

Update inner system ports connection to the Fabric.
Return: model.hostport model
Positional arguments:
FABRIC{Fabric}
HOSTPORT{HostPort}
OBJECT{HostPort}
hostport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric host sync 

```
model fabric host sync [-h] [--drop] [--no-drop] <FABRIC>
```

Synchronize with available System Host ports.
By default extra ports are only dropped if they are not connected.
Return: list[typing.Union[fortipoc.core.django.system.models.Port,
fortipoc.core.django.model.models.native.host.HostPort]]
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--drop
drop extra ports even if connected
--no-drop
drop extra ports even if connected (default)

#### model fabric host update 

```
model fabric host update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <OBJECT>
```

Update System Host.
Return: model.host model
Positional arguments:
FABRIC{Fabric}
OBJECT{Host}
host object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric import 

```
model fabric import [-h] [--if-exists IF_EXISTS] [--delete-after DELETE_AFTER
[--interactive] [--no-interactive] <INPUT> [<NAME>]
```

Create a fabric from a template file.
By default delete template file on successful fabric create.
Positional arguments:
INPUT{Path}
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--if-exists{str} ('abort', 'rename')
What to do when a fabric with same name already exists
--delete-after{str} ('always', 'never', 'success')
Do we delete after create
Default: success .
--interactive
(default)
--no-interactive

#### model fabric install policy detail 

```
model fabric install policy detail [-h] <FABRIC>
```

Return: model.installpolicy model
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric install policy update 

```
model fabric install policy update [-h] <FABRIC> <INSTALL_POLICY>
```

Return: model.installpolicy model
Positional arguments:
FABRIC{Fabric}
INSTALL_POLICY{InstallPolicy}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric layout get 

```
model fabric layout get [-h] <FABRIC>
```

Return: list
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric layout gui get 

```
model fabric layout gui get [-h] <FABRIC>
```

Return: dict
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric layout gui set 

```
model fabric layout gui set [-h] <FABRIC> <LAYOUT>
```

Positional arguments:
FABRIC{Fabric}
LAYOUT{dict}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric layout set 

```
model fabric layout set [-h] <FABRIC> <LAYOUT>
```

Positional arguments:
FABRIC{Fabric}
LAYOUT{list}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric list 

```
model fabric list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of fabric]
[--related-fields [RELATED_FIELDS ...]]
```

List fabrics.
Return: (list[model.fabric]|page[model.fabric])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of fabric{int}
Get page of given fabric ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric network create 

```
model fabric network create [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <network>
```

Create network.
Return: model.network model
Positional arguments:
FABRIC{Fabric}
network{Network}
network object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric network delete 

```
model fabric network delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <FABRIC> <NETWORK>
```

Delete network.
Return: model.network model
Positional arguments:
FABRIC{Fabric}
NETWORK{Network}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model fabric network detail 

```
model fabric network detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <NETWORK>
```

Detail view of network.
Return: model.network model
Positional arguments:
FABRIC{Fabric}
NETWORK{Network}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric network list 

```
model fabric network list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of network]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List networks.
Return: (list[model.network]|page[model.network])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of network{int}
Get page of given network ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric network update 

```
model fabric network update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <NETWORK> <OBJECT>
```

Update network.
Return: model.network model
Positional arguments:
FABRIC{Fabric}
NETWORK{Network}
OBJECT{Network}
network object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric remote import fabric-studio 

```
model fabric remote import fabric-studio [-h] [--interactive]
[--no-interactive] [--ssh-password SSH_PASSWORD] [--ssh-port SSH_PORT]
[--home-firmwares] [--no-home-firmwares] [--home-templates]
[--no-home-templates] <ADDRESS> [<FABRIC>]
```

Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
ADDRESS{str}
FABRIC{int}
Default: default: 0 .
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--ssh-password SSH_PASSWORD{str}
--ssh-port SSH_PORT{int}
Default: 22 .
--home-firmwares
(default)
--no-home-firmwares
--home-templates
(default)
--no-home-templates

#### model fabric remote import fortipoc 

```
model fabric remote import fortipoc [-h] [--ssh-port SSH_PORT]
[--local-firmwares] [--no-local-firmwares] [--local-pocs] [--no-local-pocs]
[--copy] [--no-copy] [--config] [--no-config] [--import-repositories]
[--no-import-repositories] [--import-config] [--no-import-config] [--dry-run]
[--no-dry-run] [--force] [--no-force] <ADDRESS> [<POC>]
```

Positional arguments:
ADDRESS
POC{str}
Default: default: all .
Optional arguments:
--help, -h
show this help message and exit
--ssh-port SSH_PORT{int}
Default: 22 .
--local-firmwares
Include local repository firmwares (default)
--no-local-firmwares
Include local repository firmwares
--local-pocs
Include local repository PoCs (default)
--no-local-pocs
Include local repository PoCs
--copy
Copy local repository files (default)
--no-copy
Copy local repository files
--config
Retrieve PoC definitions and snapshots information (default)
--no-config
Retrieve PoC definitions and snapshots information
--import-repositories
Import remote repositories list (default)
--no-import-repositories
Import remote repositories list
--import-config
Process PoC definitions (default)
--no-import-config
Process PoC definitions
--dry-run
Dry run the import part
--no-dry-run
Dry run the import part (default)
--force
--no-force
(default)

#### model fabric router create 

```
model fabric router create [-h] [--ports-count PORTS_COUNT]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> [<router>]
```

Create router.
Return: model.router model
Positional arguments:
FABRIC{Fabric}
router{Router}
router object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
Default: 10 .
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router delete 

```
model fabric router delete [-h] [--interactive] [--no-interactive] <FABRIC>
<ROUTER>
```

Delete router.
Return: model.router model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model fabric router detail 

```
model fabric router detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <ROUTER>
```

Detail view of router.
Return: model.router model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router list 

```
model fabric router list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of router]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List routers.
Return: (list[model.router]|page[model.router])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of router{int}
Get page of given router ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router port create 

```
model fabric router port create [-h] <FABRIC> <ROUTER> [<ROUTERPORT>]
```

Return: model.routerport model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
ROUTERPORT{RouterPort}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric router port delete 

```
model fabric router port delete [-h] <FABRIC> <ROUTER>
```

Delete the last port.
Return: model.routerport model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric router port detail 

```
model fabric router port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <ROUTER> <ROUTERPORT>
```

Detail view of router port.
Return: model.routerport model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
ROUTERPORT{RouterPort}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router port list 

```
model fabric router port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of routerport]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <ROUTER>
```

List router ports.
Return: (list[model.routerport]|page[model.routerport])
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of routerport{int}
Get page of given routerport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router port update 

```
model fabric router port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <ROUTER> <ROUTERPORT>
<OBJECT>
```

Update router port.
Return: model.routerport model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
ROUTERPORT{RouterPort}
OBJECT{RouterPort}
routerport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric router update 

```
model fabric router update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <ROUTER> <OBJECT>
```

Update router.
Return: model.router model
Positional arguments:
FABRIC{Fabric}
ROUTER{Router}
OBJECT{Router}
router object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric sanity check 

```
model fabric sanity check [-h] [<FABRIC>]
```

Return: dict
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric switch create 

```
model fabric switch create [-h] [--ports-count PORTS_COUNT]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> [<switch>]
```

Create switch.
Return: model.switch model
Positional arguments:
FABRIC{Fabric}
switch{Switch}
switch object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
Default: 10 .
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch delete 

```
model fabric switch delete [-h] [--interactive] [--no-interactive] <FABRIC>
<SWITCH>
```

Delete switch.
Return: model.switch model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model fabric switch detail 

```
model fabric switch detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <SWITCH>
```

Detail view of switch.
Return: model.switch model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch list 

```
model fabric switch list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switch]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List Switches.
Return: (list[model.switch]|page[model.switch])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switch{int}
Get page of given switch ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch port create 

```
model fabric switch port create [-h] <FABRIC> <SWITCH> [<SWITCHPORT>]
```

Return: model.switchport model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
SWITCHPORT{SwitchPort}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric switch port delete 

```
model fabric switch port delete [-h] <FABRIC> <SWITCH>
```

Delete the last port.
Return: model.switchport model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric switch port detail 

```
model fabric switch port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <SWITCH> <SWITCHPORT>
```

Detail view of switch port.
Return: model.switchport model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
SWITCHPORT{SwitchPort}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch port list 

```
model fabric switch port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switchport]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <SWITCH>
```

List switch ports.
Return: (list[model.switchport]|page[model.switchport])
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switchport{int}
Get page of given switchport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch port update 

```
model fabric switch port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <SWITCH> <SWITCHPORT>
<OBJECT>
```

Update switch port.
Return: model.switchport model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
SWITCHPORT{SwitchPort}
OBJECT{SwitchPort}
switchport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric switch update 

```
model fabric switch update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <SWITCH> <OBJECT>
```

Update switch.
Return: model.switch model
Positional arguments:
FABRIC{Fabric}
SWITCH{Switch}
OBJECT{Switch}
switch object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric update 

```
model fabric update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <fabric> <OBJECT>
```

Update fabric.
Return: model.fabric model
Positional arguments:
fabric{Fabric}
ID of the fabric
OBJECT{Fabric}
fabric object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm access create 

```
model fabric vm access create [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <VM> <vmaccess>
```

Create vm access.
Return: model.vmaccess model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
vmaccess{VmAccess}
vmaccess object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm access delete 

```
model fabric vm access delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <FABRIC> <VM> <VMACCESS>
```

Delete vm access.
Return: model.vmaccess model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMACCESS{VmAccess}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model fabric vm access detail 

```
model fabric vm access detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <VM> <VMACCESS>
```

Detail view of vm access.
Return: model.vmaccess model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMACCESS{VmAccess}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm access list 

```
model fabric vm access list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmaccess]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM>
```

List vm accesss.
Return: (list[model.vmaccess]|page[model.vmaccess])
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmaccess{int}
Get page of given vmaccess ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm access order 

```
model fabric vm access order [-h] <FABRIC> <VM> [<ACCESSES> ...]
```

Return: list[model.vmaccess]
Positional arguments:
FABRIC{Fabric}
VM{Vm}
ACCESSES{*}{VmAccess}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm access update 

```
model fabric vm access update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <VMACCESS> <OBJECT>
```

Update vm access.
Return: model.vmaccess model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMACCESS{VmAccess}
OBJECT{VmAccess}
vmaccess object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm create 

```
model fabric vm create [-h] [--ports-count PORTS_COUNT] [--auto-connect]
[--no-auto-connect] [--related-fields [RELATED_FIELDS ...]] <FABRIC> <vm>
```

Create a new VM object.
Mandatory fields are the “fabric” ID and “firmware” ID, ex:

```
{"object": {"fabric": 1, "firmware": 1}}
```

The call returns the created VM and the created ports.
The default number of ports is declared in the firmware meta (most of the time 10).
Return: model.vm model
Positional arguments:
FABRIC{Fabric}
vm{Vm}
vm object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
--auto-connect
--no-auto-connect
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm delete 

```
model fabric vm delete [-h] [--interactive] [--no-interactive] <FABRIC> <VM>
```

Delete vm.
Return: model.vm model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model fabric vm detail 

```
model fabric vm detail [-h] [--related-fields [RELATED_FIELDS ...]] <FABRIC>
<VM>
```

Detail view of vm.
Return: model.vm model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm disk create 

```
model fabric vm disk create [-h] <FABRIC> <VM> <CAPACITY>
```

Add an extra disk to the VM.
Return: model.vmdisk model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
CAPACITY{BytesSize}
MB size by default
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm disk delete 

```
model fabric vm disk delete [-h] <FABRIC> <VM>
```

Remove last extra disk from the VM.
Return: model.vmdisk model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm disk detail 

```
model fabric vm disk detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <VM> <VMDISK>
```

Detail view of vm disk.
Return: model.vmdisk model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMDISK{VmDisk}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm disk list 

```
model fabric vm disk list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmdisk]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM>
```

List vm disks.
Return: (list[model.vmdisk]|page[model.vmdisk])
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmdisk{int}
Get page of given vmdisk ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm disk update 

```
model fabric vm disk update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <VMDISK> <OBJECT>
```

Update vm disk.
Return: model.vmdisk model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMDISK{VmDisk}
OBJECT{VmDisk}
vmdisk object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm license detail 

```
model fabric vm license detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <VM>
```

Detail view of vm license.
Return: model.vmlicense model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm license release 

```
model fabric vm license release [-h] <FABRIC> <VM>
```

Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm license reset 

```
model fabric vm license reset [-h] <FABRIC> <VM>
```

Update vm license.
Return: model.vmlicense model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm license update 

```
model fabric vm license update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <OBJECT>
```

Update vm license.
Return: model.vmlicense model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
OBJECT{VmLicense}
vmlicense object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm list 

```
model fabric vm list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vm]
[--related-fields [RELATED_FIELDS ...]] <FABRIC>
```

List VMs.
Return: (list[model.vm]|page[model.vm])
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vm{int}
Get page of given vm ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm parameters detail 

```
model fabric vm parameters detail [-h] [--related-fields [RELATED_FIELDS ...]
<FABRIC> <VM>
```

Detail view of vm parameters.
Return: model.vmparameters model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm parameters reset 

```
model fabric vm parameters reset [-h] <FABRIC> <VM>
```

Update vm parameters.
Return: model.vmparameters model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm parameters update 

```
model fabric vm parameters update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <OBJECT>
```

Update vm parameters.
Return: model.vmparameters model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
OBJECT{VmParameters}
vmparameters object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm port create 

```
model fabric vm port create [-h] <FABRIC> <VM> [<VMPORT>]
```

Create port as the new latest port.
Return: model.vmport model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMPORT{VmPort}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm port delete 

```
model fabric vm port delete [-h] <FABRIC> <VM>
```

Delete the last port.
Return: model.vmport model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model fabric vm port detail 

```
model fabric vm port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<FABRIC> <VM> <VMPORT>
```

Detail view of vm port.
Return: model.vmport model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMPORT{VmPort}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm port list 

```
model fabric vm port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmport]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM>
```

List vm ports.
Return: (list[model.vmport]|page[model.vmport])
Positional arguments:
FABRIC{Fabric}
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmport{int}
Get page of given vmport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm port update 

```
model fabric vm port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <VMPORT> <OBJECT>
```

Update vm port.
Return: model.vmport model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
VMPORT{VmPort}
OBJECT{VmPort}
vmport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model fabric vm update 

```
model fabric vm update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <FABRIC> <VM> <OBJECT>
```

Update vm.
Return: model.vm model
Positional arguments:
FABRIC{Fabric}
VM{Vm}
OBJECT{Vm}
vm object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model host 

```
model host [-h] [{list,detail,update,sync,port}]
```

Positional arguments:
[{list,detail,update,sync,port}]
list
List System Hosts.
detail
Detail view of System Host.
update
Update System Host.
sync
Synchronize with available System Host ports.
port
Optional arguments:
--help, -h
show this help message and exit

#### model host detail 

```
model host detail [-h] [--related-fields [RELATED_FIELDS ...]] <host>
```

Detail view of System Host.
Return: model.host model
Positional arguments:
host{Host}
ID of the host
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host list 

```
model host list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of host]
[--related-fields [RELATED_FIELDS ...]]
```

List System Hosts.
Return: (list[model.host]|page[model.host])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of host{int}
Get page of given host ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port create 

```
model host port create [-h] <HOST> [<HOSTPORT>]
```

Create a new host internal port, name and index are automatic.
Return: model.hostport model
Positional arguments:
HOST{Host}
HOSTPORT{HostPort}
Optional arguments:
--help, -h
show this help message and exit

#### model host port delete 

```
model host port delete [-h] <HOST>
```

Delete the last internal port.
Return: model.hostport model
Positional arguments:
HOST{Host}
Optional arguments:
--help, -h
show this help message and exit

#### model host port detail 

```
model host port detail [-h] [--related-fields [RELATED_FIELDS ...]] <hostport
```

Detail view of System Port.
Return: model.hostport model
Positional arguments:
hostport{HostPort}
ID of the hostport
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port list 

```
model host port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of hostport]
[--related-fields [RELATED_FIELDS ...]]
```

List System Ports.
Return: (list[model.hostport]|page[model.hostport])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of hostport{int}
Get page of given hostport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port redirect create 

```
model host port redirect create [-h] [--related-fields [RELATED_FIELDS ...]]
<HOST> <portredirect>
```

Create port redirect.
Return: model.portredirect model
Positional arguments:
HOST{Host}
portredirect{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port redirect delete 

```
model host port redirect delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <HOST> <PORTREDIRECT>
```

Delete port redirect.
Return: model.portredirect model
Positional arguments:
HOST{Host}
PORTREDIRECT{PortRedirect}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model host port redirect detail 

```
model host port redirect detail [-h] [--related-fields [RELATED_FIELDS ...]]
<HOST> <PORTREDIRECT>
```

Detail view of port redirect.
Return: model.portredirect model
Positional arguments:
HOST{Host}
PORTREDIRECT{PortRedirect}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port redirect list 

```
model host port redirect list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of portredirect]
[--related-fields [RELATED_FIELDS ...]] <HOST>
```

List port redirects.
Return: (list[model.portredirect]|page[model.portredirect])
Positional arguments:
HOST{Host}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of portredirect{int}
Get page of given portredirect ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port redirect update 

```
model host port redirect update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <HOST> <PORTREDIRECT> <OBJECT>
```

Update port redirect.
Return: model.portredirect model
Positional arguments:
HOST{Host}
PORTREDIRECT{PortRedirect}
OBJECT{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host port update 

```
model host port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <hostport> <OBJECT>
```

Update inner system ports connection to the Fabric.
Return: model.hostport model
Positional arguments:
hostport{HostPort}
ID of the hostport
OBJECT{HostPort}
hostport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model host sync 

```
model host sync [-h] [--drop] [--no-drop] <HOST>
```

Synchronize with available System Host ports.
By default extra ports are only dropped if they are not connected.
Return: list[typing.Union[fortipoc.core.django.system.models.Port,
fortipoc.core.django.model.models.native.host.HostPort]]
Positional arguments:
HOST{Host}
Optional arguments:
--help, -h
show this help message and exit
--drop
drop extra ports even if connected
--no-drop
drop extra ports even if connected (default)

#### model host update 

```
model host update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <host> <OBJECT>
```

Update System Host.
Return: model.host model
Positional arguments:
host{Host}
ID of the host
OBJECT{Host}
host object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model network 

```
model network [-h] [{list,detail,create,delete,update}]
```

Positional arguments:
[{list,detail,create,delete,update}]
list
List networks.
detail
Detail view of network.
create
Create network.
delete
Delete network.
update
Update network.
Optional arguments:
--help, -h
show this help message and exit

#### model network create 

```
model network create [-h] [--related-fields [RELATED_FIELDS ...]] <network>
```

Create network.
Return: model.network model
Positional arguments:
network{Network}
network object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model network delete 

```
model network delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <network>
```

Delete network.
Return: model.network model
Positional arguments:
network{Network}
ID of the network
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model network detail 

```
model network detail [-h] [--related-fields [RELATED_FIELDS ...]] <network>
```

Detail view of network.
Return: model.network model
Positional arguments:
network{Network}
ID of the network
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model network list 

```
model network list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of network]
[--related-fields [RELATED_FIELDS ...]]
```

List networks.
Return: (list[model.network]|page[model.network])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of network{int}
Get page of given network ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model network update 

```
model network update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <network> <OBJECT>
```

Update network.
Return: model.network model
Positional arguments:
network{Network}
ID of the network
OBJECT{Network}
network object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model object 

```
model object [-h] [{diff,detail}]
```

Positional arguments:
[{diff,detail}]
diff
Compare “model” and “runtime” model object with id ID for difference.
detail
Get detail view of any model object with id ID . The deepest subclass is returned.
Optional arguments:
--help, -h
show this help message and exit

#### model object detail 

```
model object detail [-h] [--related-fields [RELATED_FIELDS ...]] <MODEL>
<IDS> [<IDS> ...]
```

Get detail view of any model object with id ID . The deepest subclass is returned.
Return: list[*]
Positional arguments:
MODEL{str}
IDS{+}{int}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model object diff 

```
model object diff [-h] <MODEL> <ID>
```

Compare “model” and “runtime” model object with id ID for difference.
Specific comparision algorithm is implemented for these different classes of objects:
model.fabric
model.host
model.switch
model.router
model.vm
For other classes a generic algorithm is used.
This API call returns a dictionnary with:
model:
the “model” object or null
runtime:
the “runtime” object or null
diff:
a dictionary of fields and the required apply method. Empty when then “runtime” and “model” objects
are identical.
Apply methods are:
install:
object must be installed, ex:

```
(fabric-studio) cli prefix set -- --json
(fabric-studio) model object diff model.device 144
{
"model": {
"fabric": 67,
"nameid": "MINI1",
...
"ports": [
573,
574,
575,
576
        ],
"vm_type": "LXC",
"mgmt_port": null,
"__model": "runtime.vm",
"id": 144
    },
"runtime": null,
"diff": {
"id": "install"
    }
}
```

uninstall:
object must be uninstalled, ex:

```
(fabric-studio) cli prefix set -- --json
(fabric-studio) model object diff model.device 145
{
"model": null,
"runtime": {
"fabric": 67,
"nameid": "MINI10",
...
"ports": [
583,
584,
585,
586
        ],
"vm_type": "LXC",
"mgmt_port": null,
"__model": "runtime.vm",
"id": 145
    },
"diff": {
"id": "uninstall"
    }
}
```

synchronize:
object could be synchronized without a uninstall/install cycle (if implemented), ex:

```
(fabric-studio) cli prefix set -- --json
(fabric-studio) model object diff model.device 136
{
"model": {
"fabric": 67,
"nameid": "MINI0",
"name": "my mini 0",
...
"id": 136
    },
"runtime": {
"fabric": 67,
"nameid": "MINI0",
"name": "MINI0",
...
"id": 136
    },
"diff": {
"name": "synchronize"
    }
}
```

For a Fabric we also list as devices the device’s status by device ID, you must compare the
model.device itself to get more detail about the difference between a “model” and a “runtime” device.
added:
if the device is in “model” but not yet in “runtime”
removed:
if the device is in “runtime” but no more in “model”
modified:
if the device in “runtime” differs from the one in “model”
Example:

```
(fabric-studio) cli prefix set -- --json
(fabric-studio) model object diff model.fabric 67
{
"model": {
"name": "another fgt",
...
"__model": "model.fabric",
"id": 67
    },
"runtime": {
"name": "fgt",
...
"__model": "model.fabric",
"id": 67
    },
"diff": {
"name": "synchronize",
"devices": {
"134": "modified",
"142": "modified",
"145": "added",
"135": "modified",
"136": "modified",
"144": "removed"
        }
    }
}
```

For a device we dive into ports to detail how to apply each port difference in the device (only if port is
not identical between “runtime” and “model”), ex:

```
(fabric-studio) cli prefix set -- --json
(fabric-studio) model object diff model.device 134
{
"model": {
"fabric": 67,
"nameid": "mgmtsw",
...
"ports": [
...
521,
603,
604
        ],
"id": 134
    },
"runtime": {
"fabric": 67,
"nameid": "mgmtsw",
...
"ports": [
...
521,
522
        ],
    },
"diff": {
"ports": {
"517": {
"cable": "synchronize",
"peer": "synchronize"
            },
"519": {
"cable": "synchronize",
"peer": "synchronize"
            },
"603": {
"id": "install"
            },
"522": {
"id": "install"
            },
"604": {
"id": "install"
            }
        }
    }
}
```

Return: dict
Positional arguments:
MODEL{str}
ID{int}
Optional arguments:
--help, -h
show this help message and exit

### model port 

```
model port [-h] [{redirect,list,detail}]
```

Positional arguments:
[{redirect,list,detail}]
redirect
list
List ports.
detail
Detail view of port.
Optional arguments:
--help, -h
show this help message and exit

#### model port detail 

```
model port detail [-h] [--related-fields [RELATED_FIELDS ...]] <port>
```

Detail view of port.
Return: model.port model
Positional arguments:
port{Port}
ID of the port
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model port list 

```
model port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of port]
[--related-fields [RELATED_FIELDS ...]]
```

List ports.
Return: (list[model.port]|page[model.port])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of port{int}
Get page of given port ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model port redirect create 

```
model port redirect create [-h] [--related-fields [RELATED_FIELDS ...]]
<portredirect>
```

Create port redirect.
Return: model.portredirect model
Positional arguments:
portredirect{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model port redirect delete 

```
model port redirect delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <portredirect>
```

Delete port redirect.
Return: model.portredirect model
Positional arguments:
portredirect{PortRedirect}
ID of the portredirect
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model port redirect detail 

```
model port redirect detail [-h] [--related-fields [RELATED_FIELDS ...]]
<portredirect>
```

Detail view of port redirect.
Return: model.portredirect model
Positional arguments:
portredirect{PortRedirect}
ID of the portredirect
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model port redirect list 

```
model port redirect list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of portredirect]
[--related-fields [RELATED_FIELDS ...]]
```

List port redirects.
Return: (list[model.portredirect]|page[model.portredirect])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of portredirect{int}
Get page of given portredirect ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model port redirect update 

```
model port redirect update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <portredirect> <OBJECT>
```

Update port redirect.
Return: model.portredirect model
Positional arguments:
portredirect{PortRedirect}
ID of the portredirect
OBJECT{PortRedirect}
portredirect object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model router 

```
model router [-h] [{list,detail,create,delete,update,port}]
```

Positional arguments:
[{list,detail,create,delete,update,port}]
list
List routers.
detail
Detail view of router.
create
Create router.
delete
Delete router.
update
Update router.
port
Optional arguments:
--help, -h
show this help message and exit

#### model router create 

```
model router create [-h] [--ports-count PORTS_COUNT]
[--related-fields [RELATED_FIELDS ...]] <router>
```

Create router.
Return: model.router model
Positional arguments:
router{Router}
router object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
Default: 10 .
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router delete 

```
model router delete [-h] [--interactive] [--no-interactive] <router>
```

Delete router.
Return: model.router model
Positional arguments:
router{Router}
ID of the router
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model router detail 

```
model router detail [-h] [--related-fields [RELATED_FIELDS ...]] <router>
```

Detail view of router.
Return: model.router model
Positional arguments:
router{Router}
ID of the router
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router list 

```
model router list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of router]
[--related-fields [RELATED_FIELDS ...]]
```

List routers.
Return: (list[model.router]|page[model.router])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of router{int}
Get page of given router ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router port create 

```
model router port create [-h] <ROUTER> [<ROUTERPORT>]
```

Return: model.routerport model
Positional arguments:
ROUTER{Router}
ROUTERPORT{RouterPort}
Optional arguments:
--help, -h
show this help message and exit

#### model router port delete 

```
model router port delete [-h] <ROUTER>
```

Delete the last port.
Return: model.routerport model
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### model router port detail 

```
model router port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<routerport>
```

Detail view of router port.
Return: model.routerport model
Positional arguments:
routerport{RouterPort}
ID of the routerport
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router port list 

```
model router port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of routerport]
[--related-fields [RELATED_FIELDS ...]]
```

List router ports.
Return: (list[model.routerport]|page[model.routerport])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of routerport{int}
Get page of given routerport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router port update 

```
model router port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <routerport> <OBJECT>
```

Update router port.
Return: model.routerport model
Positional arguments:
routerport{RouterPort}
ID of the routerport
OBJECT{RouterPort}
routerport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model router update 

```
model router update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <router> <OBJECT>
```

Update router.
Return: model.router model
Positional arguments:
router{Router}
ID of the router
OBJECT{Router}
router object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model switch 

```
model switch [-h] [{list,detail,create,delete,update,port,local-port}]
```

Positional arguments:
[{list,detail,create,delete,update,port,local-port}]
list
List Switches.
detail
Detail view of switch.
create
Create switch.
delete
Delete switch.
update
Update switch.
port
local-port
Optional arguments:
--help, -h
show this help message and exit

#### model switch create 

```
model switch create [-h] [--ports-count PORTS_COUNT]
[--related-fields [RELATED_FIELDS ...]] <switch>
```

Create switch.
Return: model.switch model
Positional arguments:
switch{Switch}
switch object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
Default: 10 .
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch delete 

```
model switch delete [-h] [--interactive] [--no-interactive] <switch>
```

Delete switch.
Return: model.switch model
Positional arguments:
switch{Switch}
ID of the switch
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model switch detail 

```
model switch detail [-h] [--related-fields [RELATED_FIELDS ...]] <switch>
```

Detail view of switch.
Return: model.switch model
Positional arguments:
switch{Switch}
ID of the switch
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch list 

```
model switch list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switch]
[--related-fields [RELATED_FIELDS ...]]
```

List Switches.
Return: (list[model.switch]|page[model.switch])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switch{int}
Get page of given switch ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch local-port detail 

```
model switch local-port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<switchlocalport>
```

Detail view of switch local port.
Return: model.switchlocalport model
Positional arguments:
switchlocalport{SwitchLocalPort}
ID of the switchlocalport
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch local-port list 

```
model switch local-port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switchlocalport]
[--related-fields [RELATED_FIELDS ...]]
```

List switch local ports.
Return: (list[model.switchlocalport]|page[model.switchlocalport])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switchlocalport{int}
Get page of given switchlocalport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch local-port update 

```
model switch local-port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <switchlocalport> <OBJECT>
```

Update switch local port.
Return: model.switchlocalport model
Positional arguments:
switchlocalport{SwitchLocalPort}
ID of the switchlocalport
OBJECT{SwitchLocalPort}
switchlocalport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch port create 

```
model switch port create [-h] <SWITCH> [<SWITCHPORT>]
```

Return: model.switchport model
Positional arguments:
SWITCH{Switch}
SWITCHPORT{SwitchPort}
Optional arguments:
--help, -h
show this help message and exit

#### model switch port delete 

```
model switch port delete [-h] <SWITCH>
```

Delete the last port.
Return: model.switchport model
Positional arguments:
SWITCH{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### model switch port detail 

```
model switch port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<switchport>
```

Detail view of switch port.
Return: model.switchport model
Positional arguments:
switchport{SwitchPort}
ID of the switchport
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch port list 

```
model switch port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switchport]
[--related-fields [RELATED_FIELDS ...]]
```

List switch ports.
Return: (list[model.switchport]|page[model.switchport])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switchport{int}
Get page of given switchport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch port update 

```
model switch port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <switchport> <OBJECT>
```

Update switch port.
Return: model.switchport model
Positional arguments:
switchport{SwitchPort}
ID of the switchport
OBJECT{SwitchPort}
switchport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model switch update 

```
model switch update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <switch> <OBJECT>
```

Update switch.
Return: model.switch model
Positional arguments:
switch{Switch}
ID of the switch
OBJECT{Switch}
switch object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model tc 

```
model tc [-h] [{list,detail,update}]
```

Positional arguments:
[{list,detail,update}]
list
List traffic controls.
detail
Detail view of traffic control.
update
Update traffic control.
Optional arguments:
--help, -h
show this help message and exit

#### model tc detail 

```
model tc detail [-h] [--related-fields [RELATED_FIELDS ...]] <trafficcontrol>
```

Detail view of traffic control.
Return: model.trafficcontrol model
Positional arguments:
trafficcontrol{TrafficControl}
ID of the trafficcontrol
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model tc list 

```
model tc list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of trafficcontrol]
[--related-fields [RELATED_FIELDS ...]]
```

List traffic controls.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of trafficcontrol{int}
Get page of given trafficcontrol ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model tc update 

```
model tc update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <trafficcontrol> <OBJECT>
```

Update traffic control.
Return: model.trafficcontrol model
Positional arguments:
trafficcontrol{TrafficControl}
ID of the trafficcontrol
OBJECT{TrafficControl}
trafficcontrol object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### model vm 

```
model vm [-h]
[{list,detail,meta,create,delete,update,history,clone,port,disk,access,instal
```

Positional arguments:
[{list,detail,meta,create,delete,update,history,clone,port,disk,access,install,parameters,license}]
list
List VMs.
detail
Detail view of vm.
meta
Return the firmware meta XML or selected xpath node(s)
create
Create a new VM object.
delete
Delete vm.
update
Update vm.
history
clone
port
disk
access
install
parameters
license
Optional arguments:
--help, -h
show this help message and exit

#### model vm access create 

```
model vm access create [-h] [--related-fields [RELATED_FIELDS ...]] <vmaccess
```

Create vm access.
Return: model.vmaccess model
Positional arguments:
vmaccess{VmAccess}
vmaccess object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm access delete 

```
model vm access delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <vmaccess>
```

Delete vm access.
Return: model.vmaccess model
Positional arguments:
vmaccess{VmAccess}
ID of the vmaccess
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### model vm access detail 

```
model vm access detail [-h] [--related-fields [RELATED_FIELDS ...]] <vmaccess
```

Detail view of vm access.
Return: model.vmaccess model
Positional arguments:
vmaccess{VmAccess}
ID of the vmaccess
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm access list 

```
model vm access list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmaccess]
[--related-fields [RELATED_FIELDS ...]]
```

List vm accesss.
Return: (list[model.vmaccess]|page[model.vmaccess])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmaccess{int}
Get page of given vmaccess ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm access order 

```
model vm access order [-h] [<ACCESSES> ...]
```

Return: list[model.vmaccess]
Positional arguments:
ACCESSES{*}{VmAccess}
Optional arguments:
--help, -h
show this help message and exit

#### model vm access update 

```
model vm access update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <vmaccess> <OBJECT>
```

Update vm access.
Return: model.vmaccess model
Positional arguments:
vmaccess{VmAccess}
ID of the vmaccess
OBJECT{VmAccess}
vmaccess object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm clone 

```
model vm clone [-h] [--related-fields [RELATED_FIELDS ...]] <VM>
```

Return: model.vm model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm create 

```
model vm create [-h] [--ports-count PORTS_COUNT] [--auto-connect]
[--no-auto-connect] [--related-fields [RELATED_FIELDS ...]] <vm>
```

Create a new VM object.
Mandatory fields are the “fabric” ID and “firmware” ID, ex:

```
{"object": {"fabric": 1, "firmware": 1}}
```

The call returns the created VM and the created ports.
The default number of ports is declared in the firmware meta (most of the time 10).
Return: model.vm model
Positional arguments:
vm{Vm}
vm object
Optional arguments:
--help, -h
show this help message and exit
--ports-count PORTS_COUNT{int}
--auto-connect
--no-auto-connect
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm delete 

```
model vm delete [-h] [--interactive] [--no-interactive] <vm>
```

Delete vm.
Return: model.vm model
Positional arguments:
vm{Vm}
ID of the vm
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### model vm detail 

```
model vm detail [-h] [--related-fields [RELATED_FIELDS ...]] <vm>
```

Detail view of vm.
Return: model.vm model
Positional arguments:
vm{Vm}
ID of the vm
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm disk create 

```
model vm disk create [-h] <VM> <CAPACITY>
```

Add an extra disk to the VM.
Return: model.vmdisk model
Positional arguments:
VM{Vm}
CAPACITY{BytesSize}
MB size by default
Optional arguments:
--help, -h
show this help message and exit

#### model vm disk delete 

```
model vm disk delete [-h] <VM>
```

Remove last extra disk from the VM.
Return: model.vmdisk model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm disk detail 

```
model vm disk detail [-h] [--related-fields [RELATED_FIELDS ...]] <vmdisk>
```

Detail view of vm disk.
Return: model.vmdisk model
Positional arguments:
vmdisk{VmDisk}
ID of the vmdisk
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm disk list 

```
model vm disk list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmdisk]
[--related-fields [RELATED_FIELDS ...]]
```

List vm disks.
Return: (list[model.vmdisk]|page[model.vmdisk])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmdisk{int}
Get page of given vmdisk ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm disk update 

```
model vm disk update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <vmdisk> <OBJECT>
```

Update vm disk.
Return: model.vmdisk model
Positional arguments:
vmdisk{VmDisk}
ID of the vmdisk
OBJECT{VmDisk}
vmdisk object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm history 

```
model vm history [-h] <DEVICE>
```

Positional arguments:
DEVICE{Device}
Optional arguments:
--help, -h
show this help message and exit

#### model vm install after detail 

```
model vm install after detail [-h] [--related-fields [RELATED_FIELDS ...]]
<VM>
```

View install after constraints.
Return: model.installafter model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm install after reset 

```
model vm install after reset [-h] <VM>
```

Remove all install after constraints.
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm install after update 

```
model vm install after update [-h] <VM> [<AFTER> ...]
```

Update install after constraints.
Return: model.installafter model
Positional arguments:
VM{Vm}
AFTER{*}{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm license detail 

```
model vm license detail [-h] [--related-fields [RELATED_FIELDS ...]] <VM>
```

Detail view of vm license.
Return: model.vmlicense model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm license release 

```
model vm license release [-h] <VM>
```

Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm license reset 

```
model vm license reset [-h] <VM>
```

Reset license to default values.
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm license update 

```
model vm license update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <VM> <OBJECT>
```

Update vm license.
Return: model.vmlicense model
Positional arguments:
VM{Vm}
OBJECT{VmLicense}
vmlicense object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm list 

```
model vm list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vm]
[--related-fields [RELATED_FIELDS ...]]
```

List VMs.
Return: (list[model.vm]|page[model.vm])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vm{int}
Get page of given vm ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm meta 

```
model vm meta [-h] [--firmware] [--no-firmware] [--all] [--no-all] <VM>
[<XPATH>]
```

Return the firmware meta XML or selected xpath node(s)
Positional arguments:
VM{Vm}
XPATH{str}
Optional arguments:
--help, -h
show this help message and exit
--firmware
--no-firmware
(default)
--all
--no-all
(default)

#### model vm parameters detail 

```
model vm parameters detail [-h] [--related-fields [RELATED_FIELDS ...]] <VM>
```

Detail view of vm parameters.
Return: model.vmparameters model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm parameters reset 

```
model vm parameters reset [-h] <VM>
```

Reset parameters to default values.
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm parameters update 

```
model vm parameters update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <VM> <OBJECT>
```

Update vm parameters.
Return: model.vmparameters model
Positional arguments:
VM{Vm}
OBJECT{VmParameters}
vmparameters object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm port create 

```
model vm port create [-h] <VM> [<VMPORT>]
```

Create port as the new latest port.
Return: model.vmport model
Positional arguments:
VM{Vm}
VMPORT{VmPort}
Optional arguments:
--help, -h
show this help message and exit

#### model vm port delete 

```
model vm port delete [-h] <VM>
```

Delete the last port.
Return: model.vmport model
Positional arguments:
VM{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### model vm port detail 

```
model vm port detail [-h] [--related-fields [RELATED_FIELDS ...]] <vmport>
```

Detail view of vm port.
Return: model.vmport model
Positional arguments:
vmport{VmPort}
ID of the vmport
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm port list 

```
model vm port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmport]
[--related-fields [RELATED_FIELDS ...]]
```

List vm ports.
Return: (list[model.vmport]|page[model.vmport])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmport{int}
Get page of given vmport ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm port update 

```
model vm port update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <vmport> <OBJECT>
```

Update vm port.
Return: model.vmport model
Positional arguments:
vmport{VmPort}
ID of the vmport
OBJECT{VmPort}
vmport object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### model vm update 

```
model vm update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <vm> <OBJECT>
```

Update vm.
Return: model.vm model
Positional arguments:
vm{Vm}
ID of the vm
OBJECT{Vm}
vm object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

# RUNTIME

## General options

```
runtime [-h]
[{license,fabric,device,vm,expert,config,switch,router,host,cable,diagnose,tc
```

Positional arguments:
[{license,fabric,device,vm,expert,config,switch,router,host,cable,diagnose,tc}]
license
fabric
device
vm
expert
config
switch
router
host
cable
diagnose
tc
Optional arguments:
--help, -h
show this help message and exit

### runtime cable 

```
runtime cable [-h] [{list,detail,break,repair}]
```

Positional arguments:
[{list,detail,break,repair}]
list
List cables.
detail
Detail view of cable.
break
Break the cable but do not remove it.
repair
Repair a broken cable.
Optional arguments:
--help, -h
show this help message and exit

#### runtime cable break 

```
runtime cable break [-h] <CABLE>
```

Break the cable but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
CABLE{Cable}
Optional arguments:
--help, -h
show this help message and exit

#### runtime cable detail 

```
runtime cable detail [-h] [--related-fields [RELATED_FIELDS ...]] <cable>
```

Detail view of cable.
Return: model.cable model
Positional arguments:
cable{Cable}
ID of the cable
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime cable list 

```
runtime cable list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of cable]
[--related-fields [RELATED_FIELDS ...]]
```

List cables.
Return: (list[runtime.cable]|page[runtime.cable])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of cable{int}
Get page of given cable ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime cable repair 

```
runtime cable repair [-h] <CABLE>
```

Repair a broken cable.
Ports are set up on Fabric Studio side.
Positional arguments:
CABLE{Cable}
Optional arguments:
--help, -h
show this help message and exit

### runtime config 

```
runtime config [-h] [{list,detail}]
```

Positional arguments:
[{list,detail}]
list
List device configs.
detail
Detail view of device config.
Optional arguments:
--help, -h
show this help message and exit

#### runtime config detail 

```
runtime config detail [-h] [--related-fields [RELATED_FIELDS ...]]
<deviceconfig>
```

Detail view of device config.
Return: model.deviceconfig model
Positional arguments:
deviceconfig{DeviceConfig}
ID of the deviceconfig
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime config list 

```
runtime config list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of deviceconfig]
[--related-fields [RELATED_FIELDS ...]]
```

List device configs.
Return: (list[model.deviceconfig]|page[model.deviceconfig])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of deviceconfig{int}
Get page of given deviceconfig ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### runtime device 

```
runtime device [-h]
[{console,uninstall,install,synchronize,list,detail,power-on,shutdown,power-o
```

Positional arguments:
[{console,uninstall,install,synchronize,list,detail,power-on,shutdown,power-
off,config,cables,port,license,status,cable,tc}]
console
uninstall
Uninstall the device and delete (by default) the object from the “runtime” environment DB.
install
Install a clean device.
synchronize
Synchronize the “runtime” device object and instance with the “model” object if possible.
list
List all “runtime” devices objects.
detail
Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
power-on
Power-on the device instance and perform post boot preparation.
shutdown
Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
power-off
Power off a device instance, data may be lost and disk corrupted.
config
cables
port
license
status
Return the device instance status.
cable
tc
Optional arguments:
--help, -h
show this help message and exit

#### runtime device cable break 

```
runtime device cable break [-h] <DEVICE> <PORT>
```

Break the cable attach to the VM port but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device cable repair 

```
runtime device cable repair [-h] <DEVICE> <PORT>
```

Repair the broken cable attached to the VM port.
Ports are set up on Fabric Studio side.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device cable state 

```
runtime device cable state [-h] <DEVICE> <PORT>
```

View state of cable attached to the VM port.
Return: str
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device cables connect 

```
runtime device cables connect [-h] <DEVICE>
```

Connect all cables to the device instance, peer device instances must exist.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device cables disconnect 

```
runtime device cables disconnect [-h] <DEVICE>
```

Disconnect all cables from the device instance.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device config alternate restore 

```
runtime device config alternate restore [-h] <DEVICE> <CONFIG>
```

Restore the specified configuration for the device instance.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
CONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device config backup 

```
runtime device config backup [-h] [--overwrite] [--no-overwrite]
[--as-default] [--no-as-default] <DEVICE> <FILENAME>
```

Perform a device instance configuration backup.
Return: task.task model
Result: model.deviceconfig model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
FILENAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--as-default
--no-as-default
(default)

#### runtime device config restore 

```
runtime device config restore [-h] <DEVICE>
```

Restore the device instance original configuration.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device console 

```
runtime device console [-h] [--from-start] [--no-from-start] <DEVICE>
```

Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--from-start
--no-from-start
(default)

#### runtime device detail 

```
runtime device detail [-h] [--related-fields [RELATED_FIELDS ...]] <device>
```

Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
Access restrictions when not using a normal account access (aka OAuth2 authentication):
can only be accessed through the HostPort mgmt1 IP
API key dynamically created and configured at Fabric install
VM can retrieve key by an HTTP request that only works on HostPort mgmt1 IP
TODO: create a decorator to handle that and apply it to some other call (like set port up/down).
Return: model.device model
Positional arguments:
device{Device}
ID of the device
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device install 

```
runtime device install [-h] [--power-on] [--no-power-on] [--post-boot]
[--no-post-boot] [--timeout TIMEOUT] [--license] [--no-license]
[--configuration] [--no-configuration] <DEVICE>
```

Install a clean device.
Clone a device “model” object to “runtime” object, download, extract, spawn the instance and power
it on if necessary. Preparations are also performed. The existing device instance and “runtime” DB
object are uninstalled and destroyed first.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “model” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--power-on
do not power on (default)
--no-power-on
do not power on
--post-boot
do post boot preparation (default)
--no-post-boot
do post boot preparation
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime device license alternate install 

```
runtime device license alternate install [-h] [--reinstall] [--no-reinstall]
[--refresh] [--no-refresh] [--wait WAIT] <DEVICE> <LICENSE>
```

Install the specified device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
LICENSE{License}
Use this specific license
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, None default wait

#### runtime device license install 

```
runtime device license install [-h] [--reinstall] [--no-reinstall] [--refresh
[--no-refresh] [--wait WAIT] <DEVICE>
```

Install the default device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, unspecified default wait

#### runtime device license wait 

```
runtime device license wait [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device license to be validated.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime device list 

```
runtime device list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of device]
[--related-fields [RELATED_FIELDS ...]]
```

List all “runtime” devices objects.
Return: (list[model.device]|page[model.device])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of device{int}
Get page of given device ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device port detail 

```
runtime device port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<DEVICE> <PORT>
```

Show port detail.
Return: model.port model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device port list 

```
runtime device port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of ID]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List device instance ports.
Return: (list[model.port]|page[model.port])
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of ID{int}
Get page of given ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device port tc detail 

```
runtime device port tc detail [-h] [--related-fields [RELATED_FIELDS ...]]
<DEVICE> <PORT>
```

Detail view of traffic control.
Return: model.trafficcontrol model
Positional arguments:
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device port tc force 

```
runtime device port tc force [-h] <DEVICE> <PORT>
```

Reapply traffic control.
Positional arguments:
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device port tc stop 

```
runtime device port tc stop [-h] <DEVICE> <PORT>
```

Disable traffic control by adjusting the values.
Positional arguments:
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device port tc sync 

```
runtime device port tc sync [-h] <DEVICE> <PORT>
```

Reset traffic control with values from the model.
Positional arguments:
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime device port tc update 

```
runtime device port tc update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <DEVICE> <PORT> <OBJECT>
```

Update traffic control.
Return: model.trafficcontrol model
Positional arguments:
DEVICE{Device}
PORT{Port}
OBJECT{TrafficControl}
trafficcontrol object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device power-off 

```
runtime device power-off [-h] <DEVICE>
```

Power off a device instance, data may be lost and disk corrupted.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device power-on 

```
runtime device power-on [-h] [--timeout TIMEOUT] [--post-boot]
[--no-post-boot] [--license] [--no-license] [--configuration]
[--no-configuration] <DEVICE>
```

Power-on the device instance and perform post boot preparation.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--post-boot
(default)
--no-post-boot
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime device shutdown 

```
runtime device shutdown [-h] [--timeout TIMEOUT] [--power-off]
[--no-power-off] <DEVICE>
```

Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
return:
0 if shutdown complete in time or no timeout, 1 if forced to power off and 2 if shutdown didn’t
complete in time
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
timeout in seconds before aborting or forcing power off
Default: 30 .
--power-off
power off if shutdown doesn’t complete before timeout is reached
--no-power-off
power off if shutdown doesn’t complete before timeout is reached (default)

#### runtime device status 

```
runtime device status [-h] <DEVICE>
```

Return the device instance status.
Return: DeviceStatus
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device synchronize 

```
runtime device synchronize [-h] <DEVICE>
```

Synchronize the “runtime” device object and instance with the “model” object if possible.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime device tc list 

```
runtime device tc list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of trafficcontrol]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List traffic controls.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Positional arguments:
DEVICE{Device}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of trafficcontrol{int}
Get page of given trafficcontrol ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime device uninstall 

```
runtime device uninstall [-h] [--delete] [--no-delete] <DEVICE>
```

Uninstall the device and delete (by default) the object from the “runtime” environment DB.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--delete
delete or not the object (default)
--no-delete
delete or not the object

### runtime diagnose 

```
runtime diagnose [-h] [{interfaces,cables,tcpdump,router,host,tc,device}]
```

Positional arguments:
[{interfaces,cables,tcpdump,router,host,tc,device}]
interfaces
Any interfaces in “fabric” group.
cables
Any cable interfaces in “cables” group.
tcpdump
Run tcpdump on a device’s port on Fabric Studio side.
router
host
tc
device
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose cables 

```
runtime diagnose cables [-h] [--cable CABLE]
```

Any cable interfaces in “cables” group.
Return: list[class.systeminterface]
Optional arguments:
--help, -h
show this help message and exit
--cable CABLE{Cable}

#### runtime diagnose device port tc 

```
runtime diagnose device port tc [-h] <DEVICE> <PORT>
```

Positional arguments:
DEVICE{Device}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose host dnsmasq 

```
runtime diagnose host dnsmasq [-h]
```

Get dnsmasq router configuration.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose host firewall 

```
runtime diagnose host firewall [-h] [<ROUTER>]
```

Return: str
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose host reverse-proxy 

```
runtime diagnose host reverse-proxy [-h]
```

Return: dict
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose host route 

```
runtime diagnose host route [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose host sysctl 

```
runtime diagnose host sysctl [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose interfaces 

```
runtime diagnose interfaces [-h] [--ifname IFNAME] [<ROUTER>]
```

Any interfaces in “fabric” group.
Return: list[class.systeminterface]
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit
--ifname IFNAME{str}

#### runtime diagnose router dnsmasq 

```
runtime diagnose router dnsmasq [-h] <DEVICE>
```

Get dnsmasq router configuration.
Return: str
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose router firewall 

```
runtime diagnose router firewall [-h] <ROUTER>
```

Return: str
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose router route 

```
runtime diagnose router route [-h] <ROUTER>
```

Return: str
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose router sysctl 

```
runtime diagnose router sysctl [-h] <ROUTER>
```

Return: str
Positional arguments:
ROUTER{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose tc 

```
runtime diagnose tc [-h] <TRAFFICCONTROL>
```

Positional arguments:
TRAFFICCONTROL{TrafficControl}
Optional arguments:
--help, -h
show this help message and exit

#### runtime diagnose tcpdump 

```
runtime diagnose tcpdump [-h] <DEVICE> <PORT> [<ARGS> ...]
```

Run tcpdump on a device’s port on Fabric Studio side.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
DEVICE{Device}
PORT{Port}
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

### runtime expert 

```
runtime expert [-h] [{vm,fabric,device,switch,router,host,reset}]
```

Positional arguments:
[{vm,fabric,device,switch,router,host,reset}]
vm
fabric
device
switch
router
host
reset
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device access 

```
runtime expert device access [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert device clone 

```
runtime expert device clone [-h] <DEVICE>
```

Clone the device “model” object from “model” DB to the “runtime” DB. The command fails if the
device is already cloned.
Return: model.device model
Positional arguments:
DEVICE{Device}
A device’s “model” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device firewall 

```
runtime expert device firewall [-h] <DEVICE>
```

Init the firewall rules entry points.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device firmware download 

```
runtime expert device firmware download [-h] <DEVICE>
```

Download the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device “runtime” or “model” object id (CLI accepts name and nameid too).
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device firmware extract 

```
runtime expert device firmware extract [-h] <DEVICE>
```

Extract the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device “runtime” or “model” object id (CLI accepts name and nameid too).
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device freeze 

```
runtime expert device freeze [-h] <DEVICE>
```

Uninstall and destroy the “runtime” device instance and DB object and clone a new one from the
“model” object.
Return: model.device model
Positional arguments:
DEVICE{Device}
A device’s “model” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device is-spawned 

```
runtime expert device is-spawned [-h] <DEVICE>
```

Does’s “runtime” device object has been spawned as an instance.
Return: bool
Positional arguments:
DEVICE{Device}
A device “runtime” or “model” object id (CLI accepts name and nameid too).
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device license is-installed 

```
runtime expert device license is-installed [-h] <DEVICE>
```

Has a license been applied to the device instance?
Return: bool
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device port down 

```
runtime expert device port down [-h] <DEVICE> <PORT>
```

Bring device instance port down.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device port up 

```
runtime expert device port up [-h] <DEVICE> <PORT>
```

Bring device instance port up.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device post-boot is-prepared 

```
runtime expert device post-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared after first boot?
Return: bool
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device post-boot prepare 

```
runtime expert device post-boot prepare [-h] [--timeout TIMEOUT] [--again]
[--no-again] [--license] [--no-license] [--configuration] [--no-configuration
<DEVICE>
```

Prepare the device instance on first boot.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert device power-on 

```
runtime expert device power-on [-h] <DEVICE>
```

Power on the runtime instance.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device pre-boot is-prepared 

```
runtime expert device pre-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared before first boot?
Return: bool
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device pre-boot prepare 

```
runtime expert device pre-boot prepare [-h] [--again] [--no-again] [--license
[--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Prepare the device instance before first boot.
Return: task.task model
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert device spawn 

```
runtime expert device spawn [-h] <DEVICE>
```

Spawn a device instance in the “runtime” engine based on the device “runtime” object.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert device wait ready 

```
runtime expert device wait ready [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device instance to be ready once powered on.
Positional arguments:
DEVICE{Device}
A device’s “runtime” object id (CLI accepts name and nameid too)
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime expert fabric clone 

```
runtime expert fabric clone [-h] [--environment ENVIRONMENT] <FABRIC>
```

Clone a Fabric object from “model” to “runtime”.
Return: model.fabric model
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--environment ENVIRONMENT{DeviceConfig}

#### runtime expert fabric spawn 

```
runtime expert fabric spawn [-h]
```

Create all runtime Fabric’s VMs.
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host access 

```
runtime expert host access [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert host clone 

```
runtime expert host clone [-h] <DEVICE>
```

Clone the device “model” object from “model” DB to the “runtime” DB. The command fails if the
device is already cloned.
Return: model.device model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host firewall 

```
runtime expert host firewall [-h] <DEVICE>
```

Init the firewall rules entry points.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host firmware download 

```
runtime expert host firmware download [-h] <DEVICE>
```

Download the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host firmware extract 

```
runtime expert host firmware extract [-h] <DEVICE>
```

Extract the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host freeze 

```
runtime expert host freeze [-h] <DEVICE>
```

Uninstall and destroy the “runtime” device instance and DB object and clone a new one from the
“model” object.
Return: model.device model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host is-spawned 

```
runtime expert host is-spawned [-h] <DEVICE>
```

Does’s “runtime” device object has been spawned as an instance.
Return: bool
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host license is-installed 

```
runtime expert host license is-installed [-h] <DEVICE>
```

Has a license been applied to the device instance?
Return: bool
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host port down 

```
runtime expert host port down [-h] <DEVICE> <PORT>
```

Bring device instance port down.
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host port up 

```
runtime expert host port up [-h] <DEVICE> <PORT>
```

Bring device instance port up.
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host post-boot is-prepared 

```
runtime expert host post-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared after first boot?
Return: bool
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host post-boot prepare 

```
runtime expert host post-boot prepare [-h] [--timeout TIMEOUT] [--again]
[--no-again] [--license] [--no-license] [--configuration] [--no-configuration
<DEVICE>
```

Prepare the device instance on first boot.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert host power-on 

```
runtime expert host power-on [-h] <DEVICE>
```

Power on the runtime instance.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host pre-boot is-prepared 

```
runtime expert host pre-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared before first boot?
Return: bool
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host pre-boot prepare 

```
runtime expert host pre-boot prepare [-h] [--again] [--no-again] [--license]
[--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Prepare the device instance before first boot.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert host spawn 

```
runtime expert host spawn [-h] <DEVICE>
```

Spawn a device instance in the “runtime” engine based on the device “runtime” object.
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert host wait ready 

```
runtime expert host wait ready [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device instance to be ready once powered on.
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime expert reset 

```
runtime expert reset [-h]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router access 

```
runtime expert router access [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert router clone 

```
runtime expert router clone [-h] <DEVICE>
```

Clone the device “model” object from “model” DB to the “runtime” DB. The command fails if the
device is already cloned.
Return: model.device model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router firewall 

```
runtime expert router firewall [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert router firmware download 

```
runtime expert router firmware download [-h] <DEVICE>
```

Download the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router firmware extract 

```
runtime expert router firmware extract [-h] <DEVICE>
```

Extract the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router freeze 

```
runtime expert router freeze [-h] <DEVICE>
```

Uninstall and destroy the “runtime” device instance and DB object and clone a new one from the
“model” object.
Return: model.device model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router is-spawned 

```
runtime expert router is-spawned [-h] <DEVICE>
```

Does’s “runtime” device object has been spawned as an instance.
Return: bool
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router license is-installed 

```
runtime expert router license is-installed [-h] <DEVICE>
```

Has a license been applied to the device instance?
Return: bool
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router port down 

```
runtime expert router port down [-h] <DEVICE> <PORT>
```

Bring device instance port down.
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router port up 

```
runtime expert router port up [-h] <DEVICE> <PORT>
```

Bring device instance port up.
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router post-boot is-prepared 

```
runtime expert router post-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared after first boot?
Return: bool
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router post-boot prepare 

```
runtime expert router post-boot prepare [-h] [--timeout TIMEOUT] [--again]
[--no-again] [--license] [--no-license] [--configuration] [--no-configuration
<DEVICE>
```

Prepare the device instance on first boot.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert router power-on 

```
runtime expert router power-on [-h] <DEVICE>
```

Power on the runtime instance.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router pre-boot is-prepared 

```
runtime expert router pre-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared before first boot?
Return: bool
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router pre-boot prepare 

```
runtime expert router pre-boot prepare [-h] [--again] [--no-again] [--license
[--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Prepare the device instance before first boot.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert router spawn 

```
runtime expert router spawn [-h] <DEVICE>
```

Spawn a device instance in the “runtime” engine based on the device “runtime” object.
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert router wait ready 

```
runtime expert router wait ready [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device instance to be ready once powered on.
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime expert switch access 

```
runtime expert switch access [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert switch clone 

```
runtime expert switch clone [-h] <DEVICE>
```

Clone the device “model” object from “model” DB to the “runtime” DB. The command fails if the
device is already cloned.
Return: model.device model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch firewall 

```
runtime expert switch firewall [-h] <DEVICE>
```

Init the firewall rules entry points.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch firmware download 

```
runtime expert switch firmware download [-h] <DEVICE>
```

Download the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch firmware extract 

```
runtime expert switch firmware extract [-h] <DEVICE>
```

Extract the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch freeze 

```
runtime expert switch freeze [-h] <DEVICE>
```

Uninstall and destroy the “runtime” device instance and DB object and clone a new one from the
“model” object.
Return: model.device model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch is-spawned 

```
runtime expert switch is-spawned [-h] <DEVICE>
```

Does’s “runtime” device object has been spawned as an instance.
Return: bool
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch license is-installed 

```
runtime expert switch license is-installed [-h] <DEVICE>
```

Has a license been applied to the device instance?
Return: bool
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch port down 

```
runtime expert switch port down [-h] <DEVICE> <PORT>
```

Bring device instance port down.
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch port up 

```
runtime expert switch port up [-h] <DEVICE> <PORT>
```

Bring device instance port up.
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch post-boot is-prepared 

```
runtime expert switch post-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared after first boot?
Return: bool
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch post-boot prepare 

```
runtime expert switch post-boot prepare [-h] [--timeout TIMEOUT] [--again]
[--no-again] [--license] [--no-license] [--configuration] [--no-configuration
<DEVICE>
```

Prepare the device instance on first boot.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert switch power-on 

```
runtime expert switch power-on [-h] <DEVICE>
```

Power on the runtime instance.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch pre-boot is-prepared 

```
runtime expert switch pre-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared before first boot?
Return: bool
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch pre-boot prepare 

```
runtime expert switch pre-boot prepare [-h] [--again] [--no-again] [--license
[--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Prepare the device instance before first boot.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert switch spawn 

```
runtime expert switch spawn [-h] <DEVICE>
```

Spawn a device instance in the “runtime” engine based on the device “runtime” object.
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert switch wait ready 

```
runtime expert switch wait ready [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device instance to be ready once powered on.
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime expert vm access 

```
runtime expert vm access [-h] [--init] [--no-init] <DEVICE>
```

Create the firewall rules.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--init
--no-init
(default)

#### runtime expert vm clone 

```
runtime expert vm clone [-h] <DEVICE>
```

Clone the device “model” object from “model” DB to the “runtime” DB. The command fails if the
device is already cloned.
Return: model.device model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm firewall 

```
runtime expert vm firewall [-h] <DEVICE>
```

Init the firewall rules entry points.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm firmware download 

```
runtime expert vm firmware download [-h] <DEVICE>
```

Download the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm firmware extract 

```
runtime expert vm firmware extract [-h] <DEVICE>
```

Extract the “runtime” device object firmware.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm freeze 

```
runtime expert vm freeze [-h] <DEVICE>
```

Uninstall and destroy the “runtime” device instance and DB object and clone a new one from the
“model” object.
Return: model.device model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm is-spawned 

```
runtime expert vm is-spawned [-h] <DEVICE>
```

Does’s “runtime” device object has been spawned as an instance.
Return: bool
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm license is-installed 

```
runtime expert vm license is-installed [-h] <DEVICE>
```

Has a license been applied to the device instance?
Return: bool
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm port down 

```
runtime expert vm port down [-h] <DEVICE> <PORT>
```

Bring device instance port down.
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm port up 

```
runtime expert vm port up [-h] <DEVICE> <PORT>
```

Bring device instance port up.
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm post-boot is-prepared 

```
runtime expert vm post-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared after first boot?
Return: bool
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm post-boot prepare 

```
runtime expert vm post-boot prepare [-h] [--timeout TIMEOUT] [--again]
[--no-again] [--license] [--no-license] [--configuration] [--no-configuration
<DEVICE>
```

Prepare the device instance on first boot.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert vm power-on 

```
runtime expert vm power-on [-h] <DEVICE>
```

Power on the runtime instance.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm pre-boot is-prepared 

```
runtime expert vm pre-boot is-prepared [-h] <DEVICE>
```

Has the device instance been prepared before first boot?
Return: bool
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm pre-boot prepare 

```
runtime expert vm pre-boot prepare [-h] [--again] [--no-again] [--license]
[--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Prepare the device instance before first boot.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--again
perform autoconf even if already done
--no-again
perform autoconf even if already done (default)
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime expert vm spawn 

```
runtime expert vm spawn [-h] <DEVICE>
```

Spawn a device instance in the “runtime” engine based on the device “runtime” object.
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime expert vm status detail 

```
runtime expert vm status detail [-h] [--related-fields [RELATED_FIELDS ...]]
<vmstatus>
```

Detail view of vm status.
Return: runtime.vmstatus model
Positional arguments:
vmstatus{VmStatus}
ID of the vmstatus
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime expert vm status list 

```
runtime expert vm status list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vmstatus]
[--related-fields [RELATED_FIELDS ...]]
```

List vm statuss.
Return: (list[runtime.vmstatus]|page[runtime.vmstatus])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vmstatus{int}
Get page of given vmstatus ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime expert vm status update 

```
runtime expert vm status update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <vmstatus> <OBJECT>
```

Update vm status.
Return: runtime.vmstatus model
Positional arguments:
vmstatus{VmStatus}
ID of the vmstatus
OBJECT{VmStatus}
vmstatus object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime expert vm wait ready 

```
runtime expert vm wait ready [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device instance to be ready once powered on.
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

### runtime fabric 

```
runtime fabric [-h]
[{documentation,uninstall,install,synchronize,detail,power-on,license}]
```

Positional arguments:
[{documentation,uninstall,install,synchronize,detail,power-on,license}]
documentation
uninstall
Uninstall Fabric from runtime environment and reseting all systems.
install
Install a Fabric in the runtime environment.
synchronize
Synchronize fabric parameters.
detail
Current running Fabric detail.
power-on
Power-on all Fabric VM in the runtime environment.
license
Optional arguments:
--help, -h
show this help message and exit

#### runtime fabric detail 

```
runtime fabric detail [-h] [--related-fields [RELATED_FIELDS ...]]
```

Current running Fabric detail.
Return: model.fabric model
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime fabric documentation download 

```
runtime fabric documentation download [-h] [--interactive] [--no-interactive]
```

Return: dict
Optional arguments:
--help, -h
show this help message and exit
--interactive
--no-interactive
(default)

#### runtime fabric install 

```
runtime fabric install [-h] [--environment ENVIRONMENT] [--power-on-vms]
[--no-power-on-vms] [--install-vms] [--no-install-vms] [--install-vms-tasks]
[--no-install-vms-tasks] [--doc-download] [--no-doc-download] <FABRIC>
```

Install a Fabric in the runtime environment.
Clone a Fabric and its devices objects from the “model” to the “runtime” environment. Spawn all
devices and finally power-on them.
Existing Fabric in the runtime environment is uninstalled first.
Return: task.task model
Result: model.fabric model
Positional arguments:
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit
--environment ENVIRONMENT{DeviceConfig}
--power-on-vms
power on (True) or do not power on (False) VMs (default)
--no-power-on-vms
power on (True) or do not power on (False) VMs
--install-vms
install (True) or do not install VMs (False) (default)
--no-install-vms
install (True) or do not install VMs (False)
--install-vms-tasks
install VMs in separate tasks (True) or not (False) (default)
--no-install-vms-tasks
install VMs in separate tasks (True) or not (False)
--doc-download
download documentation (default)
--no-doc-download
download documentation

#### runtime fabric license alive 

```
runtime fabric license alive [-h] [--mode MODE] [--quiet] [--no-quiet]
```

Notify license server we are still alive.
Alternatively can issue a “register” request instead, only when suggested by support team.
Optional arguments:
--help, -h
show this help message and exit
--mode{str} ('alive', 'register')
Default: alive .
--quiet
--no-quiet
(default)

#### runtime fabric power-on 

```
runtime fabric power-on [-h] [--vms-tasks] [--no-vms-tasks] [--on-boot]
[--no-on-boot]
```

Power-on all Fabric VM in the runtime environment.
Return: task.task model
Optional arguments:
--help, -h
show this help message and exit
--vms-tasks
power-on VMs in separate tasks (True) or not (False) (default)
--no-vms-tasks
power-on VMs in separate tasks (True) or not (False)
--on-boot
--no-on-boot
(default)

#### runtime fabric synchronize 

```
runtime fabric synchronize [-h] [--environment ENVIRONMENT]
```

Synchronize fabric parameters.
Return: task.task model
Optional arguments:
--help, -h
show this help message and exit
--environment ENVIRONMENT{DeviceConfig}

#### runtime fabric uninstall 

```
runtime fabric uninstall [-h]
```

Uninstall Fabric from runtime environment and reseting all systems.
Return: runtime.runtimetask model
Optional arguments:
--help, -h
show this help message and exit

### runtime host 

```
runtime host [-h]
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-off,confi
```

Positional arguments:
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-
off,config,cables,port,license,status,cable}]
uninstall
Uninstall the device and delete (by default) the object from the “runtime” environment DB.
install
Install a clean device.
synchronize
Synchronize the “runtime” device object and instance with the “model” object if possible.
list
Returns the runtime host definition.
detail
Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
power-on
Power-on the device instance and perform post boot preparation.
shutdown
Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
power-off
Power off a device instance, data may be lost and disk corrupted.
config
cables
port
license
status
Return the device instance status.
cable
Optional arguments:
--help, -h
show this help message and exit

#### runtime host cable break 

```
runtime host cable break [-h] <DEVICE> <PORT>
```

Break the cable attach to the host port but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host cable repair 

```
runtime host cable repair [-h] <DEVICE> <PORT>
```

Repair the broken cable attached to the host port.
Ports are set up on Fabric Studio side.
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host cable state 

```
runtime host cable state [-h] <DEVICE> <PORT>
```

View state of cable attached to the host port.
Return: str
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host cables connect 

```
runtime host cables connect [-h] <DEVICE>
```

Connect all cables to the device instance, peer device instances must exist.
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host cables disconnect 

```
runtime host cables disconnect [-h] <DEVICE>
```

Disconnect all cables from the device instance.
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host config alternate restore 

```
runtime host config alternate restore [-h] <DEVICE> <CONFIG>
```

Restore the specified configuration for the device instance.
Return: task.task model
Positional arguments:
DEVICE{Host}
CONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host config backup 

```
runtime host config backup [-h] [--overwrite] [--no-overwrite] [--as-default]
[--no-as-default] <DEVICE> <FILENAME>
```

Perform a device instance configuration backup.
Return: task.task model
Result: model.deviceconfig model
Positional arguments:
DEVICE{Host}
FILENAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--as-default
--no-as-default
(default)

#### runtime host config restore 

```
runtime host config restore [-h] <DEVICE>
```

Restore the device instance original configuration.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host detail 

```
runtime host detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
Access restrictions when not using a normal account access (aka OAuth2 authentication):
can only be accessed through the HostPort mgmt1 IP
API key dynamically created and configured at Fabric install
VM can retrieve key by an HTTP request that only works on HostPort mgmt1 IP
TODO: create a decorator to handle that and apply it to some other call (like set port up/down).
Return: model.device model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime host install 

```
runtime host install [-h] [--power-on] [--no-power-on] [--license]
[--no-license] [--configuration] [--no-configuration] [--post-boot]
[--no-post-boot] [--timeout TIMEOUT] <DEVICE>
```

Install a clean device.
Clone a device “model” object to “runtime” object, download, extract, spawn the instance and power
it on if necessary. Preparations are also performed. The existing device instance and “runtime” DB
object are uninstalled and destroyed first.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--power-on
do not power on (default)
--no-power-on
do not power on
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not
--post-boot
do post boot preparation (default)
--no-post-boot
do post boot preparation
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime host license alternate install 

```
runtime host license alternate install [-h] [--reinstall] [--no-reinstall]
[--refresh] [--no-refresh] [--wait WAIT] <DEVICE> <LICENSE>
```

Install the specified device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Host}
LICENSE{License}
Use this specific license
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, None default wait

#### runtime host license install 

```
runtime host license install [-h] [--reinstall] [--no-reinstall] [--refresh]
[--no-refresh] [--wait WAIT] <DEVICE>
```

Install the default device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, unspecified default wait

#### runtime host license wait 

```
runtime host license wait [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device license to be validated.
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime host list 

```
runtime host list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of host]
[--related-fields [RELATED_FIELDS ...]]
```

Returns the runtime host definition.
Return: (list[runtime.host]|page[runtime.host])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of host{int}
Get page of given host ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime host port detail 

```
runtime host port detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE
<PORT>
```

Show port detail.
Return: model.port model
Positional arguments:
DEVICE{Host}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime host port list 

```
runtime host port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of ID]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List device instance ports.
Return: (list[model.port]|page[model.port])
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of ID{int}
Get page of given ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime host power-off 

```
runtime host power-off [-h] <DEVICE>
```

Power off a device instance, data may be lost and disk corrupted.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host power-on 

```
runtime host power-on [-h] [--timeout TIMEOUT] [--post-boot] [--no-post-boot]
[--license] [--no-license] [--configuration] [--no-configuration] <DEVICE>
```

Power-on the device instance and perform post boot preparation.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--post-boot
(default)
--no-post-boot
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime host shutdown 

```
runtime host shutdown [-h] [--timeout TIMEOUT] [--power-off] [--no-power-off]
<DEVICE>
```

Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
return:
0 if shutdown complete in time or no timeout, 1 if forced to power off and 2 if shutdown didn’t
complete in time
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
timeout in seconds before aborting or forcing power off
Default: 30 .
--power-off
power off if shutdown doesn’t complete before timeout is reached
--no-power-off
power off if shutdown doesn’t complete before timeout is reached (default)

#### runtime host status 

```
runtime host status [-h] <DEVICE>
```

Return the device instance status.
Return: DeviceStatus
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host synchronize 

```
runtime host synchronize [-h] <DEVICE>
```

Synchronize the “runtime” device object and instance with the “model” object if possible.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit

#### runtime host uninstall 

```
runtime host uninstall [-h] [--delete] [--no-delete] <DEVICE>
```

Uninstall the device and delete (by default) the object from the “runtime” environment DB.
Return: task.task model
Positional arguments:
DEVICE{Host}
Optional arguments:
--help, -h
show this help message and exit
--delete
delete or not the object (default)
--no-delete
delete or not the object

### runtime license 

```
runtime license [-h] [{list}]
```

Positional arguments:
[{list}]
list
List licenses.
Optional arguments:
--help, -h
show this help message and exit

#### runtime license list 

```
runtime license list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of license]
[--related-fields [RELATED_FIELDS ...]]
```

List licenses.
Return: (list[license.license]|page[license.license])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of license{int}
Get page of given license ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### runtime router 

```
runtime router [-h]
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-off,confi
```

Positional arguments:
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-
off,config,cables,port,license,status,cable}]
uninstall
Uninstall the device and delete (by default) the object from the “runtime” environment DB.
install
Install a clean device.
synchronize
Synchronize the “runtime” device object and instance with the “model” object if possible.
list
List all “runtime” routers objects.
detail
Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
power-on
Power-on the device instance and perform post boot preparation.
shutdown
Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
power-off
Power off a device instance, data may be lost and disk corrupted.
config
cables
port
license
status
Return the device instance status.
cable
Optional arguments:
--help, -h
show this help message and exit

#### runtime router cable break 

```
runtime router cable break [-h] <DEVICE> <PORT>
```

Break the cable attach to the router port but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router cable repair 

```
runtime router cable repair [-h] <DEVICE> <PORT>
```

Repair the broken cable attached to the router port.
Ports are set up on Fabric Studio side.
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router cable state 

```
runtime router cable state [-h] <DEVICE> <PORT>
```

View state of cable attached to the router port.
Return: str
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router cables connect 

```
runtime router cables connect [-h] <DEVICE>
```

Connect all cables to the device instance, peer device instances must exist.
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router cables disconnect 

```
runtime router cables disconnect [-h] <DEVICE>
```

Disconnect all cables from the device instance.
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router config alternate restore 

```
runtime router config alternate restore [-h] <DEVICE> <CONFIG>
```

Restore the specified configuration for the device instance.
Return: task.task model
Positional arguments:
DEVICE{Router}
CONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router config backup 

```
runtime router config backup [-h] [--overwrite] [--no-overwrite]
[--as-default] [--no-as-default] <DEVICE> <FILENAME>
```

Perform a device instance configuration backup.
Return: model.deviceconfig model
Positional arguments:
DEVICE{Router}
FILENAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--as-default
--no-as-default
(default)

#### runtime router config restore 

```
runtime router config restore [-h] <DEVICE>
```

Restore the device instance original configuration.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router detail 

```
runtime router detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
Access restrictions when not using a normal account access (aka OAuth2 authentication):
can only be accessed through the HostPort mgmt1 IP
API key dynamically created and configured at Fabric install
VM can retrieve key by an HTTP request that only works on HostPort mgmt1 IP
TODO: create a decorator to handle that and apply it to some other call (like set port up/down).
Return: model.device model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime router install 

```
runtime router install [-h] [--power-on] [--no-power-on] [--license]
[--no-license] [--configuration] [--no-configuration] [--post-boot]
[--no-post-boot] [--timeout TIMEOUT] <DEVICE>
```

Install a clean device.
Clone a device “model” object to “runtime” object, download, extract, spawn the instance and power
it on if necessary. Preparations are also performed. The existing device instance and “runtime” DB
object are uninstalled and destroyed first.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--power-on
do not power on (default)
--no-power-on
do not power on
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not
--post-boot
do post boot preparation (default)
--no-post-boot
do post boot preparation
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime router license alternate install 

```
runtime router license alternate install [-h] [--reinstall] [--no-reinstall]
[--refresh] [--no-refresh] [--wait WAIT] <DEVICE> <LICENSE>
```

Install the specified device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Router}
LICENSE{License}
Use this specific license
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, None default wait

#### runtime router license install 

```
runtime router license install [-h] [--reinstall] [--no-reinstall] [--refresh
[--no-refresh] [--wait WAIT] <DEVICE>
```

Install the default device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, unspecified default wait

#### runtime router license wait 

```
runtime router license wait [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device license to be validated.
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime router list 

```
runtime router list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of router]
[--related-fields [RELATED_FIELDS ...]]
```

List all “runtime” routers objects.
Return: (list[runtime.router]|page[runtime.router])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of router{int}
Get page of given router ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime router port detail 

```
runtime router port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<DEVICE> <PORT>
```

Show port detail.
Return: model.port model
Positional arguments:
DEVICE{Router}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime router port list 

```
runtime router port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of ID]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List device instance ports.
Return: (list[model.port]|page[model.port])
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of ID{int}
Get page of given ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime router power-off 

```
runtime router power-off [-h] <DEVICE>
```

Power off a device instance, data may be lost and disk corrupted.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router power-on 

```
runtime router power-on [-h] [--timeout TIMEOUT] [--post-boot]
[--no-post-boot] [--license] [--no-license] [--configuration]
[--no-configuration] <DEVICE>
```

Power-on the device instance and perform post boot preparation.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--post-boot
(default)
--no-post-boot
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime router shutdown 

```
runtime router shutdown [-h] [--timeout TIMEOUT] [--power-off]
[--no-power-off] <DEVICE>
```

Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
return:
0 if shutdown complete in time or no timeout, 1 if forced to power off and 2 if shutdown didn’t
complete in time
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
timeout in seconds before aborting or forcing power off
Default: 30 .
--power-off
power off if shutdown doesn’t complete before timeout is reached
--no-power-off
power off if shutdown doesn’t complete before timeout is reached (default)

#### runtime router status 

```
runtime router status [-h] <DEVICE>
```

Return the device instance status.
Return: DeviceStatus
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router synchronize 

```
runtime router synchronize [-h] <DEVICE>
```

Synchronize the “runtime” device object and instance with the “model” object if possible.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit

#### runtime router uninstall 

```
runtime router uninstall [-h] [--delete] [--no-delete] <DEVICE>
```

Uninstall the device and delete (by default) the object from the “runtime” environment DB.
Return: task.task model
Positional arguments:
DEVICE{Router}
Optional arguments:
--help, -h
show this help message and exit
--delete
delete or not the object (default)
--no-delete
delete or not the object

### runtime switch 

```
runtime switch [-h]
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-off,confi
```

Positional arguments:
[{uninstall,install,synchronize,list,detail,power-on,shutdown,power-
off,config,cables,port,license,status,cable}]
uninstall
Uninstall the device and delete (by default) the object from the “runtime” environment DB.
install
Install a clean device.
synchronize
Synchronize the “runtime” device object and instance with the “model” object if possible.
list
List all “runtime” switches objects.
detail
Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
power-on
Power-on the device instance and perform post boot preparation.
shutdown
Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
power-off
Power off a device instance, data may be lost and disk corrupted.
config
cables
port
license
status
Return the device instance status.
cable
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch cable break 

```
runtime switch cable break [-h] <DEVICE> <PORT>
```

Break the cable attach to the switch port but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch cable repair 

```
runtime switch cable repair [-h] <DEVICE> <PORT>
```

Repair the broken cable attached to the switch port.
Ports are set up on Fabric Studio side.
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch cable state 

```
runtime switch cable state [-h] <DEVICE> <PORT>
```

View state of cable attached to the switch port.
Return: str
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch cables connect 

```
runtime switch cables connect [-h] <DEVICE>
```

Connect all cables to the device instance, peer device instances must exist.
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch cables disconnect 

```
runtime switch cables disconnect [-h] <DEVICE>
```

Disconnect all cables from the device instance.
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch config alternate restore 

```
runtime switch config alternate restore [-h] <DEVICE> <CONFIG>
```

Restore the specified configuration for the device instance.
Return: task.task model
Positional arguments:
DEVICE{Switch}
CONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch config backup 

```
runtime switch config backup [-h] [--overwrite] [--no-overwrite]
[--as-default] [--no-as-default] <DEVICE> <FILENAME>
```

Perform a device instance configuration backup.
Return: task.task model
Result: model.deviceconfig model
Positional arguments:
DEVICE{Switch}
FILENAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--as-default
--no-as-default
(default)

#### runtime switch config restore 

```
runtime switch config restore [-h] <DEVICE>
```

Restore the device instance original configuration.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch detail 

```
runtime switch detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
Access restrictions when not using a normal account access (aka OAuth2 authentication):
can only be accessed through the HostPort mgmt1 IP
API key dynamically created and configured at Fabric install
VM can retrieve key by an HTTP request that only works on HostPort mgmt1 IP
TODO: create a decorator to handle that and apply it to some other call (like set port up/down).
Return: model.device model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime switch install 

```
runtime switch install [-h] [--power-on] [--no-power-on] [--license]
[--no-license] [--configuration] [--no-configuration] [--post-boot]
[--no-post-boot] [--timeout TIMEOUT] <DEVICE>
```

Install a clean device.
Clone a device “model” object to “runtime” object, download, extract, spawn the instance and power
it on if necessary. Preparations are also performed. The existing device instance and “runtime” DB
object are uninstalled and destroyed first.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--power-on
do not power on (default)
--no-power-on
do not power on
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not
--post-boot
do post boot preparation (default)
--no-post-boot
do post boot preparation
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime switch license alternate install 

```
runtime switch license alternate install [-h] [--reinstall] [--no-reinstall]
[--refresh] [--no-refresh] [--wait WAIT] <DEVICE> <LICENSE>
```

Install the specified device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Switch}
LICENSE{License}
Use this specific license
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, None default wait

#### runtime switch license install 

```
runtime switch license install [-h] [--reinstall] [--no-reinstall] [--refresh
[--no-refresh] [--wait WAIT] <DEVICE>
```

Install the default device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, unspecified default wait

#### runtime switch license wait 

```
runtime switch license wait [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device license to be validated.
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime switch list 

```
runtime switch list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of switch]
[--related-fields [RELATED_FIELDS ...]]
```

List all “runtime” switches objects.
Return: (list[runtime.switch]|page[runtime.switch])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of switch{int}
Get page of given switch ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime switch port detail 

```
runtime switch port detail [-h] [--related-fields [RELATED_FIELDS ...]]
<DEVICE> <PORT>
```

Show port detail.
Return: model.port model
Positional arguments:
DEVICE{Switch}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime switch port list 

```
runtime switch port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of ID]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List device instance ports.
Return: (list[model.port]|page[model.port])
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of ID{int}
Get page of given ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime switch power-off 

```
runtime switch power-off [-h] <DEVICE>
```

Power off a device instance, data may be lost and disk corrupted.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch power-on 

```
runtime switch power-on [-h] [--timeout TIMEOUT] [--post-boot]
[--no-post-boot] [--license] [--no-license] [--configuration]
[--no-configuration] <DEVICE>
```

Power-on the device instance and perform post boot preparation.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort
--post-boot
(default)
--no-post-boot
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not

#### runtime switch shutdown 

```
runtime switch shutdown [-h] [--timeout TIMEOUT] [--power-off]
[--no-power-off] <DEVICE>
```

Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
return:
0 if shutdown complete in time or no timeout, 1 if forced to power off and 2 if shutdown didn’t
complete in time
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
timeout in seconds before aborting or forcing power off
Default: 30 .
--power-off
power off if shutdown doesn’t complete before timeout is reached
--no-power-off
power off if shutdown doesn’t complete before timeout is reached (default)

#### runtime switch status 

```
runtime switch status [-h] <DEVICE>
```

Return the device instance status.
Return: DeviceStatus
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch synchronize 

```
runtime switch synchronize [-h] <DEVICE>
```

Synchronize the “runtime” device object and instance with the “model” object if possible.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit

#### runtime switch uninstall 

```
runtime switch uninstall [-h] [--delete] [--no-delete] <DEVICE>
```

Uninstall the device and delete (by default) the object from the “runtime” environment DB.
Return: task.task model
Positional arguments:
DEVICE{Switch}
Optional arguments:
--help, -h
show this help message and exit
--delete
delete or not the object (default)
--no-delete
delete or not the object

### runtime tc 

```
runtime tc [-h] [{list,detail,update,sync,stop,cleanup,force}]
```

Positional arguments:
[{list,detail,update,sync,stop,cleanup,force}]
list
List traffic controls.
detail
Detail view of traffic control.
update
Update traffic control.
sync
Reset traffic control with values from the model.
stop
Disable traffic control by adjusting the values.
cleanup
Cleanup dangling traffic control.
force
Reapply traffic control.
Optional arguments:
--help, -h
show this help message and exit

#### runtime tc cleanup 

```
runtime tc cleanup [-h]
```

Cleanup dangling traffic control.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Optional arguments:
--help, -h
show this help message and exit

#### runtime tc detail 

```
runtime tc detail [-h] [--related-fields [RELATED_FIELDS ...]]
<trafficcontrol>
```

Detail view of traffic control.
Return: model.trafficcontrol model
Positional arguments:
trafficcontrol{TrafficControl}
ID of the trafficcontrol
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime tc force 

```
runtime tc force [-h] <TRAFFICCONTROL>
```

Reapply traffic control.
Return: model.trafficcontrol model
Positional arguments:
TRAFFICCONTROL{TrafficControl}
Optional arguments:
--help, -h
show this help message and exit

#### runtime tc list 

```
runtime tc list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of trafficcontrol]
[--related-fields [RELATED_FIELDS ...]]
```

List traffic controls.
Return: (list[model.trafficcontrol]|page[model.trafficcontrol])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of trafficcontrol{int}
Get page of given trafficcontrol ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime tc stop 

```
runtime tc stop [-h] <TRAFFICCONTROL>
```

Disable traffic control by adjusting the values.
Return: model.trafficcontrol model
Positional arguments:
TRAFFICCONTROL{TrafficControl}
Optional arguments:
--help, -h
show this help message and exit

#### runtime tc sync 

```
runtime tc sync [-h] <TRAFFICCONTROL>
```

Reset traffic control with values from the model.
Return: model.trafficcontrol model
Positional arguments:
TRAFFICCONTROL{TrafficControl}
Optional arguments:
--help, -h
show this help message and exit

#### runtime tc update 

```
runtime tc update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <trafficcontrol> <OBJECT>
```

Update traffic control.
Return: model.trafficcontrol model
Positional arguments:
trafficcontrol{TrafficControl}
ID of the trafficcontrol
OBJECT{TrafficControl}
trafficcontrol object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### runtime vm 

```
runtime vm [-h]
[{console,export,cdrom,disk,uninstall,install,synchronize,list,detail,power-o
```

Positional arguments:
[{console,export,cdrom,disk,uninstall,install,synchronize,list,detail,power-on,shutdown,power-
off,config,cables,port,license,status,cable}]
console
export
cdrom
disk
uninstall
Uninstall the device and delete (by default) the object from the “runtime” environment DB.
install
Install a clean device.
synchronize
Synchronize the “runtime” device object and instance with the “model” object if possible.
list
List all “runtime” VMs objects.
detail
Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
power-on
Power-on the device instance and perform post boot preparation.
shutdown
Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
power-off
Power off a device instance, data may be lost and disk corrupted.
config
cables
port
license
status
Return the device instance status.
cable
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cable break 

```
runtime vm cable break [-h] <DEVICE> <PORT>
```

Break the cable attach to the VM port but do not remove it.
Ports are set down on Fabric Studio side.
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cable repair 

```
runtime vm cable repair [-h] <DEVICE> <PORT>
```

Repair the broken cable attached to the VM port.
Ports are set up on Fabric Studio side.
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cable state 

```
runtime vm cable state [-h] <DEVICE> <PORT>
```

View state of cable attached to the VM port.
Return: str
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cables connect 

```
runtime vm cables connect [-h] <DEVICE>
```

Connect all cables to the device instance, peer device instances must exist.
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cables disconnect 

```
runtime vm cables disconnect [-h] <DEVICE>
```

Disconnect all cables from the device instance.
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm cdrom attach 

```
runtime vm cdrom attach [-h] [--bus BUS] [--dev DEV] <DEVICE> <ISO>
```

Attach a new CDROM device to the VM definition.
Hotplug is not supported. You must power-cycle the device (aka: shutdown then power on).
Positional arguments:
DEVICE{Vm}
ISO{Path}
Optional arguments:
--help, -h
show this help message and exit
--bus BUS{str}
--dev DEV{str}

#### runtime vm cdrom detach 

```
runtime vm cdrom detach [-h] <DEVICE> <ISO>
```

Detach a CDROM device from the VM definition.
Hotplug is not supported. You must power-cycle the device (aka: shutdown then power on).
Positional arguments:
DEVICE{Vm}
ISO{Path}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm config alternate restore 

```
runtime vm config alternate restore [-h] <DEVICE> <CONFIG>
```

Restore the specified configuration for the device instance.
Return: task.task model
Positional arguments:
DEVICE{Vm}
CONFIG{DeviceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm config backup 

```
runtime vm config backup [-h] [--overwrite] [--no-overwrite] [--as-default]
[--no-as-default] <DEVICE> <FILENAME>
```

Perform a device instance configuration backup.
Return: task.task model
Result: model.deviceconfig model
Positional arguments:
DEVICE{Vm}
FILENAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--as-default
--no-as-default
(default)

#### runtime vm config restore 

```
runtime vm config restore [-h] <DEVICE>
```

Restore the device instance original configuration.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm console 

```
runtime vm console [-h] [--from-start] [--no-from-start] <DEVICE>
```

Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--from-start
--no-from-start
(default)

#### runtime vm detail 

```
runtime vm detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

Return detail view of a device, to be used during runtime to interact with the Fabric from a device
script (REST call).
Access restrictions when not using a normal account access (aka OAuth2 authentication):
can only be accessed through the HostPort mgmt1 IP
API key dynamically created and configured at Fabric install
VM can retrieve key by an HTTP request that only works on HostPort mgmt1 IP
TODO: create a decorator to handle that and apply it to some other call (like set port up/down).
Return: model.device model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime vm disk list 

```
runtime vm disk list [-h] <DEVICE>
```

Return: list[dict]
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm export 

```
runtime vm export [-h] [--overwrite] [--no-overwrite] [--interactive]
[--no-interactive] [--diff] [--no-diff] [--refresh] [--no-refresh] [--switch]
[--no-switch] <DEVICE> <NAME>
```

Return: task.task model if not ‘interactive’
Positional arguments:
DEVICE{Vm}
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)
--interactive
(default)
--no-interactive
--diff
--no-diff
(default)
--refresh
(default)
--no-refresh
--switch
--no-switch
(default)

#### runtime vm install 

```
runtime vm install [-h] [--power-on] [--no-power-on] [--license]
[--no-license] [--configuration] [--no-configuration] [--post-boot]
[--no-post-boot] [--timeout TIMEOUT] <DEVICE>
```

Install a clean device.
Clone a device “model” object to “runtime” object, download, extract, spawn the instance and power
it on if necessary. Preparations are also performed. The existing device instance and “runtime” DB
object are uninstalled and destroyed first.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--power-on
do not power on (default)
--no-power-on
do not power on
--license
install the license or not (default)
--no-license
install the license or not
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not
--post-boot
do post boot preparation (default)
--no-post-boot
do post boot preparation
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime vm license alternate install 

```
runtime vm license alternate install [-h] [--reinstall] [--no-reinstall]
[--refresh] [--no-refresh] [--wait WAIT] <DEVICE> <LICENSE>
```

Install the specified device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Vm}
LICENSE{License}
Use this specific license
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, None default wait

#### runtime vm license install 

```
runtime vm license install [-h] [--reinstall] [--no-reinstall] [--refresh]
[--no-refresh] [--wait WAIT] <DEVICE>
```

Install the default device’s license.
return:
0 if license installed, already installed or no license to install or license not waited, 2 if license if
missing, 3 if no mgmt port to install license
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--reinstall
--no-reinstall
(default)
--refresh
(default)
--no-refresh
--wait WAIT{int}
wait timeout for license validation, 0 wait forever, unspecified default wait

#### runtime vm license wait 

```
runtime vm license wait [-h] [--timeout TIMEOUT] <DEVICE>
```

Waiting for device license to be validated.
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime vm list 

```
runtime vm list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of vm]
[--related-fields [RELATED_FIELDS ...]]
```

List all “runtime” VMs objects.
Return: (list[runtime.vm]|page[runtime.vm])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of vm{int}
Get page of given vm ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime vm port detail 

```
runtime vm port detail [-h] [--related-fields [RELATED_FIELDS ...]] <DEVICE>
<PORT>
```

Show port detail.
Return: model.port model
Positional arguments:
DEVICE{Vm}
PORT{Port}
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime vm port list 

```
runtime vm port list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of ID]
[--related-fields [RELATED_FIELDS ...]] <DEVICE>
```

List device instance ports.
Return: (list[model.port]|page[model.port])
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of ID{int}
Get page of given ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### runtime vm power-off 

```
runtime vm power-off [-h] <DEVICE>
```

Power off a device instance, data may be lost and disk corrupted.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm power-on 

```
runtime vm power-on [-h] [--configuration] [--no-configuration] [--license]
[--no-license] [--post-boot] [--no-post-boot] [--timeout TIMEOUT] <DEVICE>
```

Power-on the device instance and perform post boot preparation.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--configuration
restore configuration or not (default)
--no-configuration
restore configuration or not
--license
install the license or not (default)
--no-license
install the license or not
--post-boot
(default)
--no-post-boot
--timeout TIMEOUT{int}
inactivity timeout in second to abort

#### runtime vm shutdown 

```
runtime vm shutdown [-h] [--timeout TIMEOUT] [--power-off] [--no-power-off]
<DEVICE>
```

Shutdown a device. You can force a power off if shutdown didn’t complete before timeout.
return:
0 if shutdown complete in time or no timeout, 1 if forced to power off and 2 if shutdown didn’t
complete in time
Return: task.task model
Result: ShellCode
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
timeout in seconds before aborting or forcing power off
Default: 30 .
--power-off
power off if shutdown doesn’t complete before timeout is reached
--no-power-off
power off if shutdown doesn’t complete before timeout is reached (default)

#### runtime vm status 

```
runtime vm status [-h] <DEVICE>
```

Return the device instance status.
Return: DeviceStatus
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm synchronize 

```
runtime vm synchronize [-h] <DEVICE>
```

Synchronize the “runtime” device object and instance with the “model” object if possible.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit

#### runtime vm uninstall 

```
runtime vm uninstall [-h] [--delete] [--no-delete] <DEVICE>
```

Uninstall the device and delete (by default) the object from the “runtime” environment DB.
Return: task.task model
Positional arguments:
DEVICE{Vm}
Optional arguments:
--help, -h
show this help message and exit
--delete
delete or not the object (default)
--no-delete
delete or not the object

# SYSTEM

## General options

```
system [-h]
[{certificate,interfaces,monitoring,execute,mgmt,information,version,license,
```

Positional arguments:
[{certificate,interfaces,monitoring,execute,mgmt,information,version,license,disclaimer,db,openapi,prefer
certificate
Manage certificates.
interfaces
Fabric Studio interfaces.
monitoring
Monitoring.
execute
Execute general system commands.
mgmt
Management interface.
information
System detailed information.
version
Get product version.
license
Manage local licenses and server license.
disclaimer
Show disclaimer.
db
openapi
preferences
security
template
upgrade
repository
support
diagnose
hostname
forticloud
firewall
account
user
webserver
debug
expert
kernel
samba
log
disk
oauth2
parameter
ot
Optional arguments:
--help, -h
show this help message and exit

### system account 

```
system account [-h]
[{register,refresh,unregister,get,ssh,password,permissions}]
```

Positional arguments:
[{register,refresh,unregister,get,ssh,password,permissions}]
register
Register the Fabric Studio on the registration server.
refresh
Refresh the Fabric Studio registration.
unregister
Unregister the Fabric Studio.
get
Get registration user information.
ssh
password
permissions
Optional arguments:
--help, -h
show this help message and exit

#### system account get 

```
system account get [-h]
```

Get registration user information.
Return: users.userprofile model
Optional arguments:
--help, -h
show this help message and exit

#### system account password change 

```
system account password change [-h]
```

Change current user password.
Return: auth.user model
Optional arguments:
--help, -h
show this help message and exit

#### system account permissions list 

```
system account permissions list [-h] [--inactive] [--no-inactive]
```

Return current user permissions list.
Return: tuple
Optional arguments:
--help, -h
show this help message and exit
--inactive
--no-inactive
(default)

#### system account refresh 

```
system account refresh [-h] [--interactive] [--no-interactive] [--force]
[--no-force]
```

Refresh the Fabric Studio registration.
This command is usefull when new permissions are added on the registration server.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--force
--no-force
(default)

#### system account register 

```
system account register [-h] [--interactive] [--no-interactive] <MODE>
<IDENTITY> [<PASSWORD>]
```

Register the Fabric Studio on the registration server.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
MODE{str} ('fndn', 'token')
IDENTITY{str}
PASSWORD{str}
cleartext password
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system account ssh keys add 

```
system account ssh keys add [-h] <KEY>
```

Add a public key to the authorized keys.
Return: str
Positional arguments:
KEY{str}
Optional arguments:
--help, -h
show this help message and exit

#### system account ssh keys del 

```
system account ssh keys del [-h] <KEY>
```

Delete all keys matching key, key can be:
the full public key
the fingerprint
the comment
Return: list[str]
Positional arguments:
KEY{str}
Optional arguments:
--help, -h
show this help message and exit

#### system account ssh keys list 

```
system account ssh keys list [-h]
```

Show all keys.
Return: typing.List[str]
Optional arguments:
--help, -h
show this help message and exit

#### system account unregister 

```
system account unregister [-h] [--interactive] [--no-interactive]
```

Unregister the Fabric Studio.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

### system certificate 

```
system certificate [-h] [{local}]
```

Manage certificates.
Positional arguments:
[{local}]
local
Manage local certificates.
Optional arguments:
--help, -h
show this help message and exit

#### system certificate local ca delete 

```
system certificate local ca delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <cacertificate>
```

Delete ca certificate.
Return: certificates.cacertificate model
Positional arguments:
cacertificate{CACertificate}
ID of the cacertificate
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system certificate local ca detail 

```
system certificate local ca detail [-h]
[--related-fields [RELATED_FIELDS ...]] <cacertificate>
```

Detail view of ca certificate.
Return: certificates.cacertificate model
Positional arguments:
cacertificate{CACertificate}
ID of the cacertificate
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system certificate local ca import 

```
system certificate local ca import [-h] <PEM> [<NAME>]
```

Import a CA certificate.
Positional arguments:
PEM{Path}
A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST
NAME{str}
Optional arguments:
--help, -h
show this help message and exit

#### system certificate local ca list 

```
system certificate local ca list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of cacertificate]
[--related-fields [RELATED_FIELDS ...]]
```

List ca certificates.
Return: (list[certificates.cacertificate]|page[certificates.cacertificate])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of cacertificate{int}
Get page of given cacertificate ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system db 

```
system db [-h] [{schema,devices}]
```

Positional arguments:
[{schema,devices}]
schema
devices
Optional arguments:
--help, -h
show this help message and exit

#### system db devices list 

```
system db devices list [-h]
```

Supported devices.
Only list native and device by available firmware.
Return: list[class.devicetype]
Optional arguments:
--help, -h
show this help message and exit

#### system db schema detail 

```
system db schema detail [-h] <MODEL>
```

Dump model schema.
Return: dict
Positional arguments:
MODEL{str}
Optional arguments:
--help, -h
show this help message and exit

#### system db schema list 

```
system db schema list [-h]
```

List models.
Return: list[str]
Optional arguments:
--help, -h
show this help message and exit

### system debug 

```
system debug [-h] [{kernel}]
```

Positional arguments:
[{kernel}]
kernel
Optional arguments:
--help, -h
show this help message and exit

#### system debug kernel printk get 

```
system debug kernel printk get [-h]
```

Return current kernel printk levels.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system debug kernel printk set 

```
system debug kernel printk set [-h] <CURRENT> <DEFAULT> <MINIMUM>
<BOOT_TIME_DEFAULT>
```

Change the kernel printk levels.
The new value is persistant on reboot.
Positional arguments:
CURRENT{int}
DEFAULT{int}
MINIMUM{int}
BOOT_TIME_DEFAULT{int}
Optional arguments:
--help, -h
show this help message and exit

### system diagnose 

```
system diagnose [-h]
[{disks,vm,interfaces,nogroup,tcpdump,htop,boot,date,route,sysctl,firewall,ha
```

Positional arguments:
[{disks,vm,interfaces,nogroup,tcpdump,htop,boot,date,route,sysctl,firewall,hardware,lsof,nameserver,mg
disks
Show disks usage.
vm
interfaces
Show system interfaces informations.
nogroup
Any interfaces in “nogroup” group.
tcpdump
Run tcpdump on given system port.
htop
boot
Print or control the kernel ring buffer.
date
Return current UTC datetime as ISO 8601 string.
route
sysctl
firewall
hardware
lsof
nameserver
mgmt
dpkg
ss
grub
Show all grub files configuration.
user
service
upgrade
db
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose boot 

```
system diagnose boot [-h] [<OPTIONS> ...]
```

Print or control the kernel ring buffer.
See man dmesg  on a linux system for options.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose date 

```
system diagnose date [-h]
```

Return current UTC datetime as ISO 8601 string.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose db engine status 

```
system diagnose db engine status [-h]
```

Show database engine status.
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose disks 

```
system diagnose disks [-h]
```

Show disks usage.
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose dpkg info 

```
system diagnose dpkg info [-h] <NAME>
```

Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose dpkg list 

```
system diagnose dpkg list [-h] [--group GROUP]
```

Return: list[dict]
Optional arguments:
--help, -h
show this help message and exit
--group{str} ('ftnt', 'os', 'all')
Default: ftnt .

#### system diagnose firewall 

```
system diagnose firewall [-h] [<OPTIONS> ...]
```

Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose grub 

```
system diagnose grub [-h]
```

Show all grub files configuration.
Return: dict
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose hardware disk performance write 

```
system diagnose hardware disk performance write [-h] [<SIZE>]
```

Perform simple disk write performance test.
Positional arguments:
SIZE{BytesSize}
Default: default: 8589934592 .
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose hardware lscpu 

```
system diagnose hardware lscpu [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system diagnose hardware lsmem 

```
system diagnose hardware lsmem [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system diagnose hardware lspci 

```
system diagnose hardware lspci [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system diagnose hardware lsusb 

```
system diagnose hardware lsusb [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system diagnose htop 

```
system diagnose htop [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system diagnose interfaces 

```
system diagnose interfaces [-h] [<IFNAME>]
```

Show system interfaces informations.
Return: None | dict[str, typing.Any]
Positional arguments:
IFNAME{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose lsof 

```
system diagnose lsof [-h] [<ARGS> ...]
```

Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose mgmt dhcp 

```
system diagnose mgmt dhcp [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose mgmt static 

```
system diagnose mgmt static [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose nameserver 

```
system diagnose nameserver [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose nogroup 

```
system diagnose nogroup [-h]
```

Any interfaces in “nogroup” group.
Return: list[class.systeminterface]
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose route 

```
system diagnose route [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose service status 

```
system diagnose service status [-h] <SERVICE>
```

Positional arguments:
SERVICE{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose ss 

```
system diagnose ss [-h] [<ARGS> ...]
```

Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose sysctl 

```
system diagnose sysctl [-h]
```

Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose tcpdump 

```
system diagnose tcpdump [-h] <PORT> [<ARGS> ...]
```

Run tcpdump on given system port.
For port when using mgmt1, port1, … that are OpenVSwitch internal ports, the command does an
automatic conversion to use the real interface name (ex: ens4). If you really want to look to an
OpenVSwitch internal port use the “^” prefix to bypass the automatic conversion (ex: ^mgmt1).
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
PORT{str}
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose upgrade available 

```
system diagnose upgrade available [-h] [--channel CHANNEL] [<CURRENT_VERSION>
```

Return: dict
Positional arguments:
CURRENT_VERSION{Tag}
Optional arguments:
--help, -h
show this help message and exit
--channel CHANNEL{str}

#### system diagnose user cwd 

```
system diagnose user cwd [-h]
```

Return current working directory.
Return: Path
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose user ip 

```
system diagnose user ip [-h]
```

Return current user connection IP if it can be determined else “MISSING”.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system diagnose vm factory 

```
system diagnose vm factory [-h]
```

List known VM type.
Return: list[type]
Optional arguments:
--help, -h
show this help message and exit

### system disclaimer 

```
system disclaimer [-h]
```

Show disclaimer.
Return: str
Optional arguments:
--help, -h
show this help message and exit

### system disk 

```
system disk [-h] [{detail,extend,system,data}]
```

Positional arguments:
[{detail,extend,system,data}]
detail
Disk details.
extend
Extend VG.
system
data
Optional arguments:
--help, -h
show this help message and exit

#### system disk data extend 

```
system disk data extend [-h] <SIZE>
```

Extend the data disk.
If size is 0, use all the free space.
Positional arguments:
SIZE{BytesSize}
Optional arguments:
--help, -h
show this help message and exit

#### system disk detail 

```
system disk detail [-h]
```

Disk details.
Return: dict
Optional arguments:
--help, -h
show this help message and exit

#### system disk extend 

```
system disk extend [-h]
```

Extend VG.
Optional arguments:
--help, -h
show this help message and exit

#### system disk system extend 

```
system disk system extend [-h] <SIZE>
```

Extend the system partition.
If size is 0, use all the free space.
Positional arguments:
SIZE{BytesSize}
Optional arguments:
--help, -h
show this help message and exit

#### system disk system retry 

```
system disk system retry [-h]
```

Complete system partition resizing.
This is a last chance command if normal resize process has failed.
Optional arguments:
--help, -h
show this help message and exit

### system execute 

```
system execute [-h]
[{conntrack,openssl,reboot,shutdown,login,ssh,ping,resolve,factoryreset,date,
```

Execute general system commands.
Positional arguments:
[{conntrack,openssl,reboot,shutdown,login,ssh,ping,resolve,factoryreset,date,log,apt,service,upgrade}]
conntrack
openssl
reboot
Reboot the system.
shutdown
Shutdown the system.
login
Run login session.
ssh
ping
Send ICMP ECHO_REQUEST to network hosts.
resolve
DNS lookup utility.
factoryreset
Reset system to factory settings and reboot.
date
log
apt
service
upgrade
Upgrade the product.
Optional arguments:
--help, -h
show this help message and exit

#### system execute apt clean 

```
system execute apt clean [-h]
```

Clean apt cache.
Optional arguments:
--help, -h
show this help message and exit

#### system execute conntrack 

```
system execute conntrack [-h] [<OPTIONS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute date sync 

```
system execute date sync [-h]
```

Force date synchronization.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit

#### system execute factoryreset 

```
system execute factoryreset [-h] [--interactive] [--no-interactive] [--reboot
[--no-reboot]
```

Reset system to factory settings and reboot.
Home repository is cleared.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--reboot
(default)
--no-reboot

#### system execute log system purge 

```
system execute log system purge [-h] [--vacuum-time VACUUM_TIME]
```

Remove old system logs files including systemd journal older than vacuum_time.
Optional arguments:
--help, -h
show this help message and exit
--vacuum-time VACUUM_TIME{str}
Default: 1month .

#### system execute log system rotate 

```
system execute log system rotate [-h] [--force] [--no-force] [--verbose]
[--no-verbose] [--dry-run] [--no-dry-run]
```

Perform log rotation (logrotate and journalctl).
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)
--verbose
(default)
--no-verbose
--dry-run
--no-dry-run
(default)

#### system execute login 

```
system execute login [-h]
```

Run login session.
Optional arguments:
--help, -h
show this help message and exit

#### system execute openssl 

```
system execute openssl [-h] [<OPTIONS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute ping 

```
system execute ping [-h] <DESTINATION> [<OPTIONS> ...]
```

Send ICMP ECHO_REQUEST to network hosts.
See man ping  on a linux system for options.``
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
DESTINATION{str}
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute reboot 

```
system execute reboot [-h] [--interactive] [--no-interactive]
```

Reboot the system.
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system execute resolve 

```
system execute resolve [-h] <NAME> [<OPTIONS> ...]
```

DNS lookup utility.
See man dig  on a linux system for options.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
NAME{str}
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute service restart 

```
system execute service restart [-h] [<SERVICE> ...]
```

Restart one or more services.
Positional arguments:
SERVICE{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute shutdown 

```
system execute shutdown [-h] [--interactive] [--no-interactive]
```

Shutdown the system.
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system execute ssh 

```
system execute ssh [-h] [<OPTIONS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system execute upgrade 

```
system execute upgrade [-h] [--channel CHANNEL] [--version VERSION]
[--upgrade-script-source UPGRADE_SCRIPT_SOURCE]
[--upgrade-repository-source UPGRADE_REPOSITORY_SOURCE] [--force] [--no-force
[--interactive] [--no-interactive] [--dangerous] [--no-dangerous]
```

Upgrade the product.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--channel{str}
Upgrade channel, conflicts with “version” option
--version VERSION{Tag}
Specific version to upgrade to, conflict with channel option
--upgrade-script-source UPGRADE_SCRIPT_SOURCE{UrlInfo}
Upgrade script source, for expert only
--upgrade-repository-source UPGRADE_REPOSITORY_SOURCE{UrlInfo}
Package repository source, for expert only
--force
Force the upgrade
--no-force
Force the upgrade (default)
--interactive
Interactive upgrade or not (default)
--no-interactive
Interactive upgrade or not
--dangerous
Dangerous upgrade with Fabric running and no reboot
--no-dangerous
Dangerous upgrade with Fabric running and no reboot (default)

### system expert 

```
system expert [-h]
[{server,django,debug,editor,virsh,ovs-vsctl,ovs-ofctl,ip,interface}]
```

Positional arguments:
[{server,django,debug,editor,virsh,ovs-vsctl,ovs-ofctl,ip,interface}]
server
django
debug
editor
virsh
Start “virsh” tool.
ovs-vsctl
ovs-ofctl
ip
interface
Optional arguments:
--help, -h
show this help message and exit

#### system expert debug license alive 

```
system expert debug license alive [-h]
```

Notify license server we are still alive.
Optional arguments:
--help, -h
show this help message and exit

#### system expert debug license assets breakpoint 

```
system expert debug license assets breakpoint [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system expert debug license assets data 

```
system expert debug license assets data [-h] [--serialNumber SERIALNUMBER]
```

Return: list[dict]
Optional arguments:
--help, -h
show this help message and exit
--serialNumber SERIALNUMBER{str}

#### system expert debug license legacy 

```
system expert debug license legacy [-h] <ACTION> <FABRIC>
```

All vms of the Fabric at once.
Positional arguments:
ACTION{str} ('provision', 'register')
FABRIC{Fabric}
Optional arguments:
--help, -h
show this help message and exit

#### system expert debug license release all 

```
system expert debug license release all [-h]
```

Release all licenses.
Optional arguments:
--help, -h
show this help message and exit

#### system expert debug license release dangling 

```
system expert debug license release dangling [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system expert django manage 

```
system expert django manage [-h] [<COMMANDS> ...]
```

Execute Django manage command.
Positional arguments:
COMMANDS{*}
Optional arguments:
--help, -h
show this help message and exit

#### system expert editor virsh 

```
system expert editor virsh [-h]
```

Remove selected editor fort virsh.
Optional arguments:
--help, -h
show this help message and exit

#### system expert interface link 

```
system expert interface link [-h] <NAME> <SYSNAME>
```

Link a Fabric Studio interface to a specific system interface.
Positional arguments:
NAME{str}
SYSNAME{str}
Optional arguments:
--help, -h
show this help message and exit

#### system expert interface unlink 

```
system expert interface unlink [-h] <NAME>
```

Unlink a Fabric Studio interface from the system interface.
Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit

#### system expert ip 

```
system expert ip [-h] [<OPTIONS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
OPTIONS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system expert ovs-ofctl 

```
system expert ovs-ofctl [-h] [<ARGS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system expert ovs-vsctl 

```
system expert ovs-vsctl [-h] [<ARGS> ...]
```

Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

#### system expert server zone create 

```
system expert server zone create [-h] [--related-fields [RELATED_FIELDS ...]]
<serverzone>
```

Create server zone.
Return: repository.serverzone model
Positional arguments:
serverzone{ServerZone}
serverzone object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system expert server zone delete 

```
system expert server zone delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <serverzone>
```

Delete server zone.
Return: repository.serverzone model
Positional arguments:
serverzone{ServerZone}
ID of the serverzone
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system expert server zone detail 

```
system expert server zone detail [-h] [--related-fields [RELATED_FIELDS ...]]
<serverzone>
```

Detail view of server zone.
Return: repository.serverzone model
Positional arguments:
serverzone{ServerZone}
ID of the serverzone
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system expert server zone list 

```
system expert server zone list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of serverzone]
[--related-fields [RELATED_FIELDS ...]]
```

List server zones.
Return: (list[repository.serverzone]|page[repository.serverzone])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of serverzone{int}
Get page of given serverzone ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system expert server zone update 

```
system expert server zone update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <serverzone> <OBJECT>
```

Update server zone.
Return: repository.serverzone model
Positional arguments:
serverzone{ServerZone}
ID of the serverzone
OBJECT{ServerZone}
serverzone object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system expert virsh 

```
system expert virsh [-h] [<ARGS> ...]
```

Start “virsh” tool.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ARGS{*}{str}
Optional arguments:
--help, -h
show this help message and exit

### system firewall 

```
system firewall [-h] [{address}]
```

Positional arguments:
[{address}]
address
Optional arguments:
--help, -h
show this help message and exit

#### system firewall address create 

```
system firewall address create [-h] [--force] [--no-force]
[--related-fields [RELATED_FIELDS ...]] <firewalladdress>
```

Create firewall address.
Return: system.firewalladdress model
Positional arguments:
firewalladdress{FirewallAddress}
firewalladdress object
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system firewall address delete 

```
system firewall address delete [-h] [--force] [--no-force] [--interactive]
[--no-interactive] [--yes] [--no-yes] <firewalladdress>
```

Delete firewall address.
Return: system.firewalladdress model
Positional arguments:
firewalladdress{FirewallAddress}
ID of the firewalladdress
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system firewall address detail 

```
system firewall address detail [-h] [--related-fields [RELATED_FIELDS ...]]
<firewalladdress>
```

Detail view of firewall address.
Return: system.firewalladdress model
Positional arguments:
firewalladdress{FirewallAddress}
ID of the firewalladdress
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system firewall address flush 

```
system firewall address flush [-h]
```

Flush all firewall addresses.
Optional arguments:
--help, -h
show this help message and exit

#### system firewall address list 

```
system firewall address list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of firewalladdress]
[--related-fields [RELATED_FIELDS ...]]
```

List firewall addresss.
Return: (list[system.firewalladdress]|page[system.firewalladdress])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of firewalladdress{int}
Get page of given firewalladdress ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system firewall address update 

```
system firewall address update [-h] [--force] [--no-force]
[--update-fields UPDATE_FIELDS] [--related-fields [RELATED_FIELDS ...]]
<firewalladdress> <OBJECT>
```

Update firewall address.
Return: system.firewalladdress model
Positional arguments:
firewalladdress{FirewallAddress}
ID of the firewalladdress
OBJECT{FirewallAddress}
firewalladdress object
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system forticloud 

```
system forticloud [-h] [{account}]
```

Positional arguments:
[{account}]
account
Optional arguments:
--help, -h
show this help message and exit

#### system forticloud account disclaimer 

```
system forticloud account disclaimer [-h]
```

Return the FortiCloud API usage disclaimer.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system forticloud account get 

```
system forticloud account get [-h]
```

Get FortiCloud account registration information.
Optional arguments:
--help, -h
show this help message and exit

#### system forticloud account reset 

```
system forticloud account reset [-h] [--interactive] [--no-interactive]
```

Clear FortiCloud API user credentials.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system forticloud account set 

```
system forticloud account set [-h] [--password PASSWORD] [--interactive]
[--no-interactive] [--yes] [--no-yes] [--accountId ACCOUNTID] [--refresh]
[--no-refresh] <APIID>
```

Set FortiCloud API user credentials.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
APIID{str}
Optional arguments:
--help, -h
show this help message and exit
--password PASSWORD{str}
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)
--accountId ACCOUNTID{int}
--refresh
(default)
--no-refresh

#### system forticloud account token get 

```
system forticloud account token get [-h]
```

Return token refresh time.
Optional arguments:
--help, -h
show this help message and exit

#### system forticloud account token renew 

```
system forticloud account token renew [-h] [--interactive] [--no-interactive]
[--force] [--no-force]
```

Renew the API access token.
The token is unique for all processes/threads that requires to do API call. The token is stored in a
JSON file along expiration information so the token can be reused between multiple processes and
only refreshed one time when required (we use the apilock lock to handle concurent access/update.
As we always load the JSON file, any process that may have renew the token (ex: by changing
credential) should be automatically aware of the new token.
If the token is not globally handled, when refresh time is reached, process 1 renews the token and do
a successfull call, then process 2 arrives, it also renews the token because for it it has expired and
not been renewed, breaking the one from process 1 that is supposed to be valid for a long time.
Return: runtime.runtimetask model if not ‘interactive’
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--force
--no-force
(default)

#### system forticloud account upload 

```
system forticloud account upload [-h] [--accountId ACCOUNTID] [--interactive]
[--no-interactive] [--yes] [--no-yes] [--password PASSWORD] <FILE>
```

Configure FortiCloud credentials from the API credentials file generated by
https://support.fortinet.com/ site.
Positional arguments:
FILE{Path}
Optional arguments:
--help, -h
show this help message and exit
--accountId ACCOUNTID{int}
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)
--password PASSWORD{str}

### system hostname 

```
system hostname [-h] [{set,get}]
```

Positional arguments:
[{set,get}]
set
Set system hostname.
get
Get system hostname.
Optional arguments:
--help, -h
show this help message and exit

#### system hostname get 

```
system hostname get [-h]
```

Get system hostname.
Optional arguments:
--help, -h
show this help message and exit

#### system hostname set 

```
system hostname set [-h] <HOSTNAME>
```

Set system hostname.
Positional arguments:
HOSTNAME{str}
Optional arguments:
--help, -h
show this help message and exit

### system information 

```
system information [-h]
```

System detailed information.
Return: SystemInformation
Optional arguments:
--help, -h
show this help message and exit

### system interfaces 

```
system interfaces [-h] [{list,cleanup,sync,mgmt,ports}]
```

Fabric Studio interfaces.
Positional arguments:
[{list,cleanup,sync,mgmt,ports}]
list
List ports.
cleanup
Delete missing interfaces not used.
sync
Sync logical system ports with physical ports.
mgmt
Management interface.
ports
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces cleanup 

```
system interfaces cleanup [-h]
```

Delete missing interfaces not used.
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces list 

```
system interfaces list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of port]
[--related-fields [RELATED_FIELDS ...]]
```

List ports.
Return: (list[system.port]|page[system.port])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of port{int}
Get page of given port ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system interfaces mgmt configure 

```
system interfaces mgmt configure [-h]
```

Interactive management interface configuration.
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces mgmt get 

```
system interfaces mgmt get [-h]
```

Get management interface configuration.
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces mgmt public-address 

```
system interfaces mgmt public-address [-h] [--ipv IPV] [--operator OPERATOR]
[--ns NS]
```

Return public address by questionning opendns (default), google or cloudfare.
Return: str
Optional arguments:
--help, -h
show this help message and exit
--ipv{int} (4, 6)
Default: 4 .
--operator{str} ('cloudfare', 'google', 'opendns')
Default: opendns .
--ns NS{int}
Default: 1 .

#### system interfaces mgmt restart 

```
system interfaces mgmt restart [-h] [--uninstall] [--no-uninstall]
```

Optional arguments:
--help, -h
show this help message and exit
--uninstall
--no-uninstall
(default)

#### system interfaces mgmt set 

```
system interfaces mgmt set [-h] <OBJECT>
```

Configure mangement interface.
Positional arguments:
OBJECT{SystemInterfaceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces mgmt show 

```
system interfaces mgmt show [-h]
```

Show system interface configuration.
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces ports down 

```
system interfaces ports down [-h]
```

Down all system ports except the management port.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces ports uninstall 

```
system interfaces ports uninstall [-h]
```

Optional arguments:
--help, -h
show this help message and exit

#### system interfaces ports up 

```
system interfaces ports up [-h]
```

Up all system ports except the management port.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit

#### system interfaces sync 

```
system interfaces sync [-h]
```

Sync logical system ports with physical ports.
Optional arguments:
--help, -h
show this help message and exit

### system kernel 

```
system kernel [-h] [{hugepages,grub}]
```

Positional arguments:
[{hugepages,grub}]
hugepages
grub
Optional arguments:
--help, -h
show this help message and exit

#### system kernel grub flush 

```
system kernel grub flush [-h]
```

Flush all custom grub configruation.
Optional arguments:
--help, -h
show this help message and exit

#### system kernel hugepages free 

```
system kernel hugepages free [-h]
```

Return free hugepages count.
Return: int
Optional arguments:
--help, -h
show this help message and exit

#### system kernel hugepages get 

```
system kernel hugepages get [-h]
```

Return configured hugepages count.
Return: int
Optional arguments:
--help, -h
show this help message and exit

#### system kernel hugepages set 

```
system kernel hugepages set [-h] [--force] [--no-force] <COUNT>
```

Define hugepages count to reserve on next boot.
Positional arguments:
COUNT{int}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

### system license 

```
system license [-h]
[{list,detail,import,update,delete,release,server,client,flex,assets}]
```

Manage local licenses and server license.
Positional arguments:
[{list,detail,import,update,delete,release,server,client,flex,assets}]
list
List VM licenses.
detail
Detail view of a VM license.
import
Upload a VM licence.
update
Update VM licenses meta information.
delete
Delete VM licenses.
release
Release a license.
server
Manage license server service.
client
Manage client license requests.
flex
Manage FortiCloud FlexVM licenses.
assets
Manage FortiCloud license assets (experimental).
Optional arguments:
--help, -h
show this help message and exit

#### system license assets api flow info 

```
system license assets api flow info [-h]
```

Return flow of calls information.
The flow information tracks the calls to respect the API calls contraints (see official assets API
documentation.).
Return: dict
Optional arguments:
--help, -h
show this help message and exit

#### system license assets api license download 

```
system license assets api license download [-h] <SERIALNUMBER>
```

Download an assets license LIC file.
Positional arguments:
SERIALNUMBER{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license assets api product detail 

```
system license assets api product detail [-h] <SERIALNUMBER>
```

An assets product detail (see official assets API documentation).
Positional arguments:
SERIALNUMBER{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license assets api product list 

```
system license assets api product list [-h] <SERIALNUMBER>
```

List assets products matching serialNumber (see official assets API documentation).
Positional arguments:
SERIALNUMBER{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license assets api product refresh 

```
system license assets api product refresh [-h] [--serialNumber SERIALNUMBER]
```

Refresh assets products information.
Optional arguments:
--help, -h
show this help message and exit
--serialNumber SERIALNUMBER{str}

#### system license assets fp-type create 

```
system license assets fp-type create [-h]
[--related-fields [RELATED_FIELDS ...]] <fptype>
```

Create FPType.
Return: assets.fptype model
Positional arguments:
fptype{FPType}
fptype object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets fp-type delete 

```
system license assets fp-type delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <fptype>
```

Delete FPType.
Return: assets.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system license assets fp-type detail 

```
system license assets fp-type detail [-h]
[--related-fields [RELATED_FIELDS ...]] <fptype>
```

Detail view of FPType.
Return: assets.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets fp-type list 

```
system license assets fp-type list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of fptype]
[--related-fields [RELATED_FIELDS ...]]
```

List FPTypes.
Return: (list[assets.fptype]|page[assets.fptype])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of fptype{int}
Get page of given fptype ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets fp-type update 

```
system license assets fp-type update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <fptype> <OBJECT>
```

Update FPType.
Return: assets.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
OBJECT{FPType}
fptype object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets license detail 

```
system license assets license detail [-h]
[--related-fields [RELATED_FIELDS ...]] <license>
```

Detail view of license.
Return: assets.license model
Positional arguments:
license{License}
ID of the license
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets license download 

```
system license assets license download [-h] [--save] [--no-save]
[--serial-number SERIAL_NUMBER]
```

Download .lic files from the FortiCloud server.
To download only a specific license use “–serial-number <SERIAL_NUMBER>”.
Use “–save” to save licenses as .lic  file under home repository/ assets .
Optional arguments:
--help, -h
show this help message and exit
--save
--no-save
(default)
--serial-number SERIAL_NUMBER{str}

#### system license assets license list 

```
system license assets license list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of license]
[--related-fields [RELATED_FIELDS ...]]
```

List licenses.
Return: (list[assets.license]|page[assets.license])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of license{int}
Get page of given license ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license assets license refresh 

```
system license assets license refresh [-h] [--serial-number SERIAL_NUMBER]
```

Download licenses information from the FortiCloud server.
To download only a specific license use “–serial-number <SERIAL_NUMBER>”.
Optional arguments:
--help, -h
show this help message and exit
--serial-number SERIAL_NUMBER{str}

#### system license client request group get 

```
system license client request group get [-h]
```

Get the license group.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system license client request group set 

```
system license client request group set [-h] <GROUP>
```

Set the license group.
Positional arguments:
GROUP{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license client request supported get 

```
system license client request supported get [-h]
```

Get the supported license classes to request licenses.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system license client request supported set 

```
system license client request supported set [-h] [<CLASS> ...]
```

Set the supported license classes to request licenses.
LIC:
accept .lic file licenses
FLEX:
accept FortiFlex licenses
Positional arguments:
CLASS{*}{str} ('LIC', 'FLEX')
Optional arguments:
--help, -h
show this help message and exit

#### system license client server disable 

```
system license client server disable [-h]
```

Disable use of remote license server.
Optional arguments:
--help, -h
show this help message and exit

#### system license client server enable 

```
system license client server enable [-h]
```

Enable use of remote license server.
Optional arguments:
--help, -h
show this help message and exit

#### system license client server get 

```
system license client server get [-h]
```

Return remote license server use.
Return: bool
Optional arguments:
--help, -h
show this help message and exit

#### system license client server legacy disable 

```
system license client server legacy disable [-h]
```

Set remote license server is NOT legacy.
Optional arguments:
--help, -h
show this help message and exit

#### system license client server legacy enable 

```
system license client server legacy enable [-h]
```

Set remote license server is legacy.
Optional arguments:
--help, -h
show this help message and exit

#### system license client server legacy get 

```
system license client server legacy get [-h]
```

Return remote license server legacy flag.
Return: bool
Optional arguments:
--help, -h
show this help message and exit

#### system license client server url get 

```
system license client server url get [-h]
```

Return the remote license server URL.
Return: UrlInfo
Optional arguments:
--help, -h
show this help message and exit

#### system license client server url set 

```
system license client server url set [-h] <SERVER>
```

Set the remote license server URL.
Set to empty value to disable license server.
Positional arguments:
SERVER{UrlInfo}
Optional arguments:
--help, -h
show this help message and exit

#### system license delete 

```
system license delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <license>
```

Delete VM licenses.
Return: license.license model
Positional arguments:
license{License}
ID of the license
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system license detail 

```
system license detail [-h] [--related-fields [RELATED_FIELDS ...]] <license>
```

Detail view of a VM license.
Return: license.license model
Positional arguments:
license{License}
ID of the license
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex config create 

```
system license flex config create [-h] <NAME> <PRODUCTID> <PARAMETERS>
[<PROGRAMSERIALNUMBER>]
```

Create a configuration using Flex API syntax.
Positional arguments:
NAME{str}
PRODUCTID{int}
PARAMETERS{list}
PROGRAMSERIALNUMBER{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license flex config detail 

```
system license flex config detail [-h] [--related-fields [RELATED_FIELDS ...]
<config>
```

Detail view of config.
Return: flexvm.config model
Positional arguments:
config{Config}
ID of the config
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex config export 

```
system license flex config export [-h]
[--programSerialNumber PROGRAMSERIALNUMBER] [--accountId ACCOUNTID]
```

Export configs in native Flex format.
Return the “configs/list” native Flex API call result:

```
ssh admin@<ADDR1> -- --json system license flex config export > configs.json
```

Return: dict
Optional arguments:
--help, -h
show this help message and exit
--programSerialNumber PROGRAMSERIALNUMBER{str}
--accountId ACCOUNTID{int}
Default: 0 .

#### system license flex config import 

```
system license flex config import [-h] [--update] [--no-update] [--continue]
[--no-continue] <FILENAME>
```

Import configs as JSON in native Flex format to create or update them.
Import:

```
scp config.json admin@<ADDR2>:
ssh admin@<ADDR2> system licence flex config import configs.json
```

Positional arguments:
FILENAME{Path}
Optional arguments:
--help, -h
show this help message and exit
--update
(default)
--no-update
--continue
--no-continue
(default)

#### system license flex config list 

```
system license flex config list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of config]
[--related-fields [RELATED_FIELDS ...]]
```

List configs.
Return: (list[flexvm.config]|page[flexvm.config])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of config{int}
Get page of given config ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex config refresh 

```
system license flex config refresh [-h]
```

Refresh FortiFlex Config information for current FortiFlex API account.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit

#### system license flex debug post 

```
system license flex debug post [-h] [--json JSON] [--timeout TIMEOUT] [--lock
[--no-lock] <URL>
```

Do FortiCloud API HTTP POST with proper headers and validate the reply.
Return: dict
Positional arguments:
URL{Path}
Optional arguments:
--help, -h
show this help message and exit
--json JSON{dict}
--timeout TIMEOUT{int}
--lock
(default)
--no-lock

#### system license flex fp-type create 

```
system license flex fp-type create [-h]
[--related-fields [RELATED_FIELDS ...]] <fptype>
```

Create FPType.
Return: flexvm.fptype model
Positional arguments:
fptype{FPType}
fptype object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex fp-type delete 

```
system license flex fp-type delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <fptype>
```

Delete FPType.
Return: flexvm.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system license flex fp-type detail 

```
system license flex fp-type detail [-h]
[--related-fields [RELATED_FIELDS ...]] <fptype>
```

Detail view of FPType.
Return: flexvm.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex fp-type list 

```
system license flex fp-type list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of fptype]
[--related-fields [RELATED_FIELDS ...]]
```

List FPTypes.
Return: (list[flexvm.fptype]|page[flexvm.fptype])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of fptype{int}
Get page of given fptype ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex fp-type update 

```
system license flex fp-type update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <fptype> <OBJECT>
```

Update FPType.
Return: flexvm.fptype model
Positional arguments:
fptype{FPType}
ID of the fptype
OBJECT{FPType}
fptype object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex license detail 

```
system license flex license detail [-h]
[--related-fields [RELATED_FIELDS ...]] <license>
```

Detail view of license.
Return: flexvm.license model
Positional arguments:
license{License}
ID of the license
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex license list 

```
system license flex license list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of license]
[--related-fields [RELATED_FIELDS ...]]
```

List licenses.
Return: (list[flexvm.license]|page[flexvm.license])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of license{int}
Get page of given license ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex license reactivate all 

```
system license flex license reactivate all [-h] [--force] [--no-force]
```

To reactivate all known licenses.
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system license flex license reactivate license 

```
system license flex license reactivate license [-h] [--force] [--no-force]
<LICENSE>
```

To reactivate specific license.
Positional arguments:
LICENSE{License}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system license flex license refresh 

```
system license flex license refresh [-h] [--save] [--no-save]
[--serial-number SERIAL_NUMBER] [--select SELECT] [--interactive]
[--no-interactive] <TYPE>
```

Download and refresh licenses from the FortiFlex server.
Use “*” as type to refresh all supported types.
If BYOL mode is enabled, use “–select all” to retrieve all licenses.
If BYOL mode is disabled, use “–select known” to retrieve known licenses only.
When all licenses must be downloaded, confirmation is required, use “–no-interactive” to bypass it.
To download only a specific license use “–serial-number <SERIAL_NUMBER>”.
Use “–save” to save licenses as .flexvm  file under home repository/ flexvm .
Return: list[flexvm.license]
Positional arguments:
TYPE{str}
Optional arguments:
--help, -h
show this help message and exit
--save
--no-save
(default)
--serial-number SERIAL_NUMBER{str}
--select{str} ('known', 'all')
--interactive
(default)
--no-interactive

#### system license flex license stop all 

```
system license flex license stop all [-h] [--force] [--no-force]
```

To stop all known licenses.
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system license flex license stop license 

```
system license flex license stop license [-h] [--force] [--no-force] <LICENSE
```

To stop specific license.
Positional arguments:
LICENSE{License}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system license flex license token refresh 

```
system license flex license token refresh [-h] <FLEXVM>
```

Refresh a VM license token.
Return: str
Positional arguments:
FLEXVM{License}
Optional arguments:
--help, -h
show this help message and exit

#### system license flex license transfer 

```
system license flex license transfer [-h] [--targetConfigId TARGETCONFIGID]
<TARGETACCOUNTID> [<SERIALS> ...]
```

Transfer license(s) between two accounts.
Positional arguments:
TARGETACCOUNTID{int}
SERIALS{*}{str}
Optional arguments:
--help, -h
show this help message and exit
--targetConfigId TARGETCONFIGID{int}

#### system license flex pool clear 

```
system license flex pool clear [-h] <TYPE>
```

Disable pool for the device type.
Positional arguments:
TYPE{str}
Optional arguments:
--help, -h
show this help message and exit

#### system license flex pool detail 

```
system license flex pool detail [-h] [--related-fields [RELATED_FIELDS ...]]
<pool>
```

Detail view of pool.
Return: flexvm.pool model
Positional arguments:
pool{Pool}
ID of the pool
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex pool generate 

```
system license flex pool generate [-h] [--save] [--no-save] <POOL> <COUNT>
```

Generate new FortiFlex VM license in selected pool.
The count is the number of license to create. The count is sliced in auto max part. See official
FortiFlex API documentation for limitations and constraints.
Use “–save” to save licenses as .flexvm  file under local repository/ flexvm .
Return: list[flexvm.license]
Positional arguments:
POOL{Pool}
COUNT{int}
Optional arguments:
--help, -h
show this help message and exit
--save
--no-save
(default)

#### system license flex pool list 

```
system license flex pool list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of pool]
[--related-fields [RELATED_FIELDS ...]]
```

List pools.
Return: (list[flexvm.pool]|page[flexvm.pool])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of pool{int}
Get page of given pool ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex pool set 

```
system license flex pool set [-h] [--config CONFIG] [--refresh] [--no-refresh
<TYPE>
```

Enable config for the device type.
If the config is not specified, it must exist only one progam/config for the device type.
When uploading FortiFlex VM license, the corresponding pool is automatically enabled.
Positional arguments:
TYPE{str}
Optional arguments:
--help, -h
show this help message and exit
--config CONFIG{Config}
--refresh
--no-refresh
(default)

#### system license flex product detail 

```
system license flex product detail [-h]
[--related-fields [RELATED_FIELDS ...]] <producttype>
```

Detail view of product type.
Return: flexvm.producttype model
Positional arguments:
producttype{ProductType}
ID of the producttype
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex product list 

```
system license flex product list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of producttype]
[--related-fields [RELATED_FIELDS ...]]
```

List product types.
Return: (list[flexvm.producttype]|page[flexvm.producttype])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of producttype{int}
Get page of given producttype ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex product update 

```
system license flex product update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <producttype> <OBJECT>
```

Update product type.
Return: flexvm.producttype model
Positional arguments:
producttype{ProductType}
ID of the producttype
OBJECT{ProductType}
producttype object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex program detail 

```
system license flex program detail [-h]
[--related-fields [RELATED_FIELDS ...]] <program>
```

Detail view of program.
Return: flexvm.program model
Positional arguments:
program{Program}
ID of the program
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex program list 

```
system license flex program list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of program]
[--related-fields [RELATED_FIELDS ...]]
```

List programs.
Return: (list[flexvm.program]|page[flexvm.program])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of program{int}
Get page of given program ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license flex program refresh 

```
system license flex program refresh [-h]
```

Refresh FortiFlex Program information for current FortiFlex API account.
Optional arguments:
--help, -h
show this help message and exit

#### system license flex settings get 

```
system license flex settings get [-h]
```

Return license manager configuration for FortiFlex.
Return: FlexVMSettings
Optional arguments:
--help, -h
show this help message and exit

#### system license flex settings set 

```
system license flex settings set [-h] <SETTINGS>
```

Set license manager configuration for FortiFlex.
Return: FlexVMSettings
Positional arguments:
SETTINGS{FlexVMSettings}
Optional arguments:
--help, -h
show this help message and exit

#### system license import 

```
system license import [-h] [--erase-source] [--no-erase-source] <INPUT>
[<LICENSE>]
```

Upload a VM licence.
param erase_source:
erase the temporary source file once successfully imported.
Return: license.license model
Positional arguments:
INPUT{Path}
LICENSE{License}
Optional arguments:
--help, -h
show this help message and exit
--erase-source
(default)
--no-erase-source

#### system license list 

```
system license list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of license]
[--related-fields [RELATED_FIELDS ...]]
```

List VM licenses.
Return: (list[license.license]|page[license.license])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of license{int}
Get page of given license ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system license release 

```
system license release [-h] [--force] [--no-force] <LICENSE>
```

Release a license.
In normal condition a license is automatically released when a fabric is uninstalled.
This command should only be used if the Fabric Studio is a license server and the Fabric Studio
client has been destroyed without uninstalling the fabric.
Return: dict
Positional arguments:
LICENSE{License}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system license server legacy set 

```
system license server legacy set [-h] <STATE>
```

LabSetup only command. Do NOT use.
Define remote license server legacy flag.
Return: bool
Positional arguments:
STATE{bool}
Optional arguments:
--help, -h
show this help message and exit

#### system license server service disable 

```
system license server service disable [-h]
```

Disable service for remote client.
Optional arguments:
--help, -h
show this help message and exit

#### system license server service enable 

```
system license server service enable [-h]
```

Enable service for remote client.
Optional arguments:
--help, -h
show this help message and exit

#### system license server service get 

```
system license server service get [-h]
```

Return service state for remote client.
Return: bool
Optional arguments:
--help, -h
show this help message and exit

#### system license server service local disable 

```
system license server service local disable [-h]
```

Disable service for local client.
Optional arguments:
--help, -h
show this help message and exit

#### system license server service local enable 

```
system license server service local enable [-h]
```

Enable service for local client.
Optional arguments:
--help, -h
show this help message and exit

#### system license server service local get 

```
system license server service local get [-h]
```

Return service state for local client.
Return: bool
Optional arguments:
--help, -h
show this help message and exit

#### system license server set 

```
system license server set [-h] <SERVER>
```

LabSetup only command. Do NOT use.
Set the remote license server URL.
Set to empty value to disable license server.
Positional arguments:
SERVER{UrlInfo}
Optional arguments:
--help, -h
show this help message and exit

#### system license server supported get 

```
system license server supported get [-h]
```

Get the supported license classes to serve licenses.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system license server supported set 

```
system license server supported set [-h] [<CLASS> ...]
```

Set the supported license classes to serve licenses.
LIC:
support local .lic licenses
FLEX:
support FortiFlex licenses
Positional arguments:
CLASS{*}{str} ('LIC', 'FLEX')
Optional arguments:
--help, -h
show this help message and exit

#### system license update 

```
system license update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <license> <OBJECT>
```

Update VM licenses meta information.
Return: license.license model
Positional arguments:
license{License}
ID of the license
OBJECT{License}
license object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system log 

```
system log [-h] [{list,detail,purge}]
```

Positional arguments:
[{list,detail,purge}]
list
List api calls.
detail
Detail view of api call.
purge
Delete all API call logs.
Optional arguments:
--help, -h
show this help message and exit

#### system log detail 

```
system log detail [-h] [--related-fields [RELATED_FIELDS ...]] <apicall>
```

Detail view of api call.
Return: log.apicall model
Positional arguments:
apicall{APICall}
ID of the apicall
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system log list 

```
system log list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of apicall]
[--related-fields [RELATED_FIELDS ...]]
```

List api calls.
Return: (list[log.apicall]|page[log.apicall])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of apicall{int}
Get page of given apicall ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system log purge 

```
system log purge [-h] [--yes] [--no-yes]
```

Delete all API call logs.
Optional arguments:
--help, -h
show this help message and exit
--yes
--no-yes
(default)

### system mgmt 

```
system mgmt [-h] [{interface}]
```

Management interface.
Positional arguments:
[{interface}]
interface
Management interface, DEPRECATED use “system interfaces mgmt”.
Optional arguments:
--help, -h
show this help message and exit

#### system mgmt interface configure 

```
system mgmt interface configure [-h]
```

Deprecated call, use ‘system interfaces mgmt configure’ instead
Interactive management interface configuration.
Optional arguments:
--help, -h
show this help message and exit

#### system mgmt interface get 

```
system mgmt interface get [-h]
```

Deprecated call, use ‘system interfaces mgmt get’ instead
Get management interface configuration.
Optional arguments:
--help, -h
show this help message and exit

#### system mgmt interface public address 

```
system mgmt interface public address [-h] [--ipv IPV] [--operator OPERATOR]
[--ns NS]
```

Deprecated call, use ‘system interfaces mgmt public-address’ instead
Return public address by questionning opendns (default), google or cloudfare.
Return: str
Optional arguments:
--help, -h
show this help message and exit
--ipv{int} (4, 6)
Default: 4 .
--operator{str} ('cloudfare', 'google', 'opendns')
Default: opendns .
--ns NS{int}
Default: 1 .

#### system mgmt interface restart 

```
system mgmt interface restart [-h] [--uninstall] [--no-uninstall]
```

Deprecated call, use ‘system interfaces mgmt restart’ instead
Optional arguments:
--help, -h
show this help message and exit
--uninstall
--no-uninstall
(default)

#### system mgmt interface set 

```
system mgmt interface set [-h] <OBJECT>
```

Deprecated call, use ‘system interfaces mgmt set’ instead
Configure mangement interface.
Positional arguments:
OBJECT{SystemInterfaceConfig}
Optional arguments:
--help, -h
show this help message and exit

#### system mgmt interface show 

```
system mgmt interface show [-h]
```

Deprecated call, use ‘system interfaces mgmt show’ instead
Show system interface configuration.
Optional arguments:
--help, -h
show this help message and exit

### system monitoring 

```
system monitoring [-h] [{debug,snmp}]
```

Monitoring.
Positional arguments:
[{debug,snmp}]
debug
Capture one monitoring message.
snmp
Optional arguments:
--help, -h
show this help message and exit

#### system monitoring debug 

```
system monitoring debug [-h] [--count COUNT] [--interactive]
[--no-interactive] [--type TYPE]
```

Capture one monitoring message.
Optional arguments:
--help, -h
show this help message and exit
--count COUNT{int}
Default: 1 .
--interactive
(default)
--no-interactive
--type TYPE{str}
Default: ````.

#### system monitoring snmp listen 

```
system monitoring snmp listen [-h] <STATE>
```

Positional arguments:
STATE{str} ('public', 'private')
Optional arguments:
--help, -h
show this help message and exit

### system oauth2 

```
system oauth2 [-h] [{application,access}]
```

Positional arguments:
[{application,access}]
application
access
Optional arguments:
--help, -h
show this help message and exit

#### system oauth2 access token delete 

```
system oauth2 access token delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <accesstoken>
```

Delete access token.
Return: oauth2_provider.accesstoken model
Positional arguments:
accesstoken{AccessToken}
ID of the accesstoken
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system oauth2 access token detail 

```
system oauth2 access token detail [-h] [--related-fields [RELATED_FIELDS ...]
<accesstoken>
```

Detail view of access token.
Return: oauth2_provider.accesstoken model
Positional arguments:
accesstoken{AccessToken}
ID of the accesstoken
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system oauth2 access token list 

```
system oauth2 access token list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of accesstoken]
[--related-fields [RELATED_FIELDS ...]]
```

List access tokens.
Return: (list[oauth2_provider.accesstoken]|page[oauth2_provider.accesstoken])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of accesstoken{int}
Get page of given accesstoken ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system oauth2 application create 

```
system oauth2 application create [-h] [--related-fields [RELATED_FIELDS ...]]
<application>
```

Create application.
Return: oauth2_provider.application model
Positional arguments:
application{Application}
application object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system oauth2 application default create 

```
system oauth2 application default create [-h] [--user USER] [--yes] [--no-yes
<NAME>
```

Create a confidential client-credentials using HMAC with SHA-2 256.
return:
the credential string
Return: str
Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--user USER{User}
--yes
--no-yes
(default)

#### system oauth2 application delete 

```
system oauth2 application delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <application>
```

Delete application.
Return: oauth2_provider.application model
Positional arguments:
application{Application}
ID of the application
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system oauth2 application detail 

```
system oauth2 application detail [-h] [--related-fields [RELATED_FIELDS ...]]
<application>
```

Detail view of application.
Return: oauth2_provider.application model
Positional arguments:
application{Application}
ID of the application
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system oauth2 application list 

```
system oauth2 application list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of application]
[--related-fields [RELATED_FIELDS ...]]
```

List applications.
Return: (list[oauth2_provider.application]|page[oauth2_provider.application])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of application{int}
Get page of given application ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system openapi 

```
system openapi [-h] [{list,get}]
```

Positional arguments:
[{list,get}]
list
List available OpenAPI definition created during upgrade.
get
Get the version OpenAPI definition if available.
Optional arguments:
--help, -h
show this help message and exit

#### system openapi get 

```
system openapi get [-h] <VERSION>
```

Get the version OpenAPI definition if available.
Return: dict
Positional arguments:
VERSION{str}
Optional arguments:
--help, -h
show this help message and exit

#### system openapi list 

```
system openapi list [-h]
```

List available OpenAPI definition created during upgrade.
Return: list[str]
Optional arguments:
--help, -h
show this help message and exit

### system ot 

```
system ot [-h] [{xorg}]
```

Positional arguments:
[{xorg}]
xorg
Optional arguments:
--help, -h
show this help message and exit

#### system ot xorg configuration get 

```
system ot xorg configuration get [-h]
```

Return OT Xorg configuration.
Return: OTXorgConfiguration
Optional arguments:
--help, -h
show this help message and exit

#### system ot xorg configuration set 

```
system ot xorg configuration set [-h] <CONFIGURATION>
```

Update XOrg configuration.
Return: OTXorgConfiguration
Positional arguments:
CONFIGURATION{OTXorgConfiguration}
Optional arguments:
--help, -h
show this help message and exit

#### system ot xorg configuration xscreensaver 

```
system ot xorg configuration xscreensaver [-h]
```

Start Xscreensaver configuration screen.
Optional arguments:
--help, -h
show this help message and exit

#### system ot xorg user password 

```
system ot xorg user password [-h] [<PASSWORD>]
```

Set OT DemoCase XUser password.
If a password is passed on command line it must be encrypted, e.g.:

```
openssl passwd -6 <PASSWORD>
```

Positional arguments:
PASSWORD{str}
Optional arguments:
--help, -h
show this help message and exit

#### system ot xorg user reset 

```
system ot xorg user reset [-h]
```

Block OT XUser.
Optional arguments:
--help, -h
show this help message and exit

### system parameter 

```
system parameter [-h] [{list,detail,create,update,delete}]
```

Positional arguments:
[{list,detail,create,update,delete}]
list
List parameters.
detail
Detail view of parameter.
create
Create parameter.
update
Update parameter.
delete
Delete parameter.
Optional arguments:
--help, -h
show this help message and exit

#### system parameter create 

```
system parameter create [-h] [--related-fields [RELATED_FIELDS ...]]
<parameter>
```

Create parameter.
Return: system.parameter model
Positional arguments:
parameter{Parameter}
parameter object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system parameter delete 

```
system parameter delete [-h] [--interactive] [--no-interactive] [--yes]
[--no-yes] <parameter>
```

Delete parameter.
Return: system.parameter model
Positional arguments:
parameter{Parameter}
ID of the parameter
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system parameter detail 

```
system parameter detail [-h] [--related-fields [RELATED_FIELDS ...]]
<parameter>
```

Detail view of parameter.
Return: system.parameter model
Positional arguments:
parameter{Parameter}
ID of the parameter
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system parameter list 

```
system parameter list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of parameter]
[--related-fields [RELATED_FIELDS ...]]
```

List parameters.
Return: (list[system.parameter]|page[system.parameter])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of parameter{int}
Get page of given parameter ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system parameter update 

```
system parameter update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <parameter> <OBJECT>
```

Update parameter.
Return: system.parameter model
Positional arguments:
parameter{Parameter}
ID of the parameter
OBJECT{Parameter}
parameter object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system preferences 

```
system preferences [-h] [{set,get}]
```

Positional arguments:
[{set,get}]
set
Set system preferencies.
get
Return system preferences.
Optional arguments:
--help, -h
show this help message and exit

#### system preferences get 

```
system preferences get [-h]
```

Return system preferences.
Return: SystemPreferences
Optional arguments:
--help, -h
show this help message and exit

#### system preferences set 

```
system preferences set [-h] <PREFERENCES>
```

Set system preferencies.
Return: SystemPreferences
Positional arguments:
PREFERENCES{SystemPreferences}
Optional arguments:
--help, -h
show this help message and exit

### system repository 

```
system repository [-h] [{remote,firmware,template,home}]
```

Positional arguments:
[{remote,firmware,template,home}]
remote
firmware
template
home
Optional arguments:
--help, -h
show this help message and exit

#### system repository firmware delete 

```
system repository firmware delete [-h] [--interactive] [--no-interactive]
[--db-delete] [--no-db-delete] <FIRMWARE>
```

Remove downloaded firmware from remote repositories cache or delete it from home repository.
Fail if multiple firmwares using same backingstore are currenlty used by an installed fabric. Use the
“force” option to bypass check/
Return: repository.firmware model
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--db-delete
--no-db-delete

#### system repository firmware detail 

```
system repository firmware detail [-h] [--related-fields [RELATED_FIELDS ...]
<firmware>
```

Detail view of sync firmware.
Return: repository.firmware model
Positional arguments:
firmware{SyncFirmware}
ID of the syncfirmware
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository firmware download 

```
system repository firmware download [-h] [--force] [--no-force] <FIRMWARE>
```

NYI Launch a task to download a firmware to the repositories cache.
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository firmware extract 

```
system repository firmware extract [-h] <FIRMWARE>
```

NYI Launch a task to extract firmware archive content from the repositories cache.
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit

#### system repository firmware list 

```
system repository firmware list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of firmware]
[--related-fields [RELATED_FIELDS ...]]
```

List firmwares available in repositories.
Return: (list[repository.syncfirmware]|page[repository.syncfirmware])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of firmware{int}
Get page of given syncfirmware ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository firmware resolve 

```
system repository firmware resolve [-h] [--force] [--no-force] <FIRMWARE>
```

Trigger parent diff resolution and return state.
Return: BackupState
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository firmware sync-download 

```
system repository firmware sync-download [-h] [--force] [--no-force]
<FIRMWARE>
```

Download firmware to the repositories cache.
Return: repository.firmware model
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository firmware sync-extract 

```
system repository firmware sync-extract [-h] [--force] [--no-force] <FIRMWARE
```

Extract firmware archive content from the repositories cache.
Return: repository.firmware model
Positional arguments:
FIRMWARE{Firmware}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository home deploy 

```
system repository home deploy [-h] [--rebuild] [--no-rebuild]
```

Deploy local repository structure if required.
Optional arguments:
--help, -h
show this help message and exit
--rebuild
--no-rebuild
(default)

#### system repository home detail 

```
system repository home detail [-h] [--related-fields [RELATED_FIELDS ...]]
```

Detail view of repository.
Return: repository.repository model
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository home firmware delete 

```
system repository home firmware delete [-h] [--interactive] [--no-interactive
<NAME>
```

Erase a home repository firmware by filename.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system repository home firmware import 

```
system repository home firmware import [-h] [--if-exists IF_EXISTS] <INPUT>
```

Import a firmware in the home repository.
Positional arguments:
INPUT{Path}
Optional arguments:
--help, -h
show this help message and exit
--if-exists{str} ('abort', 'rename', 'overwrite')
What to do when a template with same name already exists in the home repository
Default: abort .

#### system repository home firmware list 

```
system repository home firmware list [-h]
```

List home repository firmwares by filenames.
Optional arguments:
--help, -h
show this help message and exit

#### system repository home firmware package 

```
system repository home firmware package [-h] [--output-dir OUTPUT_DIR]
[--overwrite] [--no-overwrite] [--interactive] [--no-interactive] <NAME>
```

Package a custom splited firmware as a zip archive.
The newly created firmware file is automatically added to the home repository.
If your custom splited firmware is a diff based on an original firmare in the home repository too and
your original firmware is either:
an archive: home repository must have been refreshed to also have the associated meta
a custom splited firmware:
the original firmware must be packaged first
home repository must have been refreshed to also have the associated meta of this packaged
original firmware
Original firmware chksum may be updated by this call.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--output-dir OUTPUT_DIR{Path}
--overwrite
--no-overwrite
(default)
--interactive
(default)
--no-interactive

#### system repository home purge 

```
system repository home purge [-h] [--interactive] [--no-interactive]
[--in-model] [--no-in-model]
```

Purge home repository backingstore of unused or obsolete firmwares.
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--in-model
(default)
--no-in-model

#### system repository home refresh 

```
system repository home refresh [-h] [--dry-run] [--no-dry-run] [--database]
[--no-database] [--filename FILENAME]
```

Refresh local repository with new firmwares and templates.
When new firmwares or templates are deployed in the home repository, build meta information and
synchronize database.
Return: runtime.runtimetask model if not ‘interactive’
Result: repository.repository model
Optional arguments:
--help, -h
show this help message and exit
--dry-run
simulate meta generation
--no-dry-run
simulate meta generation (default)
--database
refresh or not information in Fabric Studio database (default)
--no-database
refresh or not information in Fabric Studio database
--filename FILENAME{Path}

#### system repository home shell 

```
system repository home shell [-h] [<ARGS> ...]
```

Open a shell in the local repository environment.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ARGS{*}
Optional arguments:
--help, -h
show this help message and exit

#### system repository home template delete 

```
system repository home template delete [-h] [--interactive] [--no-interactive
<NAME>
```

Erase a home repository fabric template by filename.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system repository home template import 

```
system repository home template import [-h] [--if-exists IF_EXISTS] <INPUT>
```

Import a fabric template in the home repository.
Positional arguments:
INPUT{Path}
Optional arguments:
--help, -h
show this help message and exit
--if-exists{str} ('abort', 'rename', 'overwrite')
What to do when a template with same name already exists in the home repository
Default: rename .

#### system repository home template list 

```
system repository home template list [-h]
```

List home repository fabric templates by filenames.
Optional arguments:
--help, -h
show this help message and exit

#### system repository remote create 

```
system repository remote create [-h] [--related-fields [RELATED_FIELDS ...]]
<repository>
```

Create repository.
Return: repository.repository model
Positional arguments:
repository{Repository}
repository object
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository remote delete 

```
system repository remote delete [-h] [--interactive] [--no-interactive]
[--yes] [--no-yes] <repository>
```

Delete repository.
Return: repository.repository model
Positional arguments:
repository{Repository}
ID of the repository
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--yes
--no-yes
(default)

#### system repository remote detail 

```
system repository remote detail [-h] [--related-fields [RELATED_FIELDS ...]]
<repository>
```

Detail view of repository.
Return: repository.repository model
Positional arguments:
repository{Repository}
ID of the repository
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository remote list 

```
system repository remote list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of repository]
[--related-fields [RELATED_FIELDS ...]]
```

List Repositories.
Return: (list[repository.repository]|page[repository.repository])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of repository{int}
Get page of given repository ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository remote purge 

```
system repository remote purge [-h] [--interactive] [--no-interactive]
[--in-model] [--no-in-model]
```

Cleanup repository cache from unused firmwares.
Firmwares currently used by running Vm are preserved.
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--in-model
(default)
--no-in-model

#### system repository remote refresh 

```
system repository remote refresh [-h] [--force] [--no-force] <REPOSITORY>
```

Refresh list of firmwares and pocs available from a remote repository.
Return: runtime.runtimetask model
Result: repository.repository model
Positional arguments:
REPOSITORY{Repository}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository remote refresh-all 

```
system repository remote refresh-all [-h] [--force] [--no-force]
```

Refresh all remote repositories
Return: runtime.runtimetask model
Result: list[repository.repository]
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system repository remote update 

```
system repository remote update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <repository> <OBJECT>
```

Update repository.
Return: repository.repository model
Positional arguments:
repository{Repository}
ID of the repository
OBJECT{Repository}
repository object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository template delete 

```
system repository template delete [-h] [--interactive] [--no-interactive]
<TEMPLATE>
```

Remove downloaded Fabric template from remote repositories cache or delete it from home or
system repository.
Return: repository.template model
Positional arguments:
TEMPLATE{Template}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system repository template detail 

```
system repository template detail [-h] [--related-fields [RELATED_FIELDS ...]
<template>
```

Detail view of template.
Return: repository.template model
Positional arguments:
template{Template}
ID of the template
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository template documentation download 

```
system repository template documentation download [-h] [--interactive]
[--no-interactive] <TEMPLATE>
```

Download the template documentation.
Return: runtime.runtimetask model if not ‘interactive’
Result: str
Positional arguments:
TEMPLATE{Template}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system repository template download 

```
system repository template download [-h] [--force] [--no-force]
[--interactive] [--no-interactive] [--prefetch-documentation]
[--no-prefetch-documentation] [--prefetch-firmware] [--no-prefetch-firmware]
<TEMPLATE>
```

Download a Fabric template from remote repository to the repositories cache.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
TEMPLATE{SyncTemplate}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)
--interactive
(default)
--no-interactive
--prefetch-documentation
--no-prefetch-documentation
(default)
--prefetch-firmware
--no-prefetch-firmware
(default)

#### system repository template firmware download 

```
system repository template firmware download [-h] [--interactive]
[--no-interactive] <TEMPLATE>
```

Download firmwares used by the template.
Return: runtime.runtimetask model if not ‘interactive’
Positional arguments:
TEMPLATE{Template}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive

#### system repository template layout 

```
system repository template layout [-h] <TEMPLATE>
```

Return template topology layout.
Return: dict
Positional arguments:
TEMPLATE{Template}
Optional arguments:
--help, -h
show this help message and exit

#### system repository template list 

```
system repository template list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of template]
[--related-fields [RELATED_FIELDS ...]]
```

List Fabric templates available in repositories.
Return: (list[repository.template]|page[repository.template])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of template{int}
Get page of given template ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system repository template sync-download 

```
system repository template sync-download [-h] [--force] [--no-force]
<TEMPLATE>
```

DEPRECATED Download Fabric template to the repositories cache.
Positional arguments:
TEMPLATE{Template}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

### system samba 

```
system samba [-h] [{services,account,configuration}]
```

Positional arguments:
[{services,account,configuration}]
services
account
configuration
Optional arguments:
--help, -h
show this help message and exit

#### system samba account disable 

```
system samba account disable [-h]
```

Disable admin user.
Optional arguments:
--help, -h
show this help message and exit

#### system samba account enable 

```
system samba account enable [-h]
```

Enable admin user.
Optional arguments:
--help, -h
show this help message and exit

#### system samba account password 

```
system samba account password [-h] [--enable] [--no-enable] <PASSWORD>
```

Change password and enable (default) samba access for admin.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
PASSWORD
Optional arguments:
--help, -h
show this help message and exit
--enable
(default)
--no-enable

#### system samba configuration get 

```
system samba configuration get [-h]
```

Return SAMBA configuration.
Return: dict
Optional arguments:
--help, -h
show this help message and exit

#### system samba services start 

```
system samba services start [-h]
```

Start smb and nmb services.
Optional arguments:
--help, -h
show this help message and exit

#### system samba services stop 

```
system samba services stop [-h]
```

Stop smb and nmb services.
Optional arguments:
--help, -h
show this help message and exit

### system security 

```
system security [-h] [{preferences}]
```

Positional arguments:
[{preferences}]
preferences
Optional arguments:
--help, -h
show this help message and exit

#### system security preferences get 

```
system security preferences get [-h]
```

Return security preferences.
Return: SecurityPreferences
Optional arguments:
--help, -h
show this help message and exit

#### system security preferences set 

```
system security preferences set [-h] <PREFERENCES>
```

Define security preferences.
Return: SecurityPreferences
Positional arguments:
PREFERENCES{SecurityPreferences}
Optional arguments:
--help, -h
show this help message and exit

### system support 

```
system support [-h] [{session}]
```

Positional arguments:
[{session}]
session
Optional arguments:
--help, -h
show this help message and exit

#### system support session close 

```
system support session close [-h]
```

Close a support session.
Optional arguments:
--help, -h
show this help message and exit

#### system support session open 

```
system support session open [-h] [--yes] [--no-yes] [--force] [--no-force]
```

Open a support session, allowing Fabric Studio Support Team to login on the instance.
VPN tunnel is: support.fabricstudio.com:12002
**** DISCLAIMER ****
By opening a support session you agree to:
Open a VPN tunnel with the Fabric Studio Support Server (support.fabricstudio.net on UDP port
12002).
Allow Fabric Studio Support Team to access your Fabric Studio instance.
By allowing Fabric Studio Support Team to access your Fabric Studio instance you acknowledge the
following:
Fabric Studio Support Team could have access to any network or device that your Fabric Studio
instance has currently access to, including but not limited to your home or lab network, corporate
networks, IoT devices, any devices connected to the same network.
To limit this exposure you have reviewed your firewall policies and implemented network
segmentation.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Optional arguments:
--help, -h
show this help message and exit
--yes
automatic agree and continue
--no-yes
automatic agree and continue (default)
--force
force a new session even if one already exists
--no-force
force a new session even if one already exists (default)

#### system support session status 

```
system support session status [-h]
```

Show support session information.
Return: bool
Optional arguments:
--help, -h
show this help message and exit

### system template 

```
system template [-h] [{create,delete,rename,list}]
```

Positional arguments:
[{create,delete,rename,list}]
create
Create a system template from a Fabric.
delete
Delete a system template.
rename
Rename a system template.
list
List available system templates.
Optional arguments:
--help, -h
show this help message and exit

#### system template create 

```
system template create [-h] [--interactive] [--no-interactive] [--overwrite]
[--no-overwrite] <FABRIC> [<NAME>]
```

Create a system template from a Fabric.
Return: runtime.runtimetask model if not ‘interactive’
Result: repository.template model
Positional arguments:
FABRIC{Fabric}
NAME{str}
Optional arguments:
--help, -h
show this help message and exit
--interactive
(default)
--no-interactive
--overwrite
--no-overwrite
(default)

#### system template delete 

```
system template delete [-h] <TEMPLATE>
```

Delete a system template.
Return: repository.template model
Positional arguments:
TEMPLATE{Template}
Specify template file name
Optional arguments:
--help, -h
show this help message and exit

#### system template list 

```
system template list [-h]
```

List available system templates.
Return: list[repository.template]
Optional arguments:
--help, -h
show this help message and exit

#### system template rename 

```
system template rename [-h] <TEMPLATE> <NAME>
```

Rename a system template.
Positional arguments:
TEMPLATE{Template}
Specify template file name
NAME{str}
Optional arguments:
--help, -h
show this help message and exit

### system upgrade 

```
system upgrade [-h] [{channel}]
```

Positional arguments:
[{channel}]
channel
Optional arguments:
--help, -h
show this help message and exit

#### system upgrade channel get 

```
system upgrade channel get [-h]
```

Get the current upgrade channel.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system upgrade channel set 

```
system upgrade channel set [-h] <CHANNEL>
```

Change the default upgrade channel.
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
CHANNEL{str} ('interim', 'testing', 'stable')
Optional arguments:
--help, -h
show this help message and exit

### system user 

```
system user [-h] [{list,detail,update,password}]
```

Positional arguments:
[{list,detail,update,password}]
list
List users.
detail
Detail view of user.
update
Update user.
password
Optional arguments:
--help, -h
show this help message and exit

#### system user detail 

```
system user detail [-h] [--related-fields [RELATED_FIELDS ...]] <user>
```

Detail view of user.
Return: auth.user model
Positional arguments:
user{User}
ID of the user
Optional arguments:
--help, -h
show this help message and exit
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system user list 

```
system user list [-h] [--select SELECT] [--exclude EXCLUDE]
[--order-by [ORDER_BY ...]] [--startIndex STARTINDEX] [--endIndex ENDINDEX]
[--limit LIMIT] [--page PAGE] [--page-of user]
[--related-fields [RELATED_FIELDS ...]]
```

List users.
Return: (list[auth.user]|page[auth.user])
Optional arguments:
--help, -h
show this help message and exit
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--limit LIMIT{int}
--page PAGE{int}
--page-of user{int}
Get page of given user ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

#### system user password change 

```
system user password change [-h] [--new-password NEW_PASSWORD] [--encrypted]
[--no-encrypted] [<USER>]
```

Change user password.
Return: auth.user model
Positional arguments:
USER{User}
Optional arguments:
--help, -h
show this help message and exit
--new-password NEW_PASSWORD{str}
--encrypted
--no-encrypted
(default)

#### system user password disable 

```
system user password disable [-h] [<USER>]
```

Disable a user password.
Positional arguments:
USER{User}
Optional arguments:
--help, -h
show this help message and exit

#### system user update 

```
system user update [-h] [--update-fields UPDATE_FIELDS]
[--related-fields [RELATED_FIELDS ...]] <user> <OBJECT>
```

Update user.
Return: auth.user model
Positional arguments:
user{User}
ID of the user
OBJECT{User}
user object
Optional arguments:
--help, -h
show this help message and exit
--update-fields UPDATE_FIELDS{str}
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### system version 

```
system version [-h]
```

Get product version.
Return: Tag
Optional arguments:
--help, -h
show this help message and exit

### system webserver 

```
system webserver [-h] [{https,sync,async}]
```

Positional arguments:
[{https,sync,async}]
https
sync
async
Optional arguments:
--help, -h
show this help message and exit

#### system webserver async daemon 

```
system webserver async daemon [-h] [--reload] [--no-reload]
[--reload-engine RELOAD_ENGINE] [--kill] [--no-kill] [--django-debug]
[--no-django-debug] <ACTION>
```

API call to manage gunicorn daemon. Daemon information are extracted from
context._.settings.GUNICORN (default).
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ACTION{str} ('start', 'stop', 'debug', 'reload', 'status', 'restart')
Optional arguments:
--help, -h
show this help message and exit
--reload
start gunicorn with “–reload”
--no-reload
start gunicorn with “–reload” (default)
--reload-engine RELOAD_ENGINE{str}
gunicorn reload engine
Default: auto .
--kill
kill master daemon with SIGKILL when normal stop fails
--no-kill
kill master daemon with SIGKILL when normal stop fails (default)
--django-debug
(default)
--no-django-debug

#### system webserver https certificate current get 

```
system webserver https certificate current get [-h]
```

Current webserver certificate.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificate current set 

```
system webserver https certificate current set [-h] [--force] [--no-force]
<FQDN>
```

Change webserver certificate.
Positional arguments:
FQDN{str}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system webserver https certificate delete 

```
system webserver https certificate delete [-h] <FQDN>
```

Delete a webserver certificate.
Can’t delete the default certificate or the active certificate.
Return: str
Positional arguments:
FQDN{str}
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificate get 

```
system webserver https certificate get [-h]
```

Deprecated call, use ‘webserver https certificate current get’ instead
Current webserver certificate.
Return: str
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificate import 

```
system webserver https certificate import [-h] [--overwrite] [--no-overwrite]
<FQDN> <CRT> <KEY>
```

Upload a webserver certificate.
crt and key can be path to files stored in the home repository (relative
path) or they can be HTTP REST upload files.
Positional arguments:
FQDN{str}
CRT{Path}
A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST
KEY{Path}
A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)

#### system webserver https certificate list 

```
system webserver https certificate list [-h]
```

List available webserver certificates.
Return: tuple
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificate set 

```
system webserver https certificate set [-h] [--force] [--no-force] <FQDN>
```

Deprecated call, use ‘webserver https certificate current set’ instead
Change webserver certificate.
Positional arguments:
FQDN{str}
Optional arguments:
--help, -h
show this help message and exit
--force
--no-force
(default)

#### system webserver https certificate source get 

```
system webserver https certificate source get [-h]
```

Return URL of the webserver certificate archive source.
Return: UrlInfo
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificate source refresh 

```
system webserver https certificate source refresh [-h] [--restart]
[--no-restart]
```

Retrieve the webserver certificate archive from source and install it.
Optional arguments:
--help, -h
show this help message and exit
--restart
(default)
--no-restart

#### system webserver https certificate source set 

```
system webserver https certificate source set [-h] [--key KEY] [--crt CRT]
<URL>
```

Set URL to the webserver certificate archive source.
The archive must contains a certificate and the associated private key, if not specified the certificate
must be public.crt  and the key private.key .
Positional arguments:
URL{UrlInfo}
Optional arguments:
--help, -h
show this help message and exit
--key KEY{str}
--crt CRT{str}

#### system webserver https certificates delete 

```
system webserver https certificates delete [-h] <FQDN>
```

Deprecated call, use ‘webserver https certificate delete’ instead
Delete a webserver certificate.
Can’t delete the default certificate or the active certificate.
Return: str
Positional arguments:
FQDN{str}
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https certificates import 

```
system webserver https certificates import [-h] [--overwrite] [--no-overwrite
<FQDN> <CRT> <KEY>
```

Deprecated call, use ‘webserver https certificate import’ instead
Upload a webserver certificate.
crt and key can be path to files stored in the home repository (relative
path) or they can be HTTP REST upload files.
Positional arguments:
FQDN{str}
CRT{Path}
A relative path to a PEM certificate file in the home repository or an upload file for HTTP REST
KEY{Path}
A relative path to a certificate KEY file in the home repository or an upload file for HTTP REST
Optional arguments:
--help, -h
show this help message and exit
--overwrite
--no-overwrite
(default)

#### system webserver https certificates list 

```
system webserver https certificates list [-h]
```

Deprecated call, use ‘webserver https certificate list’ instead
List available webserver certificates.
Return: tuple
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https port get 

```
system webserver https port get [-h]
```

The webserver HTTPS listening port.
Return: int
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https port set 

```
system webserver https port set [-h] <PORT>
```

Change the webserver HTTPS listening port.
Positional arguments:
PORT{int}
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https redirect get 

```
system webserver https redirect get [-h]
```

Tell if webserver listen to HTTP port (80) and does a redirect to HTTPS.
Optional arguments:
--help, -h
show this help message and exit

#### system webserver https redirect set 

```
system webserver https redirect set [-h] <STATE>
```

Enable or disable listening on HTTP port (80) and doing a redirect to HTTPS.
Positional arguments:
STATE{str} ('enable', 'disable')
Optional arguments:
--help, -h
show this help message and exit

#### system webserver sync daemon 

```
system webserver sync daemon [-h] [--reload] [--no-reload]
[--reload-engine RELOAD_ENGINE] [--kill] [--no-kill] [--django-debug]
[--no-django-debug] <ACTION>
```

API call to manage gunicorn daemon. Daemon information are extracted from
context._.settings.GUNICORN (default).
Return: typing.Annotated[int, {‘rtype’: ‘ShellCode’, ‘cast’: <class ‘int’>}]
Positional arguments:
ACTION{str} ('start', 'stop', 'debug', 'reload', 'status', 'restart')
Optional arguments:
--help, -h
show this help message and exit
--reload
start gunicorn with “–reload”
--no-reload
start gunicorn with “–reload” (default)
--reload-engine RELOAD_ENGINE{str}
gunicorn reload engine
Default: auto .
--kill
kill master daemon with SIGKILL when normal stop fails
--no-kill
kill master daemon with SIGKILL when normal stop fails (default)
--django-debug
(default)
--no-django-debug

# TASK

## General options

```
task [-h]
[{list,purge,queue,kill,kill-all,detail,refresh-all,wait,log,device,fabric}]
```

Positional arguments:
[{list,purge,queue,kill,kill-all,detail,refresh-all,wait,log,device,fabric}]
list
List tasks.
purge
Purge system and old fabric tasks log.
queue
Queue a new task (as cls instance).
kill
Stop a running task.
kill-all
Stop all running tasks.
detail
Show a running task status.
refresh-all
wait
log
Get a task log.
device
fabric
Optional arguments:
--help, -h
show this help message and exit

### task detail 

```
task detail [-h] [--refresh] [--no-refresh]
[--related-fields [RELATED_FIELDS ...]] <TASK.id>
```

Show a running task status.
Return: task.task model
Positional arguments:
TASK.id{Task}
Optional arguments:
--help, -h
show this help message and exit
--refresh
--no-refresh
(default)
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### task device 

```
task device [-h] [{list}]
```

Positional arguments:
[{list}]
list
List tasks.
Optional arguments:
--help, -h
show this help message and exit

#### task device list 

```
task device list [-h] [--running] [--no-running] [--limit LIMIT]
[--select SELECT] [--exclude EXCLUDE] [--order-by [ORDER_BY ...]]
[--startIndex STARTINDEX] [--endIndex ENDINDEX] [--page PAGE] [--page-of task
[--related-fields [RELATED_FIELDS ...]] [<DEVICE_ID>]
```

List tasks.
Return: list[model.devicetask]
Positional arguments:
DEVICE_ID{int}
Optional arguments:
--help, -h
show this help message and exit
--running
--no-running
--limit LIMIT{int}
Default: 10 .
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--page PAGE{int}
--page-of task{int}
Get page of given task ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### task fabric 

```
task fabric [-h] [{list}]
```

Positional arguments:
[{list}]
list
List tasks.
Optional arguments:
--help, -h
show this help message and exit

#### task fabric list 

```
task fabric list [-h] [--running] [--no-running] [--limit LIMIT]
[--select SELECT] [--exclude EXCLUDE] [--order-by [ORDER_BY ...]]
[--startIndex STARTINDEX] [--endIndex ENDINDEX] [--page PAGE] [--page-of task
[--related-fields [RELATED_FIELDS ...]] [<FABRIC_ID>]
```

List tasks.
Return: list[model.devicetask]
Positional arguments:
FABRIC_ID{int}
Optional arguments:
--help, -h
show this help message and exit
--running
--no-running
--limit LIMIT{int}
Default: 10 .
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--page PAGE{int}
--page-of task{int}
Get page of given task ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### task kill 

```
task kill [-h] [--timeout TIMEOUT] <TASK.id>
```

Stop a running task.
Return: task.task model
Positional arguments:
TASK.id{Task}
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
Default: 0 .

### task kill-all 

```
task kill-all [-h] [--timeout TIMEOUT]
```

Stop all running tasks.
Return: list[task.task]
Optional arguments:
--help, -h
show this help message and exit
--timeout TIMEOUT{int}
If 0 use SIGKILL else use SIGTERM and wait for timeout before doing a SGIKILL if necessary
Default: 0 .

### task list 

```
task list [-h] [--running] [--no-running] [--limit LIMIT] [--select SELECT]
[--exclude EXCLUDE] [--order-by [ORDER_BY ...]] [--startIndex STARTINDEX]
[--endIndex ENDINDEX] [--page PAGE] [--page-of task]
[--related-fields [RELATED_FIELDS ...]]
```

List tasks.
Return: list[task.task]
Optional arguments:
--help, -h
show this help message and exit
--running
--no-running
--limit LIMIT{int}
Default: 10 .
--select SELECT{filter}
--exclude EXCLUDE{filter}
--order-by ORDER_BY{*}{tuple}
List of fields separated by a comma
--startIndex STARTINDEX{int}
--endIndex ENDINDEX{int}
--page PAGE{int}
--page-of task{int}
Get page of given task ID
--related-fields RELATED_FIELDS{*}{str}
Extra fields to dump

### task log 

```
task log [-h] [--offset OFFSET] [--file FILE] <TASK.id>
```

Get a task log.
Return: IOBase
Positional arguments:
TASK.id{Task}
Optional arguments:
--help, -h
show this help message and exit
--offset OFFSET{int}
Default: 0 .
--file{str} ('cmdline', 'monitor.log', 'monitor.pid', 'status.json', 'stdout', 'watched.pid', 'result.json')
Default: stdout .

### task purge 

```
task purge [-h] [--yes] [--no-yes]
```

Purge system and old fabric tasks log.
Always keep current installed fabric logs.
Return: list[int]
Optional arguments:
--help, -h
show this help message and exit
--yes
--no-yes
(default)

### task queue 

```
task queue [-h] [--cls-kwargs CLS_KWARGS] [--kwargs KWARGS] <CLS> <TITLE>
<TOOL> <TOOL_ARGS>
```

Queue a new task (as cls instance).
Return: task.task model
Positional arguments:
CLS{Task}
TITLE{str}
Title of the task
TOOL{sh}
The tool
TOOL_ARGS{sh}
The tool arguments
Optional arguments:
--help, -h
show this help message and exit
--cls-kwargs CLS_KWARGS{dict}
passed to cls create
--kwargs KWARGS{dict}
passed to queue manager

### task refresh-all 

```
task refresh-all [-h] [--wait-launch] [--no-wait-launch]
```

Return: list[task.task]
Optional arguments:
--help, -h
show this help message and exit
--wait-launch
(default)
--no-wait-launch

### task wait 

```
task wait [-h] [{task}]
```

Positional arguments:
[{task}]
task
Wait for the task to complete or return on timeout.
Optional arguments:
--help, -h
show this help message and exit

#### task wait task 

```
task wait task [-h] <TASK.id> [<TIMEOUT>] [<PAUSE>]
```

Wait for the task to complete or return on timeout.
Return: bool
Positional arguments:
TASK.id{Task}
TIMEOUT{int}
Default: default: 0 .
PAUSE{float}
Default: default: 5 .
Optional arguments:
--help, -h
show this help message and exit

#### 5.2.2. Fabric Studio Objects Model

## admin.logentry  model

LogEntry(id, action_time, user, content_type, object_id, object_repr, action_flag, change_message)
JSON:

```
{
"action_flag": null,
"action_time": "func:django.utils.timezone.now",
"change_message": null,
"content_type": null,
"id": null,
"object_id": null,
"object_repr": null,
"user": null
}
```

Required fields:

```
action_flag
object_repr
user
```

Readonly attributes on update:

```
id
```

Fields documentation:
action_flag:
(int)
1:
Addition
2:
Change
3:
Deletion
action_time:
(datetime)
change_message:
(str)
content_type:
“contenttypes.contenttype” object ID. (contenttypes.contenttype)
id:
(int)
object_id:
(str)
object_repr:
(str[200])
user:
“auth.user” object ID. (auth.user)

## assets.fptype  model

A Fabric Studio product type
JSON:

```
{
"id": null,
"name": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[32])

## assets.license  model

License(id, license, api_username, registrationDate, description, isDecommissioned, productModel,
productModelEoR, productModelEoS, partner, expirationDate, licenseNumber, licenseSKU,
licenseType, nb_cpu, fp_type)
JSON:

```
{
"api_username": null,
"description": null,
"expirationDate": null,
"fp_type": null,
"id": null,
"isDecommissioned": null,
"license": null,
"licenseNumber": null,
"licenseSKU": null,
"licenseType": null,
"nb_cpu": 1,
"partner": null,
"productModel": null,
"productModelEoR": null,
"productModelEoS": null,
"registrationDate": null
}
```

Required fields:

```
api_username
fp_type
isDecommissioned
license
productModel
registrationDate
```

Readonly attributes on update:

```
id
```

Fields documentation:
api_username:
(str[256])
description:
(str[256])
expirationDate:
(datetime)
fp_type:
“assets.fptype” object ID. (assets.fptype)
id:
(int)
isDecommissioned:
(bool)
license:
“license.license” object ID. (license.license)
licenseNumber:
(str[128])
licenseSKU:
(str[128])
licenseType:
(str[128])
nb_cpu:
(int)
partner:
(str[128])
productModel:
(str[128])
productModelEoR:
(datetime)
productModelEoS:
(datetime)
registrationDate:
(datetime)

## auth.group  model

Groups are a generic way of categorizing users to apply permissions, or some other label, to those
users. A user can belong to any number of groups.
A user in a group automatically has all the permissions granted to that group. For example, if the
group ‘Site editors’ has the permission can_edit_home_page, any user in that group will have that
permission.
Beyond permissions, groups are a convenient way to categorize users to apply some label, or
extended functionality, to them. For example, you could create a group ‘Special users’, and you could
write code that would do special things to those users – such as giving them access to a members-
only portion of your site, or sending them members-only email messages.
JSON:

```
{
"id": null,
"name": null,
"permissions": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[150])
permissions:
(auth.permission)

## auth.permission  model

The permissions system provides a way to assign permissions to specific users and groups of users.
The permission system is used by the Django admin site, but may also be useful in your own code.
The Django admin site uses permissions as follows:
The “add” permission limits the user’s ability to view the “add” form and add an object.
The “change” permission limits a user’s ability to view the change list, view the “change” form and
change an object.
The “delete” permission limits the ability to delete an object.
The “view” permission limits the ability to view an object.
Permissions are set globally per type of object, not per specific object instance. It is possible to say
“Mary may change news stories,” but it’s not currently possible to say “Mary may change news
stories, but only the ones she created herself” or “Mary may only change news stories that have a
certain status or publication date.”
The permissions listed above are automatically created for each model.
JSON:

```
{
"codename": null,
"content_type": null,
"id": null,
"name": null
}
```

Required fields:

```
codename
content_type
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
codename:
(str[100])
content_type:
“contenttypes.contenttype” object ID. (contenttypes.contenttype)
id:
(int)
name:
(str[255])

## auth.user  model

Users within the Django authentication system are represented by this model.
Username and password are required. Other fields are optional.
JSON:

```
{
"date_joined": "func:django.utils.timezone.now",
"email": null,
"first_name": null,
"id": null,
"last_login": null,
"last_name": null,
"username": null
}
```

Required fields:

```
username
```

Readonly attributes on update:

```
id
```

Fields documentation:
date_joined:
(datetime)
email:
(email)
first_name:
(str[150])
id:
(int)
last_login:
(datetime)
last_name:
(str[150])
username:
Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. (str[150])

## certificates.cacertificate  model

CACertificate(id, name, internal_name, not_after, subject, issuer, fingerprint, readonly, pem)
JSON:

```
{
"fingerprint": null,
"id": null,
"internal_name": null,
"issuer": null,
"name": null,
"not_after": null,
"pem": null,
"readonly": false,
"subject": null
}
```

Required fields:

```
name
pem
```

Readonly attributes:

```
fingerprint
internal_name
issuer
not_after
readonly
subject
```

Readonly attributes on update:

```
id
pem
```

Fields and attributes documentation:
fingerprint:
(str[256])
id:
(int)
internal_name:
(str[256])
issuer:
(str[256])
name:
(str[256])
not_after:
(datetime)
pem:
(?:certificates.CACertificate.pem)
readonly:
(bool)
subject:
(str[256])

## contenttypes.contenttype  model

ContentType(id, app_label, model)
JSON:

```
{
"app_label": null,
"id": null,
"model": null
}
```

Required fields:

```
app_label
model
```

Readonly attributes on update:

```
id
```

Fields documentation:
app_label:
(str[100])
id:
(int)
model:
(str[100])

## flexvm.config  model

Configuration of a product for a program serial number.
JSON:

```
{
"id": null,
"name": null,
"productType": null,
"program": null,
"status": null
}
```

Required fields:

```
name
productType
program
status
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[128])
productType:
“flexvm.producttype” object ID. (flexvm.producttype)
program:
“flexvm.program” object ID. (flexvm.program)
status:
(str[32])

## flexvm.configparameter  model

A config parameter and its value.
JSON:

```
{
"config": null,
"id": null,
"parameter": null,
"value": null
}
```

Required fields:

```
config
parameter
value
```

Readonly attributes on update:

```
id
```

Fields documentation:
config:
“flexvm.config” object ID. (flexvm.config)
id:
(int)
parameter:
“flexvm.parameter” object ID. (flexvm.parameter)
value:
(str[64])

## flexvm.fptype  model

A Fabric Studio product type
JSON:

```
{
"id": null,
"name": null,
"products": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[32])
products:
(flexvm.producttype)

## flexvm.license  model

A FortiFlex VM License.
JSON:

```
{
"config": null,
"description": "",
"id": null,
"license": null,
"not_before": null,
"status": null,
"tokenStatus": null
}
```

Required fields:

```
license
not_before
status
tokenStatus
```

Readonly attributes on update:

```
id
```

Fields documentation:
config:
“flexvm.config” object ID. (flexvm.config)
description:
(str[128])
id:
(int)
license:
“license.license” object ID. (license.license)
not_before:
(datetime)
status:
(str[32])
tokenStatus:
(str[32])

## flexvm.parameter  model

A config parameter.
JSON:

```
{
"id": null,
"name": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[64])

## flexvm.pool  model

Select for a product which program serial number/config to look for licenses.
JSON:

```
{
"config": null,
"fp_type": null,
"id": null
}
```

Required fields:

```
config
fp_type
```

Readonly attributes on update:

```
id
```

Fields documentation:
config:
“flexvm.config” object ID. (flexvm.config)
fp_type:
“flexvm.fptype” object ID. (flexvm.fptype)
id:
(int)

## flexvm.producttype  model

A FortiFlex VM product augmented with the Fabric product type.
JSON:

```
{
"id": null,
"name": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[64])

## flexvm.program  model

Program(id, accountId, serialNumber, startDate, endDate, hasSupportCoverage, api_username)
JSON:

```
{
"accountId": null,
"api_username": null,
"endDate": null,
"hasSupportCoverage": null,
"id": null,
"serialNumber": null,
"startDate": null
}
```

Required fields:

```
accountId
api_username
endDate
hasSupportCoverage
serialNumber
startDate
```

Readonly attributes on update:

```
id
```

Fields documentation:
accountId:
(int)
api_username:
(str[256])
endDate:
(datetime)
hasSupportCoverage:
(bool)
id:
(int)
serialNumber:
(str[128])
startDate:
(datetime)

## history.block  model

Block(id, script, start_date, direction, offset, length)
JSON:

```
{
"direction": null,
"id": null,
"length": null,
"offset": null,
"script": null,
"start_date": null
}
```

Required fields:

```
direction
length
offset
script
start_date
```

Readonly attributes on update:

```
id
```

Fields documentation:
direction:
(str[64])
id:
(int)
length:
(int)
offset:
(int)
script:
“history.script” object ID. (history.script)
start_date:
(datetime)

## history.script  model

Script(id, session, name, start_date, end_date, result, next_offset)
JSON:

```
{
"end_date": null,
"id": null,
"name": null,
"next_offset": null,
"result": null,
"session": null,
"start_date": null
}
```

Required fields:

```
name
next_offset
session
start_date
```

Readonly attributes on update:

```
id
```

Fields documentation:
end_date:
(datetime)
id:
(int)
name:
(str[256])
next_offset:
(int)
result:
(str[256])
session:
“history.session” object ID. (history.session)
start_date:
(datetime)

## history.session  model

Session(id, vm, task, start_date, next_offset)
JSON:

```
{
"id": null,
"next_offset": null,
"start_date": null,
"task": null,
"vm": null
}
```

Required fields:

```
next_offset
start_date
task
vm
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
next_offset:
(int)
start_date:
(datetime)
task:
“model.devicetask” object ID. (model.devicetask)
vm:
“model.vm” object ID. (model.vm)

## license.client  model

Client(id, uuid, address, last_heartbeat, owner)
JSON:

```
{
"address": null,
"id": null,
"last_heartbeat": "func:django.utils.timezone.now",
"owner": "",
"uuid": null
}
```

Readonly attributes on update:

```
id
```

Fields documentation:
address:
Fabric Studio client public address using the license. (ipaddress)
id:
(int)
last_heartbeat:
last time owner have been seen online. (datetime)
owner:
(str[254])
uuid:
Client UUID. (str[36])

## license.license  model

A Fortinet product license.
Parent model: storage.pstorage model
JSON:

```
{
"chksum": null,
"created_at": "func:django.utils.timezone.now",
"enable": true,
"from_server": null,
"group": "",
"id": null,
"lic_type": null,
"max_cpu": 1,
"mgmt_addr": null,
"mgmt_hwaddr": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"not_after": null,
"size": null,
"subtype": "",
"valid_until": null,
"vm_type": null,
"vm_uuid": null
}
```

Readonly attributes:

```
from_server
lic_type
name
size
```

Fields and attributes documentation:
chksum:
Internal chksum (without space and new line) to detect duplicated. (str[128])
created_at:
(datetime)
enable:
(bool)
from_server:
If received from a server the server address, blank for local. (url)
group:
license group. (str[64])
id:
“license.license” object ID (int)
lic_type:
Type as it appears in the “lic” file. (str[32])
max_cpu:
Maximum number of CPU supported by the license. (int)
mgmt_addr:
IP Address associated to the license. (ipaddress)
mgmt_hwaddr:
Port hardware address associated to the license. (str[17])
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
not_after:
license expiration date if available. (datetime)
size:
(?)
subtype:
Extra license supported (ex: carrier). (str[32])
valid_until:
can’t be used after this date, only when from a server. (datetime)
vm_type:
The type of the license for Fabric Studio. (str[32])
vm_uuid:
VM UUID associated to the license, overrides the VM UUID defined in the Fabric. (str[36])

## license.served  model

A license on a license server.
JSON:

```
{
"id": null,
"license": null,
"owner": null,
"registered_at": null,
"valid_until": null,
"vm_id": 0,
"vm_nameid": ""
}
```

Required fields:

```
license
owner
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
license:
“license.license” object ID. (license.license)
owner:
“license.client” object ID. (license.client)
registered_at:
date when license is assigned to the owner. (datetime)
valid_until:
can be reused after this date. (datetime)
vm_id:
(int)
vm_nameid:
(str[6])

## log.apicall  model

APICall(id, user, timestamp, command, arguments)
JSON:

```
{
"arguments": null,
"command": null,
"id": null,
"timestamp": "func:django.utils.timezone.now",
"user": null
}
```

Required fields:

```
arguments
command
```

Readonly attributes on update:

```
id
```

Fields documentation:
arguments:
(str)
command:
(str[256])
id:
(int)
timestamp:
(datetime)
user:
“auth.user” object ID. (auth.user)

## model.cable  model

A cable connects two ports together.
Internally implemented with an OpenVSWicth and a copy openflow rule.
JSON:

```
{
"conn1": null,
"conn2": null,
"description": "",
"hwaddr": null,
"id": null,
"runtime": null
}
```

Required fields:

```
conn1
conn2
```

Readonly attributes:

```
runtime
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
conn1:
Port connected to one end of the cable. “model.port” object ID. (model.port)
conn2:
Port connected to other end of the cable. “model.port” object ID. (model.port)
description:
(str)
hwaddr:
Internal hardware address used to manage the cable. Automatically filled by the API. (str[17])
id:
(int)
runtime:
Return the runtime element if it exists. (model.cable)

## model.defaultvmaccess  model

DefaultVmAccess(id, vm, type, name, redirect, mode, path, fqdn, dport, fport, fport_idx, _order,
vmaccess_ptr)
Parent model: model.vmaccess model
JSON:

```
{
"_order": null,
"dport": 0,
"fport": 0,
"fport_idx": 0,
"fqdn": "",
"id": null,
"mode": "PRIVATE",
"name": null,
"path": "",
"redirect": null,
"type": null,
"vm": null
}
```

Required fields:

```
_order
name
type
vm
```

Readonly attributes on update:

```
name
type
vm
```

Fields documentation:
_order:
(int)
dport:
Destination port when is not default one. (int)
fport:
Source port, use 0 to use default one, exclusive with fport_idx and redirect. (int)
fport_idx:
Source port index, use 0 to user default one, exclusive with fport and redirect. (int)
fqdn:
Only for HTTP/HTTPS. (str[255])
id:
“model.defaultvmaccess” object ID (int)
mode:
(str[32])
ADMIN:
Access for admin only using frontend
PRIVATE:
Access for admin and guest using frontend
PUBLIC:
Public access
name:
(str[32])
path:
Only for HTTP/HTTPS. (str[256])
redirect:
Use redirection rule, exclusive with fport and fport_idx. “model.portredirect” object ID.
(model.portredirect)
type:
(str[32])
SERIAL:
Serial Console
HTTP:
HTTP
HTTPS:
HTTPS
SSH:
SSH
VNC:
VNC Console
SPICE:
Spice Console
HTTPS2HTTP:
HTTPS to HTTP
vm:
“model.vm” object ID. (model.vm)

## model.device  model

Base model for all devices handled by the Fabric.
Children model:
model.host model
model.router model
model.switch model
model.vm model
JSON:

```
{
"auto_address_network": null,
"config": null,
"description": "",
"fabric": null,
"id": null,
"name": null,
"nameid": null,
"ports": null,
"runtime": null,
"vm_type": null
}
```

Required fields:

```
fabric
name
nameid
```

Readonly attributes:

```
ports
runtime
vm_type
```

Readonly attributes on update:

```
fabric
id
```

Fields and attributes documentation:
auto_address_network:
To automatically assign an address to the peer port when connecting a cable. “model.network” object
ID. (model.network)
config:
The configuration to load on the device. “model.deviceconfig” object ID. (model.deviceconfig)
description:
A device description. (str[128])
fabric:
the fabric. “model.fabric” object ID. (model.fabric)
id:
(int)
name:
The device name. (str[64])
nameid:
Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the
API. (str[6])
ports:
All device’s ports. (?)
runtime:
Return the runtime element if it exists. (model.device)
vm_type:
The VM type. (?)

## model.deviceconfig  model

DeviceConfig(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr,
fabric, fabricstorage_ptr, vm_type, method)
Parent model: model.fabricstorage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"export_name": null,
"fabric": null,
"id": null,
"local_name": null,
"method": "RESTORE",
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null,
"vm_type": null
}
```

Required fields:

```
vm_type
```

Readonly attributes:

```
export_name
size
```

Fields and attributes documentation:
created_at:
(datetime)
export_name:
(?)
fabric:
“model.fabric” object ID. (model.fabric)
id:
“model.deviceconfig” object ID (int)
local_name:
(str[128])
method:
Method to restore a VM configuration. (str[24])
RESTORE:
Restore
BACKUP-APPEND-RESTORE:
Backup-Append-Restore
SCRIPT:
Script
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)
vm_type:
(str[64])

## model.fabric  model

A Fabric represents multiple devices interconnected all together by different virtual networks and
connections.
JSON:

```
{
"console_password": "",
"create_date": "func:django.utils.timezone.now",
"description": "",
"docurl": null,
"export_date": "func:django.utils.timezone.now",
"http_password": "",
"id": null,
"maintainer": null,
"name": null,
"override_pair_hwaddr_prefix": "",
"override_router_pair_hwaddr_prefix": "",
"pair_hwaddr_prefix": null,
"password": null,
"poweron_all_on_boot": false,
"revert_mode": "SCR",
"rt_hwaddr_prefix": null,
"runtime": null,
"sw_hwaddr_prefix": null,
"timeout": 180,
"version": "0.0.0",
"vm_hwaddr_prefix": null
}
```

Required fields:

```
name
password
```

Readonly attributes:

```
export_date
pair_hwaddr_prefix
runtime
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
console_password:
Graphical console access password. (str[64])
create_date:
(datetime)
description:
A short description of the fabric. (str[128])
docurl:
An URL to a zip archive with the fabric documentation. (url)
export_date:
(datetime)
http_password:
Default HTTP password to use when default is not working, use password value if empty. (str[64])
id:
(int)
maintainer:
(email)
name:
The name of the fabric. (str[64])
override_pair_hwaddr_prefix:
Internal peer virtual port OUI. Automatically managed. (str[12])
override_router_pair_hwaddr_prefix:
Internal peer router port OUI. Automatically managed. (str[12])
pair_hwaddr_prefix:
(?)
password:
Default account password to use when default is not working, automatically changed on supported
device. (str[64])
poweron_all_on_boot:
Power-on all devices on Fabric Studio boot. (bool)
revert_mode:
How to use device’s snapshots on fabric/devices install. (str[3])
SCR:
no snapshot at PoC launch
LAS:
use latest snapshots at PoC launch
rt_hwaddr_prefix:
Default OUI to generate router’s port hardware addresses. Automatically filled by the API. (str[12])
runtime:
Return the runtime fabric if it exists. (?)
sw_hwaddr_prefix:
Default OUI to generate switches’s port hardware addresses. Automatically filled by the API. (str[12])
timeout:
Communication timeout in seconds with a device. (int)
version:
(str[128])
vm_hwaddr_prefix:
Default OUI to generate device’s port hardware addresses. Automatically filled by the API. (str[12])

## model.fabricdocstatus  model

FabricDocStatus(id, fabric, status)
JSON:

```
{
"fabric": null,
"id": null,
"status": "NONE"
}
```

Required fields:

```
fabric
```

Readonly attributes on update:

```
id
```

Fields documentation:
fabric:
“model.fabric” object ID. (model.fabric)
id:
(int)
status:
(str[16])
NONE:
No documentation
READY:
Ready
DOWNLOAD:
Downloading
UNVERIFIED:
Unverified
OBSOLETE:
Obsolete
FAILED:
Download failed, no doc

## model.fabricstorage  model

Storage directory for a Fabric related files.
Parent model: storage.storage model
Children model:
model.deviceconfig model
visual.nodeimage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"fabric": null,
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null
}
```

Readonly attributes:

```
size
```

Fields and attributes documentation:
created_at:
(datetime)
fabric:
“model.fabric” object ID. (model.fabric)
id:
“model.fabricstorage” object ID (int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)

## model.host  model

Inner Fabric view of the Fabric host system.
This device allows to attach host system’s ports to other devices through the HostPort .
The host is unique by Fabric and is automatically created with the Fabric.
Parent model: model.device model
JSON:

```
{
"auto_address_network": null,
"config": null,
"description": "",
"fabric": null,
"id": null,
"ipv4dns": null,
"name": null,
"nameid": null
}
```

Required fields:

```
fabric
name
```

Readonly attributes:

```
nameid
```

Readonly attributes on update:

```
fabric
```

Fields and attributes documentation:
auto_address_network:
To automatically assign an address to the peer port when connecting a cable. “model.network” object
ID. (model.network)
config:
The configuration to load on the device. “model.deviceconfig” object ID. (model.deviceconfig)
description:
A device description. (str[128])
fabric:
the fabric. “model.fabric” object ID. (model.fabric)
id:
“model.host” object ID (int)
ipv4dns:
The main nameserver address, system one if empty. (ipaddress)
name:
The device name. (str[64])
nameid:
Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the
API. (str[6])

## model.hostport  model

The host system’s port exposed to the Fabric.
Automatically created with a Fabric and mirror a fortipoc.core.django.system.models.Port  port.
Parent model: model.port model
JSON:

```
{
"cable": null,
"device": null,
"dhcp_service": false,
"egress_nat": false,
"external": null,
"forwarding": true,
"hwaddr": null,
"id": null,
"index": 0,
"ingress_nat": false,
"ipv4addr": null,
"ipv4netmask": null,
"name": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null,
"type": null
}
```

Required fields:

```
device
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
type
```

Readonly attributes on update:

```
device
index
name
```

Fields and attributes documentation:
cable:
(optional[model.cable])
device:
“model.device” object ID. (model.device)
dhcp_service:
Enable dhcp server (only for internal ports). (bool)
egress_nat:
Masquerade egress traffic. (bool)
external:
The external host port, only managed by the API. “system.port” object ID. (system.port)
forwarding:
(bool)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
“model.hostport” object ID (int)
index:
(int)
ingress_nat:
Masquerade ingress traffic. (bool)
ipv4addr:
(ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
(optional[str])
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.hostport)
type:
(?)

## model.installafter  model

Track list of devices that must be started prior to the device.
JSON:

```
{
"after": null,
"id": null,
"vm": null
}
```

Required fields:

```
vm
```

Readonly attributes on update:

```
id
```

Fields documentation:
after:
The list of all VM to be installed before the VM. (model.vm)
id:
(int)
vm:
The VM to be started after all other listed VM. “model.vm” object ID. (model.vm)

## model.installpolicy  model

InstallPolicy(id, mode, fabric, max_queue)
JSON:

```
{
"fabric": null,
"id": null,
"max_queue": 0,
"mode": "PAR"
}
```

Required fields:

```
fabric
```

Readonly attributes on update:

```
id
```

Fields documentation:
fabric:
“model.fabric” object ID. (model.fabric)
id:
(int)
max_queue:
(int)
mode:
(str[3])
SEQ:
Power-on devices in sequence
PAR:
Power-on all devices in parallel

## model.network  model

To help managing networks defined in a Fabric and assigning addresses to devices ports.
JSON:

```
{
"description": "",
"fabric": null,
"id": null,
"ipv4dns1": null,
"ipv4dns2": null,
"ipv4gateway": null,
"ipv4netmask": null,
"ipv4network": null,
"name": null
}
```

Required fields:

```
fabric
ipv4netmask
ipv4network
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
description:
(str[128])
fabric:
The fabric. “model.fabric” object ID. (model.fabric)
id:
(int)
ipv4dns1:
First nameserver address for this network. (ipaddress)
ipv4dns2:
Second nameserver address for this network. (ipaddress)
ipv4gateway:
Default gateway for this network. (ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
ipv4network:
Network subnet. (ipaddress)
name:
Name of the network. (str[64])

## model.port  model

Base class for all device’s port that can be interconnected.
Children model:
model.hostport model
model.routerport model
model.switchport model
model.switchlocalport model
model.vmport model
JSON:

```
{
"cable": null,
"device": null,
"hwaddr": null,
"id": null,
"index": 0,
"name": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null
}
```

Required fields:

```
device
hwaddr
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
```

Readonly attributes on update:

```
device
id
index
name
```

Fields and attributes documentation:
cable:
(optional[model.cable])
device:
“model.device” object ID. (model.device)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
(int)
index:
(int)
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
(optional[str])
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.port)

## model.portredirect  model

PortRedirect(id, device, name, from_port, to_addr, to_port, snat, socktype, description, enabled)
JSON:

```
{
"description": "",
"device": null,
"enabled": true,
"from_port": null,
"id": null,
"name": null,
"snat": true,
"socktype": "TCP",
"to_addr": null,
"to_port": null
}
```

Required fields:

```
device
from_port
name
to_addr
to_port
```

Readonly attributes on update:

```
id
```

Fields documentation:
description:
(str[256])
device:
“model.host” object ID. (model.host)
enabled:
(bool)
from_port:
(int)
id:
(int)
name:
(str[64])
snat:
Use to_addr as source. (bool)
socktype:
(str[3])
UDP:
Sock Dgram
TCP:
Sock Stream
to_addr:
(ipaddress)
to_port:
(int)

## model.router  model

A router is used to connect multiple ports from different networks.
A router can define a default route.
A router runs dnsmasq, tftp and ftp daemons.
Internally a router is managed in a dedicated netns to isolate traffic.
Parent model: model.device model
JSON:

```
{
"auto_address_network": null,
"auto_params_network": null,
"config": null,
"description": "",
"fabric": null,
"id": null,
"ipv4dns": null,
"ipv4gateway": null,
"name": null,
"nameid": null,
"ports": null,
"runtime": null,
"vm_type": null
}
```

Required fields:

```
fabric
name
```

Readonly attributes:

```
ports
runtime
vm_type
```

Readonly attributes on update:

```
fabric
```

Fields and attributes documentation:
auto_address_network:
To automatically assign an address to the peer port when connecting a cable. “model.network” object
ID. (model.network)
auto_params_network:
Use this network default gateway and DNS’. “model.network” object ID. (model.network)
config:
The configuration to load on the device. “model.deviceconfig” object ID. (model.deviceconfig)
description:
A device description. (str[128])
fabric:
the fabric. “model.fabric” object ID. (model.fabric)
id:
“model.router” object ID (int)
ipv4dns:
The router nameserver address, none if empty. (ipaddress)
ipv4gateway:
The router’s default gateway. (ipaddress)
name:
The device name. (str[64])
nameid:
Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the
API. (str[6])
ports:
All device’s ports. (?)
runtime:
Return the runtime element if it exists. (model.router)
vm_type:
The VM type. (?)

## model.routerport  model

A router’s port.
Parent model: model.port model
JSON:

```
{
"addrmode": "STA",
"auto_config": true,
"cable": null,
"device": null,
"dhcp_service": false,
"egress_nat": false,
"hwaddr": null,
"id": null,
"index": 0,
"ingress_nat": false,
"ipv4addr": null,
"ipv4netmask": null,
"mgmt": false,
"mtu": 0,
"name": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null
}
```

Required fields:

```
device
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
```

Readonly attributes on update:

```
device
index
name
```

Fields and attributes documentation:
addrmode:
(str[4])
STA:
static
DHCP:
dhcp
auto_config:
Address is configured by the Fabric Studio. (bool)
cable:
(optional[model.cable])
device:
“model.device” object ID. (model.device)
dhcp_service:
Enable dhcp server. (bool)
egress_nat:
Masquerade egress traffic. (bool)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
“model.routerport” object ID (int)
index:
(int)
ingress_nat:
Masquerade ingress traffic. (bool)
ipv4addr:
(ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
mgmt:
(bool)
mtu:
Force MTU of the interface, use 0 for system default. (int)
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
(optional[str])
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.routerport)

## model.runtimedhcpentry  model

RuntimeDHCPEntry(id, router, port_id, nameid, hwaddr, ipv4addr, ipv4gateway, ipv4dns1, ipv4dns2,
options)
JSON:

```
{
"hwaddr": null,
"id": null,
"ipv4addr": null,
"ipv4dns1": null,
"ipv4dns2": null,
"ipv4gateway": null,
"nameid": null,
"options": "",
"port_id": null,
"router": null
}
```

Required fields:

```
hwaddr
ipv4addr
nameid
port_id
router
```

Readonly attributes on update:

```
id
```

Fields documentation:
hwaddr:
(str[17])
id:
(int)
ipv4addr:
(ipaddress)
ipv4dns1:
(ipaddress)
ipv4dns2:
(ipaddress)
ipv4gateway:
(ipaddress)
nameid:
(str[16])
options:
Options in TOML format. (str)
port_id:
(int)
router:
“model.device” object ID. (model.device)

## model.switch  model

A switch is used to connect multiple ports.
Internally a router is managed by an OpenVSwitch bridge.
Parent model: model.device model
JSON:

```
{
"auto_address_network": null,
"config": null,
"description": "",
"fabric": null,
"id": null,
"mgmt": false,
"name": null,
"nameid": null,
"ports": null,
"runtime": null,
"vm_type": null
}
```

Required fields:

```
fabric
name
```

Readonly attributes:

```
ports
runtime
vm_type
```

Readonly attributes on update:

```
fabric
```

Fields and attributes documentation:
auto_address_network:
To automatically assign an address to the peer port when connecting a cable. “model.network” object
ID. (model.network)
config:
The configuration to load on the device. “model.deviceconfig” object ID. (model.deviceconfig)
description:
A device description. (str[128])
fabric:
the fabric. “model.fabric” object ID. (model.fabric)
id:
“model.switch” object ID (int)
mgmt:
Is it a management switch or not. (bool)
name:
The device name. (str[64])
nameid:
Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the
API. (str[6])
ports:
All device’s ports. (?)
runtime:
Return the runtime element if it exists. (model.switch)
vm_type:
The VM type. (?)

## model.switchlocalport  model

Internal. The default port created with the switch.
Parent model: model.port model
JSON:

```
{
"cable": null,
"device": null,
"hwaddr": null,
"id": null,
"index": 0,
"ipv4addr": null,
"ipv4netmask": null,
"name": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null
}
```

Required fields:

```
device
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
```

Readonly attributes on update:

```
device
index
name
```

Fields and attributes documentation:
cable:
(optional[model.cable])
device:
“model.device” object ID. (model.device)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
“model.switchlocalport” object ID (int)
index:
(int)
ipv4addr:
(ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
A Switch Local Port has no pair hwaddr, always return None. (?)
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.switchlocalport)

## model.switchport  model

A switch port.
Parent model: model.port model
JSON:

```
{
"cable": null,
"device": null,
"hwaddr": null,
"id": null,
"index": 0,
"mode": "default",
"name": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null,
"trunk": "",
"vlan": 0
}
```

Required fields:

```
device
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
```

Readonly attributes on update:

```
device
index
name
```

Fields and attributes documentation:
cable:
(optional[model.cable])
device:
“model.device” object ID. (model.device)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
“model.switchport” object ID (int)
index:
(int)
mode:
(str[32])
default:
Default
access:
Access
native-tagged:
Native Tagged
native-untagged:
Native Untagged
trunk:
Trunk
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
A Switch Port has no pair hwaddr, always return None. (?)
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.switchport)
trunk:
Comma separated list of VLANs or VLAN ranges. (str[10000])
vlan:
Port native VLAN. (int)

## model.trafficcontrol  model

Ingress traffic control for a port.
JSON:

```
{
"bandwidth": 0,
"bucket_size": 15000,
"corrupt": 0,
"delay": 0,
"duplicate": 0,
"id": null,
"jitter": 0,
"loss": 0,
"override": false,
"port": null,
"reorder": 0
}
```

Readonly attributes:

```
override
port
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
bandwidth:
in bps, 0 is no bandwidth limit, minimum is 8. (int)
bucket_size:
bucket size in bytes. (int)
corrupt:
(float)
delay:
Delay in ms. (int)
duplicate:
(float)
id:
(int)
jitter:
Jitter in ms. (int)
loss:
(float)
override:
(bool)
port:
“model.port” object ID. (model.port)
reorder:
Requires delay. (float)

## model.vm  model

Represent a device running in a virtual machine (either KVM or LXC).
Parent model: model.device model
JSON:

```
{
"auto_address_network": null,
"auto_params_network": null,
"config": null,
"console_password": "",
"description": "",
"fabric": null,
"firmware": null,
"http_password": "",
"id": null,
"ipv4dns1": null,
"ipv4dns2": null,
"ipv4gateway": null,
"mgmt_port": null,
"name": null,
"nameid": null,
"password": "",
"port_idx": null,
"ports": null,
"poweron_on_boot": false,
"poweron_on_install": true,
"runtime": null,
"timeout": 0,
"uuid": null,
"vm_type": null
}
```

Required fields:

```
fabric
firmware
name
port_idx
```

Readonly attributes:

```
mgmt_port
ports
runtime
vm_type
```

Readonly attributes on update:

```
fabric
```

Fields and attributes documentation:
auto_address_network:
To automatically assign an address to the peer port when connecting a cable. “model.network” object
ID. (model.network)
auto_params_network:
Use this network default gateway and DNS’. “model.network” object ID. (model.network)
config:
The configuration to load on the device. “model.deviceconfig” object ID. (model.deviceconfig)
console_password:
Graphical console access password. Supersed Fabric console password if not empty. (str[64])
description:
A device description. (str[128])
fabric:
the fabric. “model.fabric” object ID. (model.fabric)
firmware:
The firmware to run on this VM. “repository.firmware” object ID. (repository.firmware)
http_password:
Default HTTP account password to use when default is not working. Supersed Fabric HTTP
password if not empty. (str[64])
id:
“model.vm” object ID (int)
ipv4dns1:
The primary nameserver to configure on this VM. (ipaddress)
ipv4dns2:
The secondary nameserver to configure on this VM. (ipaddress)
ipv4gateway:
The default gateway to configure on this VM. (ipaddress)
mgmt_port:
Return management port. (model.vmport)
name:
The device name. (str[64])
nameid:
Unique short name identifier by fabric. Used internally to name resources. Automatically filled by the
API. (str[6])
password:
Default account password to use when default is not working, automatically changed on supported
device. Supersed Fabric password if not empty. (str[64])
port_idx:
Port forwarding index for automatic forwarding rules, automatically generated if null. (int)
ports:
Ports of this VM. (list[model.vmport])
poweron_on_boot:
Should the device be powered on after the Fabric Studio boot. (bool)
poweron_on_install:
Should the device be powered on during the Fabric installation. (bool)
runtime:
Return the runtime element if it exists. (model.vm)
timeout:
When 0 use Fabric global timeout. (int)
uuid:
VM UUID, automatically generated if empty. (str[36])
vm_type:
The VM type. (str)

## model.vmaccess  model

VmAccess(id, vm, type, name, redirect, mode, path, fqdn, dport, fport, fport_idx, _order)
Children model:
model.defaultvmaccess model
JSON:

```
{
"_order": null,
"dport": 0,
"fport": 0,
"fport_idx": 0,
"fqdn": "",
"id": null,
"mode": "PRIVATE",
"name": null,
"path": "",
"redirect": null,
"type": null,
"vm": null
}
```

Required fields:

```
_order
name
type
vm
```

Readonly attributes on update:

```
id
name
type
vm
```

Fields documentation:
_order:
(int)
dport:
Destination port when is not default one. (int)
fport:
Source port, use 0 to use default one, exclusive with fport_idx and redirect. (int)
fport_idx:
Source port index, use 0 to user default one, exclusive with fport and redirect. (int)
fqdn:
Only for HTTP/HTTPS. (str[255])
id:
(int)
mode:
(str[32])
ADMIN:
Access for admin only using frontend
PRIVATE:
Access for admin and guest using frontend
PUBLIC:
Public access
name:
(str[32])
path:
Only for HTTP/HTTPS. (str[256])
redirect:
Use redirection rule, exclusive with fport and fport_idx. “model.portredirect” object ID.
(model.portredirect)
type:
(str[32])
SERIAL:
Serial Console
HTTP:
HTTP
HTTPS:
HTTPS
SSH:
SSH
VNC:
VNC Console
SPICE:
Spice Console
HTTPS2HTTP:
HTTPS to HTTP
vm:
“model.vm” object ID. (model.vm)

## model.vmdisk  model

Represent a Vm disk.
Disk are declared or not in the meta.
When disks are not extra disks:
A static disk is listed in the meta with a declared size of 0, it’s a disk from the firmware. It can be
extended: capacity >= declared. If capacity < declared, the capacity is ignored. By default capacity is
0.
A dynamic disk is listed in the meta with a declared size > 0, it’s not a disk from the firmware, it’s
created empty. It can be extended or shrinked: 0 < capacity. By default capacity is set to declared
value.
When disks are extra disks:
A manually added disk in the DB with a declared size of 0, the capacity > 0. The disk is created
empty.
A static disk, result of a firmware backup, the declared size > 0 but it’s a disk from the firmware. It can
be extended: capacity >= declared. If capacity < declared, the capacity is ignored.
All sizes are in MB.
declared
(from meta)
capacity
(DB)
extra
0 0 > 0 > 0
>= 0 > 0 >
0 > 0
False True
False True
static disk, build from firmware extra disk, manually added
dynamic disk, empty on build extra disk, build from firmware
JSON:

```
{
"_order": null,
"capacity": null,
"declared": null,
"extra": false,
"id": null,
"name": "",
"physical": 0,
"vm": null
}
```

Required fields:

```
_order
capacity
declared
vm
```

Readonly attributes:

```
name
physical
```

Readonly attributes on update:

```
declared
extra
id
vm
```

Fields and attributes documentation:
_order:
(int)
capacity:
expected disk size in MB for VM. (int)
declared:
size in MB: declared in the meta. (int)
extra:
Extra disk. (bool)
id:
(int)
name:
(str[256])
physical:
Static disk physical size in the firmware archive if available. (int)
vm:
“model.vm” object ID. (model.vm)

## model.vmlicense  model

Link a VM to a license. This is a weak reference, so if license is removed we can still know which
license it was linked to.
A license can only be associated to one VM in a Fabric. But the license can be associated to multiple
VMs in multiple Fabric.
serial_number is always synchronized on save if a license is present (license) and serial_number or
license must be updated (update_fields).
JSON:

```
{
"id": null,
"license": null,
"mode": "AUTO",
"serial_number": "",
"served": null,
"supported": "",
"vm": null
}
```

Readonly attributes:

```
served
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
id:
(int)
license:
“license.license” object ID. (license.license)
mode:
Method to select a license for the VM. (str[8])
NONE:
No License
AUTO:
Auto
CUSTOM:
Prefered serial number/license
serial_number:
(str[128])
served:
“license.license” object ID. (license.license)
supported:
Supported licenses type NONE, FLEX or LIC separated by comma, when empty use meta default.
(str[16])
vm:
“model.vm” object ID. (model.vm)

## model.vmparameters  model

VmParameters  are used to override the default meta values.
Override is a XML file, possible syntax:

```
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
```

Problem: this syntax requires to repeat multiple time the same tree/xpath …
JSON:

```
{
"as_version": "",
"boot_menu_time": 0,
"cpu_count": 0,
"cpu_mode": "DECLARED",
"cpu_model": "",
"cpu_set": "",
"expert": "",
"hugepages": false,
"id": null,
"install_license": "FIRMWARE",
"memory": 0,
"meta_patch": "",
"override": null,
"use_firmware_uuid": false,
"validate_license_wait": null,
"video": "",
"vm": null
}
```

Required fields:

```
vm
```

Readonly attributes on update:

```
id
```

Fields documentation:
as_version:
Handle the firmware as this specific version. (str[64])
boot_menu_time:
(int)
cpu_count:
Number of CPU, when 0 use default value from meta. (int)
cpu_mode:
(str[16])
DECLARED:
As declared in firmware meta
PASSTHROUGH:
Full passthrough mode
HYPERVISOR:
Default hypervisor CPU
MANUAL:
Selected overriden CPU
cpu_model:
Override CPU model, CPU mode must be set accordingly. (str[64])
cpu_set:
comma separated list of CPUs number or CPUs range. (str[512])
expert:
Expert parameters in TOML format. (str)
hugepages:
Use 1GB hugepages if available. (bool)
id:
(int)
install_license:
Install the license before the configuration or not, when undefined use meta default. (str[16])
FIRST:
Install license before configuration
LAST:
Install license after configuration
FIRMWARE:
Default installation order from firmware meta
memory:
VM memory size, when 0 use default value from meta. (int)
meta_patch:
(str)
override:
XML to update libvirt VM XML definition. (?:model.VmParameters.override)
use_firmware_uuid:
Use VM UUID stored in the firmware meta, for custom firmware it can be required if disk are
encrytpted using the VM UUID. (bool)
validate_license_wait:
not set: default value, 0: infinite wait, time in seconds, negative: no wait. (int)
video:
Override video driver, when empty use default value from meta. (str[64])
vm:
“model.vm” object ID. (model.vm)

## model.vmport  model

A VM port.
Parent model: model.port model
JSON:

```
{
"addrmode": "STA",
"auto_config": true,
"cable": null,
"copy_hwaddr_from_peer": false,
"device": null,
"dhcp_server": null,
"hwaddr": null,
"id": null,
"index": 0,
"ipv4addr": null,
"ipv4netmask": null,
"license_ip": false,
"mgmt": false,
"mtu": 0,
"name": null,
"network": null,
"override_pair_hwaddr": "",
"pair_hwaddr": null,
"peer": null,
"runtime": null
}
```

Required fields:

```
device
name
```

Readonly attributes:

```
cable
pair_hwaddr
peer
runtime
```

Readonly attributes on update:

```
device
index
name
```

Fields and attributes documentation:
addrmode:
(str[4])
STA:
static
DHCP:
dhcp
auto_config:
Address is configured by the Fabric Studio. (bool)
cable:
(optional[model.cable])
copy_hwaddr_from_peer:
Override HW address with the external System Host port peer on runtime. (bool)
device:
“model.device” object ID. (model.device)
dhcp_server:
Native router that offers the address or empty if it’s another device. “model.device” object ID.
(model.device)
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
“model.vmport” object ID (int)
index:
(int)
ipv4addr:
(ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
license_ip:
License is bound to this port IP. (bool)
mgmt:
(bool)
mtu:
Force MTU of the interface, use 0 for system default. (int)
name:
Interface name. (str[8])
network:
To configure gateway and nameserver served by the native DHCP service. “model.network” object
ID. (model.network)
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
pair_hwaddr:
(optional[str])
peer:
(optional[model.port])
runtime:
Return the runtime element if it exists. (model.vmport)

## model.vmstorage  model

Storage to store files related to a VM.
Storage is destroyed with the VM.
Parent model: storage.storage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null,
"vm": null
}
```

Required fields:

```
vm
```

Readonly attributes:

```
size
```

Fields and attributes documentation:
created_at:
(datetime)
id:
“model.vmstorage” object ID (int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)
vm:
“model.vm” object ID. (model.vm)

## oauth2_provider.accesstoken  model

AccessToken(id, user, source_refresh_token, token, token_checksum, id_token, application, expires,
scope, created, updated)
JSON:

```
{
"application": null,
"created": null,
"expires": null,
"id": null,
"id_token": null,
"scope": null,
"source_refresh_token": null,
"token": null,
"token_checksum": null,
"updated": null,
"user": null
}
```

Required fields:

```
expires
token
token_checksum
```

Readonly attributes on update:

```
id
```

Fields documentation:
application:
“oauth2_provider.application” object ID. (oauth2_provider.application)
created:
(datetime)
expires:
(datetime)
id:
(int)
id_token:
“oauth2_provider.idtoken” object ID. (oauth2_provider.idtoken)
scope:
(str)
source_refresh_token:
“oauth2_provider.refreshtoken” object ID. (oauth2_provider.refreshtoken)
token:
(str)
token_checksum:
(str[64])
updated:
(datetime)
user:
“auth.user” object ID. (auth.user)

## oauth2_provider.application  model

Application(id, client_id, user, redirect_uris, post_logout_redirect_uris, client_type,
authorization_grant_type, client_secret, hash_client_secret, name, skip_authorization, created,
updated, algorithm, allowed_origins)
JSON:

```
{
"algorithm": "",
"allowed_origins": "",
"authorization_grant_type": null,
"client_id": "func:oauth2_provider.generators.generate_client_id",
"client_secret": "func:oauth2_provider.generators.generate_client_secret"
"client_type": null,
"created": null,
"hash_client_secret": true,
"id": null,
"name": null,
"post_logout_redirect_uris": "",
"redirect_uris": null,
"skip_authorization": false,
"updated": null,
"user": null
}
```

Required fields:

```
authorization_grant_type
client_type
```

Readonly attributes on update:

```
id
```

Fields documentation:
algorithm:
(str[5])
:: No OIDC support :RS256: RSA with SHA-2 256 :HS256: HMAC with SHA-2 256
allowed_origins:
Allowed origins list to enable CORS, space separated. (str)
authorization_grant_type:
(str[32])
authorization-code:
Authorization code
implicit:
Implicit
password:
Resource owner password-based
client-credentials:
Client credentials
openid-hybrid:
OpenID connect hybrid
client_id:
(str[100])
client_secret:
Hashed on Save. Copy it now if this is a new secret. (str[255])
client_type:
(str[32])
confidential:
Confidential
public:
Public
created:
(datetime)
hash_client_secret:
(bool)
id:
(int)
name:
(str[255])
post_logout_redirect_uris:
Allowed Post Logout URIs list, space separated. (str)
redirect_uris:
Allowed URIs list, space separated. (str)
skip_authorization:
(bool)
updated:
(datetime)
user:
“auth.user” object ID. (auth.user)

## oauth2_provider.grant  model

Grant(id, user, code, application, expires, redirect_uri, scope, created, updated, code_challenge,
code_challenge_method, nonce, claims)
JSON:

```
{
"application": null,
"claims": null,
"code": null,
"code_challenge": "",
"code_challenge_method": "",
"created": null,
"expires": null,
"id": null,
"nonce": "",
"redirect_uri": null,
"scope": null,
"updated": null,
"user": null
}
```

Required fields:

```
application
code
expires
redirect_uri
user
```

Readonly attributes on update:

```
id
```

Fields documentation:
application:
“oauth2_provider.application” object ID. (oauth2_provider.application)
claims:
(str)
code:
(str[255])
code_challenge:
(str[128])
code_challenge_method:
(str[10])
plain:
plain
S256:
S256
created:
(datetime)
expires:
(datetime)
id:
(int)
nonce:
(str[255])
redirect_uri:
(str)
scope:
(str)
updated:
(datetime)
user:
“auth.user” object ID. (auth.user)

## oauth2_provider.idtoken  model

IDToken(id, user, jti, application, expires, scope, created, updated)
JSON:

```
{
"application": null,
"created": null,
"expires": null,
"id": null,
"jti": "func:uuid.uuid4",
"scope": null,
"updated": null,
"user": null
}
```

Required fields:

```
expires
```

Readonly attributes on update:

```
id
```

Fields documentation:
application:
“oauth2_provider.application” object ID. (oauth2_provider.application)
created:
(datetime)
expires:
(datetime)
id:
(int)
jti:
(uuid)
scope:
(str)
updated:
(datetime)
user:
“auth.user” object ID. (auth.user)

## oauth2_provider.refreshtoken  model

RefreshToken(id, user, token, application, access_token, token_family, created, updated, revoked)
JSON:

```
{
"access_token": null,
"application": null,
"created": null,
"id": null,
"revoked": null,
"token": null,
"token_family": null,
"updated": null,
"user": null
}
```

Required fields:

```
application
token
user
```

Readonly attributes on update:

```
id
```

Fields documentation:
access_token:
“oauth2_provider.accesstoken” object ID. (oauth2_provider.accesstoken)
application:
“oauth2_provider.application” object ID. (oauth2_provider.application)
created:
(datetime)
id:
(int)
revoked:
(datetime)
token:
(str[255])
token_family:
(uuid)
updated:
(datetime)
user:
“auth.user” object ID. (auth.user)

## repository.firmware  model

VM firmware.
Parent model: repository.repositoryfile model
JSON:

```
{
"added_at": null,
"backup_state": null,
"build": 0,
"diff_from": null,
"expiration": null,
"hexdigest": null,
"id": null,
"is_diff": false,
"major": 0,
"meta_hexdigest": null,
"minor": 0,
"original_detail": null,
"patch": 0,
"path": null,
"repository": null,
"revision": 0,
"size": null,
"status": "remote",
"version_s": "",
"vm_type": "BASIC"
}
```

Required fields:

```
hexdigest
meta_hexdigest
path
repository
size
```

Readonly attributes:

```
backup_state
diff_from
is_diff
original_detail
```

Fields and attributes documentation:
added_at:
Date when firmware information has been added locally. (datetime)
backup_state:
(BackupState)
build:
(int)
diff_from:
“repository.firmware” object ID. (repository.firmware)
expiration:
(date)
hexdigest:
(str[512])
id:
“repository.firmware” object ID (int)
is_diff:
Is the firmware a diff snapshot firmware. (bool)
major:
(int)
meta_hexdigest:
Checksum of the file meta information. (str[512])
minor:
(int)
original_detail:
Return original firmware details. (fortipoc.repository.django.client._class.OriginalInformation | None)
patch:
(int)
path:
(str[512])
repository:
“repository.repository” object ID. (repository.repository)
revision:
(int)
size:
(int)
status:
Status of the file. (str[16])
unknown:
Unknown
remote:
Remote
downloaded:
Download
ready:
Ready
obsolete:
Obsolete
deleted:
Deleted
version_s:
(str[256])
vm_type:
(str[32])

## repository.remotefile  model

A file coming from a remote repository.
JSON:

```
{
"file": null,
"id": null
}
```

Required fields:

```
file
```

Readonly attributes on update:

```
id
```

Fields documentation:
file:
“repository.repositoryfile” object ID. (repository.repositoryfile)
id:
(int)

## repository.repository  model

A repository that contains firmwares and Fabrics.
JSON:

```
{
"active": true,
"chksum": true,
"cli": false,
"client_key": null,
"client_pem": null,
"date": null,
"description": "",
"hide": false,
"id": null,
"name": null,
"private_ca": null,
"reg": false,
"signed": false,
"source": null,
"split": false,
"sync": null
}
```

Required fields:

```
name
source
```

Readonly attributes on update:

```
id
```

Fields documentation:
active:
active repository. (bool)
chksum:
validate checksum of files. (bool)
cli:
added by CLI. (bool)
client_key:
(?:repository.Repository.client_key)
client_pem:
(?:repository.Repository.client_pem)
date:
repository update date. (datetime)
description:
(str[128])
hide:
hide repository. (bool)
id:
(int)
name:
name of the repository. (str[64])
private_ca:
“certificates.cacertificate” object ID. (certificates.cacertificate)
reg:
added by registration. (bool)
signed:
repository is signed by a SSL certificate. (bool)
source:
Repository location. (url)
split:
allow split directory. (bool)
sync:
repository last synchronization date. (datetime)

## repository.repositoryfile  model

A file stored in a repository.
Children model:
repository.firmware model
repository.template model
JSON:

```
{
"expiration": null,
"hexdigest": null,
"id": null,
"meta_hexdigest": null,
"path": null,
"repository": null,
"size": null,
"status": "remote"
}
```

Required fields:

```
hexdigest
meta_hexdigest
path
repository
size
```

Readonly attributes on update:

```
id
```

Fields documentation:
expiration:
(date)
hexdigest:
(str[512])
id:
(int)
meta_hexdigest:
Checksum of the file meta information. (str[512])
path:
(str[512])
repository:
“repository.repository” object ID. (repository.repository)
size:
(int)
status:
Status of the file. (str[16])
unknown:
Unknown
remote:
Remote
downloaded:
Download
ready:
Ready
obsolete:
Obsolete
deleted:
Deleted

## repository.serverzone  model

ServerZone(id, zone, hostname, cname)
JSON:

```
{
"cname": null,
"hostname": null,
"id": null,
"zone": null
}
```

Required fields:

```
cname
hostname
zone
```

Readonly attributes on update:

```
id
```

Fields documentation:
cname:
(str[255])
hostname:
(str[255])
id:
(int)
zone:
(str[64])

## repository.template  model

A Fabric template.
Parent model: repository.repositoryfile model
JSON:

```
{
"create_date": "1945-11-13 00:00:00+00:00",
"description": "",
"docurl": null,
"expiration": null,
"export_date": "1945-11-13 00:00:00+00:00",
"hexdigest": null,
"id": null,
"maintainer": null,
"meta_hexdigest": null,
"name": null,
"path": null,
"repository": null,
"size": null,
"status": "remote",
"version": "0.0.0"
}
```

Required fields:

```
hexdigest
meta_hexdigest
path
repository
size
```

Fields documentation:
create_date:
(datetime)
description:
(str[128])
docurl:
(url)
expiration:
(date)
export_date:
(datetime)
hexdigest:
(str[512])
id:
“repository.template” object ID (int)
maintainer:
(email)
meta_hexdigest:
Checksum of the file meta information. (str[512])
name:
(str[64])
path:
(str[512])
repository:
“repository.repository” object ID. (repository.repository)
size:
(int)
status:
Status of the file. (str[16])
unknown:
Unknown
remote:
Remote
downloaded:
Download
ready:
Ready
obsolete:
Obsolete
deleted:
Deleted
version:
(str[128])

## runtime.fabricparameters  model

Env.
JSON:

```
{
"environment": null,
"fabric": null,
"id": null
}
```

Required fields:

```
fabric
```

Readonly attributes on update:

```
id
```

Fields documentation:
environment:
“model.deviceconfig” object ID. (model.deviceconfig)
fabric:
“runtime.fabric” object ID. (runtime.fabric)
id:
(int)

## runtime.runtimetask  model

A global task related to the runtime.
Parent model: task.task model
JSON:

```
{
"author": null,
"created_date": "func:django.utils.timezone.now",
"id": null,
"launched_date": null,
"monitor_error": "",
"monitor_pid": 0,
"name": null,
"parent": null,
"related_obj": null,
"returncode": null,
"returned_date": null,
"signal": null
}
```

Required fields:

```
name
```

Fields documentation:
author:
“auth.user” object ID. (auth.user)
created_date:
Task Creation date. (datetime)
id:
“runtime.runtimetask” object ID (int)
launched_date:
Task launched date. (datetime)
monitor_error:
error returned by the monitoring process. (str[512])
monitor_pid:
PID of monitoring process. (int)
name:
Task name. (str[256])
parent:
“task.task” object ID. (task.task)
related_obj:
“task.taskobject” object ID. (task.taskobject)
returncode:
Task command return code. (int)
returned_date:
Task returned date. (datetime)
signal:
Task command exited on this signal. (int)

## runtime.vmstatus  model

Information about a VM.
JSON:

```
{
"created": null,
"id": null,
"last_modified": null,
"licensed": false,
"post_boot_prepared": false,
"powered": false,
"pre_boot_prepared": false,
"vm": null
}
```

Required fields:

```
vm
```

Readonly attributes on update:

```
id
```

Fields documentation:
created:
(datetime)
id:
(int)
last_modified:
(datetime)
licensed:
Is the VM been licensed. (bool)
post_boot_prepared:
Is the VM been post configured. (bool)
powered:
Is the VM power-on or not. (bool)
pre_boot_prepared:
Is the VM been pre configured. (bool)
vm:
“model.vm” object ID. (model.vm)

## sessions.session  model

Django provides full support for anonymous sessions. The session framework lets you store and
retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the
sending and receiving of cookies. Cookies contain a session ID – not the data itself.
The Django sessions framework is entirely cookie-based. It does not fall back to putting session IDs
in URLs. This is an intentional design decision. Not only does that behavior make URLs ugly, it
makes your site vulnerable to session-ID theft via the “Referer” header.
For complete documentation on using Sessions in your code, consult the sessions documentation
that is shipped with Django (also available on the Django web site).
JSON:

```
{
"expire_date": null,
"session_data": null,
"session_key": null
}
```

Required fields:

```
expire_date
session_data
session_key
```

Readonly attributes on update:

```
session_key
```

Fields documentation:
expire_date:
(datetime)
session_data:
(str)
session_key:
(str[40])

## storage.pstorage  model

PStorage(id, parent, created_at, modified_at, name, local_name, mime_types)
Children model:
license.license model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null
}
```

Readonly attributes:

```
size
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
created_at:
(datetime)
id:
(int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.pstorage” object ID. (storage.pstorage)
size:
(?)

## storage.storage  model

Storage(id, parent, created_at, modified_at, name, local_name, mime_types)
Children model:
model.fabricstorage model
model.vmstorage model
task.taskstorage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null
}
```

Readonly attributes:

```
size
```

Readonly attributes on update:

```
id
```

Fields and attributes documentation:
created_at:
(datetime)
id:
(int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)

## system.firewalladdress  model

Address that can access the Fabric Studio.
JSON:

```
{
"enabled": true,
"id": null,
"ipaddr": null,
"policy": null
}
```

Required fields:

```
ipaddr
policy
```

Readonly attributes on update:

```
id
ipaddr
policy
```

Fields documentation:
enabled:
(bool)
id:
(int)
ipaddr:
(?:system.FirewallAddress.ipaddr)
policy:
(str[8])
TRUSTED:
Trusted address
BLOCKED:
Blocked address

## system.kernelmodule  model

KernelModule(id, name, policy)
JSON:

```
{
"id": null,
"name": null,
"policy": null
}
```

Required fields:

```
name
policy
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
name:
(str[255])
policy:
(str[32])
BLOCK:
Block module
LOAD:
Load module

## system.parameter  model

A simple key/value pair associated to a user.
A parameter can only be changed by it’s owner.
JSON:

```
{
"id": null,
"name": null,
"owner": null,
"value": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
name
owner
```

Fields documentation:
id:
(int)
name:
(str[255])
owner:
“auth.user” object ID. (auth.user)
value:
(str[255])

## system.port  model

A system port attached to a physical interface.
JSON:

```
{
"addrmode": "STA",
"hwaddr": null,
"id": null,
"index": 0,
"ipv4addr": null,
"ipv4netmask": null,
"mgmt": false,
"missing": true,
"name": null,
"override_pair_hwaddr": "",
"status": "Enabled",
"sysname": null
}
```

Required fields:

```
hwaddr
name
sysname
```

Readonly attributes on update:

```
id
```

Fields documentation:
addrmode:
(str[4])
STA:
static
DHCP:
dhcp
hwaddr:
Device side port hardware address. Automatically filled by the API. (str[17])
id:
(int)
index:
(int)
ipv4addr:
(ipaddress)
ipv4netmask:
Network mask as cidr or quad-dotted notation. (ipaddress)
mgmt:
(bool)
missing:
True is the interface does not exists. (bool)
name:
Interface name. (str[8])
override_pair_hwaddr:
Internal peer virtual port hardware address. Automatically managed. (str[17])
status:
(str[16])
Disabled:
Disabled
Enabled:
Enabled
sysname:
Interface name. (str[16])

## task.acktask  model

AckTask(id, task, user, ack_date)
JSON:

```
{
"ack_date": "func:django.utils.timezone.now",
"id": null,
"task": null,
"user": null
}
```

Required fields:

```
task
user
```

Readonly attributes on update:

```
id
```

Fields documentation:
ack_date:
Task Acknowledge date. (datetime)
id:
(int)
task:
“task.task” object ID. (task.task)
user:
“auth.user” object ID. (auth.user)

## task.task  model

A task tracks an asynchronous process monitored by a monitor process.
The returncode  is the command exit code, it should be betwwen 0 and 255. On normal termination
it’s normally 0 (but it doesn’t mean that the task was successful.)
There are 3 negative values to represent internal task management errors:
QUEUEERROR = -1:
the task manager fails to queue the task (task conflict, storage error, …)
FAILED = -2:
the task manager fails to retrieve task status (monitor has died, database objects are missing,…)
SIGNALED = -3:
the task has finished on a signal, you can find the signal value in signal .
All the task’s information are stored in a log storage directory:
cmdline:
the execute command line for the task
stdout:
the stdout and stderr of the task command
watched.pid:
the task PID
monitor.pid:
PID of the monitor process
monitor.log:
the stdout and stderr of the monitor
result.json:
the result produced by the task if any
status.json:
the status of the task generated by the monitor
In case of task conflicts, the conflicting task IDs are stored as a list in the result.json file.
Children model:
runtime.runtimetask model
JSON:

```
{
"author": null,
"created_date": "func:django.utils.timezone.now",
"id": null,
"launched_date": null,
"monitor_error": "",
"monitor_pid": 0,
"name": null,
"parent": null,
"related_obj": null,
"returncode": null,
"returned_date": null,
"signal": null
}
```

Required fields:

```
name
```

Readonly attributes on update:

```
id
```

Fields documentation:
author:
“auth.user” object ID. (auth.user)
created_date:
Task Creation date. (datetime)
id:
(int)
launched_date:
Task launched date. (datetime)
monitor_error:
error returned by the monitoring process. (str[512])
monitor_pid:
PID of monitoring process. (int)
name:
Task name. (str[256])
parent:
“task.task” object ID. (task.task)
related_obj:
“task.taskobject” object ID. (task.taskobject)
returncode:
Task command return code. (int)
returned_date:
Task returned date. (datetime)
signal:
Task command exited on this signal. (int)

## task.taskobject  model

TaskObject(id, obj_model, obj_pk, obj_parent, obj_name)
JSON:

```
{
"id": null,
"obj_model": null,
"obj_name": null,
"obj_parent": null,
"obj_pk": 0
}
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
obj_model:
(str[256])
obj_name:
(str[256])
obj_parent:
“task.taskobject” object ID. (task.taskobject)
obj_pk:
(int)

## task.taskstorage  model

TaskStorage(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr, task)
Parent model: storage.storage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null,
"task": null
}
```

Readonly attributes:

```
size
```

Fields and attributes documentation:
created_at:
(datetime)
id:
“task.taskstorage” object ID (int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)
task:
“task.task” object ID. (task.task)

## users.userprofile  model

UserProfile(id, user, authmode, timezone, regmode, identity, email, title, uuid, status, expiration,
update_date, is_empty_pam_password)
JSON:

```
{
"authmode": "LOC",
"email": "",
"expiration": null,
"id": null,
"identity": null,
"is_empty_pam_password": true,
"regmode": "fndn",
"status": "FAILED",
"timezone": "",
"title": null,
"update_date": null,
"user": null,
"uuid": null
}
```

Required fields:

```
user
```

Readonly attributes on update:

```
id
```

Fields documentation:
authmode:
(str[8])
LOC:
local
PAM:
PAM
LOCKED:
PAM Locked
email:
(email)
expiration:
(datetime)
id:
(int)
identity:
(str[320])
is_empty_pam_password:
(bool)
regmode:
(str[8])
status:
(str[16])
ACTIVE:
Active
EXPIRED:
Expired license
DISABLED:
Account disabled
FAILED:
Failed registration
IDISABLED:
Instance disabled
OWNERRM:
Owner deleted
timezone:
(str[128])
title:
(str[64])
update_date:
(datetime)
user:
“auth.user” object ID. (auth.user)
uuid:
(str[64])

## visual.devicenode  model

Define a node over a device, by default the image used is the device vm_type.
Parent model: visual.node model
JSON:

```
{
"device": null,
"fabric": null,
"id": null,
"image": null,
"level": -1,
"name": null,
"nameid": null,
"vm_type": ""
}
```

Required fields:

```
device
fabric
name
nameid
```

Readonly attributes on update:

```
device
```

Fields documentation:
device:
“model.device” object ID. (model.device)
fabric:
“model.fabric” object ID. (model.fabric)
id:
“visual.devicenode” object ID (int)
image:
“visual.nodeimage” object ID. (visual.nodeimage)
level:
(int)
name:
(str[255])
nameid:
(str[64])
vm_type:
(str[32])

## visual.edge  model

Edge(id, nameid, node_from, node_to)
JSON:

```
{
"id": null,
"nameid": null,
"node_from": null,
"node_to": null
}
```

Required fields:

```
nameid
node_from
node_to
```

Readonly attributes on update:

```
id
```

Fields documentation:
id:
(int)
nameid:
(str[129])
node_from:
“visual.node” object ID. (visual.node)
node_to:
“visual.node” object ID. (visual.node)

## visual.node  model

Represent a graphical object on the topology.
If the object is an image, it can be a custom image stored as a NodeImage or a device vm_type to
use standard images.
To define a node over a device, use a DeviceNode.
param fabric:
the fabric
param name:
name of the node
param level:
define the layer level
Children model:
visual.devicenode model
JSON:

```
{
"fabric": null,
"id": null,
"image": null,
"level": -1,
"name": null,
"nameid": null,
"vm_type": ""
}
```

Required fields:

```
fabric
name
nameid
```

Readonly attributes on update:

```
fabric
id
```

Fields documentation:
fabric:
“model.fabric” object ID. (model.fabric)
id:
(int)
image:
“visual.nodeimage” object ID. (visual.nodeimage)
level:
(int)
name:
(str[255])
nameid:
(str[64])
vm_type:
(str[32])

## visual.nodeimage  model

NodeImage(id, parent, created_at, modified_at, name, local_name, mime_types, storage_ptr, fabric,
fabricstorage_ptr)
Parent model: model.fabricstorage model
JSON:

```
{
"created_at": "func:django.utils.timezone.now",
"fabric": null,
"id": null,
"mime_types": "",
"modified_at": "func:django.utils.timezone.now",
"name": null,
"parent": null,
"size": null
}
```

Readonly attributes:

```
size
```

Fields and attributes documentation:
created_at:
(datetime)
fabric:
“model.fabric” object ID. (model.fabric)
id:
“visual.nodeimage” object ID (int)
mime_types:
(str[256])
modified_at:
(datetime)
name:
(str[128])
parent:
“storage.storage” object ID. (storage.storage)
size:
(?)

### 5.3. OpenAPI documentation

Browse API in OpenAPI format.

### 5.4. OAuth2 Authorization Grants

(This documentation is based on Django OAuth Toolkit documentation.)
An authorization grant is a credential representing the resource owner’s authorization (to access its
protected resources) used by the client to obtain an access token. – RFC6749
The OAuth framework specifies several grant types for different use cases. – Grant Types
We will start by given a try to the grant types listed below:
Client credential
Authorization code
These two grant types cover the most initially used use cases.

> **Warning**
> All examples are using the -k  option of curl  because of the default self signed certificate of Fabric
> Studio. You MUST install valid SSL certificate and NOT USE this option in production.

#### 5.4.1. Client Credential

The Client Credential grant is suitable for machine-to-machine authentication. It is simpler than the
Authorization Code flow.

> **Important**
> In Fabric Studio the access token is automatically associated to the application user and API calls
> are executed as this user.

### Application and credential

#### Using CLI

You can use the CLI to generate an application (confidential client credential using HMAC with SHA-
2 256) and get the associated CREDENTIAL value, you only need to provide a name to your
application:

```
$ system oauth2 application default create service-worker
SEZzVE14emtwVGRYUTdGRVhXMHBxUWpVZjh5cERlYllBb2dRNFZJcTpWZG1uSHlXeVlOY29UT0x3U
```

Store the credential as an environment variable:

```
CREDENTIAL=SEZzVE14emtwVGRYUTdGRVhXMHBxUWpVZjh5cERlYllBb2dRNFZJcTpWZG1uSHlXeV
```

#### Using web interface

#### Register application

Point your browser to the application creations page /oauth2/applications/register/.
Fill the form as show in the screenshot below, and before saving take note of Client id  and
Client secret  we will use it in a minute.
Client credential application registration
Store your Fabric Studio address, Client id  and Client secret  values as environment variables,
eg:

```
FABRIC_HOST=255.255.255.255
ID=X2zbRLkjW9YE2wCSgne9iv8gh6hxihR2cfor0qWf
SECRET=pYCwBlv5zRI8Sk03IJN6nv66ZEJaw0VmcV9IsGvq39IiyyXeQMdgY6VWpM9Kh7pmIt9oZB
```

#### Create credential

We need to encode client_id  and client_secret  as HTTP base authentication encoded in
base64 , you can use the following code to do that:

```
cat << EOF | python3
import base64
client_id = "${ID}"
secret = "${SECRET}"
credential = "{0}:{1}".format(client_id, secret)
credential_enc = base64.b64encode(credential.encode("utf-8")).decode("utf-8")
print(f'CREDENTIAL={credential_enc}')
EOF
```

Store the credential as an environment variable, eg:

```
CREDENTIAL=WDJ6YlJMa2pXOVlFMndDU2duZTlpdjhnaDZoeGloUjJjZm9yMHFXZjpwWUN3Qmx2NX
```

### Get access token

To start the Client Credential flow you call /oauth2/token/  endpoint directly:

```
curl -k -X POST \
-H "Authorization: Basic ${CREDENTIAL}" \
-H "Cache-Control: no-cache" \
-H "Content-Type: application/x-www-form-urlencoded" \
"https://${FABRIC_HOST}/oauth2/token/" \
-d "grant_type=client_credentials"
```

The OAuth2 provider returns a response with the access token, eg:

```
{
"access_token": "GYeR7cpPFRYSMN3paSkB7utwdoYDUT",
"expires_in": 36000,
"token_type": "Bearer",
"scope": "read write"
}
```

### Test API access

To access the user resources we just use the access_token :

```
BEARER=GYeR7cpPFRYSMN3paSkB7utwdoYDUT
curl -k -X GET \
-H "Authorization: Bearer ${BEARER}" \
"https://${FABRIC_HOST}/api/v1/model/fabric"
```

#### 5.4.2. Authorization Code

> **Warning**
> You only have one minute to validate your authorization code flow. See the Python script example.
> The Authorization Code flow is best used in web and mobile apps. This is the flow used for third party
> integration, the user authorizes your partner to access its products in your APIs.

### Register application

Point your browser to the applications registration page: /oauth2/applications/register/.
Fill the form as show in the screenshot below and before save take note of Client id  and
Client secret  we will use it in a minute.
Authorization code application registration
Store your Fabric Studio address, Client id  and Client secret  values as environment variables:

```
FABRIC_HOST=255.255.255.255
ID=ByNDkFULqhFLooV41PQcLYHKfeM40EA8nWbHVaMm
SECRET=r3Dl6gcgeK59H3J2vhH8Uj0q1hPWovDAUKbW5GtqVEEgc6wVNk2YTgagK8EFb5BpaHfMxC
```

### Create code challenge

Now let’s generate an authentication code grant with PKCE (Proof Key for Code Exchange), useful to
prevent authorization code injection. To do so, you must first generate a code_verifier  random
string between 43 and 128 characters, which is then encoded to produce a code_challenge :

```
cat << EOF | python3
import random
import string
import base64
import hashlib
code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits)
code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
code_challenge = hashlib.sha256(code_verifier).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').rst
print('')
print(f'CODE_VERIFIER={code_verifier.decode("utf-8")}')
print(f'CODE_CHALLENGE={code_challenge}')
EOF
```

You can copy the two generated variable lines to paste in your shell terminal, eg:

```
CODE_VERIFIER=TTlNNU03WjNMNjJXSkc3MERXTlJBMjhLMjlLUEJXRFVOOFhTOUk1VjczUDlIU0l
CODE_CHALLENGE=YHz2T6ZtmouJixttPAJWBR1R-Bz61ztcnMFSKGZGmFM
```

### Authorization code

To start the Authorization code flow go to this URL:

```
x-www-browser "https://${FABRIC_HOST}/oauth2/authorize/?response_type=code&co
```

Note the parameters we pass:
response_type: code
code_challenge: XRi41b-5yHtTojvCpXFpsLUnmGFz6xR15c3vpPANAvM
code_challenge_method: S256
client_id: vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8
redirect_uri: http://127.0.0.1:8000/noexist/callback
This identifies your application, the user is asked to authorize your application to access its
resources.
Go ahead and authorize the web-app .

> **Important**
> Once authorized, you only have 1 minutes to complete the validation process.
> Authorization code authorize web-app
> Remember we used http://127.0.0.1:8000/noexist/callback  as redirect_uri  you should get a
> Page not found (404), a This site can’t be reached or a Unable to connect page, but you must
> have a url like this:

```
http://127.0.0.1:8000/noexist/callback?code=WAEtiTmPzvA6ecGxspFSqCnkev0ylo
```

This is the OAuth2 provider trying to give you a code , in this case WAEtiTmPzvA6ecGxspFSqCnkev0ylo .
Store it as an environment variable:

```
CODE=WAEtiTmPzvA6ecGxspFSqCnkev0ylo
```

### Get access token

Now that you have the user authorization, it’s time to get an access token:

```
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

The OAuth2 provider returns a response with the access token, eg:

```
{
"access_token": "AAZe4twJZWlmRYRjnU5pDCpWTLfZLM",
"expires_in": 36000,
"token_type": "Bearer",
"scope": "read write",
"refresh_token": "HNvDQjjsnvDySaK0miwG4lttJEl9yD"
}
```

### Test API access

To access the user resources we just use the access_token , eg:

```
BEARER=AAZe4twJZWlmRYRjnU5pDCpWTLfZLM
curl -k -X GET \
-H "Authorization: Bearer ${BEARER}" \
"https://${FABRIC_HOST}/api/v1/model/fabric"
```

### Python script example

This python script do the whole process and wait for the callback to extract the authorization code
(download):

```
#!/bin/python3
# -*- coding: utf-8 *-*
import random, string, base64, hashlib, threading, shlex, json
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs
from subprocess import run, PIPE
class OneTimeServer(HTTPServer):
    code = None
class ValidateCode(BaseHTTPRequestHandler):
def do_GET(self, *args, **kwargs):
        path = urlparse(self.path)
        query = parse_qs(path.query)
self.server.code = query['code'][0]
self.send_response(HTTPStatus.OK)
self.end_headers()
return
def generate_code():
    code_verifier = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
for _ in range(random.randint(43, 128)))
    code_verifier = base64.urlsafe_b64encode(code_verifier.encode('utf-8'))
    code_challenge = hashlib.sha256(code_verifier).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode(
'utf-8').rstrip('=')
return code_verifier.decode('utf-8'), code_challenge
def main(server_class=HTTPServer, handler_class=ValidateCode):
    fs_addr = input('Fabric Studio Address:')
print('Run browser to create the application:')
    cmd = ('x-www-browser', f'https://{fs_addr}/oauth2/applications/register/
print('$', shlex.join(cmd))
    run(cmd)
print('> Client type: Confidential')
print('> Authorization grant type: Authorization code')
print('> Redirect uris: http://127.0.0.1:8000/noexist/callback')
print('> Algorythm: HMAC with SHA-2 256')
    application_id = input('< Application ID:')
    application_secret = input('< Application Secret:')
    code_verifier, code_challenge = generate_code()
print('< Code verifier:', code_verifier)
print('< Code challenge:', code_challenge)
    server_address = ('127.0.0.1', 8000)
print('Start callback server on', server_address)
    httpd = OneTimeServer(server_address, ValidateCode)
    thread = threading.Thread(target=httpd.handle_request)
    thread.start()
print('Run browser to create code challenge:')
    cmd = (
'x-www-browser',
f'https://{fs_addr}/oauth2/authorize/?response_type=code&code_challen
    )
print('$', shlex.join(cmd))
    run(cmd)
print('Wait browser callback:')
    thread.join()
    code = httpd.code
print('< Code received:', code)
print('Validate code:')
    cmd = ('curl', '-k', '-X', 'POST', '-H', 'Cache-Control: no-cache', '-H',
'Content-Type: application/x-www-form-urlencoded',
f'https://{fs_addr}/oauth2/token/', '-d',
f'client_id={application_id}', '-d',
f'client_secret={application_secret}', '-d', f'code={code}', '-d',
f'code_verifier={code_verifier}', '-d',
'redirect_uri=http://127.0.0.1:8000/noexist/callback', '-d',
'grant_type=authorization_code')
print('$', shlex.join(cmd))
    proc = run(cmd, stdout=PIPE, encoding='utf-8')
print('< Content:', proc.stdout)
    data = json.loads(proc.stdout)
    bearer = data['access_token']
print('< Bearer:', bearer)
print('Test bearer:')
    cmd = ('curl', '-k', '-X', 'GET', '-H', f'Authorization: Bearer {bearer}
f'https://{fs_addr}/api/v1/model/fabric')
print('$', shlex.join(cmd))
return run(cmd).returncode
if __name__ == '__main__':
raise SystemExit(main())
```

## 6. Working with licenses

### 6.1. License Sources

#### 6.1.1. BYOL

For basic usage, Fabric Studio relies on a Bring Your Own License model. You can use both .lic
file or Flex-VM license (see FortiFlex licenses).
You can import a license by the GUI (Repositories/Home:Licenses).
You can also use the CLI in two steps:

```
scp FGVM00000000.lic admin@FABRIC_STUDIO_IP:
ssh admin@FABRIC_STUDIO_IP system license import FGVM00000000.lic
```

By default the copied license file is removed when the operation completes.

#### 6.1.2. License Server

It’s possible to retrieve licenses from a Fabric Studio, a FortiPoC or a labsetup license server.

> **Warning**
> A Fabric Studio CAN NOT be a license server for a FortiPoC.

### Configuring server

On the server you must copy licenses and/or configure a FortiFlex account. You can group licenses
together so clients part of a group will get licenses only from their group.
You MUST enable the license server as by default a Fabric Studio only serves license to itself. By the
GUI (System/Settings - Licensing/License Service) or by the CLI:

```
system license server service enable
```

See Fabric Studio License Server for security recommendation about the server SSL certificate.

### Configuring client

#### For a Fabric Studio License Server

On the client you must configure the server, by the GUI (System/Settings - Licensing/Remote
License Server URL) or by the CLI, eg:

```
system license client server url set https://FS_LICSRV/license/
```

> **Warning**
> DON’T FORGET the /license/  path.
> The Fabric Studio client is validating the server SSL certificate:
> FS_LICSRV  is a FQDN: strict validation (certificate for that exact FQDN)
> FS_LICSRV  is an IP: only CA chain validation (it also accepts the default self-signed Fabric Studio
> certificate)
> If you use a license group, set it too, eg:

```
system license client request group set wkshop1
```

#### For a FortiPoC or LabSetup License Server

If the license server is a FortiPoC or a labsetup, the URL is different and you must enable the legacy
mode:

```
system license client server url set https://LICSRV/
system license client server legacy enable
```

The license group should work too if you set it (see For a Fabric Studio License Server).

### 6.2. Configuring device’s license

> **Important**
> The UUID attached to a license supersedes the VM’s UUID defined in the Fabric when creating the
> VM.

#### 6.2.1. Linking license

Fabric Studio supports different modes to apply license to a device:
Automatic
Custom
None

### Automatic

In automatic mode:
if the device supports license, Fabric Studio must be able to apply a license. It’s an error if not.
if the device doesn’t support license, Fabric Studio acts as for “None” mode
Support for license is declared in the meta file associated to the firmware. It can declare if it supports
.lic file and/or FortiFlex license types. If nothing is specified in the meta, Fabric Studio considers it
supports both license types.

### Custom

You must select the license to use.

### None

No license is installed on the device.

#### 6.2.2. Exporting a Fabric

Licenses content are never exported with the Fabric. If you are using custom assignation mode, only
the license serial number is exported.

#### 6.2.3. License meta information

When importing a license to a Fabric Studio, a VM UUID is automatically computed from the serial
number (extracted from the filename) as uuid.uuid5(uuid.NAMESPACE_DNS, license.stem.upper()) .
The mgmt_addr  is used for products known to require it. If no mgmt_addr  value is defined, Fabric
Studio can use a default one.
Fabric Studio recognizes these products with the following default mgmt_addr  value:
FortiManager: 10.0.0.1
FortiSandbox: 10.0.0.1

> **Warning**
> The other extra information (like mgmt_hwaddr , …) are only informational, they should be enforced in
> future releases.

#### 6.2.4. Devices with license key

Some devices, like FAD CM, are not using a license file but a license key. To provide the key to
Fabric Studio you must store the key in a license file:

```
-----BEGIN <MODEL> LICENSE-----
THE_KEY
-----END <MODEL> LICENSE-----
```

The MODEL  MUST be the model as in FortiCloud support site with spaces replaced by underscore,
ex:

```
FortiADC CM => FortiADC_CM
```

> **Warning**
> Experimental, may break with any FortiCloud update.

### 6.3. FortiFlex licenses

Fabric Studio supports the FortiFlex API to manage licenses.

> **Important**
> Fabric Studio DO NOT enforce any limitations or constraints in the FortiFlex API usage, but the
> FortiFlex API endpoint may do. Please refer to official FortiFlex API documentation.
> Only standalone Fabric Studio or License Server Fabric Studio should configure FortiFlex support.

#### 6.3.1. Prerequisites

We recommend to Fortinet employee to ITF the post-paid FortiFlex FC-10-ELAVS-221-02-DD .
Do not forget to activate it.

### API User

You must create an API user that supports both the FortiFlex and the Asset Management.
Permissions profile MUST include:
Asset Management: “Read & Write” for at least “Asset Maintenance” and “Entitlement Management”
resources
FortiFlex: enable access and set “Read/Write” access type

> **Warning**
> A FortiFlex API user CAN NOT be shared between multiple Fabric Studio instances, you MUST have
> one FortiFlex API user by Fabric Studio instance. All API users of an account can see all licenses of
> all others API users, so it’s highly recommended to partition your account as a OU with Sub-OU and
> use ONE and only one API user by Sub-OU. Sub-OU DO NOT see licenses of others Sub-OU at
> same level. See Organisation OU and Sub-OU for more details.

#### 6.3.2. Credentials

To configure the FortiFlex API user credentials, on CLI:

```
system forticloud account set <API ID> [--password <Password>] [--accountId <
```

If the password is not provided on command line, you’ll be prompted for it.

> **Warning**
> When you are using a Sub-OU API user, you must provide the associated account ID. Failing to do
> so may prevent some FortiFlex API calls to work (like creating FortiFlex configuration). This account
> ID is not part of the credential API file and can’t be retrieved by an API call. See Organisation OU and
> Sub-OU for more details.
> Fabric Studio uses these credentials to retrieve the enrolled Program and associated Configurations
> from the FortiFlex API endpoint.
> When you update the user on https://support.fortinet.com/, it’s highly recommended to refresh
> program and configuration with:

```
system license flex program refresh
system license flex config refresh
```

To remove the FortiFlex API user credentials, on CLI:

```
system forticloud account reset
```

#### 6.3.3. Configuration

You must activate the type of license (FTG, FWB, …) in a program as a pool of license:

```
system license flex pool set <TYPE> [--config <CONFIG_ID>]
```

If ou have more than one configuration for the corresponding Product Type TYPE  in the enrolled
programs for the API User you MUST use the Configuration ID.
You can now retrieve all available FortiFlex licenses visible to your FortiFlex API user:

```
system license flex license refresh *
```

You can generate new licenses for each pool:

```
system license flex pool generate <POOL> <COUNT>
```

The POOL can be a pool ID  or a pool Product Type TYPE .

### Standalone

By default Fabric Studio automatically creates new FortiFlex license if the pool is exhausted. You can
disable/enable this behavior with:

```
system license flex settings auto-create set disable|enable
```

> **Important**
> Each time your Fabric Studio needs to install a FortiFlex license token on a device, it first refreshes
> the token: it ensures that the token is always valid when license must be installed (eg: license
> reload).

### License Server

When acting as a license server, the Fabric Studio DO NOT automatically creates new FortiFlex
license if the pool is exhausted because the generation process takes time and request may timeout.
You MUST generate the number of necessary FortiFlex licenses first (see Configuration).
A Fabric Studio handles both classical licenses ( .lic  files) and FortiFlex licenses. If both are
available, FortiFlex licenses are used first when possible to keep .lic  for Fabric Studio clients that
may not support FortiFlex license for a given product.

> **Note**
> The Fabric Studio client announces which kind of FortiFlex license it supports.

> **Important**
> Each time a Fabric Studio client needs to install a FortiFlex license token on a device, it first requests
> the License Server to refresh the token: it ensures that the token is always valid when license must
> be installed (eg: license reload).

#### 6.3.4. Duplicating FortiFlex VM configuration

> **Important**
> In order to create configuration you must have specified the Sub-OU API user account ID. Failing to
> do so may raise a Current user is not authorized to access this item  error or similar.
> It’s recommend to use the same configuration between all your Sub-OU. You can use Fabric Studio
> to duplicate configuration:

```
ssh admin@<FS1> -- -j system license flex config export > config.json
scp config.json admin@<FS2>:
ssh admin@<FS2> system license flex config import config.json
```

> **Warning**
> FortiFlex API may change the parameters associated to a product configuration. It prevents to clone
> the configuration to another Sub-OU. In such situation you must first update the configuration before
> doing the export or use the --continue  option on import to ignore the errors and continue with the
> other configurations.

#### 6.3.5. License auto stop

Fabric Studio tries to stop licenses when they are released (on fabric uninstall) in order to limit point
consumption.

> **Important**
> It’s not guaranteed that licenses are effectively stopped, user MUST verify and track its point
> consumption.

> **Warning**
> When a license is reactivated (depending the previous stop date) it can take up to 30 minutes for
> FortiGuard server to be synchronized with FortiFlex server (see #1116921), during this period the
> license may appear expired to the device while showing correct new expiration date on
> https://support.fortinet.com/ site.
> For employee, it’s recommended for the time of a workshop:
> to disable the auto stop on release:

```
system license flex settings set '{"stop_on_release": false}'
```

to reactivate all your Flex licenses some hours before the workshop:

```
system license flex license reactivate all
```

When the workshop is done, you can then:
stop all your Flex licenses:

```
system license flex license stop all
```

enable the auto stop on release:

```
system license flex settings set '{"stop_on_release": true}'
```

### 6.4. Organisation OU and Sub-OU

#### 6.4.1. Enabling feature

A good way to separate different pools of licenses between different license servers or clients is to
use the FortiCloud organizations service.
First you must ITF a FC-15-CLDPS-219-02-DD  and activate it.
You must enable organization for your corporate account:
login to https://support.fortinet.com/
on upper right “user@fortinet.com” menu click on “My Account”
on left menu pane, click on “My Account (IAM version)”
on left menu pane, click on “Account Preferences”
Quick-links: https://support.fortinet.com/cred/#/sec/my-account/account-preferences
You should now be able to “Enable Organization Feature”.
Documentation: https://docs.fortinet.com/document/forticloud/latest/identity-access-management-
iam/381397/enabling-organizations

#### 6.4.2. Create organization

You now have access to the “Organizations” service, the top level is the OU (Organization Unit) and
is linked to your account. Note your account ID, as you will need it later (can be seen from the upper
right user dropdown).
create a Sub-OU (we recommend to put the hostname of your license server in the name)
create a new member account in the Sub-OU, you can use real email or use automatically generated
email (recommended)
logout

> **Warning**
> It’s highly recommended to note the account ID associated to each member, it’s required for some
> FortiFlex API calls (see Credentials) and can’t be retrieved by API call to FortiCloud.

#### 6.4.3. Create your IAM user

Go to IAM, in Users add a new IAM user for yourself using your corporate email.
On panel “2. User Permissions”:
select “Organization” for the type
select the top level Organization for the permissions scope
select the SysAdmin for the permission profile
Complete the registration.

#### 6.4.4. Create API user

Now login using the IAM login: use your account ID, username (not the email) and corporate
password.
You can select the member of the Sub-OU.
go to IAM service
create a permission profile (see API User)
create the API user and select the permission profile

#### 6.4.5. Moving licenses between (Sub-)OU

To move license between (Sub-)OU, you need to switch to the OU account and not the user account
in this OU.

## 7. Device configuration

### 7.1. Fortinet products

Fabric Studio uses the serial console CLI to configure the management port (connected to the
management switch) static IP address
once the management port is configured, Fabric Studio uses SSH CLI as a much more reliable way
to configure:
the default route using the system host as next hop
the nameserver using the system host as nameserver
These steps are required to let the device validate the license or retrieve the license using FortiFlex
mechanism
Fabric Studio installs the license, if any, using SSH CLI and wait for reboot messages on the serial
console
Fabric Studio waits for license validation if possible
Fabric Studio completes the configuration of the device:
by configuring ports, default route and nameserver as defined in the Fabric using SSH CLI
commands
or by restoring a configuration

> **Important**
> if the configuration is supposed to be encrypted, FS uses password fortinet

> **Important**
> Sometimes the device continue to validate the license after the reboot, you must ensure that the
> device is able to complete such validation once fully configured.
> For some products, HTTP may be used for some steps (eg: FortiPortal configuration backup).
> The supported Fortinet products have a backup configuration and a restore configuration procedure,
> it must be accessible by the CLI (preferred way) or sometimes HTTP REST.

> **Important**
> It implies that your Fortinet device must be powered on to achieve the configuration.
> There are 3 methods to apply a configuration:
> the Restore method: the configuration is a full configuration (for instance generated by the backup
> command), Fabric Studio simply restores it using a supported file transfer protocol (TFTP, FTP, …)
> the Restore-Append method: only for snippet configuration, the Fabric Studio backups the
> configuration, it appends the snippet at the end of the backup, and finally restores this patched
> configuration using a supported file transfer protocol (TFTP, FTP, …)
> the Script method: only for snippet configuration, the Fabric Studio executes line by line the snippet
> using SSH connection. You can write special directives (no preceding spaces allowed):
> the #!confirm:<REGEXP>  directive: it changes the awaited prompt to send the next command and
> <REGEXP>  must be a regular expression (see python “re” module documentation).
> the #!reboot:[<REGEXP>]  directive: it must be the last line of the script, optionally you can change the
> awaited prompt <REGEXP>  (by default the CLI prompt if nothing specified). If the SSH connection
> breaks while waiting the prompt, the error is ignored and the script is considered successful. Fabric
> Studio then waits for the device reboot.
> Example for FortiMail, supposing you are in “gateway” operation mode and you want to switch to
> “transparent” mode:

```
config system global
set operation-mode transparent
set hostname FML-t
end
#!confirm:Do you want to continue\? \(y/n\)
y
#!reboot:
```

#### 7.1.1. FortiGate

#### VDOM

Fabric Studio can backup and restore configuration or install a license when VDOM are enabled.

#### HA mode

We assume that when in cluster mode, the interface used by Fabric Studio for management is
isolated from the HA logic.
You must configure the HA as follow for port1  as management interface:

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

#### ZTP

> **Warning**
> ZTP should only be achieved using port1 (like on the hardware).
> Fabric Studio and the FortiManager managing the Fortigate must use the same IP address for the
> management port to let you access the FortiGate through the Fabric Studio SSH and HTTPS
> accesses.
> Fabric Studio doesn’t bring up the network interfaces until the management port is statically
> configured to prevent unexpected ZTP configuration and to allow license installation.
> Once normal management port static configuration and license installation is done, Fabric Studio
> executes:

```
execute factoryreset keepvmlicense
```

The Fortigate can now achieve the normal ZTP configuration using the installed license.
You can now use the native DHCP server (host or router) to pass option 240 and 241, see Extra
DHCP options.

#### 7.1.2. FortiManager

#### License .LIC file

When a .LIC file is used as a license for a FortiManager, Fabric Studio knows that it must configure a
port with the IP associated to the license.
By default Fabric Studio uses 10.0.0.1 address (cause it’s the address used in TAC Lab), it searches
for a port defined with this address to configure it prior license installation.
If your license use another address, you must associate the address to your license, eg:

```
system license update FMVMMLTM23002931 '{"mgmt_addr": "192.168.1.128"}'
```

#### Encrypted configuration

When required by a firmware version, Fabric Studio uses fortinet  as password to do the backup
and the restore of the configuration file.

> **Important**
> Fabric Studio extracts the version from the firmware’s filename e.g. v7.4.2 , if the version is short
> e.g. v7  (interim, special build, …) Fabric Studio thinks it’s a v7.0.0  instead. To let Fabric Studio
> knows the version to consider you can configure it in the vm parameters:

```
model vm parameters update VM_ID '{"as_version": "v7.4.2"}'
```

#### 7.1.3. FortiAnalyzer

#### License .LIC file

See FortiManager.

#### Encrypted configuration

See FortiManager.

### 7.2. Native devices

> **Warning**
> Script configuration is an EXPERIMENTAL feature!
> You can attach script to the System Host, Router or Switch devices in GUI or use the CLI command
> to apply a configuration.

> **Note**
> The configuration method (RESTORE, SCRIPT, …) is ignored as there is only one way to configure
> native devices.

#### 7.2.1. System Host

#### Script

The system host configuration allows the following commands:

```
sysctl net.ipv4.XYZ=....
sysctl net.ipv6.XYZ=....
```

ip ...  except for the ip netns  command

```
tc ...
```

#### 7.2.2. Router

#### Script

The router configuration allows the following commands:

```
sysctl net.ipv4.XYZ=....
sysctl net.ipv6.XYZ=....
```

ip ...  except for the ip netns  command

```
tc ...
nft ...
```

#### 7.2.3. Switch

#### Script

The switch configuration allows the following commands:
ovs-ofctl <COMMAND> ${SWITCH} ... : the ${SWITCH}  is replaced by the OpenVSwitch name, no option
(starting with - ) are allowed

#### VLAN Mode

This parameter determines what VLAN the packet is in. It also verifies that this VLAN is valid for the
port; if not, drop the packet. How the VLAN is determined and which ones are valid vary based on
the input port’s vlan-mode:
default:
(VLAN Unaware) allow any tagged and untagged packets to go through the port
access:
(Access) the packet is in the VLAN specified in the Native VLAN . The packet MUST NOT have an
802.1Q header with a nonzero VLAN ID; if it does, drop the packet
trunk:
(Trunk) the packet is in the VLAN specified in its 802.1Q header, or in VLAN 0 if there is no 802.1Q
header. The Tagged VLANs  lists the valid VLANs; if it is empty, all VLANs are valid
native-tagged:
(Native Tagged) same as trunk except that the VLAN of a packet without an 802.1Q header is not
necessarily zero; instead, it is taken from the Native VLAN
native-untagged:
(Native Untagged) same as trunk except that the VLAN of a packet without an 802.1Q header is not
necessarily zero; instead, it is taken from the Native VLAN . On out the Native VLAN  is stripped

### 7.3. Third-party Linux devices

Fabric Studio supports some Linux devices (LXC, Light Ubuntu VM with disk, …) and Fabric Studio is
able to do post installation (on first boot), backup or restore configuration.
When creating such devices, Fabric Studio automatically adds the default /fabric/init  script to
perform these actions.

> **Note**
> As the /fabric/init  file can be part of the restored configuration, Fabric Studio also creates a
> second copy as /fabric.init  to use to update your /fabric/init  script with new implemented
> features (e.g. new “Script” method execution introduced in 2.0.4).

#### 7.3.1. Backup

> **Warning**
> The backup only works when the VM is powered on.
> Before performing the backup, Fabric Studio calls the script as /fabric/init prepare . The script
> must copy and generate files to backup under the /fabric  directory.
> For instance, the script can stop the database, do the database dump under /fabric  and finally
> restart the database to keep the system in a functional state.
> Fabric Studio executes by SSH (KVM VM) or direct command (LXC VM) the command to generate a
> tar.gz file named /.fabric_backup . with the /fabric  directory content.
> Fabric Studio retrieves the generated file by SFTP.

> **Note**
> Fabric Studio backups both the /fabric  and the /fortipoc  directories to ease migration from
> FortiPoC. This backward compatibility feature is planned for removal in Fabric Studio 2.1

#### 7.3.2. Restore

The restore of configuration can happen at 3 moments.

#### Install

When: Fabric Studio installs the VM.
The content of the configuration file is extracted in VM root directory before the power on on fresh
VM install. On VM power-on, the post installation script is executed as the last service target of
SystemD.
Fabric’s author must have updated the script to perform the necessary copy of the files from /fabric
to the system, to trigger restart of services, …

#### Online

When: the VM is running.

#### Restore method

Fabric Studio copies the configuration file to the VM file system by SFTP
Fabric Studio calls the command to extract the configuration file content on the VM using SSH (KVM
VM) or direct command (LXC VM)
Fabric Studio calls /fabric/init restore  on the VM using SSH (KVM VM) or direct command (LXC
VM)

#### Script method

Fabric Studio copies the configuration file to the VM file system by SFTP as /fabric.script
Fabric Studio calls /fabric/init script  on the VM using SSH (KVM VM) or direct command (LXC
VM)

#### Append-Restore method

See Script method.

#### Offline

When: the VM is not running.

#### Restore method

Fabric Studio extracts the configuration content to the VM root directory
Fabric Studio creates a file marker /.ftnt/restore_on_boot  to notify the system to complete the
configuration restore after the boot

#### Script method

Fabric Studio copy the configuration content to the VM root directory as /fabric.script
Fabric Studio creates a file marker /.ftnt/script_on_boot  to notify the system to execute the
configuration after the boot

#### Append-Restore method

See Script method.

#### 7.3.3. Post-Installation

On first boot, the system calls /fabric/init install .
In default script, the installation finishes by calling the restore  command and the script  command
to complete a configuration restoration or to execute the configuration as a script.
In /.ftnt  you find:
the post-installation logs as postinst.<PID>.log
a symlink postint.log  to the latest log
a marker file postinst_done  created when postinst script has been executed successfully

> **Note**
> The default /fabric/init  script supports FortiPoC post installation script execution. This backward
> compatibility feature is planned for removal in Fabric Studio 2.1

### 7.4. Network

#### 7.4.1. DHCP

When your client VM’s port must be configured by DHCP, you have two cases:
the DHCP server is a VM (LXC, FGT, …)
the DHCP server is a native device (Router or System Host)

#### Served by a VM

#### Client’s VM Port

Configure the “Addressing mode” to DHCP. The “Address” and “Mask” fields are purely informational.
Leave the “Native DHCP Server” field empty.

#### Client’s VM Default gateway

The default gateway defined in the client’s VM’s “Network Parameters” is only used when it’s in the
same subnet than a port under Fabric Studio control (“Static” or “DHCP” served by a Native Device).

#### Served by a Native Device

#### Client’s VM Port

Configure the “Addressing mode” to DHCP, the “Address” and “Mask” fields are mandatory as
Fabric Studio only does static DHCP and need to know which address to use in the DHCP lease.
In the “Native DHCP Server” field, you must select which native device is the DHCP Server for this
port.

#### Client’s VM Default gateway

The Fabric Studio analyzes the client’s VM “Network Parameters” values to identify if the default
gateway must be provided by the Native DHCP Server.
If the default gateway is in same subnet than the port’s in DHCP handled by the Native DHCP
Server, then the default gateway is part of the DHCP lease (and also the DNS nameserver).
If you need a different gateway (and DNS nameserver) for a port than the one defined in client’s VM
“Network Parameters” (eg: because the port is part of VDOM, ISP and SD-WAN use-case, …), you
must attach a “Network”, that defines the gateway and nameserver, to your client’s VM port to be
used in the DHCP lease. It can only be defined by CLI:

```
model vm port update PORT_ID '{"network": NETWORK_ID}'
```

#### Extra DHCP options

> **Warning**
> This feature has only been tested with the host.
> You can configure Fabric Studio to issue extra DHCP option for VM devices through the “expert” VM
> parameters.
> This expert parameter takes a TOML formatted string, and we need a dhcp  section for each port
> with extra option to configure, e.g.:

```
[dhcp.port1]
"option:240" = "10.254.254.1"
"option:241" = "etlab.net"
```

By CLI, you must properlly escape the value, e.g.:

```
model vm parameters update VM_ID '{"expert": "[dhcp.port1]\n\"option:240\" =
```

For a FortiGate in ZTP it tells to send the option 240 and 241.
You can also use option name (see dnsmasq documentation for details), instead of option value,
e.g.:

```
"option:ntp-server" = "54.38.242.85"
```

## 8. Supported Devices

### 8.1. Fortinet products

Product
Version
License
Configuration
FortiFlex
(F)
File (L)
Backup
(B)
Restore
(R)
Restore
Append (A)
Script
SSH (S)
FortiADC
CLI
TFTP (NT) TFTP
TFTP
TFTP
(NT)
FortiADC Manager
CLI (NT)
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
FortiAIOps
CLI (NT)
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
FortiAnalyzer
7.4.2,+ CLI
CLI (NT)
FTP
FTP
NO
(NT)
FortiAnalyzer
< 7.4.2 CLI
CLI (NT)
FTP (NT)
FTP (NT)
FTP (NT)
(NT)
FortiAuthenticator
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiCache
(deprecated)
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiClient EMS
NO
NO
NO
NO
NO
NO
FortiData
NO
NO
NO
NO
NO
NO
FortiDeceptor
NO
NO
NO
NO
NO
NO
FortiDevSec
NO
NO
NO
TFTP (NT) TFTP (NT)
(NT)
FortiDDoS
CLI (NT)
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
FortiExtender
NO
NO
NO
NO
NO
NO
FortiGate
CLI
TFTP (NT) TFTP
TFTP
TFTP
(NT)
FortiGuest
CLI (NT)
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
Product
Version
License
Configuration
FortiFlex
(F)
File (L)
Backup
(B)
Restore
(R)
Restore
Append (A)
Script
SSH (S)
FortiIsolator
NO
NO
NO
NO
NO
NO
FortiIsolator
< 3
CLI (NT)
TFTP
NO
TFTP
NO
(NT)
FortiManager
7.4.2,+ CLI
CLI (NT)
FTP
FTP
NO
(NT)
FortiManager
< 7.4.2 CLI
CLI (NT)
FTP (NT)
FTP (NT)
FTP (NT)
(NT)
FortiMail
CLI
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
FortiNAC
CLI
TFTP (NT) TFTP
TFTP
TFTP (NT)
(NT)
FortiNDR
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiPAM
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiPortal
7.4,+
CLI
NO
FTP
FTP
NO
NO
FortiPortal
< 7.4
CLI
HTTP (NT) FTP
FTP
NO
NO
FortiProxy
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiRecorder
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiSandbox
CLI (NT)
FTP
TFTP
TFTP
NO
(NT)
FortiSIEM
NO
NO
NO
NO
NO
(NT)
FortiSOAR
SSH
SFTP/SSHSFTP/SSH SFTP/SSH NO
(NT)
FortiSRA
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiSwitch
CLI (NT)
TFTP
TFTP
TFTP
TFTP (NT)
(NT)
FortiSwitch-NMS
NO
HTTP
NO
NO
NO
NO
FortiTester
CLI (NT)
HTTP
HTTP
HTTP
NO
NO
Product
Version
License
Configuration
FortiFlex
(F)
File (L)
Backup
(B)
Restore
(R)
Restore
Append (A)
Script
SSH (S)
FortiWeb
CLI
TFTP (NT) TFTP
TFTP
TFTP
(NT)
NT:
not tested
NO:
not supported
HTTP:
REST API used
FTP:
FTP transfer using CLI command on serial console or SSH session
TFTP:
TFTP transfer using CLI command on serial console or SSH session
CLI:
CLI command on serial console or SSH session
SSH:
CLI command using SSH session

#### 8.1.1. FortiADC

#### Validated

Firmware
Fabric Studio VersionF LBRAS
FAD_KVM-V700-build0317-FORTINET2.0.0.interim.94
Y
YY Y

#### 8.1.2. FortiADC Manager

#### Validated

Firmware
Fabric Studio VersionFLBRAS
FADCManager-KVM-V700-build0094-FORTINET2.0.2.interim.252
YY

#### 8.1.3. FortiAIOps

#### Validated

Firmware
Fabric Studio VersionFLBRAS
FAO_VM64_KVM-v2.0.1-build0163-FORTINET2.0.0.interim.131
YY

#### 8.1.4. FortiAnalyzer

#### Validated

Firmware
Fabric Studio VersionF LBRA S
FAZ_VM64_KVM-v7.4.2-build2397-FORTINET2.0.0.interim.94
Y
YY N

#### 8.1.5. FortiAuthenticator

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FAC_VM_KVM-v6-build1617-FORTINET2.0.0.interim.96
YYY

#### 8.1.6. FortiCache (deprecated)

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FCHKVM-v400-build0222-FORTINET2.0.0.interim.102
YYY

#### 8.1.7. FortiClient EMS

> **Important**
> Experimental and limited support because:
> CLI doesn’t close session on CTRL-D
> CLI lacks commands to backup/restore configuration
> CLI lacks commands to install FortiFlex and .lic license
> FortiFlex licensing: it requires FortiCloud credentials
> .lic licensing: the .lic is associated to HWID that is randomly generated on first boot: if the VM is re-
> created, the .lic can’t be reused
> Must use DHCP to configure managment port.

#### Tested

Firmware
Fabric Studio VersionF L B RA S
forticlientems_vm.7.4.4.2034.F2.0.3.interim.160
NNNNNN

#### 8.1.8. FortiData

Only mgmt IP and default gateway are configured.

> **Warning**
> Some CPUs may not be supported (eg: unable to run it on Xeon(R) CPU E5-2670), in this case the
> FortiData may stop booting with an “Illegal instruction” error and asking to format the logdisk.

#### Tested

Firmware
Fabric Studio VersionF L B RA S
FDT_VM_KVM-v760-build0029-FORTINET2.0.1.interim.137
NNNNNN

#### 8.1.9. FortiDeceptor

Not supported:
can’t enable SSH access on admin port through CLI
no backup/restore configuration CLI command
no license installation CLI command
inside a Fabric Studio VM support is limited because of Deep nested VMs

#### Tested

Firmware
Fabric Studio VersionF L B RA S
FDC_VM-v600-build0058-FORTINET2.0.0.interim.131
NNNNNN
FDC_VM-v500-build0370-FORTINET2.0.0.interim.131
NNNNNN

#### 8.1.10. FortiDevSec

> **Warning**
> No CLI command to install LIC or Flex license
> Configuration backup complains with:

```
configuration backup failed 4
Command failed(3077). Error string: Internal error
```

May be due to a lack of license.

#### Validated

Firmware
Fabric Studio VersionF L B RAS
FortiDevSec-KVM-secureboot-v3.0.0-build00542.0.0.interim.150
NNNY

#### 8.1.11. FortiDDoS

#### Validated

Firmware
Fabric Studio VersionFLBRAS
FDD_KVM-V6.4.1-build0409-FORTINET2.0.0.interim.96
YY

#### 8.1.12. FortiExtender

Not supported.

#### Tested

Firmware
Fabric Studio VersionF L B RA S
FEXT_VM-v7.6.1-build0422.out2.0.0.interim.131
NNNNNN

#### 8.1.13. FortiGate

#### Upgrading

If you plan to perform upgrade (or downgrade) directly from the FortiGate web interface:
.out upgrade doesn’t work due to Fabric Studio reverse proxy: problem is under investigation.
Upgrade from FortiGuard is working.
if you have a log disk, upgrade/downgrade may fail if it’s not large enough (validated with 16GB)

#### Validated

Firmware
Fabric Studio VersionF LBRAS
FGT_VM64_KVM-v7.4.3.F-build2573-FORTINET2.0.0.interim.94
Y
YY Y

#### 8.1.14. FortiGuest

#### Validated

Firmware
Fabric Studio VersionFLBRAS
FortiGuest_VM64_KVM-v?.?.?-build????-FORTINET2.0.0.interim.131
YY

#### 8.1.15. FortiIsolator

V3:
Experimental support
For CSE ONLY !
V2: You may get the following error message during config restore (seen with
FIS_VM_KVM-v2-build0549.kvm.zip  and FIS_VM_KVM-v2-build0593.kvm.zip ), Fabric Studio ignores it:

```
/ftnt_isolator/scripts/fis_exec_cli: line 12: 20028 Segmentation fault      /
```

#### Validated

Firmware
Fabric Studio VersionF L B RA S
FIS_VM_KVM-v3-build01512.0.3.interim.161
NNNNNN
FIS_VM_KVM-v2-build0593 2.0.0.interim.94
Y NY N

#### 8.1.16. FortiManager

#### Validated

Firmware
Fabric Studio VersionF LBRA S
FMG_VM64_KVM-v7.4.2-build2397-FORTINET2.0.0.interim.94
Y
YY N

#### 8.1.17. FortiMail

#### Validated

Firmware
Fabric Studio VersionF LBRAS
FML_VMKV-64-v762.F-build0760-FORTINET2.0.0.interim.132
Y
YY
FML_VMKV-64-v761.F-build0729-FORTINET2.0.0.interim.131
YY

#### 8.1.18. FortiNAC

#### Validated

Firmware
Fabric Studio VersionF LBRAS
FNAC_KVM-v7-build0815-FORTINET2.0.4.interim.167
Y
YY

#### 8.1.19. FortiNDR

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FNDR_VMKV-STANDALONE.v7.4-build0540-FORTINET2.0.0.interim.126
YYY

#### 8.1.20. FortiPAM

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FPA_KVM-v100-build1138-FORTINET2.0.0.interim.119
YYY

#### 8.1.21. FortiPortal

> **Warning**
> Fabric Studio waits for the web service to be ready before installing a FortiFlex license as FortiPortal
> internals require the web service to achieve this task.

> **Warning**
> Serial console behavior may vary between two installs and may stuck Fabric Studio during the login
> process.

#### Validated

Firmware
Fabric Studio VersionF L BRA S
FPC_VM64-V7.4.5-build2119-release-kvm-Portal 2.0.2.interim.151
YNYY NN
FPC_VM64-V7.2.2-build1076-release-kvm-Portal2.0.0.interim.94
YNYY NN

#### 8.1.22. FortiProxy

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FPX_KVM-v700.F-build0587-FORTINET2.0.0.interim.102
YYY

#### 8.1.23. FortiRecorder

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FRC_VMKV-64-v72-build0231-FORTINET2.0.0.interim.125
YYY

#### 8.1.24. FortiSandbox

FortiSandbox inside a Fabric Studio VM support is limited because of Deep nested VMs
FortiSandbox inside a Fabric Studio Docker is experimental

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FSA_KVM-v400-build0393-FORTINET2.0.0.interim.131
YYY

#### 8.1.25. FortiSIEM

#### Validated

Firmware
Fabric Studio VersionF L B RA S
FSM_Full_All_KVM_7.2.3_build02562.0.0.interim.125
NNNNNN

#### 8.1.26. FortiSOAR

> **Important**
> FortiSOAR only supports one NIC (port1) and it must be in DHCP.

#### Validated

Firmware
Fabric Studio VersionF L BRAS
fortisoar-kvm-enterprise-7.6.2-55072.0.3.interim.157
YYYY
fortisoar-kvm-enterprise-7.6.1-52752.0.2.interim.149
YYY
fortisoar-kvm-enterprise-7.6.0-50122.0.0.interim.131
YY

#### 8.1.27. FortiSRA

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FRA_KVM-v100-build1138-FORTINET2.0.0.interim.119
YYY

#### 8.1.28. FortiSwitch

> **Important**
> This firmware is only available to Fortinet employee.
> License is not required in standalone mode.
> When the FortiSwitch is managed by a FortiGate using FortiLink, it requires a FortiSwitch license: it
> can be requested via ITF - SKU LIC-FS24VM-INT . Use FSW_24VM-v7 image.
> With FSW_108D_VM-v7 firmware license isn’t available via ITF, contact pm_fsw@fortinet.com.

#### Validated

Firmware
Fabric Studio VersionFL BRAS
FSW_108D_VM-v7-build5437-FORTINET2.0.0.interim.95
YYY

#### 8.1.29. FortiSwitch-NMS

> **Warning**
> The serial console and display are automatically logged in by the FortiSwitch-NMS: DO NOT
> PUBLICLY EXPOSE these accesses to the internet !

> **Important**
> Experimental support: only the management port is configured with the management router as
> nameserver and default gateway.

#### Validated

Firmware
Fabric Studio VersionF L B RA S
FSWNMS_KVM-v1.13-build08772.0.3.interim.160
NYNNNN

#### 8.1.30. FortiTester

> **Warning**
> FortiTester CLI doesn’t allow to change the default password on CLI, it must be done at first login on
> the web interface.

#### Validated

Firmware
Fabric Studio VersionFL BRA S
FTS_VM_KVM-v723-build0362-FORTINET2.0.0.interim.94
YYY NN

#### 8.1.31. FortiWeb

#### Validated

Firmware
Fabric Studio VersionF LBRAS
FWB_KVM-v700-build0603-FORTINET2.0.0.interim.94
Y
YY Y

### 8.2. Third-party devices

#### 8.2.1. ISO firmware

All ISO firmware for live image (we don’t talk about ISO to install Windows or other products) doesn’t
use a persistent disk, it means that Fabric Studio CAN’T:
configure them
backup or restore configuration
execute a postinst script
All these images must have their network port configured by DHCP.

#### 8.2.2. Debian-Lubuntu

This is an installation of the Light Ubuntu (https://lubuntu.me/) with the openssh-server installed.
We also support it when root file system is installed on a LVM, to allow people to extend the logical
volume disk during postinst.

#### 8.2.3. VyOS

#### LACP

In order to support LACP on VyOS, the interface’s type must be e1000.
If the default interface’s type of your firmware is virtio, you can use the VM parameters “meta_patch”
(see Patching) to change it to e1000:

```
model vm parameters update VM_ID '{"meta_patch": "<update node=\"./hypervisor
```

#### 8.2.4. To Be Completed

…

### 8.3. Deep nested VMs

Both FortiDeceptor and FortiSandbox needs to run VM, they end as a level 3 VM when run inside a
Fabric Studio VM:

```
L0: Hypervisor (VMWare, GCP, ...)
L1: Fabric Studio
L2: FortiDeceptor, FortiSandbox
L3: VMs
```

> **Warning**
> Such depth of VM is experimental and may not work or with poor performance.

## 9. Windows

### 9.1. Installation

You can download official images from Microsoft:
Windows 10
Windows 10 Entreprise edition
Windows 11
Windows 11 Enterprise edition
Windows Server 2022

> **Warning**
> It’s your responsibility to conform to Microsoft license and policies.
> By default Fabric Studio Windows meta template use e1000 network driver and sata disk, if you
> prefer to use virtIO, you must download the driver ISO image from Fedora

#### 9.1.1. Copying ISO image

The ISO image filename must begin (case insensitive) with “ windows ” or “ win ” followed by a
number, and a dash or underscore, eg:

```
Win10_22H2_EnglishInternational_x64v1.iso
Win11_23H2_EnglishInternational_x64v2.iso
windows-server-2022.iso
Windows2016.iso
```

Copy the ISO image using scp (or sftp) to the home repository:

```
# scp Win11_23H2_EnglishInternational_x64v2.iso admin@FS_IP:firmwares/
```

Refresh the home repository using CLI or GUI:

```
(lab-fs20) # system repository home refresh
```

../_images/repository_home_refresh.png
If you plan to use virtIO driver:
copy the driver ISO image:

```
# scp virtio-win-0.1.240.iso admin@FS_IP:
```

> **Warning**
> Do NOT copy it to the firmwares  directory !
> edit the generated meta files:

```
<devices>
...
<interface>
<target dev="eth{idx}" fp:count="10" fp:min="1" fp:start="0"/>
<model type="virtio"/>
</interface>
...
<disk device="disk" type="file" fp:size="64" fp:unit="GiB">
<target bus="virtio"/>
<source file="windows-disk.qcow2"/>
<boot order="1"/>
</disk>
...
</devices>
```

refresh the home repository

#### 9.1.2. Creating the Fabric

define a new Fabric to install the windows:
../_images/create_fabric_1.png
../_images/create_fabric_2.png
add the Windows device:
../_images/add_windows_device_1.png
../_images/add_windows_device_2.png
../_images/add_windows_device_3.png
../_images/add_windows_device_4.png
If you have more than one Windows ISO image, select the one you want before clicking on “OK”:
../_images/add_windows_device__change_firmware.png
configure Windows ethernet port in DHCP:
../_images/edit_windows_port_1.png
../_images/edit_windows_port_2.png
../_images/edit_windows_port_3.png
../_images/edit_windows_port_4.png
configure Windows default gateway and DNS:
../_images/edit_windows_1.png
../_images/edit_windows_2.png
../_images/edit_windows_3.png
../_images/edit_windows_4.png
if you are not using the management switch and network, you must enable DHCP server on System
Host port, eg:
../_images/enable_dhcp_server_1.png
../_images/enable_dhcp_server_2.png

#### 9.1.3. Installing Windows

install the Fabric:
../_images/install_fabric.png
CLI

```
(lab-fs20) # runtime fabric install fabric
```

the Windows installation process requires that you press a key to start it
../_images/press_a_key.png
If the console is already on the EFI shell, type the reset  command to be offered the press key
option:
../_images/efi_shell.png
follow the installation process

#### 9.1.4. Installing with virtIO driver

If you use virtIO device, especially for the disk controller, during the installation process you must
install the virtIO drivers.
you must power off the Windows device to attach the virtIO driver ISO image:
../_images/power_off_windows_device.png
attach the virtIO driver ISO image (only by CLI):

```
(lab-fs20) # runtime vm cdrom attach WINDOWS virtio-win-0.1.240.iso
```

power-on the Windows device:
../_images/power_on_windows_device.png
when it’s time to choose the hard disk for installation, you should not see any, but you should be able
to Load Driver:
../_images/load_driver.png
Since the virtIO driver ISO image is already mounted, you only need to click on “OK”:
../_images/search_ok.png
select the Red Hat VirtIO SCSI controller driver matching your Windows version:
../_images/choose_driver.png
once the drivers’ installation is complete, you should now see the hard disk, you can then install
Windows on it
after the installation process complete you may have to install more virtIO driver for some devices
from the Windows “Device Manager”

#### 9.1.5. Exporting the Windows device disk

shutdown the Windows device

> **Warning**
> With recent Windows release, Windows may ignore network adapter MAC address update done in
> the Fabric. To ensure your Windows always boot with the defined MAC address, you must go to the
> Device Manager and remove the network adapter(s) before the shutdown. Since the driver is cached,
> it should automatically be installed by Windows on next reboot.
> export the Windows disk:

```
(lab-fs20) # runtime vm export WINDOWS windows-install
```

> **Warning**
> When you re-export a disk it’s NOT recommended to reuse the current disk name because you won’t
> be able to start your Windows again until you reinstall it using the new firmware.
> the newly exported firmware should now be available, you can add a new Windows device in your
> fabric to test it with this firmware without touching the original Windows device

### 9.2. Timezone

The Fabric Studio is configured to be in UTC timezone and it exposes the system clock to the VM as
UTC too.
But Windows supposes the system clock is in the selected timezone. In this case, even if you change
the Windows timezone you still view the clock value exposed by the Fabric Studio (except for DST
adjustment).
In order to get the correct clock, you must tell Fabric Studio to expose a timezoned clock to the
Windows VM. This is achieved by the telling the VM hypervisor to change the exposed clock, in
libvirt/KVM XML definition you must create/update the clock  XML node, eg:

```
<clock offset="timezone" timezone="Europe/Paris"/>
```

If you can modify the firmware meta and that all VM using this firmware use the same timezone, you
can edit the meta to update/create the clock  XML node inside the <hypervisor>  node.
If you can’t modify the meta, with Fabric Studio you can patch by instance on the fly the created
libvirt/KVM XML definition with the CLI, use model vm parameters update ...  to set the meta_patch
XML string value (see Patching).
You need first to verify if your Windows VM meta already contains a clock node or not (empty result),
eg:

```
(fabric-studio) # model vm meta 32 ./hypervisor/clock --firmware
<clock offset='utc'/>
```

#### 9.2.1. Add clock  node

To add a clock, use the insert meta patch syntax, eg:

```
<insert node="./hypervisor">
<clock offset="timezone" timezone="Europe/Paris"/>
</insert>
```

On the CLI, eg:

```
model vm parameters update 32 '{"meta_patch": "<insert node=\"./hypervisor"><
```

#### 9.2.2. Update clock  node

To update a clock, use the update meta patch syntax, eg:

```
<update node="./hypervisor/clock">
<attribute name="offset" value="timezone"/>
<attribute name="timezone" value="Europe/Paris"/>
</update>
```

On the CLI, eg:

```
model vm parameters update 32 '{"meta_patch": "<update node=\"./hypervisor/cl
```

## 10. Expert

### 10.1. Backup as Firmware: creating snapshot

You can backup a VM disk to create a firmware in the home repository. It allows to maintain a
complex configuration of a product and handles the case when you have no way to just backup the
configuration to restore it on next install (eg: Windows).
It’s what we call here a snapshot firmware.
To achieve that Fabric Studio copies or consolidates the different disks and other VM related files
and information (eg: virtual TPM files, NVRAM file, …) to the home repository inside a “split” directory
(so the “.split” file in it) and processes it as a firmware archive.
Pros:
no time lost building a zip archive
no time lost uncompressing the zip archive
no space lost with a duplicate of the snapshot firmware content both in the home repository and in
the backingstore directory (where Fabric Studio uncompresses firmware archives)
Cons:
touching the snapshot firmware files in the home repository may break your fabric

> **Warning**
> To export disks you must shutdown the VM first.
> The export works for both VM types (KVM and LXC).
> Fabric Studio repository tool normally computes checksum of the different firmware archives, but for
> both performance and support of “split” directory firmware archive, checksums are not computed in
> the home directory and the empty checksum
> ( e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 ) is always used.

#### 10.1.1. Standalone snapshot firmware (default)

By default when you backup as firmware, Fabric Studio creates a standalone snapshot firmware, it
means that Fabric Studio merges the runtime VM disks content with the original standalone firmware
disks content to create the new standalone disks.
Command:

```
runtime vm export VM_ID_OR_NAMEID FIRMWARE_NAME
```

#### 10.1.2. Diff snapshot firmware

You can backup only the difference, in this case Fabric Studio creates a diff snapshot firmware, it
means that Fabric Studio extracts the delta between your runtime VM disks content and the original
standalone firmware disks content to create the new diff disks.

> **Warning**
> A diff snapshot firmware is FULLY DEPENDENT on the original standalone firmware and can’t work
> without it.
> When you create a new diff snapshot firmware over a VM running a diff snapshot firmware, you
> always end with the delta between the runtime VM disks content and the original standlone firmware
> disks content, so each diff snapshot firmware is independent of the others diff snapshot firmwares: it
> simplifies management and cleanup of unused diff snapshot firmwares.
> Command:

```
runtime vm export --diff VM_ID_OR_NAMEID FIRMWARE_NAME
```

#### 10.1.3. Tracked information

Fabric Studio tracks different information in the meta of your snapshot firmware.
In the (root) “model” XML node attributes:
if the VM has been pre-boot configured:

```
is_pre_boot_prepared="<True or False>"
```

if the VM has been licensed and with which license (serial number):

```
is_licensed="SERIAL_NUMBER"
```

if the VM had been post-boot configured:

```
is_post_boot_prepared="<True or False>"
```

For diff snapshot firmware it also tracks in the “model/diff_from” XML node the original standalone
firmware checksum, name (relative path) and other required informations.

#### 10.1.4. Publishing to a repository

To publish a snapshot firmware on a repository, you must package the snapshot firmware from Fabric
Studio CLI.
Command:

```
system repository home package <FIRMWARE_NAME>
```

It packages the split directory and the meta file as a zip file <FIRMWARE_NAME>.zip  next to the split
directory.
The archive can be copied to the repository server. If you use a repository tool version compatible
with packaged snapshot firmwares, there’s no need to copy the meta file (it’s automatically extracted
from the archive).
When Fabric Studio packages a diff snapshot firmware, it MUST track the original standalone
firmware checksum to identify the original standalone firmware to download and extract it during VM
installation:
your original standalone firmware is not in the home repository: Fabric Studio already knows its
checksum
your original standalone firmware is an archive in the home repository: Fabric Studio computes the
archive checksum (as no checksum are computed by default in the home repository). This checksum
value is cached (in <FIRMWARE>.chksum  file) to speed up future packages creation
your original firmware is a standalone snapshot firmware in the home repository: the standalone
snapshot must be packaged first as both firmwares must be published, Fabric Studio uses the
packaged standalone snapshot firmware archive checksum as the original standalone firmware
checksum

#### 10.1.5. Original standalone firmware resolution

For a diff snapshot firmware, when Fabric Studio installs a VM, it must also download and extract the
original standalone firmware:
Fabric Studio looks for a firmware with the same original standalone firmware checksum (if the
checksum is not the empty checksum)
if the checksum of the original standalone firmware is the empty checksum (it’s the case when the
original standalone firmware is in the home repository), it looks for a firmware by firmware name
(relative path) only in the home repository
in last resort it looks for a firmware by firmware name (relative path) in any known repositories
The original standalone firmware is tracked by 3 fields, they are only meaningful for diff snapshot
firmware:
is_diff:
true when the firmware is a diff snapshot firmware
diff_from:
references the selected original standalone firmware once resolved, it stays null until successfully
resolved
backup_state:
state of the resolution:
STANDALONE:
no resolution the firmware is a standalone firmware
UNRESOLVED:
no original firmware found
RESOLVED:
the original firmware is found
FALLBACK:
the original firmware is not found, but one with same name is used
As backup_state is a property, you must explicitly ask for the field using the “related-fields” option,
eg:

```
(fabric-studio) # cli json enable
(fabric-studio) # system repository firmware detail 809 --related-fields back
    {
"errors": {},
"object": {
"__db": "default",
"__model": "repository.firmware",
"added_at": "2025-07-24T13:03:22.223Z",
"build": 3510,
"diff_from": 810,
"expiration": null,
"hexdigest": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca49
"id": 809,
"is_diff": true,
"backup_state": "RESOLVED",
...
```

If the firmware is not a diff snapshot firmware:
is_diff:
is always false
diff_from:
is always null
backup_state:
is STANDALONE
Fabric Studio tries to resolve the original firmware reference on every repository refresh, as a
consequence the backup_state can change.
To force a firmware resolution use:

```
system repository firmware resolve ID
```

### 10.2. Extending disks

> **Note**
> Depending your hypervisor you may be able to resize the system disk or add extra disks on the fly. If
> you lack system disk space it may be the only solution as the Fabric Studio MAY NOT be able to
> reboot !
> Fabric Studio uses LVM to manage disks and allow dynamic size increase.

> **Important**
> On boot by default Fabric Studio adds the available free space to the data disk. If you want to add
> free space to the system disk, you must disable the auto extend:

```
system preferences set '{"auto_resources_extend": false}'
```

You have two solutions to add free space to your Fabric Studio ( virsh/kvm  commands are given as
a hint, use at your own risks):
extend an existing disk (firmware disk or extra disk):
VM is powered-off, eg:

```
qemu-img resize /path/to/FS_DOMAIN.qcow2 512G
```

VM is powered-on, eg:

```
virsh blockresize FS_DOMAIN /path/to/FS_DOMAIN.qcow2 512G
```

or add an extra disk to your VM definition
Power-on the VM or if you have done it on the fly in Fabric Studio CLI run:

```
system disk extend
```

During the reboot or using the previous command, the Fabric Studio analyses the disk(s) to add
space to the volume group.

> **Important**
> The amount of free space on the firmware disk must greater than 32GB, under this value Fabric
> Studio will not extend the volume group. To identify the available free space use system disk detail
> command, eg:

```
(fabric-studio) # system disk detail
- Main Disk device '/dev/vda' analysis
  Fix GPT
  Read GPT
{
"device": "/dev/vda",
"free-size": 0,
...
"threshold": 34359738368,
"vg": {
"free-size": 0
  }
}
```

Look to the global “free-size” not the one under “vg”.

#### 10.2.1. Data disk

On power-on, Fabric Studio adds free VG space to the data disk.
If you have disabled auto extend or have added space on the fly, use the CLI command:

```
system disk data extend <SIZE>
```

> **Warning**
> If you use 0  as size, it uses 100% of the free space. Size must be based on powers of 2. You can
> use units for the size, eg: 32GiB  ( 32GB  is also accepted)

#### 10.2.2. System disk

You MUST have disabled the auto extend or have added space on the fly, then use the CLI
command:

```
system disk system extend <SIZE>
```

> **Warning**
> If you use 0  as size, it uses 100% of the free space. Size must be based on powers of 2. You can
> use units for the size, eg: 32GiB  ( 32GB  is also accepted)

### 10.3. MTU Policy

Because user can change the interface’s MTU for some devices, Fabric Studio relies on a higher
MTU for the hypervisor virtual network in order to never be the one fragmenting packets.
Here we detail the MTU policy for internal (hypervisor) interfaces and for each device (guest)
interface:

```
+------------------------------ -- -- - -
| Fabric Studio
|
|+----------------------+
|| Device               |
|||
||    Guest Iface       |
|||||
|+---------||-----------+
|||
|       Hypervisor Iface
|
.
.
```

#### 10.3.1. VM

### LXC

Guest: the configured MTU or default if MTU = 0
Hypervisor: 65535 (max allowed for VETH)

### KVM

Guest: default
Hypervisor: 65521 (max allowed for TUN/TAP)

#### 10.3.2. Native Switch

On native switch creation the internal port MTU is set to 65535 but OpenVSwitch may decide to
reduce the value. This should not have any impact as the internal port is always down and never
used.

#### 10.3.3. Native Router

Guest: the configured MTU or default (1500) if MTU = 0
Hypervisor: 65535 (max allowed for VETH)

#### 10.3.4. Host

Because the host device represents the Fabric Studio and Fabric Studio is connected to the external
world, it always uses the default MTU (1500).

#### 10.3.5. Cables

Cables follow Native Switch MTU policy.

### 10.4. Meta files

#### 10.4.1. Templates

This section is mainly for users that must provide new firmware meta template to Fabric
Studio Support Team.

> **Warning**
> Meta templates are not related to Fabric templates.
> A meta template describes one or more meta model for device’s firmwares, it’s used on repository
> server or by the home repository to attach a meta model to a firmware:

```
<models xmlns:fp="fp" xmlns:fpt="fpt">
<model name="FMG62">...</model>
<model name="FMG">...</model>
<order>
<model name="FMG62"/>
<model name="FMG"/>
</order>
</models>
```

As different version of a firmware may have different requirements (eg: higher memory requirements
for a newer version), the meta template describes the different version of the meta and it includes
directives to validate which version of the meta match the firmware’s version. Each meta model
matching a firmware name are tested following the “order” declaration with first match win rule.

### Filename pattern matching

Fabric Studio uses filename pattern matching to identify firmwares, eg:

```
<model name="FMG62" deprecated="False">
<detection experimental="False" fpt:experimental="bool">
<firmware type="FMG" re="^(%device%FMG)_VM64_KVM-{{version}}(%beta%Beta\d
...
```

The model/detection/firmware[@re]  attribute is a python regular expression with extended match
group syntax (but you can use also normal (?P<name>...)  syntax.)
You have two types of extended match groups:
explicit named match group, eg (%device%...)  that must contains the regular expression after the
name. You can also add a converter, eg (%major:int%...) . Converters are str (default), int, hex and
oct
the common match groups {{version}}  and {{build}}  that are automatically replaced with the
complex expression to match most of the version and build string used in firmware filename. The
{{version}}  defines sub match integer groups major , minor , patch , revision  and a string group
version_s  (to match things like Beta...  suffixes)

> **Note**
> Legacy syntax is model/detection/archive .

### Meta model version matching

The detection section should contains at least a “match” node with an expression “expr” to validate
that the firmware we are analyzing must use this version of the meta, eg:

```
...
<model name="FMG62" deprecated="False">
<detection experimental="False" fpt:experimental="bool">
<firmware type="FMG" re="^(%device%FMG)_VM64_KVM-{{version}}(%beta%Beta\d
<match>version.major GT 6</match>
<match>version GTE 6.0.0.0.215</match>
<core>version GTE 1.0</core>
</firmware>
...
```

In the example, the meta only applies if the “version” has a major value greater than 6 or that is a
6.0.0-build215 or better.

> **Important**
> The “build” word is removed from the version and we have major, minor, patch, revision and build so
> 6.0.0-build215 is 6.0.0.0.215.
> The “match” node can be repeated multiple time, and only one of them should match to validate.

> **Note**
> We use multiple “match” to avoid building very long and complicated OR expression.

### Core model version matching

Once the right meta model has been selected and the meta information generated on the repository,
a Fabric Studio can now retrieve the information to analyze which firmwares it can use.
It’s the purpose of the “core” directives that declares the minimal required version of the “core” Fabric
Studio package that support this firmware.
In the example any core version greater than 1.0 supports this firmware.
The “core” directives can be declared more than once to support when two versions (or more) of the
Fabric Studio are maintained, ex:

```
<core>version:minor = 2.0 AND version GT 2.0.12</core>
<core>version GT 2.1.4</core>
```

### Evolution

When a new firmware must use a new meta model, this meta model must be declared first in the
order of detection and the matching directives must declare the correct minimal Fabric Studio core
that supports it, eg:

```
<order>
<model name="FGT72"/>
<model name="FGT62"/>
<model name="FGT"/>
</order>
```

### Version Match Syntax

EBNF grammar (case insensitive):

```
start    : expr
expr     : test | "(" expr ")" | expr OP expr
OP       : "|" | "OR" | "&" | "AND"
test     : SRC TEST_OP version
SRC      : "VERSION"
           | "VERSION.MAJOR"
           | "VERSION.MINOR"
           | "VERSION.REVISION"
           | "VERSION.BUILD"
           | "VERSION:MAJOR"
           | "VERSION:MINOR"
           | "VERSION:REVISION"
           | "VERSION:BUILD"
version  : major ("." minor ("." revision ("." build)?)?)?
major    : number
minor    : number
revision : number
build    : number
number   : /[1-9][0-9]*/
TEST_OP  : TEST_EQ | TEST_GT | TEST_GTE | TEST_LT | TEST_LTE | TEST_NE
TEST_EQ  : "==" | "=" | "EQ"
TEST_GT  : ">" | "GT"
TEST_GTE : ">=" | "GTE" | "GE"
TEST_LT  : "<" | "LT"
TEST_LTE : "<=" | "LTE" | "LE"
TEST_NE  : "!=" | "NE"
```

VERSION:
the full version (ex: for 1.2.3.4 => 1.2.3.4)
VERSION.MAJOR:
only the version’s major (ex: for 1.2.3.4 => 1)
VERSION.MINOR:
only the version’s minor (ex: for 1.2.3.4 => 2)
VERSION.REVISION:
only the version’s revision (ex: for 1.2.3.4 => 3)
VERSION.BUILD:
only the version’s build (ex: for 1.2.3.4 => 4)
VERSION:MAJOR:
the version up to major (ex: for 1.2.3.4 => 1)
VERSION:MINOR:
the version up to minor (ex: for 1.2.3.4 => 1.2)
VERSION:REVISION:
the version up to revision (ex: for 1.2.3.4 => 1.2.3)
VERSION:BUILD:
the version up to build (ex: for 1.2.3.4 => 1.2.3.4)

> **Warning**
> A missing element is interpreted as 0 , so VERSION.REVISION  for 1.2  is 0  and VERSION:REVISION  is
> 1.2.0 .

### Inherit

To reduce the burden to clone a whole “model” tree to adjust only some parameters, you can use the
“inherit” mode, ex:

```
<model name="FMG642">
<inherit name="FMG62">
<replace node="./detection/firmware/match">
<match>version GT 7</match>
<match>version GE 7.4.2.0.2397</match>
</replace>
<replace node="./detection/firmware/core">
<core>version GT 2.0.62</core>
</replace>
</inherit>
</model>
```

In the example, we only want the FMG 6.4.2 to be available to Fabric Studio with core version >
2.0.62, but the meta template is exactly the same. Here we inherit from the “FMG62” meta template
and replace the “match” and the “core” conditions.
See Patching for the syntax to patch the inherited meta.

### Firmware meta

When a meta template model matches a firmware, the generated meta for the firmware only contains
the model node and its children.
The detection node and children are updated with information extracted from the firmware name.
The disk/source[@file]  attribute may be updated with detection information (eg: when the disk
name is not static but contains firmware version). The available variables depend of the Filename
pattern matching regular expression named groups:

```
<model name="VYOS-OVA" deprecated="False">
  <detection experimental="no">
    <firmware type="VYOS" re="^(%ident%vyos)-{{version}}(%beta%-beta-\d+)?-(%
  ...
  <!-- the disk uses firmware information -->
  <disk fp:size="0" fp:unit="MiB" type="file" device="disk">
    <target bus="virtio"/>
    <source file="VyOS-{version}{beta}-{arch}-disk1.vmdk"/>
  </disk>
```

When the firmware is also the disk (eg: when the firmware is an ISO or a QCOW2):

```
<model name="ISO" deprecated="False">
  <detection experimental="no" assign="firmware">
    <firmware type="BASIC" re="\.iso$">
...
<!-- the disk is the firmware file -->
<disk type="file" device="cdrom">
  <source file="" fp:from_firmware="yes"/>
  <target bus="sata"/>
</disk>
```

The detection/firmware[@assign]  and source[@{fp}from_firmware]  are mutually required:
assign:
tells how to assign the firmware to disk, can be:
firmware:
assign the firmware as the disk
content:
assign disk(s) from the content of the archive (tar, zip, …). Not all files can be disks, filtered on
extension
auto:
try to do the best based on file type, this is a fallback and should not be used by users
from_firmware:
tells which disk(s) comes from the firmware using the defined assign method

### License Detection

> **Warning**
> This mechanism only applies to manual upload of license file, it doesn’t apply to license downloaded
> from FortiCloud !
> The license detection directives helps to associate a license to it’s VM type:

```
<detection ...>
...
<license fname="^AZA">
<id>FSWNMS</id>
</license>
</detection>
```

There is two modes of detection searched in the following order:
the ID mode, Fabric Studio analyzes the first line of the license, if it’s in the form:

```
-----BEGIN <WORD> ... LICENSE-----
```

Fabric Studio compares the WORD  to all detection license ID of the templates and stops on first match
if the ID mode detection fails, Fabric Studio checks the license filename with detection license fname
regular expression and stops on first match

### License Installation

The license node declares:
when the license must be installed (“first” or “last”)
supported type of license (LIC, FLEX or NONE)
first firmware version to support these types of license, see Version Match Syntax
Example:

```
<license install="first">
<auto supported="LIC,FLEX">version GE 7.2</auto>
<auto supported="LIC">version GT 0</auto>
</license>
```

> **Note**
> This declaration is introduced by Fabric Studio 2.0.0.beta.5 .

#### Legacy declaration

> **Important**
> Legacy declaration is deprecated and planned to be removed with the 2.1. Repository owner must
> rebuild their Fabric Studio repositories with the compatible tool version (see release notes
> https://fortinet.sharepoint.com/:u:/r/sites/FabricStudio/SitePages/Interim-Release-Notes.aspx).
> The legacy auto declaration was too simple in the version compatibility declaration, preventing
> complex declaration if new license type is introduced in two or more version branch, eg: when
> introduced in both 7.4.2 and 7.2.6.
> the “version” to compare can be “ * ” or a version
> supported type of license
> Example:

```
<license install="first">
<auto version="*">LIC,FLEX</auto>
</license>
```

### Debian image partitions

Fabric Studio mounts and patch filesystem for compatible Debian like firmwares.
In the control, you must specify the partion used as root, eg:

```
...
<control>
<filesystem>
<mount type="%TYPE%" %ATTRS%>%MOUNTPOINT%</mount>
</filesystem>
...
```

%MOUNTPOINT%  must always be / , Fabric Studio doesn’t support multi partitions mounting.
Fabric Studio recognizes following %TYPE% :
part:
for simple partition, required %ATTRS% :
part:
with the part name suffix as seen by NBD driver
Eg: <mount type="part" part="p2">/</mount>
lvm:
for LVM, required %ATTRS% :
group:
the volume group
logical:
the logical volume
Eg: <mount type="lvm" group="lubuntu" logical="root">/</mount>

#### 10.4.2. Patching

The meta patching syntax is used by the meta template inheritance mechanism or when defining a
Vm “meta_patch” parameters ( model vm parameters ... ).
All examples are patching the following accesses:

```
<accesses>
<access type="SERIAL" path="" port="0"/>
<access type="HTTP" path="" port="80"/>
<access type="HTTPS" path="" port="443"/>
<access type="SSH" path="" port="22"/>
<access type="VNC" path="" port="0"/>
<access type="SPICE" path="" port="0"/>
</accesses>
```

You have different actions that all take a node Xpath to select the node to modify:
delete:
<delete node="XPATH"/>  to delete all matching nodes, eg:

```
<delete node="./accesses/access"/>
```

New accesses:

```
<accesses>
</accesses>
```

replace:
<replace node="XPATH">NODES</replace>  to replace in parent node all matching children nodes with
NODES, eg:

```
<replace node="./accesses/access">
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</replace>
```

New accesses:

```
<accesses>
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</accesses>
```

insert:
<insert node="XPATH">NODES</insert>  to insert new children, eg:

```
<insert node="./accesses">
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</insert>
```

New accesses:

```
<accesses>
<access type="SERIAL" path="" port="0"/>
<access type="HTTP" path="" port="80"/>
<access type="HTTPS" path="" port="443"/>
<access type="SSH" path="" port="22"/>
<access type="VNC" path="" port="0"/>
<access type="SPICE" path="" port="0"/>
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</accesses>
```

append:
<append node="XPATH">NODES</append>  to append NODES after last matching node, eg:

```
<append node="./accesses/access">
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</append>
```

New accesses:

```
<accesses>
<access type="SERIAL" path="" port="0"/>
<access type="HTTP" path="" port="80"/>
<access type="HTTPS" path="" port="443"/>
<access type="SSH" path="" port="22"/>
<access type="VNC" path="" port="0"/>
<access type="SPICE" path="" port="0"/>
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</accesses>
```

prepend:
<prepend node="XPATH">NODES</prepend>  to prepend NODES before first matching node, eg:

```
<prepend node="./accesses/access">
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
</prepend>
```

New accesses:

```
<accesses>
<access type="HTTPS" name="ADMIN" path="" port="1443"/>
<access type="SERIAL" path="" port="0"/>
<access type="HTTP" path="" port="80"/>
<access type="HTTPS" path="" port="443"/>
<access type="SSH" path="" port="22"/>
<access type="VNC" path="" port="0"/>
<access type="SPICE" path="" port="0"/>
</accesses>
```

update:
<update node="XPATH"><attribute name="ATTR" [value="VALUE"]/>...</update>  to update a node
attributes, if no replacement value is specified the attribute is removed, eg:

```
<update node="./accesses/access[@type=&quot;HTTPS&quot;]>
<attribute name="port" value="1443"/>
<attribute name="path" value="/admin"/>
</update>
<update node="./accesses/access[@type=&quot;VNC&quot;]>
<attribute name="path"/>
</update>
```

New accesses:

```
<accesses>
<access type="SERIAL" path="" port="0"/>
<access type="HTTP" path="" port="80"/>
<access type="HTTPS" path="/admin" port="1443"/>
<access type="SSH" path="" port="22"/>
<access type="VNC" port="0"/>
<access type="SPICE" path="" port="0"/>
</accesses>
```

> **Note**
> The execution order is: delete, replace, insert, append, prepend, update.
> To use double quotes in XPATH value, you must use the &quot; , eg:

```
'./accesses/access[@type="HTTP"]' as './accesses/access[@type=&quot;HTTP&quot
```

### 10.5. VM Hooks

The VM hooks allow Fabric Studio to perform some extra steps during installation. These settings are
only for expert and can be configured using the “expert” VM parameter. The “expert” parameter uses
TOML syntax, eg:

```
model vmparameters update VM_ID '{"expert": "[section]\nkey=value\n..."}'
```

#### 10.5.1. Post boot configuration hooks

Before (pre-step) and after (post-step) the post boot configuration phase you can add a sleep step
defined in seconds, eg:

```
[post-boot-hooks]
pre-sleep=5
post-sleep=10
```

#### 10.5.2. License installation hooks

Before (pre-step) and after (post-step) the license installation phase you can add a sleep step
defined in seconds, eg:

```
[license-hooks]
pre-sleep=5
post-sleep=10
```

### 10.6. Baremetal

#### 10.6.1. Native

You can dump the Fabric Studio disk to a physical disk to transform a physical host into a native
baremetal Fabric Studio.

> **Important**
> It’s highly recommended to have a working serial console connection to your physical host in order to
> configure or troubleshoot network connectivity.

### Interfaces

Fabric Studio relies by default on the kernel system interface detection order and naming (eg: eno3,
eno4. enp3s1, …) to link to Fabric Studio interfaces (mgmt1, port1, port2, …). As a consequence the
first interface that normally becomes the management interface may not be the one you’re expecting.
And the extra ports order may also not match your requirements.
You can link a Fabric Studio interfaces (<NAME>) and a system interface (<SYSNAME>):

```
system expert interface link <NAME> <SYSNAME>
```

To remove a link:

```
system expert interface link <NAME>
```

To list the identified interfaces and their links:

```
system interfaces list
```

Example: to change “mgmt1” to be “ens13”:

```
(fabric-studio) # system interfaces list
1 mgmt1/ens3
2 port1/ens4
3 port2/ens5
4 port3/ens6
5 port4/ens12
6 port5/ens13
(fabric-studio) # system expert interface link mgmt1 ens13
Link 'mgmt1'
Done: you **must** reboot.
```

It’s recommended to reboot, but you can try to force the changes:

```
(fabric-studio) # system interfaces ports uninstall
(fabric-studio) # system interfaces sync
Process 'ens13'
- updating 'mgmt1' in DB
Process 'ens3'
- updating 'port1' in DB
Process 'ens4'
- updating 'port2' in DB
Process 'ens5'
- updating 'port3' in DB
Process 'ens6'
- updating 'port4' in DB
Process 'ens12'
- updating 'port5' in DB
(fabric-studio) # system interfaces mgmt restart --uninstall
Kill DHCP Client for 'mgmt1'
Kill DHCP Client for 'mgmt1'
Kill DHCP Client for 'ens13'
Start DHCP Client for 'mgmt1'
(fabric-studio) # system interfaces ports up
```

#### 10.6.2. Docker

> **Warning**
> The docker version is experimental and STRICTLY LIMITED to a reduced audience and only to use
> in labs hosted in Fortinet offices and data centers.
> This version MUST NOT be shared outside Fortinet.
> This documentation only explains the minimal information to start a Fabric Studio as a docker
> instance. It doesn’t cover network connectivity to and from your Fabric Studio instance, read Docker
> documentation for that.

> **Important**
> It’s recommended to expose all Linux capabilities. You may be able to restrict some of them, but
> you’ll have to test that by yourself (but we’ll be glad to get your feedback). The --tmpfs  options on
> create may not be required depending the exposed capabilities.
> As all dockers instances see the same hypervisor hardware, they see the same system UUID. For all
> docker instances on a hypervisor to have different serial number, you must pass the FS_SYSTEM_UUID
> with a unique UUID for each instance.

> **Warning**
> Not complying may lead to registration and license server communication troubles.
> It’s recommended to use a volume by docker instance mounted as /opt/ftnt/resources .
> You need following kernel modules to be already loaded at hypervisor level prior to any Fabric Studio
> instance start:

```
modprobe openvswitch nbd
```

> **Warning**
> All firmwares requiring disk patching are not working in docker instance (eg: FortiSOAR, debian-
> lubuntu, …).
> Eg:

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

## 11. Troubleshooting

### 11.1. Fabric Studio logs

You can access Fabric Studio logs from the home repository shell.
You can find the system logs (operating system) and the service logs (Fabric Studio):

```
(lab-fs20) # system repository home shell
admin@lab-fs20:~$ cd log/
admin@lab-fs20:~/log$ ls -la
total 16
drwxr-xr-x  4 root  root     4096 Mar 19 11:10 .
drwxr-xr-x  6 admin www-data 4096 Mar 19 09:49 ..
drwxr-xr-x  4 admin www-data 4096 Mar 19 10:45 service
drwxr-xr-x 12 admin www-data 4096 Mar 17 00:00 system
admin@lab-fs20:~/log$ ls -la service/
total 28
drwxr-xr-x 4 admin www-data 4096 Mar 19 10:45 .
drwxr-xr-x 4 root  root     4096 Mar 19 11:10 ..
drwxrwxrwx 2 admin www-data 4096 Mar 19 10:45 fortipoc
-rw-r--r-- 1 admin www-data 6251 Mar 19 14:22 nginx
admin@lab-fs20:~/log$ ls -la system
total 18008
drwxr-xr-x  12 admin www-data    4096 Mar 17 00:00 .
drwxr-xr-x   4 root  root        4096 Mar 19 11:10 ..
-rw-r--r--   1 admin www-data       0 Mar  4 09:42 alternatives.log
-rw-r--r--   1 admin www-data    7982 Feb 15 16:05 alternatives.log.1
-rw-r--r--   1 admin www-data     134 Jan 25 16:20 alternatives.log.2.gz
-rw-r--r--   1 admin www-data    2254 Dec  1 16:48 alternatives.log.3.gz
...
```

### 11.2. SystemD Journal logs

You can access Fabric Studio SystemD journal logs from the home repository shell:

```
(lab-fs20) # system repository home shell
admin@lab-fs20:~$ journalctl -D log/system/journal -u fortipoc.service -b 0
May 24 12:52:37 fabric-studio systemd[1]: Starting fortipoc.service - Fabric
May 24 12:52:37 fabric-studio systemd[1]: Started fortipoc.service - Fabric S
May 24 12:52:39 fabric-studio init[1483]: - Main Disk device '/dev/vda' analy
...
```

### 11.3. Sniff packets

In case of network problems, it’s recommended to check if packets are reaching the Fabric Studio
virtual network and are going through the different elements.
Use the runtime diagnose tcpdump  command, the command takes a device and a port, you can use
the device’s name, nameid or numerical id and port’s name or numerical id:

```
LXC(LXC):eth0 <---> port2:Management(mgmtsw):port1 <---> int1:System Host(hos
runtime diagnose tcpdump LXC eth0
runtime diagnose tcpdump mgmtsw port2
runtime diagnose tcpdump mgmtsw port1
runtime diagnose tcpdump host int1
system diagnose tcpdump mgmt1
```

> **Warning**
> To sniff packets on the Fabric Studio ports, you must use the system diagnose tcpdump  command.

### 11.4. Not enough space

See Extending disks.

### 11.5. Failing SCP

If you try to scp  files to a Fabric Studio before having changed the default password, you get this
kind of error:

```
scp fortisoar-kvm-enterprise-7.6.0-5012.qcow2 admin@10.222.10.103:firmwares/
scp: Received message too long 1500476704
scp: Ensure the remote shell produces no output for non-interactive sessions.
```

## 12. FortiPoC backward compatibility

You should be able to import any FortiPoC PoC definitions.
Limitations:
all configuration files are imported as full configuration and use the “Restore” method. You must
manually update those that are snippet and use “Append-Restore” (the method used by FortiPoC).
You can try “Script” method, but it’s not guaranteed that it works for all devices
the “copymac” introduced in FortiPoC 1.8.20 is converted to copy hwaddr from peer, you MUST
verify the peer port is the right port

## 13. Known Issues
