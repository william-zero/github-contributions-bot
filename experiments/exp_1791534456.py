# Collatz conjecture explorer — does every number eventually reach 1?
# Math says yes, nobody can prove it.

def collatz(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

champion = max(range(1, 10_001), key=collatz)
print(f"Most steps under 10000: {champion} takes {collatz(champion)} steps")
print("...and then it hits 1. Every. Single. Time.")
