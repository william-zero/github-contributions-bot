"""
Sieve of Eratosthenes — classic prime finder, now with progress bar vibes.
"""

def sieve_of_eratosthenes(limit):
    """Return all primes up to limit using the classic sieve."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [n for n, prime in enumerate(is_prime) if prime]

def goldbach_check(n):
    """Verify Goldbach's conjecture: every even n > 2 is sum of two primes."""
    primes = set(sieve_of_eratosthenes(n))
    for p in primes:
        if (n - p) in primes:
            return p, n - p
    return None

if __name__ == "__main__":
    limit = 1000
    primes = sieve_of_eratosthenes(limit)
    print(f"Primes up to {limit}: {len(primes)} found")
    print(f"First 10: {primes[:10]}")
    print(f"Last 10:  {primes[-10:]}")

    print("\nGoldbach checks (even numbers 4..30):")
    for n in range(4, 32, 2):
        pair = goldbach_check(n)
        print(f"  {n:3d} = {pair[0]} + {pair[1]}")
