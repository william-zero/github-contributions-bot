# Collatz Conjecture explorer
# Start with any positive integer n:
# If n is even, divide by 2. If odd, multiply by 3 and add 1.
# Conjecture: you always eventually reach 1.

def collatz_steps(n):
    steps = []
    while n != 1:
        steps.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    steps.append(1)
    return steps

def collatz_stats(n):
    path = collatz_steps(n)
    return {
        "start": n,
        "steps": len(path) - 1,
        "max_value": max(path),
        "path_preview": path[:8],
    }

# Find the number under 1000 with the longest Collatz sequence
longest = max(range(1, 1001), key=lambda n: len(collatz_steps(n)))
stats = collatz_stats(longest)

print(f"Collatz Conjecture Explorer")
print(f"{'='*40}")
print(f"Most stubborn number under 1000: {longest}")
print(f"  Steps to reach 1: {stats['steps']}")
print(f"  Peak value: {stats['max_value']:,}")
print(f"  Path preview: {stats['path_preview']}...")
print()

# Show some interesting starting numbers
for n in [27, 97, 871, 6171]:
    s = collatz_stats(n)
    print(f"n={n:>5}: {s['steps']:>3} steps, peaks at {s['max_value']:>8,}")
