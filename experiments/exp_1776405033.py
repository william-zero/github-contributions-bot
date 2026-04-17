# Caesar cipher experiment with varying shifts

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

messages = [
    "Hello World",
    "The quick brown fox",
    "Python is fun",
]

for msg in messages:
    for shift in [3, 13, 7]:
        encoded = caesar_cipher(msg, shift)
        decoded = caesar_cipher(encoded, -shift)
        print(f"Shift {shift:2d}: '{msg}' -> '{encoded}' -> '{decoded}'")
    print()
