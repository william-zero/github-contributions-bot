"""
Fibonacci in unexpected places: a philosophical tour.
"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def spiral_aspect_ratio(n):
    """Golden ratio approximation via consecutive Fibonacci numbers."""
    fibs = list(fib(n + 2))
    return fibs[-1] / fibs[-2]

def count_petals(flower):
    """Most flowers have Fibonacci-number petal counts."""
    petal_counts = {
        "buttercup": 5,
        "bloodroot": 8,
        "black_eyed_susan": 13,
        "shasta_daisy": 21,
        "field_daisy": 34,
        "michaelmas_daisy": 55,
    }
    count = petal_counts.get(flower, 0)
    fibs = list(fib(20))
    is_fib = count in fibs
    return count, is_fib

if __name__ == "__main__":
    print("Fibonacci sequence (first 15):", list(fib(15)))
    print(f"Golden ratio approximation (fib 30): {spiral_aspect_ratio(30):.10f}")
    print(f"True golden ratio:                   {(1 + 5**0.5) / 2:.10f}")
    print()
    flowers = ["buttercup", "black_eyed_susan", "shasta_daisy", "field_daisy"]
    for f in flowers:
        count, is_fib = count_petals(f)
        print(f"  {f}: {count} petals — {'✓ Fibonacci!' if is_fib else '✗ oddity'}")
