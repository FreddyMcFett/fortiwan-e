# FortiWAN-E

Web-based WAN Emulator for Fortinet SD-WAN demos running on Fabric Studio.

## How It Works

FortiWAN-E uses Fabric Studio's native **Router** devices as WAN emulators. Instead of inserting a separate VM into the traffic path, it applies Linux `tc` (traffic control) rules directly on Router interfaces via the Fabric Studio REST API.

**Topology Example (2 ISPs):**

```
                    +-------------------+
                    |  Fabric Studio    |
                    |                   |
  Branch FGT ──── Router (ISP1) ──── HQ FGT / Internet
       │            (tc rules)          │
       └───────── Router (ISP2) ────────┘
                   (tc rules)
```

FortiWAN-E controls the `tc netem` and `tc tbf` qdiscs on each Router port to emulate:

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

### Option 1: Direct Run (Debian/Ubuntu)

```bash
git clone <repo-url> && cd fortiwan-e
chmod +x run.sh
./run.sh
```

### Option 2: Docker

```bash
docker build -t fortiwane .
docker run -p 5000:5000 fortiwane
```

Then open `http://<your-ip>:5000` in a browser.

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
5. Use FortiWAN-E to control WAN conditions on the Router interfaces

## Requirements

- Python 3.9+
- Fabric Studio 2.0+ with REST API access
- Router devices in your Fabric Studio topology
