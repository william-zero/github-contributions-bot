"""Caesar cipher: encode, decode, and brute-force all 26 shifts."""


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


def caesar_brute(text):
    return {shift: caesar_decode(text, shift) for shift in range(26)}


if __name__ == "__main__":
    secret = "Khoor, Zruog!"
    print(f"Ciphertext: {secret}\n")
    print("Brute force:")
    for shift, plain in caesar_brute(secret).items():
        marker = " <-- likely!" if plain.startswith("Hello") else ""
        print(f"  shift={shift:2}: {plain}{marker}")
