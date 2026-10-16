# Fun experiment: The Birthday Paradox simulator
import random

def birthday_paradox_simulation(people, trials=10000):
    """Simulate the birthday paradox. Spoiler: it's weirder than you think."""
    collisions = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(people)]
        if len(birthdays) != len(set(birthdays)):
            collisions += 1
    probability = collisions / trials * 100
    return probability

print("The Birthday Paradox: When does sharing a birthday become likely?")
print("=" * 55)
for n in [10, 20, 23, 30, 40, 50, 57, 70]:
    prob = birthday_paradox_simulation(n)
    bar = "█" * int(prob / 2)
    print(f"  {n:2d} people: {prob:5.1f}%  {bar}")

print("\nFun fact: With just 23 people, there's >50% chance of a shared birthday!")
print("Math is wild. Statistics is wilder.")
