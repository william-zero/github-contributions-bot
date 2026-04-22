# Cellular automaton: Rule 110 (known to be Turing complete!)
def rule110(cells, steps=10):
    width = len(cells)
    for step in range(steps):
        rule = [int(b) for b in f"{110:08b}"][::-1]
        new = [0] * width
        for i in range(width):
            left = cells[(i - 1) % width]
            center = cells[i]
            right = cells[(i + 1) % width]
            pattern = (left << 2) | (center << 1) | right
            new[i] = rule[pattern]
        line = "".join("█" if c else " " for c in cells)
        print(f"|{line}|")
        cells = new

seed = [0] * 39 + [1]
rule110(seed, steps=20)
