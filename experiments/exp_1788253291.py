"""
Sieve of Eratosthenes with animated sparkline output.
Finds all primes up to N and shows density per block.
"""

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def density_sparkline(primes, n, blocks=20):
    block_size = n // blocks
    bars = " ▁▂▃▄▅▆▇█"
    densities = []
    for b in range(blocks):
        lo = b * block_size + 1
        hi = lo + block_size
        count = sum(1 for p in primes if lo <= p < hi)
        densities.append(count)
    max_d = max(densities) or 1
    return "".join(bars[int(d / max_d * 8)] for d in densities)

if __name__ == "__main__":
    N = 500
    primes = sieve(N)
    print(f"Primes up to {N}: {len(primes)} found")
    print(f"First 10: {primes[:10]}")
    print(f"Density:  {density_sparkline(primes, N)}")
