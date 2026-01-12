"""
Microsoft 365 Login Analyzer
Detects suspicious login patterns
"""

def analyze_logins(logs):
    alerts = []
    
    for log in logs:
        # Check login outside business hours (before 7:00 or after 20:00)
        hour = int(log['time'].split(':')[0])
        if hour < 7 or hour > 20:
            alerts.append(f"After-hours login: {log['user']} at {log['time']}")
        
        # Check login from foreign IP
        if not log['ip'].startswith('192.168.1.'):
            alerts.append(f"External IP login: {log['user']} from {log['ip']}")
        
        # Check multiple failed attempts
        if log.get('failed_attempts', 0) > 3:
            alerts.append(f"Multiple failed attempts: {log['user']} ({log['failed_attempts']} failures)")
    
    return alerts

# Example: FiktivGmbH logs during attack
logs = [
    {'user': 'employee@fiktivgmbh.de', 'time': '09:15', 'ip': '192.168.1.105', 'failed_attempts': 0},
    {'user': 'employee@fiktivgmbh.de', 'time': '14:00', 'ip': '185.224.92.15', 'failed_attempts': 0},
    {'user': 'employee@fiktivgmbh.de', 'time': '02:30', 'ip': '185.224.92.15', 'failed_attempts': 2},
]

results = analyze_logins(logs)
print("=== Login Analysis ===")
for alert in results:
    print(f"[!] {alert}")
