# Conway's Game of Life — pocket edition (10x10)
import time, os

def step(grid):
    rows, cols = len(grid), len(grid[0])
    new = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                grid[(r+dr) % rows][(c+dc) % cols]
                for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                if (dr, dc) != (0, 0)
            )
            alive = grid[r][c]
            new[r][c] = 1 if (alive and neighbors in (2, 3)) or (not alive and neighbors == 3) else 0
    return new

def display(grid):
    return "\n".join("".join("█" if c else "·" for c in row) for row in grid)

# Glider pattern
GLIDER = [
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

if __name__ == "__main__":
    grid = [row[:] for row in GLIDER]
    for gen in range(5):
        print(f"Generation {gen}:")
        print(display(grid))
        print()
        grid = step(grid)
