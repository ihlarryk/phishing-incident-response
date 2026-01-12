#!/bin/bash
# Firewall Rules for FiktivGmbH
# Purpose: Prevent ransomware spread and unauthorized access

# === FILE SERVER (192.168.1.10) PROTECTION ===

# Allow access only from internal workstations
iptables -A INPUT -s 192.168.1.100/28 -d 192.168.1.10 -p tcp --dport 445 -j ACCEPT

# Block file server from initiating external connections (stops ransomware callback)
iptables -A OUTPUT -s 192.168.1.10 -d 192.168.1.0/24 -j ACCEPT
iptables -A OUTPUT -s 192.168.1.10 -j DROP

# === BLOCK COMMON RANSOMWARE PORTS ===

# Block outbound SMB (ransomware spreads via this)
iptables -A OUTPUT -p tcp --dport 445 -j DROP
iptables -A OUTPUT -p tcp --dport 139 -j DROP

# Block Tor network (ransomware payment sites)
iptables -A OUTPUT -p tcp --dport 9001 -j DROP
iptables -A OUTPUT -p tcp --dport 9030 -j DROP

echo "Firewall rules applied."
