# Step 2: Incident Timeline

## Attack Chronology

| Time | Event |
|------|-------|
| Day 1, 09:15 | Employee receives phishing email (fake Microsoft 365 alert) |
| Day 1, 09:18 | Employee clicks link, enters credentials on fake login page |
| Day 1, 09:20 | Attacker receives stolen credentials |
| Day 1, 14:00 | Attacker logs into real Microsoft 365, reads emails |
| Day 2, 02:30 | Attacker accesses VPN using stolen credentials |
| Day 2, 02:45 | Attacker scans internal network, finds file server |
| Day 2, 03:00 | Ransomware deployed on file server |
| Day 2, 07:00 | Employees arrive, discover encrypted files |

### Analysis
Each step represents a missed opportunity to stop the attack. The company lacked: email filtering, security awareness training, MFA, and network segmentation.
