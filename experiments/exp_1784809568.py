"""
Pangram detector and generator helper
A pangram uses every letter of the alphabet at least once.
'The quick brown fox jumps over the lazy dog' is the classic,
but we can do weirder things.
"""

import string

def is_pangram(sentence: str) -> bool:
    return set(string.ascii_lowercase).issubset(set(sentence.lower()))

CANDIDATES = [
    "The quick brown fox jumps over the lazy dog",
    "Pack my box with five dozen liquor jugs",
    "Sphinx of black quartz, judge my vow",
    "Waltz, bad nymph, for quick jigs vex",
    "How vexingly quick daft zebras jump",
    "Bright vixens jump dozing fowl quack",  # not a pangram — test it
]

if __name__ == "__main__":
    for s in CANDIDATES:
        result = "PANGRAM" if is_pangram(s) else "NOT a pangram"
        missing = set(string.ascii_lowercase) - set(s.lower())
        note = f" (missing: {sorted(missing)})" if missing else ""
        print(f"[{result}] {s}{note}")
