# Number spiral: fills a grid in a clockwise spiral pattern

def spiral(n):
    grid = [[0]*n for _ in range(n)]
    num, top, bottom, left, right = 1, 0, n-1, 0, n-1
    while top <= bottom and left <= right:
        for c in range(left, right+1): grid[top][c] = num; num += 1
        top += 1
        for r in range(top, bottom+1): grid[r][right] = num; num += 1
        right -= 1
        for c in range(right, left-1, -1): grid[bottom][c] = num; num += 1
        bottom -= 1
        for r in range(bottom, top-1, -1): grid[r][left] = num; num += 1
        left += 1
    return grid

def print_spiral(n):
    g = spiral(n)
    w = len(str(n*n))
    for row in g:
        print(" ".join(str(x).rjust(w) for x in row))

if __name__ == "__main__":
    for size in [4, 5, 6]:
        print(f"\n{size}x{size} spiral:")
        print_spiral(size)
