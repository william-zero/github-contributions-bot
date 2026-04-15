#!/usr/bin/env python3
"""
Quantum-inspired coin flip simulator
Schrödinger's coin: it's both heads AND tails until observed.
"""

import random
from collections import Counter

def quantum_coin_flip(observations=1000):
    """Flip a coin in a quantum superposition, then measure."""
    results = Counter()
    superposition = ['heads', 'tails']
    
    for _ in range(observations):
        # The act of observation collapses the superposition
        outcome = random.choice(superposition)
        results[outcome] += 1
    
    return results

if __name__ == '__main__':
    flips = quantum_coin_flip(1000)
    print("🪙 Quantum Coin Flip Results 🪙")
    print(f"Heads: {flips['heads']} ({flips['heads']/10:.1f}%)")
    print(f"Tails: {flips['tails']} ({flips['tails']/10:.1f}%)")
    print("\nThe universe has spoken! 🌌")
