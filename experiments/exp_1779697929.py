# Sieve of Eratosthenes - find all primes up to N

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

primes = sieve(100)
print(f"Primes up to 100 ({len(primes)} total):")
for i, p in enumerate(primes):
    end = '\n' if (i+1) % 10 == 0 else ' '
    print(p, end=end)

twin_primes = [(p, p+2) for p in primes if p+2 in set(primes)]
print(f"\nTwin primes: {twin_primes}")
