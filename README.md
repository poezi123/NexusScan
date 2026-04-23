# NexusScan – Simple Network Toolkit

## Overview
**NexusScan** is a lightweight Python-based network toolkit designed for basic penetration testing and network analysis. It provides three core features:

* 🔍 Port Scanner (with banner grabbing)
* 📡 Packet Sniffer
* 🖧 IP → MAC → Hostname Mapper
This tool is intended for **educational purposes and authorized network testing only**.
---

## Features

### 1. Port Scanner

* Scans a specified IP over a port range
* Multi-threaded for faster results
* Identifies open ports
* Attempts **banner grabbing** to detect running services

### 2. Packet Sniffer

* Captures live network traffic
* Displays:

  * Source & Destination IP
  * TTL
  * Protocol (TCP / UDP / ICMP)
  * Ports and flags (for TCP/UDP)
* Optional IP filtering
* Auto-stop after inactivity timeout

### 3. IP-MAC Mapper (Admin Required)

* Passive network discovery tool
* Detects devices in the local network
* Resolves:

  * IP Address
  * MAC Address (BSSID)
  * Hostname (if available)
---

Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
```

### Dependencies:
* `colorama`
* `scapy`
---

##Usage
Run the program:
```bash
python your_script_name.py
```
You will see a menu:
```
1. Port scanner
2. Packet Sniffer
3. IP-MAC Mapper (Admin)
```
Enter the number of the tool you want to use.
---

##Permissions

⚠️ Some features require elevated privileges:

* **Linux/macOS:** run with `sudo`
* **Windows:** run terminal as Administrator
Packet sniffing will NOT work without proper permissions.
---

Platform Notes

### Windows:

* You may need **Npcap** installed for packet sniffing

Linux:

* Works out of the box with root privileges

---

Disclaimer

This tool is intended for:

* Educational use
* Ethical hacking labs
* Authorized penetration testing

❗ **Do NOT use this tool on networks you do not own or have permission to test.**

The author is not responsible for any misuse.

---

Author

**S1BERIA**
Version: 1.2 FREE
Date: 08.04.2026
---
Future Improvements (Ideas)
* GUI interface
* OS detection
* Service fingerprinting improvements
* Logging & export features
* Better filtering for sniffer
---
📄 License

This project is provided as-is for educational purposes. You may modify and distribute it freely.

