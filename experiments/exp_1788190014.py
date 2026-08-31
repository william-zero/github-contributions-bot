"""
Collatz conjecture visualizer - tracks the hailstone sequence for any number
"""

def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def sparkline(values, width=60):
    bars = " ▁▂▃▄▅▆▇█"
    lo, hi = min(values), max(values)
    if lo == hi:
        return bars[1] * min(len(values), width)
    scaled = [int((v - lo) / (hi - lo) * (len(bars) - 1)) for v in values]
    return ''.join(bars[s] for s in scaled[:width])

if __name__ == "__main__":
    test_numbers = [27, 97, 871, 6171]
    for n in test_numbers:
        seq = collatz(n)
        print(f"n={n:6d} | steps={len(seq):4d} | peak={max(seq):8d} | {sparkline(seq)}")
