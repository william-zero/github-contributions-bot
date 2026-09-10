"""Collatz conjecture explorer - pick any number, keep applying the rule, always reach 1."""

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def find_longest_collatz(limit):
    longest = max(range(1, limit + 1), key=lambda n: len(collatz_sequence(n)))
    return longest, collatz_sequence(longest)

if __name__ == "__main__":
    for test in [27, 871, 6171]:
        seq = collatz_sequence(test)
        print(f"n={test}: {len(seq)} steps, max value reached: {max(seq):,}")

    champion, seq = find_longest_collatz(1000)
    print(f"\nLongest under 1000: n={champion} with {len(seq)} steps")
    print(f"First 10 values: {seq[:10]}")
