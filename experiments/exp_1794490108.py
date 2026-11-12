"""Password strength checker — rates passwords with an unnecessarily dramatic flair."""

import re

def check_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 8: score += 1
    else: feedback.append("⚠ Too short — a hacker could crack this while making coffee")

    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1; feedback.append("✓ Length: a true epic of a password")

    if re.search(r'[A-Z]', password): score += 1
    else: feedback.append("⚠ No uppercase — your password lacks ambition")

    if re.search(r'[a-z]', password): score += 1
    if re.search(r'\d', password): score += 1
    else: feedback.append("⚠ No numbers — are you even trying?")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): score += 2; feedback.append("✓ Special chars: chaotic good")

    if re.search(r'(.)\1{2,}', password): score -= 1; feedback.append("✗ Repeated chars detected — originality: 0")

    ratings = {0: "🔓 CATASTROPHIC", 3: "😬 WEAK", 5: "🤔 MEDIOCRE", 7: "✅ STRONG", 9: "🏆 FORTRESS"}
    rating = next(v for k, v in sorted(ratings.items(), reverse=True) if score >= k)

    return {"score": score, "rating": rating, "feedback": feedback}

if __name__ == "__main__":
    tests = ["password", "P@ssw0rd!", "correct-horse-battery-staple", "aaaaaa1!"]
    for pw in tests:
        result = check_strength(pw)
        print(f"\n'{pw}'")
        print(f"  Rating: {result['rating']} (score: {result['score']})")
        for f in result['feedback']:
            print(f"  {f}")
