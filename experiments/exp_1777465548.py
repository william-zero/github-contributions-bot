"""
Conway's Game of Life in a terminal window — tiny edition.
Run it and watch a chaotic world evolve from a random seed.
"""
import random, time, os

W, H = 40, 20

def make_grid():
    return [[random.choice([0, 0, 0, 1]) for _ in range(W)] for _ in range(H)]

def step(grid):
    new = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            nbrs = sum(
                grid[(y+dy) % H][(x+dx) % W]
                for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                if (dy, dx) != (0, 0)
            )
            new[y][x] = 1 if (grid[y][x] and nbrs in (2, 3)) or (not grid[y][x] and nbrs == 3) else 0
    return new

def render(grid, gen):
    os.system("clear")
    print(f"  Conway's Game of Life — generation {gen}\n")
    for row in grid:
        print("  " + "".join("█" if c else " " for c in row))

g = make_grid()
for i in range(60):
    render(g, i)
    g = step(g)
    time.sleep(0.1)

print("\n  The universe has settled. Or ended. Hard to say.")
