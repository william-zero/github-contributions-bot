"""
Roman numeral converter — because sometimes you need to know
that 2024 is MMXXIV, and you need to know it NOW.
"""

def to_roman(n: int) -> str:
    """Convert integer to Roman numeral string."""
    if not 1 <= n <= 3999:
        raise ValueError(f"{n} is out of range (1–3999)")

    table = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"),
        (1, "I"),
    ]
    result = ""
    for value, numeral in table:
        while n >= value:
            result += numeral
            n -= value
    return result


def from_roman(s: str) -> int:
    """Convert Roman numeral string to integer."""
    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = roman_map[ch]
        total += val if val >= prev else -val
        prev = val
    return total


if __name__ == "__main__":
    test_years = [1, 4, 9, 14, 42, 1999, 2024, 3999]
    print("Year → Roman → Back")
    print("-" * 30)
    for year in test_years:
        roman = to_roman(year)
        back = from_roman(roman)
        status = "✓" if back == year else "✗"
        print(f"  {year:>5} → {roman:<12} → {back:>5} {status}")
