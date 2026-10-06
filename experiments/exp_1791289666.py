"""
Conway's Game of Life - tiny terminal demo
"""
import random
import time

ROWS, COLS = 20, 40

def random_grid():
    return [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]

def next_gen(grid):
    new = [[0]*COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            neighbors = sum(
                grid[(r+dr) % ROWS][(c+dc) % COLS]
                for dr in [-1, 0, 1] for dc in [-1, 0, 1]
                if (dr, dc) != (0, 0)
            )
            if grid[r][c] == 1:
                new[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new[r][c] = 1 if neighbors == 3 else 0
    return new

def display(grid):
    print("\n".join("".join("█" if c else "·" for c in row) for row in grid))

if __name__ == "__main__":
    grid = random_grid()
    for gen in range(10):
        print(f"\n--- Generation {gen} ---")
        display(grid)
        grid = next_gen(grid)
        time.sleep(0.3)
