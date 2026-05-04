"""
Fibonacci Spiral Visualizer
Prints a growing Fibonacci spiral using ASCII characters.
"""

def fibonacci_seq(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def spiral_art(terms=12):
    fibs = fibonacci_seq(terms)
    chars = ['·', '○', '●', '◉', '◎', '✦', '✧', '★', '☆', '❋', '✿', '❀']
    print("Fibonacci Spiral (values mapped to ASCII art):")
    print()
    for i, f in enumerate(fibs):
        char = chars[i % len(chars)]
        bar = char * (f % 40 + 1)  # cap width at 40 for readability
        print(f"  F({i:2d}) = {f:6d}  {bar}")
    print()
    print(f"Golden ratio approximation: {fibs[-1] / fibs[-2]:.8f}")
    print(f"True golden ratio (φ):      1.61803398...")

if __name__ == "__main__":
    spiral_art()
