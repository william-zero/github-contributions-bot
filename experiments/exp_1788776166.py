# Sieve of Eratosthenes - classic prime finder
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

primes = sieve(100)
print(f"Primes up to 100: {primes}")
print(f"Count: {len(primes)}")
print(f"Largest prime <= 100: {primes[-1]}")

# Fun: twin primes (pairs differing by 2)
twins = [(p, p+2) for p in primes if p+2 in set(primes)]
print(f"Twin prime pairs: {twins}")
