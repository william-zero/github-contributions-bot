#!/usr/bin/env python3
"""
Quantum Coin Flip Simulator
A absurdly over-engineered coin flipper for the observer effect.
"""
import random

def schrodinger_flip():
    """Until observed, the coin is both heads AND tails."""
    return "heads" if random.random() < 0.5 else "tails"

if __name__ == "__main__":
    result = schrodinger_flip()
    print(f"The coin landed on: {result}")
    print("Wave function collapsed. Observation complete. 🪙✨")
