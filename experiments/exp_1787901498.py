# The Monty Hall Problem Simulator
import random

def monty_hall(switch=True, trials=10000):
    wins = 0
    for _ in range(trials):
        doors = [0, 0, 1]  # 0=goat, 1=car
        random.shuffle(doors)
        pick = random.randint(0, 2)
        # Host opens a goat door (not the player's pick, not the car)
        available = [i for i in range(3) if i != pick and doors[i] == 0]
        host_opens = random.choice(available)
        if switch:
            new_pick = [i for i in range(3) if i != pick and i != host_opens][0]
            if doors[new_pick] == 1:
                wins += 1
        else:
            if doors[pick] == 1:
                wins += 1
    return wins / trials

stay_rate = monty_hall(switch=False)
switch_rate = monty_hall(switch=True)
print(f"Stay strategy:   {stay_rate:.1%} win rate  (expected ~33%)")
print(f"Switch strategy: {switch_rate:.1%} win rate  (expected ~67%)")
print("The math doesn't lie — always switch!")
