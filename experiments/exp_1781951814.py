"""
Caesar cipher encoder/decoder — because sometimes you need
to send secret messages to your rubber duck.
"""

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

if __name__ == "__main__":
    msg = "The bot is watching you"
    encoded = caesar(msg, 13)
    decoded = caesar(encoded, 13, decode=True)
    print(f"Original : {msg}")
    print(f"ROT13    : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"Verified : {msg == decoded}")
