"""Sieve of Eratosthenes — find all primes up to N."""

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [n for n, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    primes = sieve(100)
    print(f"Primes up to 100 ({len(primes)} total):")
    print(primes)

    twin_primes = [(p, p+2) for p, q in zip(primes, primes[1:]) if q - p == 2]
    print(f"\nTwin primes: {twin_primes}")
