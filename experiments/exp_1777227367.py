# Conway's Game of Life - minimal terminal edition
import time, os, random

def step(grid, W, H):
    new = [[0]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            n = sum(
                grid[(y+dy)%H][(x+dx)%W]
                for dy in [-1,0,1] for dx in [-1,0,1]
                if (dx,dy) != (0,0)
            )
            new[y][x] = 1 if (grid[y][x] and n in (2,3)) or (not grid[y][x] and n==3) else 0
    return new

W, H = 40, 20
grid = [[random.randint(0,1) for _ in range(W)] for _ in range(H)]

for _ in range(50):
    os.system('clear')
    print('\n'.join(''.join('█' if c else ' ' for c in row) for row in grid))
    grid = step(grid, W, H)
    time.sleep(0.1)
