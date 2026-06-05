"""
Benford's Law Checker — does your data follow the first-digit distribution?
Benford's Law: in naturally occurring numbers, the leading digit is 1 ~30% of the time.
"""

import math
from collections import Counter

def benfords_expected(digit):
    """Expected frequency of leading digit under Benford's Law."""
    return math.log10(1 + 1/digit)

def leading_digit(n):
    s = str(abs(int(n))).lstrip('0')
    return int(s[0]) if s else None

def check_benford(numbers):
    digits = [leading_digit(n) for n in numbers if leading_digit(n)]
    total = len(digits)
    counts = Counter(digits)
    
    print(f"{'Digit':<8} {'Observed%':<12} {'Expected%':<12} {'Match'}")
    print("-" * 45)
    
    chi_sq = 0
    for d in range(1, 10):
        obs = counts.get(d, 0) / total
        exp = benfords_expected(d)
        chi_sq += (obs - exp) ** 2 / exp
        match = "✓" if abs(obs - exp) < 0.05 else "✗"
        print(f"  {d:<6} {obs*100:<12.1f} {exp*100:<12.1f} {match}")
    
    print(f"\nChi-squared: {chi_sq:.4f}")
    print("Looks natural!" if chi_sq < 0.5 else "Suspicious — might be fabricated data!")

# Demo: Fibonacci numbers follow Benford's Law almost perfectly
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    print("=== Benford's Law check on first 500 Fibonacci numbers ===\n")
    check_benford(list(fibonacci(500)))
