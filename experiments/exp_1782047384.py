# Collatz conjecture visualizer - for any n, 3n+1 if odd, n/2 if even, repeat
# Math says you always reach 1. No one has proven why. It's maddening.

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        seq.append(n)
    return seq

def collatz_stopping_time(n):
    count = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        count += 1
    return count

# Find which numbers under 1000 take the longest to reach 1
champions = sorted(range(1, 1001), key=collatz_stopping_time, reverse=True)[:5]

print("Top 5 Collatz marathon runners (under 1000):")
for n in champions:
    steps = collatz_stopping_time(n)
    peak = max(collatz_sequence(n))
    print(f"  n={n}: {steps} steps, peaks at {peak:,}")

# Fun: the sequence for 27 reaches 9232 before crashing back down
seq27 = collatz_sequence(27)
print(f"\n27's wild ride: {len(seq27)} steps, peaks at {max(seq27):,}")
print(f"First 10 values: {seq27[:10]}")
