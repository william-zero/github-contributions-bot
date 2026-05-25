# Pascal's triangle generator

def pascal(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def print_pascal(rows):
    t = pascal(rows)
    width = len(' '.join(str(x) for x in t[-1]))
    for row in t:
        line = ' '.join(str(x) for x in row)
        print(line.center(width))

def fibonacci_from_pascal(rows):
    t = pascal(rows)
    fibs = []
    for diag in range(rows):
        total = sum(t[diag + j][j] for j in range(diag + 1) if diag + j < rows and j < len(t[diag + j]))
        fibs.append(total)
    return fibs

print("Pascal's Triangle (10 rows):")
print_pascal(10)
print(f"\nFibonacci from diagonals: {fibonacci_from_pascal(12)}")
