"""
Prime Spiral: plot primes on an Ulam spiral and print them as ASCII.
Purely recreational — no external deps required.
"""

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


def ulam_spiral(size=11):
    grid = [[0] * size for _ in range(size)]
    cx, cy = size // 2, size // 2
    x, y = cx, cy
    num = 1
    step = 1

    grid[y][x] = num
    num += 1

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
    d = 0

    while num <= size * size:
        for _ in range(2):
            dx, dy = directions[d % 4]
            for _ in range(step):
                if num > size * size:
                    break
                x += dx
                y += dy
                if 0 <= x < size and 0 <= y < size:
                    grid[y][x] = num
                num += 1
            d += 1
        step += 1

    print(f"Ulam Spiral ({size}x{size}) — primes marked with *")
    for row in grid:
        print(" ".join("* " if is_prime(n) else ". " for n in row))


if __name__ == "__main__":
    ulam_spiral(11)
