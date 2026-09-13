"""
Vigenere cipher — polyalphabetic encryption from the 16th century.
Uses a repeating keyword to shift letters, making frequency analysis harder.
"""

def vigenere_encrypt(text, key):
    key = key.upper()
    result = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

def vigenere_decrypt(text, key):
    key = key.upper()
    result = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == '__main__':
    message = "Hello, World! This is a secret message."
    key = "LEMON"
    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Original : {message}")
    print(f"Key      : {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    assert decrypted == message, "Round-trip failed!"
    print("Round-trip check passed!")
