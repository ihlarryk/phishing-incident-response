"""
Phishing Email Header Analyzer
Checks for common phishing indicators
"""

def analyze_email(headers):
    red_flags = []
    
    # Check sender domain
    sender = headers.get('from', '')
    if 'microsoft' in sender.lower() and 'microsoft.com' not in sender.lower():
        red_flags.append(f"Suspicious sender: {sender}")
    
    # Check for urgency keywords in subject
    subject = headers.get('subject', '').lower()
    urgent_words = ['urgent', 'suspend', 'expire', 'immediately', 'action required']
    for word in urgent_words:
        if word in subject:
            red_flags.append(f"Urgency tactic in subject: '{word}'")
    
    # Check reply-to mismatch
    reply_to = headers.get('reply-to', '')
    if reply_to and reply_to != sender:
        red_flags.append(f"Reply-to mismatch: {reply_to}")
    
    return red_flags

# Example: FiktivGmbH phishing email
phishing_email = {
    'from': 'security@micros0ft-alert.com',
    'subject': 'Urgent: Your account will be suspended',
    'reply-to': 'attacker@gmail.com'
}

results = analyze_email(phishing_email)
print("=== Phishing Analysis ===")
for flag in results:
    print(f"[!] {flag}")
