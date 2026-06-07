"""
Caesar cipher - the classic substitution cipher.
Shift each letter by a fixed amount, wrap around the alphabet.
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


if __name__ == '__main__':
    message = "Hello, World!"
    for shift in [3, 13, 25]:
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print(f"shift={shift:2d}: '{encrypted}' -> '{decrypted}'")
