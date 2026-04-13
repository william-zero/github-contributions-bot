#!/usr/bin/env python3
"""
Prime Whisperer: A mystical prime number detective.
Because finding primes is an art form.
"""

def is_prime(n):
    """Whisper sweet mathematics to determine primality."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_whispers(start, end):
    """Whisper all the primes in a range."""
    primes = [n for n in range(start, end) if is_prime(n)]
    return primes

if __name__ == "__main__":
    # Whisper the secrets of the 0-100 realm
    whispers = prime_whispers(0, 100)
    print(f"🔮 The primes whisper: {whispers}")
    print(f"Total whispers heard: {len(whispers)}")
