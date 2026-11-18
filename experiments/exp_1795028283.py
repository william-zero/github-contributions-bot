# Caesar cipher — encode and decode messages with a shift
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

msg = "Hello, World!"
encoded = caesar(msg, 13)
decoded = caesar(encoded, 13, decode=True)

print(f"Original : {msg}")
print(f"ROT-13   : {encoded}")
print(f"Decoded  : {decoded}")
