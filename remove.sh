#!/bin/bash

echo "[*] Removing pyrecon from /usr/local/bin..."
sudo rm -f /usr/local/bin/pyrecon
echo "[✓] pyrecon removed successfully."
echo "NOTE: You may uninstall dependencies if not required: requests, whois, dnspython, exifread, colorama"
