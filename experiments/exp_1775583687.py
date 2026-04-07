#!/usr/bin/env python3
"""
Recursive Palindrome Checker with Personality
Because sometimes you need your code to judge your writing choices.
"""

def is_palindrome_recursive(text):
    """
    Check if text is a palindrome using recursion.
    Ignores spaces and case sensitivity.
    """
    # Clean the text
    clean = ''.join(c.lower() for c in text if c.isalnum())
    
    def check(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return check(s[1:-1])
    
    result = check(clean)
    feedback = "✓ That's a palindrome! Your text is symmetrically poetic." if result else "✗ Nope, that's not a palindrome. Keep trying!"
    return result, feedback

if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal, Panama!",
        "Never odd or even",
        "racecar",
        "hello world",
        "Was it a car or a cat I saw?"
    ]
    
    for test in test_cases:
        is_pal, msg = is_palindrome_recursive(test)
        print(f"{test:40} → {msg}")
