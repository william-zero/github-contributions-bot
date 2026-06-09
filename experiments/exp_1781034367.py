"""
Cellular Automaton Rain - Rule 30 vertical rain simulation
Generates animated ASCII rain using Rule 30 (chaotic) cellular automata
"""

def rule30_step(row):
    n = len(row)
    new_row = []
    for i in range(n):
        left = row[(i - 1) % n]
        center = row[i]
        right = row[(i + 1) % n]
        pattern = (left << 2) | (center << 1) | right
        new_row.append((30 >> pattern) & 1)
    return new_row

def render(rows, width=60):
    chars = {0: ' ', 1: '|'}
    for row in rows:
        print(''.join(chars[c] for c in row))

if __name__ == '__main__':
    import random
    width = 60
    depth = 20
    seed = [random.randint(0, 1) for _ in range(width)]
    history = [seed]
    for _ in range(depth - 1):
        history.append(rule30_step(history[-1]))
    render(history)
    print(f"\nRule 30 rain — {width}x{depth} — chaos from simple rules!")
