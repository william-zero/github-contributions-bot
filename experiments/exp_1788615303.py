"""
Cellular automaton: Rule 30
Wolfram's Rule 30 is a 1D cellular automaton that produces surprisingly complex,
seemingly random patterns from a single starting cell. It's used as a pseudorandom
number generator in Mathematica.
"""

def rule30(cells, width):
    new_cells = [0] * width
    for i in range(width):
        left = cells[(i - 1) % width]
        center = cells[i]
        right = cells[(i + 1) % width]
        pattern = (left << 2) | (center << 1) | right
        new_cells[i] = (30 >> pattern) & 1
    return new_cells

def display(cells):
    return ''.join('█' if c else ' ' for c in cells)

width = 61
cells = [0] * width
cells[width // 2] = 1

print("Rule 30 Cellular Automaton:")
for _ in range(30):
    print(display(cells))
    cells = rule30(cells, width)
