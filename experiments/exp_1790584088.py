"""
Collatz Conjecture Explorer
Take any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
Repeat until you reach 1. Nobody knows why this always works (but it seems to).
"""

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

top_n = sorted(range(1, 1001), key=collatz_steps, reverse=True)[:10]
print("Top 10 numbers under 1000 by Collatz sequence length:")
for num in top_n:
    print(f"  {num}: {collatz_steps(num)} steps")
