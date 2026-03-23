#!/bin/bash
# FortiWAN-E — Quick Start Script
# Supports: Debian 10/11/12, Ubuntu 18.04/20.04/22.04/24.04+

set -e

echo "========================================="
echo "  FortiWAN-E — WAN Emulator Setup"
echo "========================================="

# Detect OS
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "[*] Detected: ${PRETTY_NAME:-$ID $VERSION_ID}"
else
    echo "[!] Could not detect OS, proceeding anyway..."
fi

# Install Python3 if missing
if ! command -v python3 &>/dev/null; then
    echo "[*] Installing Python3..."
    sudo apt-get update -qq
    sudo apt-get install -y -qq python3 python3-pip
fi

# python3-venv is a separate package on Debian/Ubuntu
# On older systems (Debian 10, Ubuntu 18.04) it may not be installed
if ! python3 -m venv --help &>/dev/null 2>&1; then
    echo "[*] Installing python3-venv..."
    sudo apt-get update -qq
    PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    sudo apt-get install -y -qq "python3-venv" || sudo apt-get install -y -qq "python${PYTHON_VERSION}-venv"
fi

# On very old systems, ensure pip is available
if ! python3 -m pip --version &>/dev/null 2>&1; then
    echo "[*] Installing pip..."
    sudo apt-get install -y -qq python3-pip || {
        echo "[*] Falling back to get-pip.py..."
        curl -sS https://bootstrap.pypa.io/get-pip.py | python3
    }
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
fi

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Get IP address (compatible with older systems too)
IP_ADDR=$(hostname -I 2>/dev/null | awk '{print $1}' || echo "localhost")

echo ""
echo "========================================="
echo "  FortiWAN-E running on port 80"
echo "  Open http://${IP_ADDR}"
echo "========================================="
echo ""

python3 app.py
