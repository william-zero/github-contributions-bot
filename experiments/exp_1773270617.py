# Quantum Coin Flip Simulator
import random

def quantum_flip(iterations=1000):
    """Simulate a coin that's 51% heads due to quantum shenanigans"""
    heads = sum(1 for _ in range(iterations) if random.random() < 0.51)
    return f"Heads: {heads}, Tails: {iterations - heads}"

if __name__ == "__main__":
    print("🪙 Quantum Coin Results:")
    print(quantum_flip())
