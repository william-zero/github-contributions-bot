"""
ASCII Art Generator
===================
Generating art one character at a time.
"""

import random


def box(text: str, padding: int = 1) -> str:
    """Put text in a box. Everyone loves boxes."""
    lines = text.split("\n")
    width = max(len(line) for line in lines) + padding * 2
    border = "+" + "-" * (width + 2) + "+"
    result = [border]
    for line in lines:
        padded = f" {' ' * padding}{line}{' ' * (width - len(line) - padding)} "
        result.append(f"|{padded}|")
    result.append(border)
    return "\n".join(result)


def wave(width: int = 40, height: int = 5) -> str:
    """Generate a sine-wave-ish pattern."""
    import math
    result = []
    for y in range(height):
        line = ""
        for x in range(width):
            val = math.sin(x * 0.3 + y * 0.5) * 2
            if abs(val - (y - height // 2)) < 0.5:
                line += "~"
            else:
                line += " "
        result.append(line)
    return "\n".join(result)


def random_landscape(width: int = 60, height: int = 15) -> str:
    """Generate a random ASCII landscape."""
    sky_chars = [" ", " ", " ", ".", "*"]
    ground_chars = ["_", "^", "~"]

    ground_level = height - random.randint(3, 5)
    result = []

    for y in range(height):
        line = ""
        for x in range(width):
            if y < ground_level - 2:
                line += random.choice(sky_chars)
            elif y == ground_level - 2:
                line += random.choice(["_", " ", " "])
            elif y < ground_level:
                line += random.choice([".", " ", "/", "\\"])
            else:
                line += random.choice(ground_chars)
        result.append(line)
    return "\n".join(result)


def matrix_rain(width: int = 50, height: int = 20) -> str:
    """Static snapshot of matrix rain."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%"
    result = []
    streams = [random.randint(0, height) for _ in range(width)]
    for y in range(height):
        line = ""
        for x in range(width):
            if streams[x] <= y < streams[x] + random.randint(3, 8):
                line += random.choice(chars)
            else:
                line += " "
        result.append(line)
    return "\n".join(result)


GALLERY = {
    "box": lambda: box("Hello from the bot!\nHaving a great day."),
    "wave": lambda: wave(),
    "landscape": lambda: random_landscape(),
    "matrix": lambda: matrix_rain(),
}


if __name__ == "__main__":
    for name, generator in GALLERY.items():
        print(f"\n{'='*60}")
        print(f"  {name.upper()}")
        print(f"{'='*60}")
        print(generator())
