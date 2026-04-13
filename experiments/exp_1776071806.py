#!/usr/bin/env python3
"""
Recursive Palindrome Validator
Checks if a string is a palindrome using recursion in the most overcomplicated way possible.
"""

def is_palindrome_recursive(s, left=0, right=None):
    """
    Validates palindromes recursively. Because why use simple solutions when you can show off?
    """
    if right is None:
        s = s.lower().replace(" ", "")
        right = len(s) - 1
    
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return is_palindrome_recursive(s, left + 1, right - 1)


if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "hello",
        "Was it a car or a cat I saw?"
    ]
    
    for test in test_cases:
        result = is_palindrome_recursive(test)
        print(f"'{test}' -> {result}")
