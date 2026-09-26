"""
caesar_cipher.py - encrypt and decrypt messages with a classic Caesar shift
"""

def caesar_encrypt(text, shift=13):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift=13):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    message = "Hello, World! This is a secret."
    for shift in [3, 13, 25]:
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print(f"Shift {shift:2d}: {encrypted}")
        assert decrypted == message, "Decryption failed!"
    print("All ciphers verified.")
