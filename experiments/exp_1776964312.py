"""Generates Pascal's triangle up to N rows and finds fun patterns."""

def pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def find_fibonacci(triangle):
    """Fibonacci numbers hide in the shallow diagonals of Pascal's triangle."""
    fibs = []
    for d in range(len(triangle)):
        total = 0
        r, c = d, 0
        while r >= 0 and c < len(triangle[r]):
            total += triangle[r][c]
            r -= 1
            c += 1
        fibs.append(total)
    return fibs

if __name__ == "__main__":
    t = pascals_triangle(10)
    for row in t:
        print(" ".join(str(x).center(4) for x in row))
    print("\nFibonacci sequence hidden in diagonals:", find_fibonacci(t)[:10])
