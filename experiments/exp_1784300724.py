"""
Caesar cipher — rotate letters by a fixed shift.
Handles upper and lowercase, leaves non-alpha chars unchanged.
"""

def caesar(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def crack(ciphertext: str) -> list:
    """Return all 26 rotations sorted by English letter frequency score."""
    freq = "etaoinshrdlcumwfgypbvkjxqz"
    def score(text):
        return sum(freq.index(c) for c in text.lower() if c in freq)
    candidates = [(shift, caesar(ciphertext, shift)) for shift in range(26)]
    return sorted(candidates, key=lambda x: score(x[1]))


if __name__ == "__main__":
    secret = "Khoor, Zruog!"
    print("Ciphertext:", secret)
    best_shift, plaintext = crack(secret)[0]
    print(f"Decoded (shift -{best_shift}): {plaintext}")
