"""
Sieve of Eratosthenes - ancient algorithm, still undefeated.
Find all prime numbers up to N using the classical Greek method.
"""


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1
    return [n for n, prime in enumerate(is_prime) if prime]


limit = 100
primes = sieve_of_eratosthenes(limit)
print(f"Primes up to {limit} ({len(primes)} found):")
print(primes)

# Fun fact: there are 25 primes below 100
# and Eratosthenes computed this by hand around 240 BC
