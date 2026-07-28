"""
Prime Spiral - visualize primes on a number spiral (Ulam spiral concept)
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ulam_spiral(size=11):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    cx, cy = size // 2, size // 2
    x, y = cx, cy
    n = 1
    dx, dy = 0, -1
    steps, step_count, turns = 1, 0, 0

    while n <= size * size:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = '●' if is_prime(n) else '·'
        n += 1
        x += dx
        y += dy
        step_count += 1
        if step_count == steps:
            step_count = 0
            dx, dy = -dy, dx
            turns += 1
            if turns % 2 == 0:
                steps += 1

    for row in grid:
        print(' '.join(row))

if __name__ == '__main__':
    print("Ulam Spiral (● = prime, · = composite):\n")
    ulam_spiral(15)
