"""
prime_spirals.py — visualize primes on an Ulam spiral (ASCII edition)
"""

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return set(i for i, v in enumerate(is_prime) if v)

def ulam_spiral(size=11):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    primes = sieve(size * size)
    x = y = size // 2
    dx, dy = 0, -1
    n = 1
    for _ in range(size * size):
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = '#' if n in primes else '·'
        n += 1
        if x == y or (x < y and x == -y) or (x > y and x == 1 - y):
            dx, dy = -dy, dx
        x += dx
        y += dy
    return '\n'.join(''.join(row) for row in grid)

if __name__ == '__main__':
    print("Ulam Spiral — primes marked with #")
    print(ulam_spiral(21))
