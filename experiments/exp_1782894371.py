"""
Roman numeral converter — because why not do math like it's 50 BC
"""

NUMERALS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
    (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'),
    (1,    'I'),
]

def to_roman(n: int) -> str:
    result = ''
    for value, numeral in NUMERALS:
        while n >= value:
            result += numeral
            n -= value
    return result

def from_roman(s: str) -> int:
    lookup = {n: v for v, n in NUMERALS}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        val = lookup.get(ch, 0)
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

if __name__ == '__main__':
    for year in [1, 4, 9, 14, 42, 1999, 2024, 2025, 3999]:
        roman = to_roman(year)
        back = from_roman(roman)
        check = '✓' if back == year else '✗'
        print(f'{year:>5}  →  {roman:<15}  →  {back:>5}  {check}')
