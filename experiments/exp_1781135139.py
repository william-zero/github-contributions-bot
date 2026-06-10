# fun experiment: caesar cipher with a twist

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

def rot13(text):
    return caesar_cipher(text, 13)

def auto_decrypt(ciphertext):
    """Try all 26 shifts and return the most English-looking one."""
    common_words = {'the', 'and', 'is', 'it', 'in', 'of', 'to', 'a'}
    best, best_score = ciphertext, 0
    for shift in range(26):
        candidate = caesar_cipher(ciphertext, shift)
        score = sum(1 for w in candidate.lower().split() if w in common_words)
        if score > best_score:
            best, best_score = candidate, score
    return best

secret = "Khoor, Zruog! Wklv phvvdjh zdv hqfrghg zlwk Fdhvdu +3."
print("Encrypted:", secret)
print("Decrypted:", auto_decrypt(secret))
print("ROT13 of 'hello':", rot13('hello'))
