"""
Experiment: The Overthinking Sorter
Sorts a list using increasingly unnecessary philosophical justification.
"""

import random

def philosophical_sort(items):
    """Sort items, but contemplate each comparison."""
    reasons = [
        "because smaller numbers deserve to go first, having waited long enough",
        "in accordance with the ancient laws of numerical precedence",
        "as the universe clearly intended from the moment of the Big Bang",
        "due to an overwhelming sense of numerical destiny",
        "following a vision received at 3 AM involving a spreadsheet",
    ]
    
    sorted_items = sorted(items)
    
    print("Initiating philosophical sort...")
    for i in range(len(sorted_items) - 1):
        a, b = sorted_items[i], sorted_items[i+1]
        reason = random.choice(reasons)
        print(f"  {a} precedes {b} {reason}")
    
    print(f"\nFinal order: {sorted_items}")
    print("The sorting is complete. Rest now.")
    return sorted_items

if __name__ == "__main__":
    data = [42, 7, 99, 3, 17, 55, 1, 88]
    philosophical_sort(data)
