"""Sieve of Eratosthenes — find all primes up to n."""

def sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i, v in enumerate(primes) if v]

if __name__ == "__main__":
    result = sieve(100)
    print(f"Primes up to 100: {result}")
    print(f"Count: {len(result)}")
