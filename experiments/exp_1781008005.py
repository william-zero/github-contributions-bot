"""
Langton's Ant - emergent complexity from simple rules.
After ~10,000 steps, the ant builds an infinite highway.
"""

def run_langtons_ant(steps=11000, grid_size=100):
    # Grid: False=white, True=black
    grid = [[False] * grid_size for _ in range(grid_size)]
    
    # Directions: 0=up, 1=right, 2=down, 3=left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_chars = ["^", ">", "v", "<"]
    
    r, c = grid_size // 2, grid_size // 2
    facing = 0
    
    for step in range(steps):
        if grid[r][c]:  # black: turn left, flip to white
            facing = (facing - 1) % 4
            grid[r][c] = False
        else:           # white: turn right, flip to black
            facing = (facing + 1) % 4
            grid[r][c] = True
        
        dr, dc = directions[facing]
        r = (r + dr) % grid_size
        c = (c + dc) % grid_size
        
        if step in (100, 500, 1000, 5000, 10000, steps - 1):
            black = sum(sum(row) for row in grid)
            print(f"Step {step+1:6d}: {black} black cells, ant at ({r},{c}) facing {dir_chars[facing]}")
    
    # Print final 30x60 crop around ant
    print(f"\nFinal state (60x30 crop centered on ant):")
    for dr in range(-15, 15):
        row_str = ""
        for dc in range(-30, 30):
            nr, nc = (r + dr) % grid_size, (c + dc) % grid_size
            if nr == r and nc == c:
                row_str += dir_chars[facing]
            else:
                row_str += "█" if grid[nr][nc] else " "
        print(row_str)

if __name__ == "__main__":
    run_langtons_ant()
