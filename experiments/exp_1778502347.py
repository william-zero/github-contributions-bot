"""Caesar cipher with brute-force decoder."""

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decode_all(ciphertext):
    for shift in range(26):
        candidate = caesar_encrypt(ciphertext, -shift)
        print(f"Shift {shift:2d}: {candidate}")

if __name__ == "__main__":
    msg = "Hello, World!"
    encrypted = caesar_encrypt(msg, 13)
    print(f"Original : {msg}")
    print(f"ROT13    : {encrypted}")
    print("\nBrute-force all shifts:")
    caesar_decode_all(encrypted)
