"""
Conway's Game of Life - Terminal Edition
A cellular automaton that simulates life, death, and reproduction.
"""

import time
import os
import random

WIDTH, HEIGHT = 40, 20

def random_grid():
    return [[random.choice([0, 0, 0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % HEIGHT, (c + dc) % WIDTH
            count += grid[nr][nc]
    return count

def next_generation(grid):
    new_grid = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            n = count_neighbors(grid, r, c)
            alive = grid[r][c]
            if alive and n in (2, 3):
                row.append(1)
            elif not alive and n == 3:
                row.append(1)
            else:
                row.append(0)
        new_grid.append(row)
    return new_grid

def render(grid, gen):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation: {gen}  |  Press Ctrl+C to stop")
    print("+" + "-" * WIDTH + "+")
    for row in grid:
        print("|" + "".join("█" if cell else " " for cell in row) + "|")
    print("+" + "-" * WIDTH + "+")

if __name__ == "__main__":
    grid = random_grid()
    gen = 0
    try:
        while True:
            render(grid, gen)
            grid = next_generation(grid)
            gen += 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nSimulation ended after {gen} generations.")
