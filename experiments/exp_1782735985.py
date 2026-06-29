"""
Collatz conjecture explorer.
Pick any positive integer. If even, halve it. If odd, triple it and add one.
Repeat. The conjecture: you always eventually reach 1.
Nobody has proved it. Nobody has found a counterexample.
"""

def collatz(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

def stopping_time(n):
    return len(collatz(n)) - 1

# Find the number under 1000 with the longest stopping time
longest = max(range(1, 1001), key=stopping_time)
seq = collatz(longest)

print(f"Most stubborn number under 1000: {longest}")
print(f"Stopping time: {stopping_time(longest)} steps")
print(f"Peak value reached: {max(seq):,}")
print(f"First 15 steps: {seq[:15]}")

# Distribution of stopping times
import collections
stops = collections.Counter(stopping_time(n) % 10 for n in range(1, 10001))
print("\nStopping time mod 10 distribution (1-10000):")
for k in sorted(stops):
    print(f"  mod {k}: {'█' * (stops[k] // 50)} ({stops[k]})")
