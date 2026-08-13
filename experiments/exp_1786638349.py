"""
Palindrome checker with a twist: finds all palindromic substrings.
"""

def is_palindrome(s):
    return s == s[::-1]

def all_palindromic_substrings(text):
    text = text.lower().replace(" ", "")
    found = set()
    for i in range(len(text)):
        for j in range(i + 2, len(text) + 1):
            sub = text[i:j]
            if is_palindrome(sub):
                found.add(sub)
    return sorted(found, key=len, reverse=True)

if __name__ == "__main__":
    samples = ["racecar", "A man a plan a canal Panama", "Never odd or even", "hello world"]
    for sample in samples:
        palins = all_palindromic_substrings(sample)
        print(f"'{sample}' → top palindromes: {palins[:5]}")
