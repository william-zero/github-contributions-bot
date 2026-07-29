"""
Birthday paradox simulator — how many people until two share a birthday?
"""
import random

def simulate(people: int, trials: int = 10000) -> float:
    hits = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            hits += 1
    return hits / trials

print("Birthday Paradox Probability Table")
print(f"{'People':>8}  {'Probability':>12}")
print("-" * 24)
for n in [10, 20, 23, 30, 40, 50, 57, 70, 100]:
    prob = simulate(n)
    print(f"{n:>8}  {prob:>11.1%}")
