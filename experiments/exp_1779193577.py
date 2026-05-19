"""
Caesar Cipher Carnival
A playful implementation of the classic Caesar cipher with extra flair.
"""

def caesar_encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force(text):
    print("=== Brute Force Decryption ===")
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {caesar_decrypt(text, shift)}")

if __name__ == "__main__":
    secret = "Khoor, Zruog! Wklv lv d vhfuhw phvvdjh."
    print(f"Encrypted: {secret}")
    print(f"Decrypted: {caesar_decrypt(secret, 3)}")
    print()
    custom = "The quick brown fox jumps over the lazy dog"
    encrypted = caesar_encrypt(custom, 13)
    print(f"Original : {custom}")
    print(f"ROT13    : {encrypted}")
    print(f"Back     : {caesar_decrypt(encrypted, 13)}")
