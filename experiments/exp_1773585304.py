# weekend_random_walk.py
# A tiny random walk simulation — because sometimes you just wander

import random

def random_walk(steps=20, seed=None):
    if seed:
        random.seed(seed)
    x, y = 0, 0
    path = [(x, y)]
    for _ in range(steps):
        dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
        path.append((x, y))
    return path

def render(path):
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for i, (x, y) in enumerate(path):
        c = 'S' if i == 0 else ('E' if i == len(path)-1 else '*')
        grid[y - min_y][x - min_x] = c
    for row in reversed(grid):
        print(' '.join(row))

if __name__ == '__main__':
    walk = random_walk(steps=30, seed=42)
    render(walk)
    print(f"\nStarted at {walk[0]}, ended at {walk[-1]}")
    dist = ((walk[-1][0]**2) + (walk[-1][1]**2)) ** 0.5
    print(f"Straight-line distance from origin: {dist:.2f}")
