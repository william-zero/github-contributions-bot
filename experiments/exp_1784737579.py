"""
Morse Code Encoder/Decoder
Beep boop beep boop beep (that means "hello")
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
}

REVERSE = {v: k for k, v in MORSE.items()}

def encode(text):
    result = []
    for char in text.upper():
        if char == ' ':
            result.append('/')
        elif char in MORSE:
            result.append(MORSE[char])
    return ' '.join(result)

def decode(morse):
    result = []
    for word in morse.split(' / '):
        for code in word.split():
            result.append(REVERSE.get(code, '?'))
        result.append(' ')
    return ''.join(result).strip()

if __name__ == '__main__':
    messages = [
        "Hello World",
        "SOS",
        "The quick brown fox",
        "I love Python",
    ]
    for msg in messages:
        encoded = encode(msg)
        decoded = decode(encoded)
        print(f"Original : {msg}")
        print(f"Encoded  : {encoded}")
        print(f"Decoded  : {decoded}")
        print(f"Match    : {msg.upper() == decoded.upper()}")
        print()
