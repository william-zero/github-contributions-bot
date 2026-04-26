"""
cellular automaton: rule 110
rule 110 is turing complete — complex behavior from dead-simple rules.
"""

WIDTH = 60
STEPS = 30
RULE = 110

def step(row):
    n = len(row)
    new = [0] * n
    for i in range(n):
        left  = row[(i - 1) % n]
        center = row[i]
        right = row[(i + 1) % n]
        pattern = (left << 2) | (center << 1) | right
        new[i] = (RULE >> pattern) & 1
    return new

row = [0] * WIDTH
row[WIDTH // 2] = 1

for _ in range(STEPS):
    print(''.join('█' if c else ' ' for c in row))
    row = step(row)
