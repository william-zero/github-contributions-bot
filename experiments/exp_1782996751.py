"""
Morse Code Translator — because sometimes dots and dashes
are more eloquent than words.
"""

MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/',
}
REVERSE = {v: k for k, v in MORSE.items()}


def encode(text: str) -> str:
    result = []
    for char in text.upper():
        code = MORSE.get(char)
        if code:
            result.append(code)
        elif char not in MORSE:
            result.append('?')
    return ' '.join(result)


def decode(morse: str) -> str:
    result = []
    for token in morse.split(' '):
        char = REVERSE.get(token)
        if char == '/':
            result.append(' ')
        elif char:
            result.append(char)
        else:
            result.append('?')
    return ''.join(result)


def render_audio_art(morse: str) -> str:
    """Turn morse into a visual waveform of sorts."""
    art = []
    for char in morse:
        if char == '.':
            art.append('▪')
        elif char == '-':
            art.append('▬')
        elif char == ' ':
            art.append(' ')
        elif char == '/':
            art.append('  ')
    return ''.join(art)


if __name__ == '__main__':
    messages = [
        "HELLO WORLD",
        "SOS",
        "TO BE OR NOT TO BE",
        "THE BOT COMMITS AGAIN",
    ]
    for msg in messages:
        encoded = encode(msg)
        decoded = decode(encoded)
        art = render_audio_art(encoded)
        print(f"Text   : {msg}")
        print(f"Morse  : {encoded}")
        print(f"Visual : {art}")
        print(f"Back   : {decoded}")
        print()
