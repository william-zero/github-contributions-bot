# Caesar cipher implementation with brute-force decoder
def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_brute_force(ciphertext):
    for shift in range(26):
        print(f"Shift {shift:2d}: {caesar_encrypt(ciphertext, -shift)}")

secret = caesar_encrypt("Hello, world! Cryptography is fun.", 13)
print(f"Encoded: {secret}")
print("Brute forcing:")
caesar_brute_force(secret)
