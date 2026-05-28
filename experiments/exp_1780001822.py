# Caesar cipher encoder/decoder

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

samples = [
    ("Hello, World!", 13),
    ("The quick brown fox", 3),
    ("Secret message", 7),
]

for msg, shift in samples:
    encoded = caesar(msg, shift)
    decoded = caesar(encoded, shift, decode=True)
    print(f"Original : {msg}")
    print(f"Encoded  : {encoded}  (shift={shift})")
    print(f"Decoded  : {decoded}")
    print()
