"""
Fibonacci Spiral Art Generator
Prints a spiral using Fibonacci-adjacent numbers.
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def spiral_char(row, col, center_row, center_col):
    dx, dy = col - center_col, row - center_row
    import math
    angle = math.atan2(dy, dx)
    dist = math.sqrt(dx**2 + dy**2)
    spiral = (angle + dist * 0.5) % (2 * math.pi)
    chars = "·•◦○◎●"
    idx = int(spiral / (2 * math.pi) * len(chars)) % len(chars)
    return chars[idx]

size = 21
center = size // 2
for r in range(size):
    print("".join(spiral_char(r, c, center, center) for c in range(size * 2)))

print("\nFib sequence:", list(fib(12)))
