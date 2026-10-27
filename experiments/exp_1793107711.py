"""Caesar cipher encoder/decoder - a classic cryptography experiment."""

def caesar_cipher(text, shift, encode=True):
    """Encode or decode text using Caesar cipher."""
    result = []
    if not encode:
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    messages = [
        "Hello World",
        "The quick brown fox jumps over the lazy dog",
        "Secret Message",
    ]
    shifts = [3, 13, 7]

    for msg, shift in zip(messages, shifts):
        encoded = caesar_cipher(msg, shift)
        decoded = caesar_cipher(encoded, shift, encode=False)
        print(f"Original : {msg}")
        print(f"Shift    : {shift}")
        print(f"Encoded  : {encoded}")
        print(f"Decoded  : {decoded}")
        print(f"Match    : {msg == decoded}")
        print()
