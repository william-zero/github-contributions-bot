"""
Caesar cipher: shift letters by N positions.
Classic cryptography for the paranoid pigeon.
"""

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    msg = "Hello, World!"
    shift = 13  # ROT13
    enc = caesar_encrypt(msg, shift)
    dec = caesar_decrypt(enc, shift)
    print(f"Original:  {msg}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
