# Conway's Game of Life - minimal one-liner edition

def step(board):
    rows, cols = len(board), len(board[0])
    def neighbors(r, c):
        return sum(board[r+dr][c+dc] for dr in [-1,0,1] for dc in [-1,0,1]
                   if (dr,dc)!=(0,0) and 0<=r+dr<rows and 0<=c+dc<cols)
    return [[1 if (board[r][c] and neighbors(r,c) in [2,3]) or
                  (not board[r][c] and neighbors(r,c)==3) else 0
             for c in range(cols)] for r in range(rows)]

def render(board):
    return '\n'.join(''.join('█' if cell else '·' for cell in row) for row in board)

# Glider pattern
glider = [
    [0,1,0,0,0],
    [0,0,1,0,0],
    [1,1,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

print("Generation 0:")
print(render(glider))
for gen in range(1, 5):
    glider = step(glider)
    print(f"\nGeneration {gen}:")
    print(render(glider))
