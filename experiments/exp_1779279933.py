"""
Collatz Conjecture Explorer
Pick any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat until you reach 1. No one has proven you always reach 1 (but you always do).
"""

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def collatz_stats(limit=100):
    results = []
    for start in range(2, limit + 1):
        seq = collatz_sequence(start)
        results.append((start, len(seq), max(seq)))
    longest = max(results, key=lambda x: x[1])
    highest_peak = max(results, key=lambda x: x[2])
    print(f"Collatz sequences from 2 to {limit}:")
    print(f"  Longest path: starts at {longest[0]}, takes {longest[1]} steps")
    print(f"  Highest peak: starts at {highest_peak[0]}, reaches {highest_peak[2]:,}")
    print(f"\nSample journeys:")
    for n in [7, 27, 97]:
        seq = collatz_sequence(n)
        print(f"  {n}: {len(seq)} steps, peaks at {max(seq):,}")

if __name__ == "__main__":
    collatz_stats()
