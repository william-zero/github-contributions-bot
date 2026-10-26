"""
Collatz conjecture explorer — generates sequences for any starting number.
The Collatz conjecture: starting from any positive integer n,
if n is even divide by 2, if odd multiply by 3 and add 1.
The conjecture claims this always reaches 1. Still unproven!
"""


def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def find_longest_below(limit):
    best_start, best_len = 1, 1
    for i in range(2, limit):
        length = len(collatz_sequence(i))
        if length > best_len:
            best_len, best_start = length, i
    return best_start, best_len


if __name__ == "__main__":
    for start in [6, 27, 100, 871]:
        seq = collatz_sequence(start)
        print(f"n={start}: {len(seq)} steps | peak={max(seq)}")

    print("\nLongest Collatz sequence under 1000:")
    n, steps = find_longest_below(1000)
    print(f"  Starting number: {n}, Steps: {steps}")
