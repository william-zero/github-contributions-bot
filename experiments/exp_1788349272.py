# Conway's Game of Life - single generation step
def step(board):
    rows, cols = len(board), len(board[0])
    new_board = [[0]*cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            neighbors = sum(
                board[r+dr][c+dc]
                for dr in [-1, 0, 1]
                for dc in [-1, 0, 1]
                if (dr, dc) != (0, 0)
                and 0 <= r+dr < rows
                and 0 <= c+dc < cols
            )
            alive = board[r][c]
            if alive and neighbors in (2, 3):
                new_board[r][c] = 1
            elif not alive and neighbors == 3:
                new_board[r][c] = 1
    return new_board

def render(board):
    return '\n'.join(''.join('█' if c else '·' for c in row) for row in board)

if __name__ == "__main__":
    # Glider pattern
    glider = [
        [0,1,0,0,0],
        [0,0,1,0,0],
        [1,1,1,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    print("Gen 0:")
    print(render(glider))
    for gen in range(1, 4):
        glider = step(glider)
        print(f"\nGen {gen}:")
        print(render(glider))
