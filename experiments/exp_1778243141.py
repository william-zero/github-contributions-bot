"""
Collatz Conjecture Explorer
Pick any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat. The conjecture says you'll always reach 1. Nobody has proven it yet.
"""

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def find_longest_sequences(limit=100):
    results = []
    for i in range(1, limit + 1):
        seq = collatz_sequence(i)
        results.append((i, len(seq), max(seq)))
    return sorted(results, key=lambda x: x[1], reverse=True)[:10]

if __name__ == "__main__":
    print("Top 10 longest Collatz sequences (1–100):")
    print(f"{'Start':>6}  {'Steps':>6}  {'Peak':>10}")
    print("-" * 28)
    for start, steps, peak in find_longest_sequences():
        print(f"{start:>6}  {steps:>6}  {peak:>10}")

    print("\nSequence for 27 (famous for its length):")
    seq = collatz_sequence(27)
    print(f"Steps: {len(seq)}, Peak: {max(seq)}")
    print(seq[:10], "...", seq[-5:])
