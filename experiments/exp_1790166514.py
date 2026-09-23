"""
Pangram checker — does a sentence use every letter of the alphabet?
The quick brown fox jumped over the lazy dog. (spoiler: yes)
"""

import string

def is_pangram(sentence: str) -> bool:
    letters_used = set(sentence.lower())
    return set(string.ascii_lowercase).issubset(letters_used)

def missing_letters(sentence: str) -> list[str]:
    used = set(sentence.lower())
    return sorted(set(string.ascii_lowercase) - used)

test_sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "How vexingly quick daft zebras jump",
    "Hello world",
    "The five boxing wizards jump quickly",
]

for s in test_sentences:
    if is_pangram(s):
        print(f"✓ PANGRAM: {s!r}")
    else:
        missing = missing_letters(s)
        print(f"✗ Missing {len(missing)} letters ({', '.join(missing)}): {s!r}")
