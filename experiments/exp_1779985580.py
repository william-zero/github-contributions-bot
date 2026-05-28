"""
Collatz conjecture explorer — does every number eventually reach 1?
Nobody has proven it, but it works for every number ever tested.
"""


def collatz(n):
    steps = []
    while n != 1:
        steps.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps.append(1)
    return steps


def find_longest(limit):
    best_n, best_len = 1, 1
    for n in range(2, limit + 1):
        length = len(collatz(n))
        if length > best_len:
            best_n, best_len = n, length
    return best_n, best_len


if __name__ == "__main__":
    print("Collatz Conjecture Explorer")
    print("=" * 40)

    for start in [6, 27, 871, 6171]:
        seq = collatz(start)
        print(f"  {start:>5} → {len(seq):>4} steps  (peak: {max(seq)})")

    print()
    champ_n, champ_len = find_longest(10_000)
    print(f"Longest under 10,000: n={champ_n} at {champ_len} steps")
    print("Still no proof it always ends. Sleep tight.")
