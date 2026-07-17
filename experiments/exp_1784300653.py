"""
Pascal's Triangle — with a twist: highlight multiples of a chosen number.
"""

def pascals_triangle(rows=8, highlight=3):
    triangle = []
    for n in range(rows):
        row = [1] * (n + 1)
        for k in range(1, n):
            row[k] = triangle[n-1][k-1] + triangle[n-1][k]
        triangle.append(row)

    for row in triangle:
        parts = []
        for val in row:
            cell = f"[{val:3d}]" if val % highlight == 0 else f" {val:3d} "
            parts.append(cell)
        print("  " * (rows - len(row)) + " ".join(parts))

if __name__ == "__main__":
    print("Pascal's Triangle — multiples of 3 are bracketed:\n")
    pascals_triangle(rows=9, highlight=3)
