"""
Caesar cipher encoder/decoder — a classic shift cipher for fun.
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
        "Hello, World!",
        "The quick brown fox jumps over the lazy dog",
        "Secret message goes here",
    ]
    for msg in messages:
        encoded = caesar_encode(msg)
        decoded = caesar_decode(encoded)
        print(f"Original : {msg}")
        print(f"Encoded  : {encoded}")
        print(f"Decoded  : {decoded}")
        print()
