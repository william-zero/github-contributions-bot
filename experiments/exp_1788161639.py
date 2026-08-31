"""
Collatz Conjecture Explorer
Take any positive integer. If even: divide by 2. If odd: multiply by 3 and add 1.
Repeat. Does it always reach 1? Nobody knows for sure, but it always does in practice.
"""

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

longest = max(range(1, 1001), key=collatz_steps)
print(f"Number with most steps (1-1000): {longest} → {collatz_steps(longest)} steps")

# Print sequence for 27 (famously long)
n = 27
seq = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    seq.append(n)
print(f"\n27's journey: {len(seq)} steps, peaks at {max(seq)}")
print(f"First 20 values: {seq[:20]}")
