"""
Haiku Generator
Generates random haikus from word lists following 5-7-5 syllable structure.
"""
import random

five_syllable = [
    "ancient rivers flow",
    "moonlight on still water",
    "cherry blossoms fall",
    "the fog rolls in slow",
    "silence fills the room",
]

seven_syllable = [
    "whispers travel through the pines",
    "a lost key turns up at last",
    "the coffee grows cold again",
    "three ravens watch from the oak",
    "forgotten passwords haunt me",
]

def generate_haiku():
    line1 = random.choice(five_syllable)
    line2 = random.choice(seven_syllable)
    line3 = random.choice(five_syllable)
    return f"{line1}\n{line2}\n{line3}"

if __name__ == "__main__":
    print("=== Today's Haiku ===")
    print(generate_haiku())
    print()
    print("=== Another one ===")
    print(generate_haiku())
