#!/usr/bin/env python3
"""
Random word picker - selects a fun word from our collection
"""
import random

words = [
    "serendipity",
    "ephemeral",
    "mellifluous",
    "petrichor",
    "luminous",
    "delightful",
    "whimsical",
    "ubiquitous"
]

def get_random_word():
    """Pick a random word from the collection"""
    return random.choice(words)

if __name__ == "__main__":
    print(f"Today's word: {get_random_word()}")
