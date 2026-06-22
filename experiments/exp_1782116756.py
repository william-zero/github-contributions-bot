"""
Fibonacci spiral approximation using ASCII art.
Each row grows by the golden ratio, roughly.
"""

def fib(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def spiral_row(length, char='*'):
    return char * length

sequence = fib(12)
print("Fibonacci ASCII Spiral:")
print()
for i, f in enumerate(sequence):
    indent = ' ' * (max(sequence) - f)
    bar = spiral_row(f if f > 0 else 1)
    label = f"F({i}) = {f}"
    print(f"{indent}{bar}  {label}")
