# Cellular automaton explorer: Conway's Game of Life variant
# with "zombie" cells that come back to life after 2 dead generations

import random

WIDTH, HEIGHT = 40, 20
ZOMBIE_WAIT = 2  # dead generations before zombie revival

def init_grid():
    return [[random.choice([True, False]) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def count_neighbors(grid, r, c):
    alive = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = (r + dr) % HEIGHT, (c + dc) % WIDTH
            if grid[nr][nc]:
                alive += 1
    return alive

def step(grid, dead_counts):
    new_grid = [[False]*WIDTH for _ in range(HEIGHT)]
    new_dead = [[0]*WIDTH for _ in range(HEIGHT)]
    for r in range(HEIGHT):
        for c in range(WIDTH):
            n = count_neighbors(grid, r, c)
            if grid[r][c]:
                # Standard survival: 2 or 3 neighbors
                new_grid[r][c] = n in (2, 3)
                new_dead[r][c] = 0
            else:
                dead_counts[r][c] += 1
                # Zombie revival: born again after exactly ZOMBIE_WAIT dead gens
                if dead_counts[r][c] == ZOMBIE_WAIT or n == 3:
                    new_grid[r][c] = True
                    new_dead[r][c] = 0
                else:
                    new_dead[r][c] = dead_counts[r][c]
    return new_grid, new_dead

def render(grid):
    for row in grid:
        print(''.join('█' if c else '·' for c in row))
    print()

def run(generations=10):
    grid = init_grid()
    dead_counts = [[0]*WIDTH for _ in range(HEIGHT)]
    for gen in range(generations):
        print(f"Generation {gen + 1}")
        render(grid)
        grid, dead_counts = step(grid, dead_counts)

if __name__ == "__main__":
    random.seed(42)
    run(generations=5)
