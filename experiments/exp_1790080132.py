"""Caesar cipher — classic, simple, totally unbreakable (by Romans)."""

def caesar(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

messages = [
    "Hello, World!",
    "The quick brown fox",
    "Meet me at the forum",
]

for msg in messages:
    encoded = caesar(msg, 13)  # ROT13
    decoded = caesar(encoded, 13)
    print(f"Original: {msg}")
    print(f"ROT13:    {encoded}")
    print(f"Decoded:  {decoded}")
    print()
