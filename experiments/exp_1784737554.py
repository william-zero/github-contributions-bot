"""
Conway's Game of Life - minimal terminal renderer
Press Ctrl+C to quit
"""
import time, os, random

def make_grid(rows, cols):
    return [[random.choice([0, 0, 0, 1]) for _ in range(cols)] for _ in range(rows)]

def count_neighbors(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    total = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % rows, (c + dc) % cols
            total += grid[nr][nc]
    return total

def step(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            n = count_neighbors(grid, r, c)
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if n in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if n == 3 else 0
    return new_grid

def render(grid):
    return "\n".join("".join("█" if cell else " " for cell in row) for row in grid)

if __name__ == "__main__":
    rows, cols = 20, 60
    grid = make_grid(rows, cols)
    try:
        for gen in range(100):
            os.system("clear")
            print(f"Generation {gen}")
            print(render(grid))
            grid = step(grid)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Game over!")
