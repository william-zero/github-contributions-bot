"""
Roman Numeral Decoder
Converts Roman numerals back to integers, because sometimes history needs parsing.
"""

def roman_to_int(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = values[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

test_cases = [
    ("III", 3), ("IV", 4), ("IX", 9), ("LVIII", 58),
    ("MCMXCIV", 1994), ("MMXXVI", 2026), ("CDXLIV", 444),
]

print("Roman Numeral Decoder Results:")
print("-" * 35)
for roman, expected in test_cases:
    result = roman_to_int(roman)
    status = "✓" if result == expected else "✗"
    print(f"  {roman:10s} = {result:5d}  {status}")
