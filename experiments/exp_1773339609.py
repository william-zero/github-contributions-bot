#!/usr/bin/env python3
"""Random word combinator - generates silly two-word phrases"""

import random

adjectives = ["cosmic", "sneaky", "gigantic", "sparkly", "quantum", "mischievous"]
nouns = ["llama", "philosopher", "sandwich", "keyboard", "moonbeam", "pickle"]

def generate_silly_phrase():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adj} {noun}"

if __name__ == "__main__":
    print("✨ Random silly phrases ✨")
    for _ in range(5):
        print(f"  - {generate_silly_phrase()}")
