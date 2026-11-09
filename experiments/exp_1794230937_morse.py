"""Morse code encoder with beep visualization."""

MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
    'R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
    '6':'-....','7':'--...','8':'---..','9':'----.',
    '.':'.-.-.-',',':'--..--','?':'..--..','/':'-..-.',
}

def encode(text):
    return '  '.join(MORSE.get(c.upper(), '?') for c in text if c != ' ')

def visualize(morse):
    return morse.replace('-', '━━━').replace('.', '•').replace(' ', ' ')

messages = ["SOS", "HELLO WORLD", "MORSE CODE", "42"]
for msg in messages:
    m = encode(msg)
    print(f"{msg:>12}: {visualize(m)}")
