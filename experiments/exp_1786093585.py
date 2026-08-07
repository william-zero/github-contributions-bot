# Conway's Game of Life - minimal terminal version
import time

def make_grid(rows, cols):
    return [[0] * cols for _ in range(rows)]

def seed_glider(grid, r, c):
    pattern = [(0,1),(1,2),(2,0),(2,1),(2,2)]
    for dr, dc in pattern:
        grid[r+dr][c+dc] = 1

def step(grid):
    rows, cols = len(grid), len(grid[0])
    new = make_grid(rows, cols)
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                grid[(r+dr) % rows][(c+dc) % cols]
                for dr in [-1,0,1] for dc in [-1,0,1]
                if (dr, dc) != (0, 0)
            )
            if grid[r][c] == 1 and neighbors in (2, 3):
                new[r][c] = 1
            elif grid[r][c] == 0 and neighbors == 3:
                new[r][c] = 1
    return new

def render(grid):
    return '\n'.join(''.join('█' if c else '·' for c in row) for row in grid)

if __name__ == '__main__':
    rows, cols = 20, 40
    g = make_grid(rows, cols)
    seed_glider(g, 1, 1)
    seed_glider(g, 10, 20)
    for gen in range(50):
        print(f"\033[H\033[J=== Generation {gen} ===")
        print(render(g))
        g = step(g)
        time.sleep(0.1)
    print("Done! The gliders have left the building.")
