# Incident Response Case Study: Phishing-Based Ransomware Attack

## Project Overview
A simulated incident response analysis for FiktivGmbH, a small German marketing agency (15 employees) that suffered a ransomware attack originating from a phishing email.

## Objective
Demonstrate understanding of:
- Attack vectors common in German SMEs
- Incident response procedures
- Prevention strategies aligned with BSI guidelines
- GDPR compliance requirements

## Case Summary
| Item | Detail |
|------|--------|
| Company | FiktivGmbH, Frankfurt (Oder) |
| Attack type | Phishing → Credential theft → Ransomware |
| Entry point | Fake Microsoft 365 email |
| Impact | File server encrypted, 3 days downtime |
| Estimated loss | €39,000 - €530,000 |

## Documentation
1. [Network Overview](01-network-overview.md)
2. [Incident Timeline](02-incident-timeline.md)
3. [Attack Vector Analysis](03-attack-vector.md)
4. [Vulnerability Assessment](04-vulnerabilities.md)
5. [Incident Response](05-incident-response.md)
6. [Prevention Plan](06-prevention-plan.md)
7. [Business Impact](07-business-impact.md)

### Scripts
- [email_analyzer.py](email_analyzer.py) — Python tool to detect phishing indicators in email headers
- [login_analyzer.py](ogin_analyzer.py) — Detects suspicious Microsoft 365 login patterns
- [firewall_rules.sh](firewall_rules.sh) — Firewall configuration to prevent ransomware spread

## References
- [BSI - Bundesamt für Sicherheit in der Informationstechnik](https://www.bsi.bund.de)
- [GDPR Article 33 - Notification of Personal Data Breach](https://gdpr-info.eu/art-33-gdpr/)
- [MITRE ATT&CK - Phishing](https://attack.mitre.org/techniques/T1566/)
- [No More Ransom Project](https://www.nomoreransom.org)

## Author
Ihor Illarionov
Candidate for Master's, 2026
