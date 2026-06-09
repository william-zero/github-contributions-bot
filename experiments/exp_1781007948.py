"""
Conway's Game of Life - minimal terminal renderer.
Classic cellular automaton: cells live or die by neighbor count.
"""

import random
import os
import time

ROWS, COLS = 20, 40
ALIVE = "#"
DEAD = "."

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
    new = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            n = count_neighbors(grid, r, c)
            alive = grid[r][c]
            if alive:
                row.append(1 if n in (2, 3) else 0)
            else:
                row.append(1 if n == 3 else 0)
        new.append(row)
    return new

def render(grid, gen):
    os.system("clear")
    print(f"Conway's Game of Life — Generation {gen}")
    print("+" + "-" * COLS + "+")
    for row in grid:
        print("|" + "".join(ALIVE if c else DEAD for c in row) + "|")
    print("+" + "-" * COLS + "+")

if __name__ == "__main__":
    grid = make_grid()
    for gen in range(50):
        render(grid, gen)
        time.sleep(0.15)
        grid = step(grid)
    print("Simulation complete.")
