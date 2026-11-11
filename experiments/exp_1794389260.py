# Morse code encoder/decoder — because why not
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
}
DECODE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def decode(morse):
    return ''.join(DECODE.get(tok, '?') for tok in morse.split())

messages = [
    "HELLO WORLD",
    "SEND HELP",
    "BOT ESCAPED",
    "PING ME MAYBE",
]

for msg in messages:
    encoded = encode(msg)
    decoded = decode(encoded)
    print(f"{msg}")
    print(f"  → {encoded}")
    print(f"  → {decoded}")
    print()
