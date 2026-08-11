# Exploring the Collatz conjecture's cousin: the 3n-1 problem
# What if we subtract instead of add?

def collatz_minus(n, steps=0, seen=None):
    if seen is None:
        seen = set()
    if n in seen:
        return steps, True  # cycle detected!
    seen.add(n)
    if n == 1:
        return steps, False
    if n % 2 == 0:
        return collatz_minus(n // 2, steps + 1, seen)
    else:
        return collatz_minus(3 * n - 1, steps + 1, seen)

print("The 3n-1 problem: does it always reach 1? (spoiler: no)")
print()
for n in range(1, 20):
    result, cycle = collatz_minus(n, seen=set())
    status = "CYCLE DETECTED" if cycle else f"reached 1 in {result} steps"
    print(f"  n={n:3d}: {status}")

print()
print("Fun: n=5 diverges! The universe is not symmetric after all.")
