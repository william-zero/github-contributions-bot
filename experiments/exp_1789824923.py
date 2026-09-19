"""Weekend vibes: a tiny generative poem engine."""

import random

subjects = ["the fog", "a crow", "moonlight", "the tide", "silence"]
verbs = ["whispers", "drifts", "lingers", "remembers", "forgets"]
objects = ["old names", "salt air", "tomorrow's plans", "a half-read book", "the way home"]

def make_poem(lines=4):
    poem = []
    for _ in range(lines):
        s = random.choice(subjects)
        v = random.choice(verbs)
        o = random.choice(objects)
        poem.append(f"{s} {v} {o}")
    return "\n".join(poem)

if __name__ == "__main__":
    print("=== weekend poem ===")
    print(make_poem())
