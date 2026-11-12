"""Collatz conjecture visualizer — takes any positive integer and applies
3n+1 (if odd) or n/2 (if even) until it reaches 1. Always reaches 1... probably."""

def collatz(n):
    sequence = [n]
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        sequence.append(n)
    return sequence

def visualize(sequence):
    peak = max(sequence)
    bar_max = 40
    for i, val in enumerate(sequence):
        bar = int(val / peak * bar_max)
        print(f"Step {i:3d}: {'█' * bar} {val}")

if __name__ == "__main__":
    n = 27  # famously long sequence
    seq = collatz(n)
    print(f"Collatz sequence for {n} — {len(seq)} steps, peak={max(seq)}\n")
    visualize(seq)
    print(f"\nFinal: {seq[-1]} ✓")
