"""
Caesar cipher and ROT13 variants — encoding secrets since Julius Caesar.
"""

def caesar_cipher(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def rot13(text: str) -> str:
    return caesar_cipher(text, 13)


def vigenere_cipher(text: str, key: str) -> str:
    key = key.lower()
    result = []
    key_idx = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('a')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            key_idx += 1
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == "__main__":
    secret = "Hello, World!"
    print(f"Original:        {secret}")
    print(f"Caesar (+3):     {caesar_cipher(secret, 3)}")
    print(f"ROT13:           {rot13(secret)}")
    print(f"ROT13 of ROT13:  {rot13(rot13(secret))}")  # back to original!
    print(f"Vigenere 'key':  {vigenere_cipher(secret, 'key')}")
    print()
    print("Fun fact: ROT13 applied twice always returns the original string.")
    print("Julius Caesar used a shift of 3 — the NSA was not amused.")
