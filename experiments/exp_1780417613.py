"""
Langton's Ant — a cellular automaton with emergent complexity
Rules: on a white cell, turn right, flip cell black, move forward.
       on a black cell, turn left, flip cell white, move forward.
After ~10,000 steps of apparent chaos, the ant builds a periodic "highway" forever.
"""

GRID_SIZE = 100
WHITE, BLACK = 0, 1
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W

def run_ant(steps=12000):
    grid = [[WHITE] * GRID_SIZE for _ in range(GRID_SIZE)]
    x, y = GRID_SIZE // 2, GRID_SIZE // 2
    direction = 0  # facing North

    for step in range(steps):
        cell = grid[x][y]
        if cell == WHITE:
            direction = (direction + 1) % 4   # turn right
        else:
            direction = (direction - 1) % 4   # turn left
        grid[x][y] = 1 - cell                 # flip
        dx, dy = DIRS[direction]
        x = (x + dx) % GRID_SIZE
        y = (y + dy) % GRID_SIZE

        if step in (100, 1000, 5000, 11999):
            black_cells = sum(cell for row in grid for cell in row)
            print(f"Step {step+1:6d}: {black_cells} black cells, ant at ({x},{y})")

    return grid

if __name__ == "__main__":
    print("Running Langton's Ant...")
    final_grid = run_ant()
    print("Done. The highway emerges from chaos around step 10,000.")
