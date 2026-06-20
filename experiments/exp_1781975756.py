"""
Langton's Ant — a Turing-complete cellular automaton that starts with
simple rules and produces surprisingly complex emergent behavior.
Rules: on white square, turn right, flip color, move forward
       on black square, turn left, flip color, move forward
"""

def run_langtons_ant(steps=11_000, grid_size=200):
    # Grid: True = black, False = white (start all white)
    grid = [[False] * grid_size for _ in range(grid_size)]
    x, y = grid_size // 2, grid_size // 2
    # Directions: 0=up, 1=right, 2=down, 3=left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direction = 0

    for step in range(steps):
        cell = grid[y][x]
        if cell:  # black: turn left
            direction = (direction - 1) % 4
        else:      # white: turn right
            direction = (direction + 1) % 4
        grid[y][x] = not cell
        x = (x + dx[direction]) % grid_size
        y = (y + dy[direction]) % grid_size

    return grid, x, y


def render_ascii(grid, x, y, view=40):
    cx, cy = len(grid[0]) // 2, len(grid) // 2
    rows = []
    for row in range(cy - view, cy + view):
        line = []
        for col in range(cx - view, cx + view):
            if row == y and col == x:
                line.append("@")
            elif grid[row % len(grid)][col % len(grid[0])]:
                line.append("█")
            else:
                line.append("·")
        rows.append("".join(line))
    return "\n".join(rows)


if __name__ == "__main__":
    print("Running Langton's Ant for 11,000 steps...")
    print("After ~10,000 steps it builds a 'highway' — an infinite repeating pattern.\n")
    grid, ax, ay = run_langtons_ant()
    print(render_ascii(grid, ax, ay))
