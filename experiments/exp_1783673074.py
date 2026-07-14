# Collatz conjecture visualizer
# Take any positive integer n:
#   if even: divide by 2
#   if odd:  multiply by 3, add 1
# Repeat until you reach 1. Always reaches 1 (we think...)

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def collatz_stats(n):
    seq = collatz_sequence(n)
    return {
        "start": n,
        "steps": len(seq) - 1,
        "peak": max(seq),
        "peak_at_step": seq.index(max(seq)),
    }

# Find the number under 1000 with the longest Collatz sequence
champion = max(range(1, 1001), key=lambda n: len(collatz_sequence(n)))
stats = collatz_stats(champion)

print(f"Champion under 1000: {champion}")
print(f"  Steps to reach 1: {stats['steps']}")
print(f"  Peak value:       {stats['peak']:,}")
print(f"  Peak at step:     {stats['peak_at_step']}")
print()

# A few interesting ones
for start in [27, 97, 871, 6171]:
    s = collatz_stats(start)
    print(f"n={s['start']:>6}: {s['steps']:>4} steps, peaks at {s['peak']:>10,}")
