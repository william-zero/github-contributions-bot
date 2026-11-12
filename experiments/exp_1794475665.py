# Morse code encoder/decoder

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
}
DECODE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def decode(morse):
    return ''.join(DECODE.get(code, '?') for code in morse.split())

if __name__ == '__main__':
    msg = "HELLO WORLD"
    encoded = encode(msg)
    decoded = decode(encoded)
    print(f"Original : {msg}")
    print(f"Encoded  : {encoded}")
    print(f"Decoded  : {decoded}")
    print(f"SOS in Morse: {encode('SOS')}")
