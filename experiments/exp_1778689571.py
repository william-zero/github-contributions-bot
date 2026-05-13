# Caesar cipher with ROT-N support and frequency analysis helper

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force(ciphertext):
    print("Brute-force all 26 shifts:\n")
    for shift in range(26):
        print(f"  ROT-{shift:02d}: {caesar_decrypt(ciphertext, shift)}")

def frequency_analysis(text):
    from collections import Counter
    letters = [c.lower() for c in text if c.isalpha()]
    counts = Counter(letters)
    total = sum(counts.values())
    print("\nLetter frequency (top 8):")
    for letter, count in counts.most_common(8):
        bar = '#' * count
        print(f"  {letter}: {bar} ({count/total:.1%})")

if __name__ == "__main__":
    message = "The quick brown fox jumps over the lazy dog"
    shift = 13  # classic ROT-13

    encrypted = caesar_encrypt(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    print(f"Original : {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"\nROT-13 of 'Hello, World!': {caesar_encrypt('Hello, World!', 13)}")

    frequency_analysis(message)
    print()
    brute_force("Gur dhvpx oebja sbk whzcf bire gur ynml qbt")
