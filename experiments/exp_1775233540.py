# Fun random number formatter
import random

def format_number_with_style(n):
    """Format numbers in a fun way"""
    styles = [
        lambda x: f"✨ {x} sparkles",
        lambda x: f"🎲 {x} rolls",
        lambda x: f"🚀 {x} launches",
        lambda x: f"💎 {x} gems",
    ]
    return random.choice(styles)(n)

for i in range(1, 6):
    print(format_number_with_style(i * 42))
