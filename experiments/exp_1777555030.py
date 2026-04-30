# Drunk Walk Simulator: where will the particle end up?
import random

def drunk_walk(steps=1000, seed=42):
    random.seed(seed)
    x, y = 0, 0
    trail = [(x, y)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for _ in range(steps):
        dx, dy = random.choice(directions)
        x += dx
        y += dy
        trail.append((x, y))

    dist = (x**2 + y**2) ** 0.5
    print(f"After {steps} steps, ended at ({x}, {y})")
    print(f"Distance from origin: {dist:.2f}")
    print(f"Farthest x: {max(p[0] for p in trail)}, Farthest y: {max(p[1] for p in trail)}")
    return trail

if __name__ == "__main__":
    drunk_walk()
    print("\nTrying with different seeds:")
    for s in [7, 13, 99]:
        drunk_walk(steps=500, seed=s)
