"""Collatz conjecture explorer — the sequence that nobody can prove terminates."""

def collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def find_longest(limit):
    best_n, best_len = 0, 0
    for n in range(1, limit + 1):
        length = len(collatz(n))
        if length > best_len:
            best_n, best_len = n, length
    return best_n, best_len


if __name__ == "__main__":
    seq = collatz(27)
    print(f"Collatz(27): {len(seq)} steps, peak={max(seq)}")
    print(f"First 10 values: {seq[:10]} ...")

    champion, steps = find_longest(1000)
    print(f"\nLongest under 1000: n={champion} takes {steps} steps")
