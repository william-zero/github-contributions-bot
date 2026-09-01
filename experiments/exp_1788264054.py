"""
Caesar Cipher Wheel: encode/decode messages with a rotating shift.
Displays a visual letter wheel and shows the mapping.
"""

import string

def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def draw_wheel(shift):
    letters = string.ascii_uppercase
    shifted = letters[shift:] + letters[:shift]
    print("  Plain : " + " ".join(letters))
    print("  Cipher: " + " ".join(shifted))
    bar = "  Shift : " + " ".join(str(i % 10) for i in range(shift, shift + 26))
    print(bar)

messages = [
    ("Hello, World!", 3),
    ("The quick brown fox", 13),
    ("Secret message", 7),
]

for msg, shift in messages:
    encoded = caesar_cipher(msg, shift)
    decoded = caesar_cipher(encoded, shift, decode=True)
    print(f"\nOriginal : {msg}")
    print(f"Shift    : {shift}")
    draw_wheel(shift)
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"Match    : {'✓' if decoded == msg else '✗'}")
