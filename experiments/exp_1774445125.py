#!/usr/bin/env python3
"""
Fibonacci Spiral Generator - generates beautiful Fibonacci sequences
for mathematical contemplation and ASCII art purposes.
"""

def fibonacci_spiral(n):
    """Generate first n Fibonacci numbers"""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    fib = [1, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

def spiral_visualization(count=10):
    """Create ASCII visualization of Fibonacci spiral pattern"""
    fib = fibonacci_spiral(count)
    print("🌀 Fibonacci Spiral")
    print("=" * 40)
    for i, num in enumerate(fib, 1):
        bar = "█" * (num % 20)
        print(f"F({i:2d}) = {num:6d} {bar}")

if __name__ == "__main__":
    spiral_visualization(12)
