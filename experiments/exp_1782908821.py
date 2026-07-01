"""
Caesar cipher with a twist: supports variable shift per character position.
The key is a sequence that cycles — classic Caesar if key=[3], polyalphabetic if key=[3,7,2].
"""

import string

ALPHA = string.ascii_lowercase

def encrypt(text: str, key: list[int]) -> str:
    result = []
    key_len = len(key)
    shift_idx = 0
    for ch in text:
        if ch.lower() in ALPHA:
            shift = key[shift_idx % key_len]
            is_upper = ch.isupper()
            base = ALPHA.index(ch.lower())
            shifted = ALPHA[(base + shift) % 26]
            result.append(shifted.upper() if is_upper else shifted)
            shift_idx += 1
        else:
            result.append(ch)
    return "".join(result)

def decrypt(text: str, key: list[int]) -> str:
    return encrypt(text, [-k for k in key])

if __name__ == "__main__":
    msg = "Hello, World!"
    key = [3, 7, 13]
    enc = encrypt(msg, key)
    dec = decrypt(enc, key)
    print(f"Original:  {msg}")
    print(f"Key:       {key}")
    print(f"Encrypted: {enc}")
    print(f"Decrypted: {dec}")
    assert dec == msg, "Decryption mismatch!"
    print("Round-trip OK!")

    # Classic Caesar as special case
    classic = encrypt("the quick brown fox", [13])
    print(f"\nROT-13: {classic}")
    print(f"Decode: {decrypt(classic, [13])}")
