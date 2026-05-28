"""
ROT-N cipher with a twist: different rotation per character position.
"""

def spiral_rot(text, base_rot=13):
    result = []
    for i, ch in enumerate(text):
        if ch.isalpha():
            rot = (base_rot + i) % 26
            offset = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - offset + rot) % 26 + offset))
        else:
            result.append(ch)
    return ''.join(result)

samples = [
    "Hello World",
    "The quick brown fox",
    "Secret message here",
]

for s in samples:
    encoded = spiral_rot(s)
    decoded = spiral_rot(encoded, 26 - 13)
    print(f"Original : {s}")
    print(f"Encoded  : {encoded}")
    print()
