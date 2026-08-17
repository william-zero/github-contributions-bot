"""
Conway's Game of Life — minimal terminal renderer
"""
import random
import time
import os

ROWS, COLS = 20, 40

def make_grid():
    return [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

def count_neighbors(grid, r, c):
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % ROWS, (c + dc) % COLS
            total += grid[nr][nc]
    return total

def step(grid):
    new_grid = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                row.append(1 if n in (2, 3) else 0)
            else:
                row.append(1 if n == 3 else 0)
        new_grid.append(row)
    return new_grid

def render(grid, gen):
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"Generation {gen}")
    for row in grid:
        print(''.join('█' if c else ' ' for c in row))

grid = make_grid()
for gen in range(50):
    render(grid, gen)
    grid = step(grid)
    time.sleep(0.1)
