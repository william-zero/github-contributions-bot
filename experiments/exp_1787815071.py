"""
Monty Hall Problem Simulator
The classic probability paradox that breaks brains at dinner parties.
"""
import random

def monty_hall_sim(trials=10000, switch=True):
    """Simulate the Monty Hall problem and count wins."""
    wins = 0
    for _ in range(trials):
        doors = [0, 1, 2]
        car_door = random.choice(doors)
        contestant_pick = random.choice(doors)

        # Host opens a goat door (not the car, not contestant's pick)
        remaining = [d for d in doors if d != contestant_pick and d != car_door]
        host_opens = random.choice(remaining)

        if switch:
            # Switch to the other remaining door
            new_pick = [d for d in doors if d != contestant_pick and d != host_opens][0]
            if new_pick == car_door:
                wins += 1
        else:
            if contestant_pick == car_door:
                wins += 1

    return wins / trials

if __name__ == "__main__":
    switch_rate = monty_hall_sim(switch=True)
    stay_rate = monty_hall_sim(switch=False)
    print(f"Win rate when switching: {switch_rate:.1%}")
    print(f"Win rate when staying:   {stay_rate:.1%}")
    print(f"\nSwitching wins {switch_rate/stay_rate:.1f}x more often.")
    print("Math is correct. Your intuition is wrong. Accept it.")
