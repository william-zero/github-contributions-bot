# Caesar cipher with a twist: variable shift per character position
import string

def encode(text, base_shift=3):
    result = []
    for i, ch in enumerate(text):
        shift = (base_shift + i) % 26
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def decode(text, base_shift=3):
    result = []
    for i, ch in enumerate(text):
        shift = (base_shift + i) % 26
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    secret = "Hello, World!"
    encoded = encode(secret)
    print(f"Original : {secret}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decode(encoded)}")
