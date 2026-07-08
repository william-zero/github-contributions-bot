"""
Morse Code Translator - beep boop edition
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

REVERSE = {v: k for k, v in MORSE.items()}


def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')


def decode(morse):
    return ''.join(REVERSE.get(code, '?') for code in morse.split())


def dramatic_transmission(text):
    print(f"TRANSMITTING: {text}")
    print(f"IN MORSE:     {encode(text)}")
    print(f"BACK AGAIN:   {decode(encode(text))}")
    print("...dit dah dit...")


if __name__ == '__main__':
    dramatic_transmission("HELLO WORLD")
    dramatic_transmission("SOS")
    dramatic_transmission("BEEP BOOP")
