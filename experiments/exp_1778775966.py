"""
Caesar cipher encoder/decoder with brute-force cracker.
"""

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
    print("Brute-force all 25 shifts:\n")
    for shift in range(1, 26):
        print(f"  shift {shift:2d}: {caesar_decode(ciphertext, shift)}")


if __name__ == "__main__":
    secret = "Hello, World!"
    shift = 13  # ROT13
    encoded = caesar_encode(secret, shift)
    decoded = caesar_decode(encoded, shift)

    print(f"Original : {secret}")
    print(f"Encoded  : {encoded}  (shift={shift})")
    print(f"Decoded  : {decoded}")
    print()
    brute_force("Gur dhvpx oebja sbk whzcf bire gur ynml qbt.")
