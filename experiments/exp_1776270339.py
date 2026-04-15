#!/usr/bin/env python3
"""
Reverse String Analyzer
Analyzes fun properties of reversed strings.
"""

def analyze_reverse(text):
    """Analyze a string and its reverse."""
    rev = text[::-1]
    is_palindrome = text.lower() == rev.lower()
    return {
        'original': text,
        'reversed': rev,
        'is_palindrome': is_palindrome,
        'length': len(text)
    }

if __name__ == '__main__':
    test_strings = ['racecar', 'python', 'wow', 'hello', 'madam']
    for s in test_strings:
        result = analyze_reverse(s)
        status = '🔄 PALINDROME!' if result['is_palindrome'] else '➡️ Not palindrome'
        print(f"{result['original']:10} → {result['reversed']:10} {status}")
