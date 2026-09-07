"""Conway's Game of Life in your terminal."""
import time, os, random

def make_grid(w, h, density=0.3):
    return [[1 if random.random() < density else 0 for _ in range(w)] for _ in range(h)]

def step(grid):
    h, w = len(grid), len(grid[0])
    new = [[0]*w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            neighbours = sum(
                grid[(y+dy) % h][(x+dx) % w]
                for dy in (-1,0,1) for dx in (-1,0,1)
                if (dy, dx) != (0, 0)
            )
            alive = grid[y][x]
            new[y][x] = 1 if (alive and neighbours in (2,3)) or (not alive and neighbours == 3) else 0
    return new

def draw(grid):
    chars = {0: '  ', 1: '██'}
    return '\n'.join(''.join(chars[c] for c in row) for row in grid)

if __name__ == '__main__':
    W, H, FRAMES = 40, 20, 50
    grid = make_grid(W, H)
    for i in range(FRAMES):
        os.system('clear')
        print(f"Generation {i+1}")
        print(draw(grid))
        grid = step(grid)
        time.sleep(0.1)
    print("Done!")
