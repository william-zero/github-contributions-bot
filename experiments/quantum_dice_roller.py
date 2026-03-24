#!/usr/bin/env python3
"""
Quantum Dice Roller - Simulating uncertainty with Python
Uses Heisenberg's uncertainty principle as comedy relief.
"""

import random
import time

def quantum_dice_roll(num_sides=6):
    """
    Roll a quantum die. The result only becomes real when observed.
    Before observation: exists in a superposition of all states.
    """
    states = list(range(1, num_sides + 1))
    print(f"🎲 Rolling quantum die (d{num_sides})...")
    print(f"   ↳ Currently in superposition: {states}")
    
    time.sleep(0.5)
    result = random.choice(states)
    print(f"   ↳ Observation collapsed waveform: {result}")
    return result

def main():
    """Run several quantum rolls and defy classical probability."""
    print("Welcome to the Quantum Dice Roller\n")
    
    for i in range(3):
        roll = quantum_dice_roll()
        print(f"Roll {i+1}: {roll}\n")

if __name__ == "__main__":
    main()
