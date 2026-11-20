# Caesar cipher encoder/decoder with a rotating key
def caesar_encode(text, shift=13):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decode(text, shift=13):
    return caesar_encode(text, 26 - shift)

MESSAGES = [
    ("Hello, World!", 3),
    ("The quick brown fox jumps over the lazy dog", 7),
    ("Bot life is the good life", 42),
    ("Why did the programmer quit? Because they didn't get arrays.", 13),
]

print("=== Caesar Cipher Experiments ===\n")
for msg, shift in MESSAGES:
    encoded = caesar_encode(msg, shift)
    decoded = caesar_decode(encoded, shift)
    print(f"Original : {msg}")
    print(f"Shift    : {shift}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"Match    : {decoded == msg}")
    print()
