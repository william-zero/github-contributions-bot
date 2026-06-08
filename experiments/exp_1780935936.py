# Caesar cipher with brute-force cracker

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_crack(ciphertext):
    common_words = {'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'you', 'that'}
    best_shift = 0
    best_score = -1
    for shift in range(1, 26):
        attempt = caesar_encrypt(ciphertext, shift)
        words = attempt.lower().split()
        score = sum(1 for w in words if w in common_words)
        if score > best_score:
            best_score = score
            best_shift = shift
    return best_shift, caesar_encrypt(ciphertext, best_shift)

secret = caesar_encrypt("the quick brown fox jumps over the lazy dog", 13)
print(f"Encrypted (ROT13): {secret}")
shift, decoded = caesar_crack(secret)
print(f"Cracked with shift {shift}: {decoded}")
