#!/bin/bash

echo "[*] Removing pystalk from /usr/local/bin..."
sudo rm -f /usr/local/bin/pystalk
echo "[✓] pyStalk removed successfully."
echo "NOTE: You may uninstall dependencies if not required: requests, whois, dnspython, exifread, colorama"
