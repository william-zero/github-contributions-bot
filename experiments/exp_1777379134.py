"""
Goldbach Verifier: checks Goldbach's conjecture for small even numbers.
Every even integer > 2 is the sum of two primes (unproven in general, but true up to ~4e18).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    for p in range(2, n):
        if is_prime(p) and is_prime(n - p):
            return p, n - p
    return None

print("Goldbach decompositions:")
for even in range(4, 51, 2):
    pair = goldbach(even)
    print(f"  {even:3d} = {pair[0]} + {pair[1]}")
