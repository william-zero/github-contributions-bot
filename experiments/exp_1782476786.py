"""
Ulam Spiral: Visualize prime number distribution in a spiral grid.
Primes cluster along diagonals — a mystery mathematicians still debate.
"""

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return is_prime

def ulam_spiral(size=21):
    grid = [[0] * size for _ in range(size)]
    max_n = size * size
    primes = sieve(max_n)

    x, y = size // 2, size // 2
    n = 1
    dx, dy = 0, -1
    step, steps_taken, direction_changes = 1, 0, 0

    while n <= max_n:
        grid[y][x] = n
        n += 1
        x += dx
        y += dy
        steps_taken += 1
        if steps_taken == step:
            steps_taken = 0
            dx, dy = -dy, dx  # rotate 90°
            direction_changes += 1
            if direction_changes % 2 == 0:
                step += 1

    print(f"Ulam Spiral ({size}x{size}) — primes shown as '*', composites as '.'")
    print()
    for row in grid:
        print(" ".join("*" if primes[v] else "." for v in row))

    prime_count = sum(1 for row in grid for v in row if v > 0 and primes[v])
    print(f"\nPrimes in spiral: {prime_count}/{max_n - 1} ({100*prime_count/(max_n-1):.1f}%)")

if __name__ == "__main__":
    ulam_spiral(31)
