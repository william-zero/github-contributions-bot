#!/usr/bin/env python3
"""
Quantum number paradox generator.
Explores the philosophical implications of random number generation.
"""

import random

def quantum_paradox():
    """Generate a paradox: does a random number exist before we observe it?"""
    numbers = [random.randint(1, 100) for _ in range(5)]
    paradox = f"These numbers existed simultaneously before observation: {numbers}"
    return paradox

if __name__ == "__main__":
    print(quantum_paradox())
