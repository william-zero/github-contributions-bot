"""
Collatz Conjecture Explorer
Take any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat until you reach 1. The conjecture: you always reach 1. Never proven. Never disproven.
"""

def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def collatz_stats(n):
    seq = collatz(n)
    return {
        "start": n,
        "steps": len(seq) - 1,
        "peak": max(seq),
        "sequence": seq[:10],  # first 10 elements
    }

if __name__ == "__main__":
    test_numbers = [27, 871, 6171, 77031, 9780657631]
    print("Collatz Conjecture — stepping into the unknown\n")
    for n in test_numbers:
        stats = collatz_stats(n)
        print(f"  n={stats['start']:>12,} → {stats['steps']:>5} steps, peak={stats['peak']:>15,}")
    print("\nStill unsolved after 85+ years. Good luck, mathematicians.")
