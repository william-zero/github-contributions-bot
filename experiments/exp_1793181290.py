"""Prime sieve using the Sieve of Eratosthenes — elegant and ancient."""

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [n for n, is_prime in enumerate(primes) if is_prime]

if __name__ == "__main__":
    result = sieve_of_eratosthenes(100)
    print(f"Primes up to 100: {result}")
    print(f"Count: {len(result)} primes")
    print(f"Largest twin prime pair under 100: {[(p, p+2) for p in result if p+2 in result][-1]}")
