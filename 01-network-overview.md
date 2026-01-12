# Step 1: Network Overview

## Company: FiktivGmbH

### Network Devices
| Device | IP Address | Role |
|--------|------------|------|
| Router | 192.168.1.1 | Gateway to internet |
| File Server | 192.168.1.10 | Internal documents |
| Web Server | 192.168.1.20 | Public website |
| Workstations | 192.168.1.100-114 | Employee computers |
| Printer | 192.168.1.200 | Network printer |
| Wi-Fi AP | 192.168.1.2 | Wireless access |

| Device | IP Address | Role |
|--------|------------|------|
| Router | 192.168.1.1 | Gateway to internet |
| File Server | 192.168.1.10 | Internal documents |
| Web Server | 192.168.1.20 | Public website |
| Workstations | 192.168.1.100-114 | Employee computers |
| Printer | 192.168.1.200 | Network printer |
| Wi-Fi AP | 192.168.1.2 | Wireless access |

### Why this matters
All devices share the same subnet (192.168.1.x), meaning any compromised workstation can directly access the file server without passing through additional security layers.
