#!/usr/bin/env python3
"""
Quirky quote generator - randomly generates motivational quotes 
with increasingly absurd adjectives.
"""
import random

adjectives = ["magnificent", "extraordinary", "bewildering", "snazzy", "peculiar"]
subjects = ["Python", "code", "debugging", "coffee", "procrastination"]

def generate_quote():
    adj = random.choice(adjectives)
    subj = random.choice(subjects)
    return f"You are a {adj} {subj} enthusiast!"

if __name__ == "__main__":
    for _ in range(3):
        print(generate_quote())
