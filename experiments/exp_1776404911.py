"""
Random Walk Simulation
Simulates a particle doing a random walk in 2D space.
"""
import random

def random_walk(steps=100):
    x, y = 0, 0
    positions = [(x, y)]
    
    for _ in range(steps):
        direction = random.choice(['N', 'S', 'E', 'W'])
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        positions.append((x, y))
    
    distance = (x**2 + y**2) ** 0.5
    print(f"Final position: ({x}, {y})")
    print(f"Distance from origin: {distance:.2f}")
    return positions

if __name__ == "__main__":
    random_walk(100)
