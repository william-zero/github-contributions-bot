# Morse code encoder/decoder

MORSE = {
    'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....',
    'I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.',
    'Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
    'Y':'-.--','Z':'--..',
    '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
    '6':'-....','7':'--...','8':'---..','9':'----.',
    '.':'.-.-.-',',':'--..--','?':'..--..','!':'-.-.--',' ':'/'
}
MORSE_REV = {v: k for k, v in MORSE.items()}

def encode(text):
    return ' '.join(MORSE.get(c.upper(), '?') for c in text)

def decode(morse):
    return ''.join(MORSE_REV.get(code, '?') for code in morse.split())

sos = encode('SOS')
print(f"SOS in morse: {sos}")
print(f"Decoded back: {decode(sos)}")
msg = "HELLO WORLD"
enc = encode(msg)
print(f"\nOriginal: {msg}")
print(f"Encoded:  {enc}")
print(f"Decoded:  {decode(enc)}")
