# The Birthday Paradox Simulator
# How many people does it take before two share a birthday?
# The answer (23) shocks everyone. Let's prove it empirically.

import random

def birthday_collision(group_size, trials=10000):
    """Estimate probability that at least 2 people share a birthday."""
    collisions = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(group_size)]
        if len(birthdays) != len(set(birthdays)):
            collisions += 1
    return collisions / trials

print("Birthday Paradox — simulated probabilities:")
print(f"{'Group Size':<12} {'Simulated %':<14} {'Expected %'}")
print("-" * 40)

import math
def expected_prob(n):
    p_no_collision = 1.0
    for k in range(n):
        p_no_collision *= (365 - k) / 365
    return 1 - p_no_collision

for n in [10, 20, 23, 30, 40, 50, 57, 70]:
    sim = birthday_collision(n, 5000)
    exp = expected_prob(n)
    marker = " ← >50% here!" if n == 23 else ""
    print(f"{n:<12} {sim*100:<14.1f} {exp*100:.1f}%{marker}")
