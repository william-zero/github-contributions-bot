"""
Collatz Conjecture Explorer
Take any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat. You always eventually reach 1. (We think. Nobody has proved it yet.)
"""

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def analyze(limit=100):
    results = []
    for n in range(1, limit + 1):
        seq = collatz_sequence(n)
        results.append((n, len(seq), max(seq)))
    return results

if __name__ == "__main__":
    print(f"{'Start':>6} | {'Steps':>6} | {'Peak':>10}")
    print("-" * 28)
    for start, steps, peak in analyze(20):
        print(f"{start:>6} | {steps:>6} | {peak:>10}")
    
    all_data = analyze(1000)
    hardest = max(all_data, key=lambda x: x[1])
    print(f"\nHardest journey (1-1000): {hardest[0]} takes {hardest[1]} steps, peaks at {hardest[2]}")
