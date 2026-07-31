"""
Caesar cipher: encode/decode messages with a classic rotation cipher.
"""

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

if __name__ == "__main__":
    messages = [
        ("Hello, World!", 3),
        ("The quick brown fox", 13),
        ("Secret message: zebra", 7),
    ]
    print("=== Caesar Cipher Demo ===\n")
    for msg, shift in messages:
        encoded = caesar_encode(msg, shift)
        decoded = caesar_decode(encoded, shift)
        print(f"Original:  {msg}")
        print(f"Shift:     {shift}")
        print(f"Encoded:   {encoded}")
        print(f"Decoded:   {decoded}")
        print(f"Round-trip OK: {decoded == msg}\n")
