"""
Roman numeral converter - convert between integers and Roman numerals.
Handles numbers from 1 to 3999.
"""

NUMERALS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
]

def to_roman(num: int) -> str:
    if not 1 <= num <= 3999:
        raise ValueError(f"Number must be between 1 and 3999, got {num}")
    result = ""
    for value, numeral in NUMERALS:
        while num >= value:
            result += numeral
            num -= value
    return result

def from_roman(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = roman_values[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

if __name__ == "__main__":
    test_cases = [1, 4, 9, 14, 42, 1994, 2024, 3999]
    print("Integer -> Roman -> Integer (round-trip):")
    for n in test_cases:
        roman = to_roman(n)
        back = from_roman(roman)
        print(f"  {n:4d} -> {roman:12s} -> {back:4d}  {'OK' if back == n else 'FAIL'}")
