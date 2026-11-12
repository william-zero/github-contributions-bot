# Binary to text decoder with dramatic flair
import sys

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9',
}

def decode_morse(code):
    words = code.strip().split('   ')
    result = []
    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(MORSE_CODE.get(l, '?') for l in letters)
        result.append(decoded_word)
    return ' '.join(result)

def encode_morse(text):
    reverse = {v: k for k, v in MORSE_CODE.items()}
    words = text.upper().split()
    encoded = []
    for word in words:
        letters = [reverse.get(c, '?') for c in word if c in reverse]
        encoded.append(' '.join(letters))
    return '   '.join(encoded)

if __name__ == '__main__':
    secret = "HELLO WORLD"
    encoded = encode_morse(secret)
    print(f"Original: {secret}")
    print(f"Encoded:  {encoded}")
    print(f"Decoded:  {decode_morse(encoded)}")
    
    print("\n--- Secret message ---")
    mystery = "... . -.-. .-. . -"
    print(f"Morse: {mystery}")
    print(f"Means: {decode_morse(mystery)}")
