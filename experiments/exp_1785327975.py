"""Caesar cipher encoder/decoder with brute-force mode."""

def caesar(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def brute_force(ciphertext):
    for shift in range(1, 26):
        print(f"Shift {shift:2d}: {caesar(ciphertext, shift, decode=True)}")


if __name__ == "__main__":
    msg = "Hello, World!"
    encrypted = caesar(msg, 13)
    print(f"Original : {msg}")
    print(f"ROT13    : {encrypted}")
    print(f"Decoded  : {caesar(encrypted, 13, decode=True)}")
    print("\nBrute-force 'Khoor, Zruog!':")
    brute_force("Khoor, Zruog!")
