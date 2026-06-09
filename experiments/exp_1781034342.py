# Rock Paper Scissors with a twist: Lizard & Spock!
import random

MOVES = ["rock", "paper", "scissors", "lizard", "spock"]

BEATS = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

def play(player, computer):
    if player == computer:
        return "tie"
    return "win" if computer in BEATS[player] else "loss"

def run_simulation(rounds=1000):
    results = {"win": 0, "loss": 0, "tie": 0}
    for _ in range(rounds):
        player = random.choice(MOVES)
        computer = random.choice(MOVES)
        results[play(player, computer)] += 1
    total = sum(results.values())
    print(f"Simulation over {total} rounds:")
    for outcome, count in results.items():
        print(f"  {outcome}: {count} ({count/total*100:.1f}%)")

if __name__ == "__main__":
    run_simulation()
