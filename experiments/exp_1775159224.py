#!/usr/bin/env python3
"""
The Infinite Coffee Theorem

This experiment proves that developers can write infinite code while 
only drinking finite amounts of coffee. The secret? Quantum superposition.
A developer is simultaneously debugging and sleeping until observed.
"""

def quantum_coffee_level(cups_consumed):
    """Returns productivity on a logarithmic scale."""
    import math
    if cups_consumed == 0:
        return "confused"
    return math.log(cups_consumed) * 100

if __name__ == "__main__":
    for cups in range(1, 6):
        print(f"{cups} cups = {quantum_coffee_level(cups):.0f}% productivity")
