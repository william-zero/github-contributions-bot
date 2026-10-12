# Caesar cipher encoder/decoder - ancient secrets, modern Python

def caesar_cipher(text, shift, decode=False):
    if decode:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

messages = [
    ("Hello, World!", 13),
    ("The quick brown fox jumps over the lazy dog", 7),
    ("Python is fun", 3),
]

for msg, shift in messages:
    encoded = caesar_cipher(msg, shift)
    decoded = caesar_cipher(encoded, shift, decode=True)
    print(f"Original : {msg}")
    print(f"Encoded  : {encoded} (shift={shift})")
    print(f"Decoded  : {decoded}")
    print()

# ROT13 is shift=13, a popular internet tradition
print("ROT13 of 'Why did the programmer quit?':")
print(caesar_cipher("Why did the programmer quit?", 13))
print("(decode it to find the punchline)")
