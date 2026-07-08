"""
Caesar cipher — but dramatic. Encrypts and decrypts with theatrical flair.
"""

def caesar(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def dramatic_encrypt(message):
    shift = len(message) % 26 or 13  # fallback to ROT13 for empty strings
    encrypted = caesar(message, shift)
    print(f"🔐 Original : {message}")
    print(f"🌀 Shift    : {shift}")
    print(f"🗝️  Encrypted: {encrypted}")
    print(f"✅ Decrypted: {caesar(encrypted, shift, decrypt=True)}")
    return encrypted


if __name__ == "__main__":
    dramatic_encrypt("Hello, World!")
    dramatic_encrypt("The quick brown fox")
    dramatic_encrypt("Veni vidi vici")
