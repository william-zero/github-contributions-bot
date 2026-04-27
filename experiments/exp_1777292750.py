"""Collatz conjecture explorer — pick a number, see how long until you reach 1."""

def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

for n in range(1, 21):
    print(f"{n:3d} → {collatz_steps(n):3d} steps")
