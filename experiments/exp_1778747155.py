# prime_spiral.py — Ulam spiral: visualize primes in a square grid
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def ulam_spiral(size=21):
    if size % 2 == 0:
        size += 1
    grid = [[0] * size for _ in range(size)]
    x, y = size // 2, size // 2
    n, step, turns = 1, 1, 0
    dx, dy = 0, -1

    grid[y][x] = n
    n += 1

    while n <= size * size:
        for _ in range(2):
            for _ in range(step):
                if n > size * size:
                    break
                x += dx
                y += dy
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = n
                n += 1
            dx, dy = -dy, dx
        step += 1

    print(f"Ulam Spiral ({size}x{size}) — primes marked with *")
    print()
    for row in grid:
        print(" ".join("*" if is_prime(v) else "." for v in row))

if __name__ == "__main__":
    ulam_spiral(21)
    print()
    primes_to_100 = [n for n in range(2, 101) if is_prime(n)]
    print(f"Primes up to 100 ({len(primes_to_100)} total): {primes_to_100}")
