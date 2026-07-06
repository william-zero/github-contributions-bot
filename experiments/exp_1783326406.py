"""
Morse Code Encoder/Decoder
Because sometimes you just need to communicate in dots and dashes.
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def decode(code):
    return ''.join(REVERSE.get(w, '?') for w in code.split())

samples = ["SOS", "HELLO WORLD", "BOT"]
for s in samples:
    encoded = encode(s)
    print(f"{s!r:20} → {encoded}")
    print(f"{'':20}   decoded back: {decode(encoded)}")
    print()
