# Langton's Ant: a surprisingly complex emergent system
import sys

def langtons_ant(steps=200, size=40):
    grid = [[0] * size for _ in range(size)]
    x, y = size // 2, size // 2
    # directions: 0=up, 1=right, 2=down, 3=left
    direction = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    history = []

    for step in range(steps):
        if 0 <= x < size and 0 <= y < size:
            if grid[y][x] == 0:
                direction = (direction + 1) % 4  # turn right
                grid[y][x] = 1
            else:
                direction = (direction - 1) % 4  # turn left
                grid[y][x] = 0
            x += dx[direction]
            y += dy[direction]

        if step in (10, 50, 100, 199):
            history.append((step + 1, [row[:] for row in grid], x, y))

    for step_num, snapshot, ax, ay in history:
        print(f"\n--- Step {step_num} ---")
        for row_i, row in enumerate(snapshot):
            line = ""
            for col_i, cell in enumerate(row):
                if col_i == ax and row_i == ay:
                    line += "A"
                elif cell:
                    line += "#"
                else:
                    line += "."
            print(line)

if __name__ == "__main__":
    steps = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    print(f"Langton's Ant — {steps} steps on a 40x40 grid")
    print("Simple rules. Chaotic behavior. Classic emergence.")
    langtons_ant(steps)
