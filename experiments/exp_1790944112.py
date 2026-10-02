"""
Cellular Automata: Conway's Game of Life
Because sometimes you just need to watch virtual cells live and die.
"""
import random
import time

def create_grid(rows, cols, random_init=True):
    if random_init:
        return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return [[0]*cols for _ in range(rows)]

def count_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            r, c = (row + dr) % rows, (col + dc) % cols
            count += grid[r][c]
    return count

def next_generation(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid

def render(grid):
    return '\n'.join(''.join('█' if cell else ' ' for cell in row) for row in grid)

def count_alive(grid):
    return sum(sum(row) for row in grid)

# Run a few generations
random.seed(42)
grid = create_grid(10, 20)
print("Conway's Game of Life — 5 generations")
print(f"Gen 0: {count_alive(grid)} alive")
for gen in range(1, 6):
    grid = next_generation(grid)
    print(f"Gen {gen}: {count_alive(grid)} alive")

print("\nFinal state:")
print(render(grid))
