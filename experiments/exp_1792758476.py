# A script that generates a self-avoiding random walk and visualizes it in ASCII

import random

def random_walk(steps=20):
    visited = set()
    x, y = 0, 0
    visited.add((x, y))
    path = [(x, y)]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for _ in range(steps):
        random.shuffle(directions)
        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                x, y = nx, ny
                visited.add((x, y))
                path.append((x, y))
                moved = True
                break
        if not moved:
            break  # stuck
    
    return path

def render(path):
    if not path:
        return
    xs = [p[0] for p in path]
    ys = [p[1] for p in path]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    
    grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    
    for i, (x, y) in enumerate(path):
        gx = x - min_x
        gy = y - min_y
        if i == 0:
            grid[gy][gx] = 'S'
        elif i == len(path) - 1:
            grid[gy][gx] = 'E'
        else:
            grid[gy][gx] = '*'
    
    for row in reversed(grid):
        print(''.join(row))

if __name__ == '__main__':
    print("Self-Avoiding Random Walk:")
    path = random_walk(steps=30)
    render(path)
    print(f"Steps taken: {len(path) - 1}")
