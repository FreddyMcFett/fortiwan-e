#!/bin/bash
# FortiWAN-E — Quick Start Script
# Run on Debian/Ubuntu 22.04+

set -e

echo "========================================="
echo "  FortiWAN-E — WAN Emulator Setup"
echo "========================================="

# Check Python
if ! command -v python3 &>/dev/null; then
    echo "[*] Installing Python3..."
    sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-venv
fi

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
fi

echo "[*] Activating virtual environment..."
source venv/bin/activate

echo "[*] Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "========================================="
echo "  Starting FortiWAN-E on port 5000"
echo "  Open http://$(hostname -I | awk '{print $1}'):5000"
echo "========================================="
echo ""

python3 app.py
