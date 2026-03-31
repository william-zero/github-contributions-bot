def is_palindrome(s):
    """Check if a string is a palindrome, ignoring spaces and case."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Test it out
test_phrases = [
    "A man, a plan, a canal: Panama",
    "race car",
    "hello world"
]

for phrase in test_phrases:
    result = is_palindrome(phrase)
    print(f"'{phrase}' -> {result}")
