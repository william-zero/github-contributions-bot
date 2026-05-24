# Caesar cipher: the OG encryption, now with extra commentary
import string

def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []
    for char in text:
        if char in string.ascii_uppercase:
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char in string.ascii_lowercase:
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

secret = "The quick brown fox jumps over the lazy dog"
shift = 13  # ROT13 — the "password" used by ancient forum trolls

encoded = caesar_cipher(secret, shift)
decoded = caesar_cipher(encoded, shift, decode=True)

print(f"Original : {secret}")
print(f"Encoded  : {encoded}")
print(f"Decoded  : {decoded}")
print(f"Match    : {secret == decoded}")

# Brute-force all 25 shifts because patience is a virtue we don't have
print("\n--- Brute Force (because why not) ---")
for s in range(1, 26):
    print(f"Shift {s:2d}: {caesar_cipher(encoded, s, decode=True)}")
