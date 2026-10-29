"""
Morse code encoder/decoder — because sometimes you need to communicate
in a way that sounds like a tiny robot having a conversation with itself.
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}
DECODE = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text)

def decode(morse):
    words = morse.split(' / ')
    return ' '.join(
        ''.join(DECODE.get(c, '?') for c in word.split())
        for word in words
    )

if __name__ == '__main__':
    messages = [
        "Hello World",
        "Send help",
        "The cake is a lie",
        "SOS",
    ]
    for msg in messages:
        encoded = encode(msg)
        decoded = decode(encoded)
        match = "✓" if decoded == msg.upper() else "✗"
        print(f"{match} '{msg}' → {encoded[:40]}{'...' if len(encoded) > 40 else ''}")
