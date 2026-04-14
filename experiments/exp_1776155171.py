import random

def fibonacci_sequence(n):
    """Generate the first n Fibonacci numbers with a twist!"""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    seq = [1, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    
    return seq

# Generate first 10 Fibonacci numbers
fib = fibonacci_sequence(10)
print(f"Fibonacci sequence: {fib}")
print(f"Sum: {sum(fib)}")
print(f"Average: {sum(fib) / len(fib):.2f}")
