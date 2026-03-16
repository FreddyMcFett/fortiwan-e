# FortiWAN-E

Web-based WAN Emulator for Fortinet SD-WAN demos on Fabric Studio.

## Architecture

FortiWAN-E runs as a **standalone web application** outside of Fabric Studio (on a separate machine, VM, or container). It connects to the Fabric Studio REST API over the network to apply Linux `tc` (traffic control) rules on native Router devices inside the fabric.

```
+-----------------------------------------------------+
|                   Fabric Studio (ESXi VM)            |
|                                                      |
|   Branch FGT ──── Router (ISP1) ──── HQ / Internet  |
|        │           (tc rules)            │           |
|        └────────── Router (ISP2) ────────┘           |
|                    (tc rules)                        |
|                                                      |
+---------------------------┬--------------------------+
                            │ REST API (HTTPS)
                            │
               +────────────┴────────────+
               │       FortiWAN-E        │
               │  (Debian/Ubuntu/Docker) │
               │    http://<ip>:5000     │
               +─────────────────────────+
                        ▲
                        │ Browser
                      Admin
```

FortiWAN-E controls `tc netem` and `tc tbf` qdiscs on each Router port to emulate:

| Parameter       | Range         | Description                    |
|----------------|---------------|--------------------------------|
| Delay          | 0-2000 ms     | Fixed latency added to packets |
| Jitter         | 0-500 ms      | Latency variation              |
| Packet Loss    | 0-100%        | Random packet drop rate        |
| Bandwidth      | 0-1 Gbit/s    | Rate limiting (tbf)            |
| Corruption     | 0-50%         | Random bit errors              |
| Duplication    | 0-50%         | Duplicate packets              |
| Reorder        | 0-50%         | Out-of-order delivery          |

## Quick Start

### Option 1: Docker Compose (Recommended)

**Prerequisites — Install Docker and Docker Compose:**

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh

# Add your user to the docker group (log out and back in after)
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker compose version
```

> Docker Compose v2 is included with Docker Engine. On older systems with
> standalone `docker-compose`, replace `docker compose` with `docker-compose`.

**Install and run FortiWAN-E:**

```bash
# Clone the repository
git clone https://github.com/FreddyMcFett/fortiwan-e.git
cd fortiwan-e

# Start FortiWAN-E (builds the image automatically on first run)
docker compose up -d
```

The application will be available at `http://<your-ip>:5000`.

**Manage the container:**

```bash
# Check status
docker compose ps

# View logs
docker compose logs -f

# Stop
docker compose down

# Rebuild after pulling updates
git pull
docker compose up -d --build

# Restart
docker compose restart
```

### Option 2: Docker Manual

```bash
git clone https://github.com/FreddyMcFett/fortiwan-e.git
cd fortiwan-e
docker build -t fortiwane .
docker run -d --name fortiwane -p 5000:5000 --restart unless-stopped fortiwane
```

### Option 3: Direct Run (Debian/Ubuntu)

Supports Debian 10/11/12 and Ubuntu 18.04/20.04/22.04/24.04+.

```bash
git clone https://github.com/FreddyMcFett/fortiwan-e.git
cd fortiwan-e
chmod +x run.sh
./run.sh
```

## Usage

1. **Connect** to your Fabric Studio instance (IP/hostname + credentials)
2. **Select** the fabric containing your SD-WAN topology
3. **Click** a Router device (ISP1 or ISP2) in the topology view
4. **Adjust** WAN parameters per interface using sliders, or pick a preset
5. **Apply** — rules are pushed to the Router via Fabric Studio API

### WAN Presets

| Preset           | Delay  | Jitter | Loss  | Bandwidth  |
|-----------------|--------|--------|-------|------------|
| Perfect Link    | 0 ms   | 0 ms   | 0%    | Unlimited  |
| MPLS Enterprise | 10 ms  | 2 ms   | 0%    | 100 Mbit/s |
| Broadband       | 20 ms  | 5 ms   | 0.1%  | 50 Mbit/s  |
| 4G LTE          | 50 ms  | 15 ms  | 0.5%  | 30 Mbit/s  |
| 3G Mobile       | 100 ms | 40 ms  | 2%    | 5 Mbit/s   |
| Satellite       | 600 ms | 50 ms  | 1%    | 10 Mbit/s  |
| Congested       | 80 ms  | 60 ms  | 5%    | 2 Mbit/s   |
| Degraded WAN    | 150 ms | 80 ms  | 8%    | 1 Mbit/s   |

## Fabric Studio Setup

1. Create a fabric with your SD-WAN topology
2. Add **Router** devices as ISP1 and ISP2
3. Wire FortiGate WAN ports to the Router ports
4. Install the fabric
5. Point FortiWAN-E at the Fabric Studio IP to control WAN conditions

## Requirements

- **FortiWAN-E host:** Debian/Ubuntu (any version) or Docker
- **Fabric Studio:** 2.0+ with REST API access reachable from FortiWAN-E host
- **Fabric topology:** Router devices acting as ISP links
