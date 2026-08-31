"""
Prime spiral visualizer - generates a Ulam spiral of primes in ASCII art
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
    
    dx, dy = 0, -1
    n = 1
    steps = 1
    step_count = 0
    turns = 0
    
    while n <= size * size:
        if 0 <= x < size and 0 <= y < size:
            grid[y][x] = '★' if is_prime(n) else '·'
        n += 1
        x += dx
        y += dy
        step_count += 1
        if step_count == steps:
            step_count = 0
            dx, dy = -dy, dx  # turn left
            turns += 1
            if turns % 2 == 0:
                steps += 1
    
    return '\n'.join(' '.join(row) for row in grid)

if __name__ == '__main__':
    print("Ulam Prime Spiral (★ = prime, · = composite):\n")
    print(ulam_spiral(15))
