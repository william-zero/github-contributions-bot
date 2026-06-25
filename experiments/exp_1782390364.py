"""
Langton's Ant — a surprisingly complex Turing machine made of one rule:
  - On a white cell: turn right, flip cell to black, move forward
  - On a black cell: turn left, flip cell to white, move forward
After ~10,000 steps it produces a 'highway' that repeats every 104 steps forever.
"""

def run_langtons_ant(steps=12000, grid_size=80):
    grid = set()  # black cells
    x, y = grid_size // 2, grid_size // 2
    dx, dy = 0, -1  # facing up

    for _ in range(steps):
        if (x, y) in grid:
            # black: turn left, uncolor
            dx, dy = dy, -dx
            grid.discard((x, y))
        else:
            # white: turn right, color
            dx, dy = -dy, dx
            grid.add((x, y))
        x += dx
        y += dy

    return grid, (x, y), grid_size

def render(grid, ant_pos, size):
    lines = []
    for row in range(size):
        line = ""
        for col in range(size):
            if (col, row) == ant_pos:
                line += "A"
            elif (col, row) in grid:
                line += "█"
            else:
                line += "·"
        lines.append(line)
    return "\n".join(lines)

if __name__ == "__main__":
    grid, ant, size = run_langtons_ant()
    print(render(grid, ant, size))
    print(f"\nBlack cells: {len(grid)}  |  Ant at: {ant}")
    print("Notice the 'highway' corridor in the lower-right — emergent order from chaos.")
