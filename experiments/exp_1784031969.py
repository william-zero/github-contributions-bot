# Philosophical Number Classifier
# Categorizes numbers by their vibe, not their value

def classify_number(n):
    vibes = {
        lambda x: x == 0: "void — the number that questions its own existence",
        lambda x: x == 1: "lone wolf — refuses to factor into anything interesting",
        lambda x: x == 42: "the answer — no further comment needed",
        lambda x: x < 0: "negative energy — needs therapy",
        lambda x: x > 1000: "overachiever — probably a phone number",
        lambda x: x % 2 == 0: "even-keeled — suspiciously balanced",
        lambda x: x % 2 != 0: "odd — embraces being misunderstood",
        lambda x: str(x) == str(x)[::-1]: "palindrome — same from all directions, very zen",
        lambda x: all(int(d)**len(str(x)) == 0 or sum(int(d)**len(str(x)) for d in str(x)) == x: "narcissistic — only loves itself",
    }
    for condition, label in vibes.items():
        try:
            if condition(n):
                return f"{n}: {label}"
        except Exception:
            pass
    return f"{n}: undefined vibe (consult a numerologist)"

test_numbers = [0, 1, 7, 42, -5, 1001, 153, 121, 8]
for num in test_numbers:
    print(classify_number(num))
