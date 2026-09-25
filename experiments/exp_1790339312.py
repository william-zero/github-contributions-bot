"""
Cellular automaton: Rule 110.
One of only a handful of elementary cellular automata proven to be Turing-complete.
Wolfram called it. The universe agreed.
"""

def rule110(cells, steps=20, width=60):
    rows = []
    for _ in range(steps):
        rows.append(''.join('#' if c else '.' for c in cells))
        new_cells = [0] * width
        for i in range(width):
            left  = cells[(i - 1) % width]
            curr  = cells[i]
            right = cells[(i + 1) % width]
            pattern = (left << 2) | (curr << 1) | right
            # Rule 110 table: 01101110 in binary
            new_cells[i] = (110 >> pattern) & 1
        cells = new_cells
    return rows

width = 60
seed = [0] * width
seed[width // 2] = 1  # single live cell in the middle

for row in rule110(seed, steps=25, width=width):
    print(row)
