#!/usr/bin/env python3
"""
Fibonacci sequence generator with a twist.
Shows how many steps it takes to reach a target number.
"""

def fibonacci_steps(target):
    """Generate Fibonacci sequence until we exceed target."""
    a, b = 0, 1
    steps = 0
    while a < target:
        yield a
        a, b = b, a + b
        steps += 1
    return steps

target = 1000
fib_seq = list(fibonacci_steps(target))
print(f"Fibonacci numbers under {target}: {len(fib_seq)} numbers")
print(f"Last few: {fib_seq[-3:]}")
print(f"Sum of all: {sum(fib_seq)}")
