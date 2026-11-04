"""morse_encoder.py — translate text to Morse code dots and dashes"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/',
}

def encode(text: str) -> str:
    return ' '.join(MORSE.get(c.upper(), '?') for c in text)

if __name__ == '__main__':
    messages = ['HELLO WORLD', 'SOS', 'PYTHON IS FUN']
    for msg in messages:
        print(f"{msg!r:20} → {encode(msg)}")
