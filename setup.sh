#!/bin/bash

set -e

echo "[*] Setting up pyStalk..."

# Check for Python3
if ! command -v python3 &> /dev/null; then
    echo "[!] Python3 is not installed. Please install Python 3 before running this script."
    exit 1
fi

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "[!] pip3 is not installed. Installing pip..."
    sudo apt install -y python3-pip
fi

# Install Python dependencies
echo "[*] Installing required Python packages..."
REQUIREMENTS=("requests" "whois" "dnspython" "exifread" "colorama")
for pkg in "${REQUIREMENTS[@]}"; do
    if ! pip3 show "$pkg" &> /dev/null; then
        echo "[*] Installing $pkg..."
        pip3 install "$pkg"
    else
        echo "[✓] $pkg is already installed"
    fi
done

# Make the script executable
chmod +x pystalk.py

# Move to /usr/local/bin as pystalk
echo "[*] Installing pystalk system-wide..."
sudo cp pystalk.py /usr/local/bin/pystalk

echo "[✓] Installation complete! You can now use 'pystalk' from anywhere."
