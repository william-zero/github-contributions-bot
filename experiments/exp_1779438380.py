"""
Fibonacci Spiral Generator
Prints an ASCII spiral approximation using Fibonacci numbers.
"""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    fibs = list(fibonacci(12))
    print("Fibonacci Sequence:")
    print(" -> ".join(str(f) for f in fibs))
    print()

    print("Fibonacci Spiral Sizes (blocks):")
    for i, f in enumerate(fibs[1:], 1):
        bar = "█" * min(f, 50)
        label = f"{f:>5}"
        print(f"  F({i:2d}) = {label}  {bar}")

    print()
    golden = fibs[-1] / fibs[-2]
    print(f"Golden Ratio approximation: {golden:.6f} (actual φ ≈ 1.618034)")

if __name__ == "__main__":
    main()
