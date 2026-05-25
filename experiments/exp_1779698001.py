# Caesar cipher encoder/decoder with brute-force cracker

def caesar_encode(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decode(text, shift):
    return caesar_encode(text, 26 - shift)

def brute_force(cipher):
    print("Brute force attempts:")
    for shift in range(1, 26):
        print(f"  Shift {shift:2}: {caesar_decode(cipher, shift)}")

# Demo
message = "The quick brown fox jumps over the lazy dog"
encoded = caesar_encode(message, 13)  # ROT13
print(f"Original: {message}")
print(f"ROT13:    {encoded}")
print(f"Decoded:  {caesar_decode(encoded, 13)}")
