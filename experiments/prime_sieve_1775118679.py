#!/usr/bin/env python3
"""
Sieve of Eratosthenes - Finding primes like it's 200 BC
But with modern Python vibes
"""

def sieve_of_eratosthenes(limit):
    """Generate all primes up to limit"""
    if limit < 2:
        return []
    
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    
    return [num for num, prime in enumerate(is_prime) if prime]

if __name__ == "__main__":
    primes = sieve_of_eratosthenes(100)
    print(f"🔢 Primes up to 100: {primes}")
    print(f"📊 Found {len(primes)} primes")
