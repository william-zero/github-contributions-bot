"""
Collatz Conjecture Explorer
Pick any positive integer. If even, halve it. If odd, triple it and add 1.
Repeat. The conjecture says you'll always eventually reach 1.
Nobody has proven it yet, but it holds for every number tried so far.
"""

def collatz_sequence(n):
    """Return the full Collatz sequence starting from n."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def collatz_stats(n):
    seq = collatz_sequence(n)
    return {
        "start": n,
        "steps": len(seq) - 1,
        "peak": max(seq),
        "sequence": seq,
    }

def find_longest_below(limit):
    """Find the number below limit with the longest Collatz sequence."""
    return max(range(1, limit), key=lambda n: len(collatz_sequence(n)))

if __name__ == "__main__":
    for start in [6, 27, 871, 6171]:
        stats = collatz_stats(start)
        print(f"n={stats['start']:>6}: {stats['steps']:>4} steps, peak={stats['peak']}")

    champion = find_longest_below(1000)
    print(f"\nLongest sequence below 1000: n={champion} ({len(collatz_sequence(champion))-1} steps)")
