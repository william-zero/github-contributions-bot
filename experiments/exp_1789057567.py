"""
Roman Numeral Converter: because sometimes you want to feel ancient.
"""

def to_roman(num: int) -> str:
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result

def from_roman(s: str) -> int:
    roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        curr = roman_vals[ch]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

if __name__ == '__main__':
    samples = [1, 4, 9, 14, 40, 58, 399, 1994, 2024, 3999]
    print("Number → Roman → Back")
    for n in samples:
        r = to_roman(n)
        back = from_roman(r)
        check = "✓" if back == n else "✗"
        print(f"  {n:>5} → {r:<12} → {back} {check}")
