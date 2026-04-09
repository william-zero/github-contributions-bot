#!/usr/bin/env python3
"""
Chaotic Palindrome Checker - finds words that are ALMOST palindromes
"""
import random

words = ["racecar", "python", "noon", "level", "radar", "stressed", "bot"]

def chaos_palindrome_check(word):
    rev = word[::-1]
    mismatches = sum(1 for a, b in zip(word, rev) if a != b)
    return f"{word}: {mismatches} chars off from palindrome"

for word in random.sample(words, 3):
    print(chaos_palindrome_check(word))
