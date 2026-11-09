"""
Collatz Conjecture Explorer
Take any positive integer: if even, divide by 2; if odd, multiply by 3 and add 1.
Repeat. It always reaches 1. (We think. Nobody has proven it.)
"""

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def collatz_stats(limit=100):
    longest = max(range(1, limit + 1), key=lambda n: len(collatz_sequence(n)))
    seq = collatz_sequence(longest)
    print(f"Among 1-{limit}, number {longest} has the longest Collatz sequence:")
    print(f"  Length: {len(seq)} steps")
    print(f"  Peak value: {max(seq)}")
    print(f"  First 10 steps: {seq[:10]}...")

if __name__ == "__main__":
    collatz_stats()
    collatz_stats(1000)
