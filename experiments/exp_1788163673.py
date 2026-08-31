"""
Caesar Cipher Cracker
If you don't know the shift, try all 26 and look for English words.
Julius Caesar used ROT-3. ROT-13 is more popular now. Neither is secure.
"""

FREQ_ORDER = "etaoinshrdlcumwfgypbvkjxqz"

def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def frequency_score(text):
    text = text.lower()
    total = sum(1 for c in text if c.isalpha())
    if total == 0:
        return 0
    score = 0
    for i, letter in enumerate(FREQ_ORDER):
        count = text.count(letter)
        score += count * (26 - i)
    return score / total

def crack_caesar(ciphertext):
    best_shift, best_score, best_text = 0, -1, ""
    for shift in range(26):
        candidate = caesar_encrypt(ciphertext, shift)
        score = frequency_score(candidate)
        if score > best_score:
            best_score, best_shift, best_text = score, shift, candidate
    return best_shift, best_text

secret = caesar_encrypt("The quick brown fox jumps over the lazy dog", 13)
print(f"Encrypted (ROT-13): {secret}")
shift, decrypted = crack_caesar(secret)
print(f"Cracked (shift -{shift}): {decrypted}")
