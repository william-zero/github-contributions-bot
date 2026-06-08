"""
ROT13 encoder/decoder — the classic "encryption" used in Usenet to hide spoilers.
Every letter is shifted by 13 positions. Applying it twice gives back the original.
"""

import string

def rot13(text):
    result = []
    for ch in text:
        if ch in string.ascii_uppercase:
            result.append(chr((ord(ch) - ord('A') + 13) % 26 + ord('A')))
        elif ch in string.ascii_lowercase:
            result.append(chr((ord(ch) - ord('a') + 13) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)

samples = [
    "Hello, World!",
    "Python is fun",
    "The quick brown fox jumps over the lazy dog",
    "ROT13 is its own inverse",
]

print("=== ROT13 Encoder/Decoder ===\n")
for s in samples:
    encoded = rot13(s)
    decoded = rot13(encoded)
    print(f"Original : {s}")
    print(f"ROT13    : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"Round-trip OK: {s == decoded}")
    print()
