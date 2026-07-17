"""
Palindrome explorer: find and generate palindromes with style.
"""

def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def make_palindrome(s: str) -> str:
    """Append the minimum characters to make s a palindrome."""
    for i in range(len(s)):
        if is_palindrome(s[i:]):
            return s + s[:i][::-1]
    return s

CLASSICS = [
    "racecar",
    "A man a plan a canal Panama",
    "Was it a car or a cat I saw",
    "Never odd or even",
    "Do geese see God",
    "Taco cat",
]

if __name__ == "__main__":
    print("=== Classic Palindromes ===")
    for p in CLASSICS:
        status = "✓" if is_palindrome(p) else "✗"
        print(f"  {status} {p!r}")

    print("\n=== Palindrome Generator ===")
    words = ["hello", "race", "noon", "bot", "level"]
    for w in words:
        result = make_palindrome(w)
        print(f"  {w!r} -> {result!r} (palindrome: {is_palindrome(result)})")
