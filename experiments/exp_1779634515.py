# Caesar cipher with adjustable shift

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

if __name__ == "__main__":
    messages = [
        "Hello, World!",
        "The quick brown fox jumps over the lazy dog",
        "Attack at dawn",
    ]
    for msg in messages:
        encrypted = caesar_encrypt(msg, 13)  # ROT13
        decrypted = caesar_decrypt(encrypted, 13)
        print(f"Original:  {msg}")
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {decrypted}")
        print()
