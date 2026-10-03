"""
Roman Numeral Converter: Because sometimes you need to feel like you're
reading a movie sequel or a Super Bowl.
"""


def to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result


def from_roman(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr
    return result


if __name__ == "__main__":
    print("Converting numbers to Roman numerals:")
    for n in [1, 4, 9, 14, 42, 99, 2024, 2026, 3999]:
        r = to_roman(n)
        back = from_roman(r)
        check = "✓" if back == n else "✗"
        print(f"  {n:5d} → {r:15s} → {back:5d} {check}")
