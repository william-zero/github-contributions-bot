"""Collatz conjecture explorer — visualizes sequence lengths."""

def collatz_length(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

def find_champion(limit):
    """Find the number under `limit` with the longest Collatz sequence."""
    champion = max(range(1, limit + 1), key=collatz_length)
    return champion, collatz_length(champion)

if __name__ == "__main__":
    for limit in [100, 1000, 10_000]:
        num, length = find_champion(limit)
        bar = "█" * (length // 10)
        print(f"Under {limit:>6}: {num:>5} takes {length:>4} steps  {bar}")
