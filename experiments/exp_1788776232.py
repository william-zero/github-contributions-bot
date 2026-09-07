"""Conway's Game of Life in terminal — minimal edition."""
import time
import os
import random

WIDTH, HEIGHT = 40, 20

def make_grid():
    return [[random.random() < 0.3 for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % HEIGHT, (c + dc) % WIDTH
            count += grid[nr][nc]
    return count

def step(grid):
    new = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            n = count_neighbors(grid, r, c)
            alive = grid[r][c]
            row.append(n == 3 or (alive and n == 2))
        new.append(row)
    return new

def render(grid):
    os.system('clear')
    for row in grid:
        print(''.join('██' if cell else '  ' for cell in row))

grid = make_grid()
for _ in range(50):
    render(grid)
    time.sleep(0.1)
    grid = step(grid)
