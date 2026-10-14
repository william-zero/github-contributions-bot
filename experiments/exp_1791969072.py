"""
Braille dot counter - counts how many dots appear in a string of Braille characters.
Just for fun, definitely not something you'd normally need.
"""

BRAILLE_DOTS = {
    '⠀': 0, '⠁': 1, '⠂': 1, '⠃': 2, '⠄': 1, '⠅': 2, '⠆': 2, '⠇': 3,
    '⠈': 1, '⠉': 2, '⠊': 2, '⠋': 3, '⠌': 2, '⠍': 3, '⠎': 3, '⠏': 4,
    '⠐': 1, '⠑': 2, '⠒': 2, '⠓': 3, '⠔': 2, '⠕': 3, '⠖': 3, '⠗': 4,
    '⠘': 2, '⠙': 3, '⠚': 3, '⠛': 4, '⠜': 3, '⠝': 4, '⠞': 4, '⠟': 5,
}

def count_dots(braille_str):
    return sum(BRAILLE_DOTS.get(ch, bin(ord(ch) - 0x2800).count('1'))
               for ch in braille_str)

samples = [
    ("Hello in Braille", "⠓⠑⠇⠇⠕"),
    ("Empty cell", "⠀"),
    ("All dots", "⠿"),
]

for label, text in samples:
    total = count_dots(text)
    print(f"{label!r}: {total} dots total ({total / max(len(text), 1):.1f} avg per cell)")
