"""
Password strength analyzer with unnecessary dramatic flair.
"""

def analyze_password(pw: str) -> dict:
    score = 0
    verdicts = []

    if len(pw) >= 12:
        score += 2
        verdicts.append("Length: adequate for a mediocre fortress")
    elif len(pw) >= 8:
        score += 1
        verdicts.append("Length: shorter than most grocery lists")
    else:
        verdicts.append("Length: embarrassingly brief")

    if any(c.isupper() for c in pw):
        score += 1
        verdicts.append("Uppercase: present, like an uninvited guest")
    if any(c.islower() for c in pw):
        score += 1
        verdicts.append("Lowercase: exists, technically")
    if any(c.isdigit() for c in pw):
        score += 1
        verdicts.append("Digits: numbers have arrived")
    if any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in pw):
        score += 2
        verdicts.append("Symbols: chaos embraced")

    if score <= 2:
        rating = "Catastrophically Weak"
    elif score <= 4:
        rating = "Mildly Concerning"
    elif score <= 6:
        rating = "Passable, Barely"
    else:
        rating = "Actually Decent"

    return {"score": score, "rating": rating, "verdicts": verdicts}


if __name__ == "__main__":
    test_passwords = ["abc", "hunter2", "Tr0ub4dor&3", "correct-horse-battery-staple!"]
    for pw in test_passwords:
        result = analyze_password(pw)
        print(f"\n'{pw}'")
        print(f"  Rating: {result['rating']} ({result['score']}/7)")
        for v in result['verdicts']:
            print(f"  - {v}")
