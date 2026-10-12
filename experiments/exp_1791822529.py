"""
Password strength estimator — rates passwords on entropy and pattern avoidance.
"""
import math
import re

def estimate_strength(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32

    entropy = len(password) * math.log2(charset) if charset else 0

    penalties = []
    if re.search(r'(.)\1{2,}', password):
        penalties.append("repeated characters")
        entropy *= 0.8
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        penalties.append("sequential digits")
        entropy *= 0.85
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi)', password, re.I):
        penalties.append("sequential letters")
        entropy *= 0.85
    if password.lower() in ('password', 'qwerty', 'letmein', '123456', 'admin'):
        penalties.append("common password")
        entropy *= 0.1

    if entropy < 28:   rating = "Terrible"
    elif entropy < 36: rating = "Weak"
    elif entropy < 60: rating = "Fair"
    elif entropy < 80: rating = "Strong"
    else:              rating = "Excellent"

    return {"entropy": round(entropy, 1), "rating": rating, "penalties": penalties}

if __name__ == "__main__":
    tests = ["hunter2", "Tr0ub4dor&3", "correct-horse-battery-staple", "P@ssw0rd!", "aaaaaa", "X#9mQ!vL2kP"]
    for p in tests:
        r = estimate_strength(p)
        print(f"{p!r:35s} → {r['rating']:10s} ({r['entropy']} bits){' [' + ', '.join(r['penalties']) + ']' if r['penalties'] else ''}")
