"""
Morse Code Translator
Because sometimes dots and dashes are more expressive than words.
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

def to_morse(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def from_morse(code):
    reverse = {v: k for k, v in MORSE.items()}
    return ''.join(reverse.get(c, '?') for c in code.split())

messages = ["SOS", "HELLO", "PYTHON"]
for msg in messages:
    encoded = to_morse(msg)
    decoded = from_morse(encoded)
    print(f"{msg:10} -> {encoded:40} -> {decoded}")
