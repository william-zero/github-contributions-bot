# Caesar cipher encoder/decoder with brute force cracker

def caesar_encode(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decode(text, shift):
    return caesar_encode(text, -shift)

def brute_force(ciphertext):
    print("=== Brute Force Decryption ===")
    for shift in range(26):
        attempt = caesar_decode(ciphertext, shift)
        print(f"  Shift {shift:2d}: {attempt}")

if __name__ == "__main__":
    msg = "Hello, Secret World!"
    encoded = caesar_encode(msg, 13)
    print(f"Original : {msg}")
    print(f"ROT-13   : {encoded}")
    print(f"Decoded  : {caesar_decode(encoded, 13)}")
    print()
    brute_force("Khoor, Zruog!")
