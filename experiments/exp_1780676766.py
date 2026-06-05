"""
Caesar cipher with frequency analysis hint
"""

import string
from collections import Counter

ENGLISH_FREQ = "etaoinshrdlcumwfgypbvkjxqz"

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)

def caesar_crack(ciphertext):
    letters = [c.lower() for c in ciphertext if c.isalpha()]
    if not letters:
        return ciphertext, 0
    freq = Counter(letters)
    most_common = freq.most_common(1)[0][0]
    # Assume most common letter maps to 'e'
    shift = (ord(most_common) - ord('e')) % 26
    return caesar_encrypt(ciphertext, -shift), shift

if __name__ == "__main__":
    msg = "The quick brown fox jumps over the lazy dog"
    for s in [3, 13, 19]:
        enc = caesar_encrypt(msg, s)
        dec, guessed = caesar_crack(enc)
        print(f"Shift {s:2d} | Encrypted: {enc[:30]}...")
        print(f"         | Cracked  : {dec[:30]}... (guessed shift={guessed})")
        print()
