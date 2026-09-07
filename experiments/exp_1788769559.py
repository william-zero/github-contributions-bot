# Langton's Ant - a cellular automaton that creates emergent highway patterns
import sys

def run_langtons_ant(steps=12000, grid_size=150):
    grid = [[0] * grid_size for _ in range(grid_size)]
    x, y = grid_size // 2, grid_size // 2
    # directions: 0=up, 1=right, 2=down, 3=left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direction = 0

    for _ in range(steps):
        cell = grid[y][x]
        if cell == 0:  # white cell: turn right, flip, move
            direction = (direction + 1) % 4
        else:           # black cell: turn left, flip, move
            direction = (direction - 1) % 4
        grid[y][x] = 1 - cell
        x = (x + dx[direction]) % grid_size
        y = (y + dy[direction]) % grid_size

    return grid, x, y

def render_ascii(grid, ant_x, ant_y):
    chars = {0: '.', 1: '#'}
    size = len(grid)
    # show a 40x40 window around center
    cx, cy = size // 2, size // 2
    half = 20
    print(f"Langton's Ant after 12000 steps (ant at {ant_x},{ant_y}):")
    print("+" + "-" * 40 + "+")
    for row in range(cy - half, cy + half):
        line = "|"
        for col in range(cx - half, cx + half):
            if row == ant_y and col == ant_x:
                line += "A"
            else:
                line += chars[grid[row][col]]
        line += "|"
        print(line)
    print("+" + "-" * 40 + "+")
    black = sum(cell for row in grid for cell in row)
    print(f"Black cells: {black} / {size*size} ({100*black/(size*size):.1f}%)")

if __name__ == "__main__":
    grid, ax, ay = run_langtons_ant()
    render_ascii(grid, ax, ay)
