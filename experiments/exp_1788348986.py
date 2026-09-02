# Fibonacci spiral approximation using turtle-like coordinate math
import math

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def golden_spiral_points(steps=20):
    phi = (1 + math.sqrt(5)) / 2
    points = []
    for i in range(steps):
        r = phi ** (i / 4)
        theta = i * (2 * math.pi / phi)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        points.append((round(x, 3), round(y, 3)))
    return points

if __name__ == "__main__":
    fibs = fibonacci(10)
    print("Fibonacci sequence:", fibs)
    print(f"Golden ratio approx: {fibs[-1]/fibs[-2]:.6f}")
    print(f"True golden ratio:   {(1+math.sqrt(5))/2:.6f}")
    print("\nSpiral points (first 5):")
    for pt in golden_spiral_points()[:5]:
        print(f"  {pt}")
