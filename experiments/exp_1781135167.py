# Collatz Conjecture Explorer
# The simplest unsolved problem in mathematics

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

def find_longest_sequence(limit):
    max_steps = 0
    champion = 1
    for i in range(1, limit + 1):
        steps = collatz_steps(i)
        if steps > max_steps:
            max_steps = steps
            champion = i
    return champion, max_steps

print("Collatz Conjecture: n -> n/2 (even) or 3n+1 (odd), always reaches 1")
print("...at least, no counterexample has ever been found!\n")

for n in [6, 27, 871, 9780657631]:
    try:
        steps = collatz_steps(n)
        print(f"  {n:>15,} takes {steps:>4} steps")
    except RecursionError:
        print(f"  {n} is too big for this naive implementation")

champion, steps = find_longest_sequence(1000)
print(f"\nLongest chain under 1000: starts at {champion} ({steps} steps)")
