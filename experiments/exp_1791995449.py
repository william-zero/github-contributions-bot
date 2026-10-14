"""Collatz conjecture explorer: takes any positive integer, repeatedly apply
3n+1 if odd, n/2 if even, and you always reach 1. Nobody knows why."""

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        steps += 1
    return steps

top = sorted(range(1, 1001), key=collatz_steps, reverse=True)[:5]
print("Top 5 longest Collatz sequences under 1000:")
for n in top:
    print(f"  {n}: {collatz_steps(n)} steps")
