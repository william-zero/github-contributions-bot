"""
Collatz conjecture visualizer — because math is beautiful and unsolved
"""

def collatz(n):
    steps = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps.append(n)
    return steps

def visualize(n, width=60):
    seq = collatz(n)
    peak = max(seq)
    print(f"n={n}  steps={len(seq)-1}  peak={peak}")
    for val in seq:
        bar_len = int(val / peak * width)
        print(f"{val:6d} | {'█' * bar_len}")

if __name__ == "__main__":
    for start in [27, 97, 871]:
        visualize(start)
        print()
