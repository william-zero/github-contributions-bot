"""Conway's Game of Life in a terminal — because why not simulate the universe."""
import time
import random

def make_grid(rows, cols, density=0.3):
    return [[1 if random.random() < density else 0 for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    return sum(
        grid[(r + dr) % rows][(c + dc) % cols]
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr, dc) != (0, 0)
    )

def step(grid):
    rows, cols = len(grid), len(grid[0])
    return [
        [1 if (grid[r][c] and count_neighbors(grid, r, c) in (2, 3))
              or (not grid[r][c] and count_neighbors(grid, r, c) == 3)
         else 0 for c in range(cols)]
        for r in range(rows)
    ]

def render(grid):
    return "\n".join("".join("█" if cell else "·" for cell in row) for row in grid)

if __name__ == "__main__":
    grid = make_grid(20, 40)
    for gen in range(50):
        print(f"\033[H\033[J")  # clear screen
        print(f"Generation {gen}\n")
        print(render(grid))
        grid = step(grid)
        time.sleep(0.1)
