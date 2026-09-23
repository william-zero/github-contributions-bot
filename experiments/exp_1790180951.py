# Caesar cipher — the original "encryption" (it isn't really)

def encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def decrypt(text, shift):
    return encrypt(text, -shift)

def crack(ciphertext):
    """Try all 25 shifts and return the most English-looking result."""
    freq = 'etaoinshrdlcumwfgypbvkjxqz'
    best, best_score = None, -1
    for shift in range(1, 26):
        candidate = decrypt(ciphertext, shift)
        score = sum(1 for c in candidate.lower() if c in freq[:8])
        if score > best_score:
            best, best_score = (candidate, shift), score
    return best

if __name__ == '__main__':
    msg = "The quick brown fox jumps over the lazy dog"
    for shift in [3, 13, 25]:
        enc = encrypt(msg, shift)
        dec = decrypt(enc, shift)
        print(f"Shift {shift:2d}: {enc[:30]}...")
        print(f"  Back: {dec[:30]}...")
    
    secret = "Khoor, Zruog!"  # Hello, World! shift 3
    guessed, shift = crack(secret)
    print(f"\nCracked '{secret}' → '{guessed}' (shift={shift})")
