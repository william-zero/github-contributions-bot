"""
Fibonacci meets chaos: what if we apply a bit of noise to each step?
"""
import random

def chaotic_fibonacci(n, noise_chance=0.1):
    a, b = 0, 1
    sequence = [a, b]
    for _ in range(n - 2):
        next_val = a + b
        if random.random() < noise_chance:
            next_val += random.randint(-b, b)  # inject chaos
        sequence.append(next_val)
        a, b = b, next_val
    return sequence

if __name__ == "__main__":
    print("Normal Fibonacci:  ", [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    print("Chaotic Fibonacci: ", chaotic_fibonacci(10))
    print("(Results may vary. That's the point.)")
