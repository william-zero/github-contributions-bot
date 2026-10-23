# Cellular automaton: Conway's Game of Life, tiny edition

import time
import os

def step(grid):
    rows, cols = len(grid), len(grid[0])
    new = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            alive = sum(
                grid[(r+dr) % rows][(c+dc) % cols]
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if (dr, dc) != (0, 0)
            )
            if grid[r][c]:
                new[r][c] = 1 if alive in (2, 3) else 0
            else:
                new[r][c] = 1 if alive == 3 else 0
    return new

def render(grid):
    return '\n'.join(''.join('█' if c else '·' for c in row) for row in grid)

# Glider pattern
glider = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

if __name__ == '__main__':
    grid = glider
    for gen in range(5):
        print(f"Generation {gen}:")
        print(render(grid))
        print()
        grid = step(grid)
