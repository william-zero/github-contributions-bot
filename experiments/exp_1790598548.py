"""
Mood Ring Commit Analyzer
Detects the emotional state of a repository based on commit message sentiment.
"""

import random
from datetime import datetime

WEEKDAY_MOODS = {
    0: ("Monday", "reluctant", "why do we even have repos"),
    1: ("Tuesday", "cautiously optimistic", "maybe this PR will get reviewed"),
    2: ("Wednesday", "existentially neutral", "it is what it is"),
    3: ("Thursday", "pre-weekend anxious", "must ship before Friday 5pm"),
    4: ("Friday", "chaotically hopeful", "YOLO pushing to main"),
    5: ("Saturday", "regretfully coding", "why am I doing this"),
    6: ("Sunday", "dreading tomorrow", "one last commit I promise"),
}

def get_mood():
    day = datetime.now().weekday()
    day_name, mood, commit_vibe = WEEKDAY_MOODS[day]
    return {
        "day": day_name,
        "mood": mood,
        "suggested_commit_prefix": commit_vibe,
        "energy_level": random.randint(1, 10),
        "coffee_cups_needed": max(1, (7 - day) % 5 + 1),
    }

def analyze_commit_message(msg):
    """Returns the emotional weight of a commit message."""
    red_flags = ["fix", "hotfix", "urgent", "broken", "oops", "revert"]
    green_flags = ["feat", "add", "improve", "refactor", "clean"]
    
    msg_lower = msg.lower()
    if any(flag in msg_lower for flag in red_flags):
        return "🚨 Distress signal detected"
    elif any(flag in msg_lower for flag in green_flags):
        return "✨ Genuine progress vibes"
    else:
        return "😶 Inscrutably neutral"

if __name__ == "__main__":
    mood = get_mood()
    print(f"Today is {mood['day']}. You are feeling: {mood['mood']}.")
    print(f"Suggested energy level: {mood['energy_level']}/10")
    print(f"Required coffee: {mood['coffee_cups_needed']} cups")
    print(f"Vibe check: {mood['suggested_commit_prefix']}")
    print()
    test_messages = ["fix: stop everything from exploding", "feat: add cool new thing", "chore: stuff"]
    for msg in test_messages:
        print(f"  '{msg}' → {analyze_commit_message(msg)}")
