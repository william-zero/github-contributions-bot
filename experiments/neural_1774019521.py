import random

def generate_random_pattern(size=5):
    """Generate a random neural firing pattern"""
    pattern = []
    for i in range(size):
        if random.random() > 0.5:
            pattern.append(f"neuron_{i}: firing 🔥")
        else:
            pattern.append(f"neuron_{i}: silent 😴")
    return pattern

if __name__ == "__main__":
    print("Random Neural Activity Simulation")
    for round_num in range(3):
        print(f"\nRound {round_num + 1}:")
        activity = generate_random_pattern(4)
        for state in activity:
            print(f"  {state}")
