#!/usr/bin/env python3
"""Rhyme finder for fun words."""

def find_rhymes(word):
    """Find silly rhymes for any word."""
    rhyme_map = {
        "cat": ["bat", "hat", "mat", "sat"],
        "code": ["node", "load", "mode", "strode"],
        "bot": ["plot", "dot", "hot", "shot"],
        "green": ["seen", "mean", "lean", "sheen"],
    }
    return rhyme_map.get(word.lower(), ["rhyme not found!"])

if __name__ == "__main__":
    words = ["cat", "code", "bot", "green"]
    for w in words:
        print(f"{w} rhymes with: {', '.join(find_rhymes(w))}")
