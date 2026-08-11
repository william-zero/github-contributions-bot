# Cellular automaton explorer — Rule 30, 90, 110, etc.
import sys

def apply_rule(cells, rule_num):
    rule = f"{rule_num:08b}"
    patterns = {
        (1,1,1): int(rule[0]),
        (1,1,0): int(rule[1]),
        (1,0,1): int(rule[2]),
        (1,0,0): int(rule[3]),
        (0,1,1): int(rule[4]),
        (0,1,0): int(rule[5]),
        (0,0,1): int(rule[6]),
        (0,0,0): int(rule[7]),
    }
    n = len(cells)
    return [patterns[(cells[(i-1)%n], cells[i], cells[(i+1)%n])] for i in range(n)]

def display(cells):
    return "".join("█" if c else " " for c in cells)

def run(rule_num=30, width=79, steps=40):
    cells = [0] * width
    cells[width // 2] = 1
    print(f"Rule {rule_num}:")
    for _ in range(steps):
        print(display(cells))
        cells = apply_rule(cells, rule_num)

if __name__ == "__main__":
    rule = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    run(rule_num=rule)
