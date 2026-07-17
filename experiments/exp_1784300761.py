"""
Sieve of Eratosthenes — classic prime-finding algorithm.
Returns all primes up to n in O(n log log n) time.
"""

def sieve(n: int) -> list[int]:
    if n < 2:
        return []
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i::i] = bytearray(len(is_prime[i*i::i]))
    return [i for i, v in enumerate(is_prime) if v]


if __name__ == "__main__":
    primes = sieve(100)
    print(f"Primes up to 100 ({len(primes)} total): {primes}")
    print(f"10,000th prime: {sieve(105000)[9999]}")
