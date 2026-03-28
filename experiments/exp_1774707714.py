# Weekend experiment: Conway's Game of Life (tiny version)
import time

def next_gen(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                grid[(r+dr) % rows][(c+dc) % cols]
                for dr in [-1,0,1] for dc in [-1,0,1]
                if (dr, dc) != (0, 0)
            )
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid

def display(grid):
    return '\n'.join(''.join('█' if c else '·' for c in row) for row in grid)

# Blinker oscillator seed
grid = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
]

for gen in range(4):
    print(f"Generation {gen}:")
    print(display(grid))
    print()
    grid = next_gen(grid)
