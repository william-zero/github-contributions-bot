# Sierpinski triangle via chaos game
import random

def chaos_triangle(steps=5000):
    vertices = [(0.5, 1.0), (0.0, 0.0), (1.0, 0.0)]
    x, y = 0.5, 0.5
    points = []
    for _ in range(steps):
        vx, vy = random.choice(vertices)
        x = (x + vx) / 2
        y = (y + vy) / 2
        points.append((round(x, 4), round(y, 4)))
    return points

if __name__ == "__main__":
    pts = chaos_triangle(200)
    print(f"Generated {len(pts)} chaos game points")
    print(f"Sample: {pts[:5]}")
    # Rough ASCII render (40x20)
    grid = [['.' for _ in range(40)] for _ in range(20)]
    for px, py in pts:
        col = int(px * 39)
        row = int((1 - py) * 19)
        grid[row][col] = '*'
    for row in grid:
        print(''.join(row))
