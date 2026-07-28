"""
Caesar Cipher - classic ROT-N encryption with brute force decoder
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

def brute_force(text):
    print("All possible decryptions:")
    for shift in range(26):
        print(f"  ROT-{shift:2d}: {caesar_decrypt(text, shift)}")

if __name__ == '__main__':
    msg = "Hello, World!"
    encrypted = caesar_encrypt(msg, 13)
    print(f"Original : {msg}")
    print(f"ROT-13   : {encrypted}")
    print(f"Decrypted: {caesar_decrypt(encrypted, 13)}\n")
    brute_force("Gur dhvpx oebja sbk")
