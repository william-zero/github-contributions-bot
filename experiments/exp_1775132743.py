# Collatz Conjecture Explorer
import random

def collatz_steps(n):
    """Count steps until reaching 1"""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

# Test with random numbers
numbers = [random.randint(1, 1000) for _ in range(5)]
for num in numbers:
    print(f"{num}: {collatz_steps(num)} steps")
