"""Pascal's triangle generator — prints n rows."""

def pascals_triangle(n):
    row = [1]
    for i in range(n):
        print(' '.join(map(str, row)).center(n * 3))
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]

pascals_triangle(10)
