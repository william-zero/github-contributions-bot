"""
Caesar cipher encoder/decoder — because sometimes your messages
deserve to be unreadable to anyone born before 100 BCE.
"""

def caesar(text, shift, decode=False):
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


messages = [
    ("Hello, World!", 13),
    ("The quick brown fox jumps over the lazy dog.", 3),
    ("Attack at dawn!", 7),
]

for msg, shift in messages:
    encoded = caesar(msg, shift)
    decoded = caesar(encoded, shift, decode=True)
    print(f"Original : {msg}")
    print(f"Shift {shift:2d}  : {encoded}")
    print(f"Decoded  : {decoded}")
    print()
