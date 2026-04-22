"""
Roman numeral converter — because sometimes you need to know that 1994 is MCMXCIV.
"""

def to_roman(n: int) -> str:
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, numeral in vals:
        while n >= value:
            result += numeral
            n -= value
    return result


def from_roman(s: str) -> int:
    roman_vals = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = roman_vals[ch]
        total += val if val >= prev else -val
        prev = val
    return total


if __name__ == "__main__":
    samples = [1, 4, 9, 14, 42, 1999, 2024, 3999]
    for n in samples:
        roman = to_roman(n)
        back = from_roman(roman)
        print(f"{n:>4} -> {roman:<15} -> {back}")
