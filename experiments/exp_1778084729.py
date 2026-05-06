"""
Prime Spiral Visualizer
Plots primes on an Ulam spiral and displays them in ASCII.
"""

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return set(i for i in range(2, n+1) if is_prime[i])

def ulam_spiral(size):
    grid = [[' '] * size for _ in range(size)]
    primes = sieve(size * size)
    x, y = size // 2, size // 2
    dx, dy = 0, -1
    steps, step_count, turns = 1, 0, 0

    for n in range(1, size * size + 1):
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = '*' if n in primes else '.'
        x += dx
        y += dy
        step_count += 1
        if step_count == steps:
            step_count = 0
            dx, dy = -dy, dx
            turns += 1
            if turns % 2 == 0:
                steps += 1

    return grid

def display(size=21):
    grid = ulam_spiral(size)
    print(f"Ulam Spiral ({size}x{size}) — * = prime, . = composite\n")
    for row in grid:
        print(' '.join(row))

if __name__ == '__main__':
    display()
