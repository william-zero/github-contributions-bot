# Sieve of Eratosthenes — find all primes up to N
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i, v in enumerate(is_prime) if v]

limit = 100
primes = sieve(limit)
print(f"Primes up to {limit}: {primes}")
print(f"Count: {len(primes)}")
print(f"Largest twin-prime pair under {limit}: {next((p, p+2) for p, q in zip(reversed(primes), reversed(primes[1:])) if q - p == 2)}")
