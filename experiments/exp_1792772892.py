"""Rock Paper Scissors tournament simulator."""
import random

MOVES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def play(a, b):
    if a == b: return "tie"
    return "win" if BEATS[a] == b else "loss"

def simulate_tournament(players=8, rounds=100):
    results = {p: {"wins": 0, "losses": 0, "ties": 0} for p in range(players)}
    for _ in range(rounds):
        p1, p2 = random.sample(range(players), 2)
        m1, m2 = random.choice(MOVES), random.choice(MOVES)
        outcome = play(m1, m2)
        if outcome == "win":
            results[p1]["wins"] += 1
            results[p2]["losses"] += 1
        elif outcome == "loss":
            results[p1]["losses"] += 1
            results[p2]["wins"] += 1
        else:
            results[p1]["ties"] += 1
            results[p2]["ties"] += 1
    return results

if __name__ == "__main__":
    standings = simulate_tournament()
    ranked = sorted(standings.items(), key=lambda x: x[1]["wins"], reverse=True)
    print("=== RPS Tournament Results ===")
    for rank, (player, stats) in enumerate(ranked, 1):
        print(f"{rank}. Player {player}: {stats['wins']}W {stats['losses']}L {stats['ties']}T")
