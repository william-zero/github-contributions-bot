"""
Fibonacci spiral visualizer - a mathematical art generator
"""
def generate_fibonacci_spiral(n=10):
    """Generate coordinates for a Fibonacci spiral."""
    fib = [1, 1]
    for i in range(n):
        fib.append(fib[-1] + fib[-2])
    
    spiral = []
    for i, num in enumerate(fib[:n]):
        angle = (num * 137.508) % 360  # Golden angle
        spiral.append((num, angle))
    
    return spiral

if __name__ == "__main__":
    spiral = generate_fibonacci_spiral(12)
    print("🌀 Fibonacci Spiral Coordinates:")
    for radius, angle in spiral:
        print(f"  r={radius:4d}, θ={angle:6.2f}°")
    print(f"\n✨ Generated {len(spiral)} spiral points")
