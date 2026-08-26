# Sieve of Eratosthenes — ancient prime finder, still unbeaten for small ranges
# Named after a Greek mathematician who also accurately calculated Earth's circumference
# around 240 BC using shadows and a well. Truly an overachiever.

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [n for n, prime in enumerate(is_prime) if prime]

primes = sieve(100)
print(f"Primes up to 100: {primes}")
print(f"Count: {len(primes)} — about {len(primes)/100:.0%} of numbers")

# Twin primes (pairs that differ by 2) — are there infinitely many? Unknown.
twins = [(p, p+2) for p in primes if p+2 in set(primes)]
print(f"Twin prime pairs under 100: {twins}")
