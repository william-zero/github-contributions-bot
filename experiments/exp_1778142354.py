"""Conway's Game of Life — terminal ASCII renderer."""
import time, random

WIDTH, HEIGHT, GENS = 40, 20, 30

def make_grid():
    return [[random.choice([0, 0, 0, 1]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(g, r, c):
    total = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            total += g[(r + dr) % HEIGHT][(c + dc) % WIDTH]
    return total

def step(g):
    new = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            n = count_neighbors(g, r, c)
            if g[r][c]:
                row.append(1 if n in (2, 3) else 0)
            else:
                row.append(1 if n == 3 else 0)
        new.append(row)
    return new

def render(g, gen):
    border = "+" + "-" * WIDTH + "+"
    print(f"\033[H\033[2J", end="")
    print(f"Conway's Game of Life — Generation {gen}")
    print(border)
    for row in g:
        print("|" + "".join("█" if c else " " for c in row) + "|")
    print(border)

grid = make_grid()
for gen in range(GENS):
    render(grid, gen)
    grid = step(grid)
    time.sleep(0.12)
print("Simulation complete.")
