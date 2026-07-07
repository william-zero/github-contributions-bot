# A simulation of the Monty Hall problem
import random

def monty_hall(switch):
    doors = [0, 1, 2]
    car = random.choice(doors)
    chosen = random.choice(doors)
    # Host opens a goat door (not chosen, not the car)
    remaining = [d for d in doors if d != chosen and d != car]
    host_opens = random.choice(remaining)
    # The door you can switch to
    switch_to = [d for d in doors if d != chosen and d != host_opens][0]
    final = switch_to if switch else chosen
    return final == car

trials = 10_000
stay_wins = sum(monty_hall(switch=False) for _ in range(trials))
switch_wins = sum(monty_hall(switch=True) for _ in range(trials))

print(f"Stay win rate:   {stay_wins / trials:.1%}  (expected ~33.3%)")
print(f"Switch win rate: {switch_wins / trials:.1%}  (expected ~66.7%)")
print("Lesson: always switch. Always.")
