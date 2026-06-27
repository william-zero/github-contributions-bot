"""
Bifurcation diagram for the logistic map:
  x_{n+1} = r * x_n * (1 - x_n)
Shows how a simple equation transitions from order to chaos as r grows.
"""

import sys

WIDTH = 70
HEIGHT = 30
R_MIN = 2.4
R_MAX = 4.0

cols = []
for col in range(WIDTH):
    r = R_MIN + (R_MAX - R_MIN) * col / WIDTH
    x = 0.5
    # warm up
    for _ in range(300):
        x = r * x * (1 - x)
    points = set()
    for _ in range(200):
        x = r * x * (1 - x)
        row = int((1 - x) * (HEIGHT - 1))
        points.add(row)
    cols.append(points)

grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
for col, points in enumerate(cols):
    for row in points:
        grid[row][col] = '*'

print("Logistic Map Bifurcation Diagram")
print(f"r: {R_MIN:.1f} {'':>58} {R_MAX:.1f}")
print()
for row in grid:
    print(''.join(row))
print()
print("Stable fixed points → period doubling → beautiful chaos")
