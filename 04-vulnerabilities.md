# Step 4: Vulnerability Assessment

## Why the Attack Succeeded

| Vulnerability | Impact |
|---------------|--------|
| No email filtering | Phishing email reached inbox |
| No security training | Employee didn't recognize red flags |
| No MFA | Stolen password was enough to log in |
| Single password for all services | Email password = VPN password |
| Flat network | Attacker moved freely to file server |
| No backup system | Encrypted files couldn't be restored |

## Key Insight
FiktivGmbH had no defense in depth. A single successful phishing email led directly to full system compromise because there were no additional barriers after the initial breach.
