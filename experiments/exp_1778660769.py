# Conway's Game of Life — infinite grid simulation with pattern library

from collections import defaultdict

def neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                yield x + dx, y + dy

def step(cells):
    neighbor_count = defaultdict(int)
    for (x, y) in cells:
        for nb in neighbors(x, y):
            neighbor_count[nb] += 1
    return {pos for pos, count in neighbor_count.items()
            if count == 3 or (count == 2 and pos in cells)}

def render(cells, size=20):
    if not cells:
        print("<empty>")
        return
    xs = [x for x, _ in cells]
    ys = [y for _, y in cells]
    cx, cy = sum(xs) // len(xs), sum(ys) // len(ys)
    half = size // 2
    rows = []
    for dy in range(-half, half):
        row = ""
        for dx in range(-half, half):
            row += "█" if (cx + dx, cy + dy) in cells else "·"
        rows.append(row)
    print("\n".join(rows))

PATTERNS = {
    "glider": {(1,0),(2,1),(0,2),(1,2),(2,2)},
    "blinker": {(0,1),(1,1),(2,1)},
    "block": {(0,0),(1,0),(0,1),(1,1)},
    "r_pentomino": {(1,0),(2,0),(0,1),(1,1),(1,2)},
    "beacon": {(0,0),(1,0),(0,1),(2,2),(3,2),(2,3),(3,3)},
}

def run(pattern_name, generations=10):
    cells = PATTERNS.get(pattern_name, PATTERNS["glider"])
    print(f"\n=== {pattern_name} — gen 0 ===")
    render(cells)
    for gen in range(1, generations + 1):
        cells = step(cells)
        if gen % 5 == 0 or gen == generations:
            print(f"\n=== gen {gen} (pop: {len(cells)}) ===")
            render(cells)

if __name__ == "__main__":
    for name in ["glider", "r_pentomino", "beacon"]:
        run(name, generations=15)
