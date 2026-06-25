# Fourier series drawing - approximate any shape with rotating circles
import math

def fourier_circle(n_terms=5, t_steps=200):
    """Draw a square wave using Fourier series of rotating circles."""
    print("Fourier Square Wave Approximation")
    print("=" * 40)
    print(f"Using {n_terms} harmonic(s)")
    print()

    width = 60
    height = 20
    canvas = [[' '] * width for _ in range(height)]

    for step in range(t_steps):
        t = (step / t_steps) * 2 * math.pi
        # Fourier series: sum of odd harmonics for square wave
        y = sum(
            (4 / math.pi) * (1 / k) * math.sin(k * t)
            for k in range(1, 2 * n_terms, 2)
        )
        x_idx = int((t / (2 * math.pi)) * (width - 1))
        y_idx = int(((1 - y) / 2) * (height - 1))
        y_idx = max(0, min(height - 1, y_idx))
        canvas[y_idx][x_idx] = '*'

    for row in canvas:
        print(''.join(row))

    print()
    print("Each additional harmonic sharpens the corners.")
    print("Infinite terms = perfect square wave. Math is wild.")

if __name__ == "__main__":
    for terms in [1, 3, 7]:
        fourier_circle(n_terms=terms)
        print()
