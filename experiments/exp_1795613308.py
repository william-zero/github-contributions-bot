"""
Collatz Conjecture Explorer
Every positive integer eventually reaches 1 when you:
  - If even: divide by 2
  - If odd: multiply by 3 and add 1
Nobody has proven WHY this always works. It just... does.
"""

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def find_most_steps(limit=1000):
    best = max(range(1, limit + 1), key=lambda n: len(collatz_sequence(n)))
    seq = collatz_sequence(best)
    print(f"Among 1-{limit}, {best} takes the most steps: {len(seq) - 1}")
    print(f"Highest value reached: {max(seq)}")
    print(f"First 10 steps: {seq[:10]}...")

find_most_steps()
