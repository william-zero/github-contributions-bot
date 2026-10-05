"""
Fibonacci Spiral Generator
Generates the Fibonacci sequence and draws an ASCII spiral approximation.
"""

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def spiral_ascii(size=10):
    grid = [['.' for _ in range(size * 2)] for _ in range(size)]
    cx, cy = size, size // 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0
    r, c = cy, cx
    fibs = fibonacci(20)
    
    for i, f in enumerate(fibs[:15]):
        char = str(i % 10)
        for _ in range(f):
            if 0 <= r < size and 0 <= c < size * 2:
                grid[r][c] = char
            dr, dc = directions[d % 4]
            r, c = r + dr, c + dc
        d += 1

    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    fibs = fibonacci(15)
    print("Fibonacci sequence:", fibs)
    print("\nASCII Spiral:")
    spiral_ascii()
