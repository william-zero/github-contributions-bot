# Chaos Game - fractal geometry through random iteration
import random

def chaos_game(vertices, ratio=0.5, iterations=10000):
    """Generate fractal points via the chaos game algorithm."""
    x, y = 0.5, 0.5
    points = []
    for _ in range(iterations):
        target = random.choice(vertices)
        x = x + (target[0] - x) * ratio
        y = y + (target[1] - y) * ratio
        points.append((x, y))
    return points

# Sierpinski triangle vertices
triangle = [(0.5, 1.0), (0.0, 0.0), (1.0, 0.0)]
pts = chaos_game(triangle, ratio=0.5, iterations=5000)

# ASCII render (40x20 grid)
grid = [[' '] * 40 for _ in range(20)]
for px, py in pts:
    col = int(px * 39)
    row = int((1 - py) * 19)
    if 0 <= col < 40 and 0 <= row < 20:
        grid[row][col] = '*'

for row in grid:
    print(''.join(row))

print(f"\nChaos game: {len(pts)} points → Sierpinski triangle emerges from pure randomness.")
