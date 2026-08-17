"""
Rock Paper Scissors with win rate tracker.
"""
import random

MOVES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


def play_round(human_move):
    bot_move = random.choice(MOVES)
    if human_move == bot_move:
        result = "tie"
    elif BEATS[human_move] == bot_move:
        result = "win"
    else:
        result = "lose"
    return bot_move, result


def simulate(n=1000):
    wins = losses = ties = 0
    for _ in range(n):
        _, result = play_round(random.choice(MOVES))
        if result == "win":
            wins += 1
        elif result == "lose":
            losses += 1
        else:
            ties += 1
    print(f"After {n} rounds: W={wins} L={losses} T={ties}")
    print(f"Win rate: {wins/n*100:.1f}%  (expected ~33.3%)")


if __name__ == "__main__":
    simulate()
