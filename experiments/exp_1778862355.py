# Sierpinski triangle generator using ASCII art
import sys

def sierpinski(n):
    if n == 0:
        return ["*"]
    smaller = sierpinski(n - 1)
    width = len(smaller[-1])
    top = [" " * (width // 2 + 1) + row + " " * (width // 2 + 1) for row in smaller]
    bottom = [row + " " + row for row in smaller]
    return top + bottom

def draw(n):
    triangle = sierpinski(n)
    for row in triangle:
        print(row)

if __name__ == "__main__":
    level = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    draw(level)
