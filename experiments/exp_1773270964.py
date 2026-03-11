#!/usr/bin/env python3
"""
Midnight theorem explorer
Find the number where adding digits equals itself
"""

def midnight_check(n):
    """Check if n equals the sum of its digits multiplied by something mystical"""
    digits = sum(int(d) for d in str(n))
    return n % (digits or 1) == 0

results = [n for n in range(100, 200) if midnight_check(n)]
print(f"Midnight numbers (100-200): {results[:5]}")
