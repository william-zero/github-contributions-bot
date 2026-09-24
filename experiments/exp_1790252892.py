#!/usr/bin/env python3
"""
ROT13: The cipher so simple it makes Caesar look paranoid.
Rot 13 positions forward, decode by rotting 13 more. Elegantly self-inverse.
"""

def rot13(text):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)


examples = [
    "Hello, World!",
    "The quick brown fox",
    "Secrets are overrated",
    "Why did the chicken cross the road?",
]

for msg in examples:
    encoded = rot13(msg)
    decoded = rot13(encoded)
    print(f"Original : {msg}")
    print(f"ROT13    : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"Round-trip OK: {msg == decoded}")
    print()
