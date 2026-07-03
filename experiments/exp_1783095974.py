"""
Collatz Conjecture Explorer

The Collatz conjecture: take any positive integer.
If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat. The conjecture says you always reach 1.
Nobody has proved it. Nobody has disproved it.
It is one of the most frustratingly simple unsolved problems in math.
"""

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


def find_high_flyers(limit=1000):
    """Find numbers that take the most steps to reach 1."""
    results = [(n, collatz_steps(n)) for n in range(1, limit + 1)]
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:10]


def collatz_path(n):
    path = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        path.append(n)
    return path


if __name__ == "__main__":
    print("Top 10 numbers under 1000 by Collatz step count:")
    for num, steps in find_high_flyers():
        print(f"  {num:4d} → {steps} steps")

    print("\nCollatz path for 27 (notorious long one):")
    path = collatz_path(27)
    print(f"  Length: {len(path)} steps, Peak: {max(path)}")
    print(f"  First 15: {path[:15]}")
