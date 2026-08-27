"""
Caesar Cipher vs ROT13 vs Base64 — Encoding Olympics
Comparing ways humans have tried to keep secrets, ranked by how much they actually work.
"""
import base64

def caesar(text, shift=13):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def rot13(text):
    return caesar(text, 13)

def encode_b64(text):
    return base64.b64encode(text.encode()).decode()

def decode_b64(text):
    return base64.b64decode(text.encode()).decode()

if __name__ == "__main__":
    secret = "The password is hunter2"

    print("=== Encoding Olympics ===\n")
    print(f"Original: {secret}")
    print(f"Caesar+3: {caesar(secret, 3)}")
    print(f"ROT13:    {rot13(secret)}")
    print(f"Base64:   {encode_b64(secret)}")
    print(f"\nSecurity ranking:")
    print("  ROT13:  Cracked by anyone who reads the Wikipedia article once")
    print("  Caesar: Cracked by Julius Caesar, who is dead")
    print("  Base64: Not encryption at all. Stops exactly zero hackers.")
    print("\nConclusion: use a password manager.")
