# Fun experiment: Conway's Game of Life (mini edition)
# Because what is life if not a grid of 1s and 0s?

def step(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                grid[(r+dr) % rows][(c+dc) % cols]
                for dr in [-1,0,1] for dc in [-1,0,1]
                if not (dr == 0 and dc == 0)
            )
            if grid[r][c] == 1:
                new_grid[r][c] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[r][c] = 1 if neighbors == 3 else 0
    return new_grid

def display(grid):
    for row in grid:
        print("".join("██" if c else "  " for c in row))
    print()

# Glider pattern — the simplest traveling structure
glider = [
    [0,0,1,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

print("Conway's Game of Life — Glider (3 generations)")
print("=" * 40)
current = glider
for gen in range(3):
    print(f"Generation {gen}:")
    display(current)
    current = step(current)
