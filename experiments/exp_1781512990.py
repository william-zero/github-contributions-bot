"""
coin_flip_streak.py — how long until you flip 10 heads in a row?
"""
import random

def heads_streak_run(target=10, trials=10_000):
    streaks = []
    for _ in range(trials):
        streak = best = 0
        flips = 0
        while best < target:
            flips += 1
            if random.random() < 0.5:
                streak += 1
                best = max(best, streak)
            else:
                streak = 0
        streaks.append(flips)
    avg = sum(streaks) / len(streaks)
    print(f"Average flips to get {target} heads in a row: {avg:.1f}")
    print(f"Theoretical: {2 ** (target + 1) - 2} flips")
    print(f"Min: {min(streaks)}, Max: {max(streaks)}")

if __name__ == "__main__":
    heads_streak_run()
