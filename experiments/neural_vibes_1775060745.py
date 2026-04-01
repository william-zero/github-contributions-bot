# Neural Vibes Generator
import random

def generate_vibes(mood="cosmic"):
    """Generate random vibes for the day."""
    vibes = {
        "cosmic": ["stardust", "nebula", "black hole", "photons dancing"],
        "chill": ["lo-fi beats", "coffee warmth", "sunset vibes"],
        "epic": ["dragon awakens", "destiny calls", "legends rise"],
    }
    return random.choice(vibes.get(mood, vibes["cosmic"]))

if __name__ == "__main__":
    for _ in range(3):
        print(f"✨ Today's vibe: {generate_vibes()}")
