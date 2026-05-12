# Langton's Ant — a cellular automaton that emergies from two simple rules
# Despite simple rules, it produces complex "highway" patterns after ~10k steps

def langtons_ant(steps=100, grid_size=41):
    grid = [[0] * grid_size for _ in range(grid_size)]
    cx, cy = grid_size // 2, grid_size // 2
    # directions: 0=up, 1=right, 2=down, 3=left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction = 0

    for _ in range(steps):
        if grid[cx][cy] == 0:
            direction = (direction + 1) % 4  # turn right on white
            grid[cx][cy] = 1
        else:
            direction = (direction - 1) % 4  # turn left on black
            grid[cx][cy] = 0
        cx += dx[direction]
        cy += dy[direction]
        # wrap around
        cx %= grid_size
        cy %= grid_size

    return grid

def render(grid):
    for row in grid:
        print("".join("##" if cell else "  " for cell in row))

if __name__ == "__main__":
    print("=== Langton's Ant after 500 steps ===")
    g = langtons_ant(steps=500)
    render(g)
    print()
    print("=== Langton's Ant after 11000 steps (highway phase) ===")
    g2 = langtons_ant(steps=11000)
    render(g2)
