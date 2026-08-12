"""
Morse code encoder/decoder
Because sometimes you need to communicate via dots and dashes.
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    '!': '-.-.--', ' ': '/'
}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text)

def decode(code):
    words = code.split(' / ')
    return ''.join(
        ''.join(REVERSE.get(c, '?') for c in word.split())
        for word in words
    )

# Tests
cases = [
    "Hello World",
    "SOS",
    "Python is fun",
    "42 is the answer",
]

print("=== Morse Code Encoder/Decoder ===\n")
for phrase in cases:
    encoded = encode(phrase)
    decoded = decode(encoded)
    status = "✓" if decoded.upper() == phrase.upper() else "✗"
    print(f"{status} '{phrase}'")
    print(f"  → {encoded}")
    print(f"  ← '{decoded}'")
    print()
