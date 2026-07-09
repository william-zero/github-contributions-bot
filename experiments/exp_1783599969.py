"""
Prime number sieve with overly dramatic commentary.
"""

def sieve_of_eratosthenes(limit):
    """Find all primes up to limit. The ancient Greeks were onto something."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not invited to the prime party

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False  # eliminated! justice served.

    return [n for n, prime in enumerate(is_prime) if prime]

if __name__ == "__main__":
    limit = 100
    primes = sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {primes}")
    print(f"Found {len(primes)} primes. Eratosthenes would be proud.")
    print(f"Largest prime: {primes[-1]}. A true survivor.")
