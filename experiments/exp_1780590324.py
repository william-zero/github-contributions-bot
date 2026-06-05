"""
Fibonacci spiral approximation using the golden ratio.
Explores how Phi (≈1.618) connects to Fibonacci numbers
and why spirals in nature follow this pattern.
"""

PHI = (1 + 5 ** 0.5) / 2

def fib_phi_ratio(n):
    """Show how fib(n+1)/fib(n) converges to Phi."""
    a, b = 1, 1
    ratios = []
    for _ in range(n):
        ratios.append(b / a)
        a, b = b, a + b
    return ratios

def spiral_point(n):
    """Approximate point on a golden spiral at step n."""
    import math
    r = PHI ** (n / 4)
    theta = n * math.pi / 2
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return round(x, 4), round(y, 4)

if __name__ == "__main__":
    print(f"Golden Ratio (Phi): {PHI:.10f}")
    print()
    print("Fibonacci ratio convergence to Phi:")
    for i, r in enumerate(fib_phi_ratio(15), start=2):
        print(f"  F({i+1})/F({i}) = {r:.8f}  Δ = {abs(r - PHI):.2e}")
    print()
    print("Golden spiral sample points:")
    for step in range(0, 13, 3):
        x, y = spiral_point(step)
        print(f"  step {step:2d}: ({x:8.4f}, {y:8.4f})")
