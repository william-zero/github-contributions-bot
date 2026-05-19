# vigenere cipher: the slightly fancier cousin of caesar
import string

ALPHA = string.ascii_lowercase

def vigenere_encrypt(text, key):
    key = key.lower()
    result = []
    ki = 0
    for ch in text.lower():
        if ch in ALPHA:
            shift = ALPHA.index(key[ki % len(key)])
            result.append(ALPHA[(ALPHA.index(ch) + shift) % 26])
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

def vigenere_decrypt(text, key):
    key = key.lower()
    result = []
    ki = 0
    for ch in text.lower():
        if ch in ALPHA:
            shift = ALPHA.index(key[ki % len(key)])
            result.append(ALPHA[(ALPHA.index(ch) - shift) % 26])
            ki += 1
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    secret = "the quick brown fox jumps over the lazy dog"
    key = "lemur"
    encrypted = vigenere_encrypt(secret, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"original:  {secret}")
    print(f"key:       {key}")
    print(f"encrypted: {encrypted}")
    print(f"decrypted: {decrypted}")
    print(f"verified:  {secret == decrypted}")
