#!/usr/bin/env python3
"""Fibonacci chaos: what happens if we mix recursion with randomness?"""
import random

def chaotic_fib(n, chaos_level=0.1):
    """Compute Fibonacci with random mutations for maximum confusion."""
    if n <= 1:
        return n
    # Random chaos: sometimes skip a step
    if random.random() < chaos_level:
        return random.randint(0, 100)
    return chaotic_fib(n - 1, chaos_level) + chaotic_fib(n - 2, chaos_level)

if __name__ == "__main__":
    print("Chaotic Fibonacci Sequence (n=10):")
    for i in range(10):
        print(f"  fib({i}) = {chaotic_fib(i)}")
    print("\n✨ Determinism is overrated ✨")
