# Morse code encoder/decoder

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}
REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def decode(morse):
    return ''.join(REVERSE.get(code, '?') for code in morse.split())

messages = ["HELLO WORLD", "SOS", "THE QUICK BROWN FOX"]
for msg in messages:
    encoded = encode(msg)
    decoded = decode(encoded)
    print(f"Original : {msg}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print()
