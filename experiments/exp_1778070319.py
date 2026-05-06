# Towers of Hanoi with move counter and ASCII visualization

def hanoi(n, source, target, auxiliary, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
        return moves
    hanoi(n - 1, source, auxiliary, target, moves)
    moves.append((source, target))
    hanoi(n - 1, auxiliary, target, source, moves)
    return moves

def render(pegs, n):
    width = n * 2 + 1
    lines = []
    for level in range(n, 0, -1):
        row = []
        for peg in ['A', 'B', 'C']:
            disk = pegs[peg][level - 1] if level <= len(pegs[peg]) else 0
            if disk:
                block = '#' * (disk * 2 - 1)
                row.append(block.center(width))
            else:
                row.append('|'.center(width))
        lines.append('  '.join(row))
    lines.append('  '.join(['=' * width] * 3))
    lines.append('  '.join([' A '.center(width), ' B '.center(width), ' C '.center(width)]))
    return '\n'.join(lines)

def solve(n):
    pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    moves = hanoi(n, 'A', 'C', 'B')
    print(f"Solving Towers of Hanoi with {n} disks ({len(moves)} moves)\n")
    print(render(pegs, n))
    for i, (src, dst) in enumerate(moves):
        disk = pegs[src].pop()
        pegs[dst].append(disk)
        print(f"\nMove {i + 1}: disk {disk} from {src} → {dst}")
        print(render(pegs, n))
    print(f"\nDone! Solved in {len(moves)} moves (minimum possible: {2**n - 1})")

if __name__ == '__main__':
    solve(3)
