# Caesar cipher with ROT13 twist
def caesar(text, shift=13):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

secrets = ["Hello World", "Python is fun", "ROT13 is ROT13 applied twice"]
for s in secrets:
    encoded = caesar(s)
    print(f"Original: {s}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {caesar(encoded)}")
    print()
