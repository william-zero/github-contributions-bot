"""
Fibonacci spiral visualizer using ASCII art.
Prints a growing Fibonacci sequence with a simple bar chart.
"""

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def ascii_bar(value, max_val, width=40):
    filled = int((value / max_val) * width)
    return "█" * filled + "░" * (width - filled)

if __name__ == "__main__":
    terms = 15
    seq = fibonacci(terms)
    max_val = max(seq) or 1

    print("Fibonacci Sequence Visualizer")
    print("=" * 50)
    for i, val in enumerate(seq):
        bar = ascii_bar(val, max_val)
        print(f"F({i:2d}) = {val:5d}  {bar}")

    golden = seq[-1] / seq[-2] if seq[-2] else 0
    print(f"\nApprox golden ratio (F{terms-1}/F{terms-2}): {golden:.6f}")
    print(f"True golden ratio φ:                    1.618034")
