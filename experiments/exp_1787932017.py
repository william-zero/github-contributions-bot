# palindrome checker with a twist
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Fun palindromes
phrases = [
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Never odd or even",
    "Hello World",
    "racecar"
]

for phrase in phrases:
    result = "✓" if is_palindrome(phrase) else "✗"
    print(f"{result} '{phrase}'")
