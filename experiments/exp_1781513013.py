"""
roman_numeral_converter.py — because who doesn't need this in 2026?
"""

def to_roman(n: int) -> str:
    vals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
        (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'), (1, 'I'),
    ]
    result = ''
    for value, numeral in vals:
        while n >= value:
            result += numeral
            n -= value
    return result

def from_roman(s: str) -> int:
    roman_vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s.upper()):
        v = roman_vals[ch]
        total += v if v >= prev else -v
        prev = v
    return total

if __name__ == "__main__":
    for n in [1, 4, 9, 14, 42, 1999, 2024, 3999]:
        r = to_roman(n)
        back = from_roman(r)
        print(f"{n:>5} → {r:<15} → {back}")
