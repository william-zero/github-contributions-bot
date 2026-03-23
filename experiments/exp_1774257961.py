#!/usr/bin/env python3
"""Palindrome Detective: Find hidden word palindromes in random strings"""

import random
import string

def find_palindromes(text):
    """Extract all palindromic words from text"""
    words = text.lower().split()
    palindromes = [w for w in words if w == w[::-1] and len(w) > 1]
    return palindromes

# Generate random string with hidden palindromes
secret_words = ['level', 'radar', 'noon', 'civic', 'kayak']
noise_words = ''.join(random.choices(string.ascii_letters, k=100))
hidden_msg = ' '.join(random.sample(secret_words, 3))
mixed = f"{noise_words[:30]} {hidden_msg} {noise_words[30:]}"

found = find_palindromes(mixed)
print(f"🔍 Palindromes found: {found}")
