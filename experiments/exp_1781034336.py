"""
Prime Spiral Visualizer — prints a Ulam spiral of primes in the terminal.
"""

import math


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def ulam_spiral(size=11):
    grid = [[" " for _ in range(size)] for _ in range(size)]
    is_prime = sieve(size * size)

    x, y = size // 2, size // 2
    dx, dy = 0, -1
    n = 1

    for _ in range(size * size):
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = "★" if is_prime[n] else "·"
        n += 1
        if x == y or (x < size // 2 and x == -y) or (x > size // 2 and x == size - 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy

    print(f"\nUlam Prime Spiral ({size}x{size})\n")
    for row in grid:
        print("  " + " ".join(row))
    print()


if __name__ == "__main__":
    ulam_spiral(19)
