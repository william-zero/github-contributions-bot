# Collatz Conjecture Explorer
# Take any positive integer: if even, divide by 2; if odd, multiply by 3 and add 1.
# Repeat. The conjecture says you always reach 1. Nobody has proven it.

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

# Find numbers with surprisingly long journeys
longest = max(range(1, 1000), key=collatz_steps)
print(f"Among 1-999, {longest} takes the longest path: {collatz_steps(longest)} steps")

for n in [27, 703, 871]:
    print(f"  {n} → {collatz_steps(n)} steps")
