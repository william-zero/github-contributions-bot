"""
Roman Numeral Converter
MMXXVI is a great year. So is any year you can represent in all caps.
"""

def to_roman(n):
    vals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
        (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'), (1, 'I')
    ]
    result = ''
    for v, s in vals:
        while n >= v:
            result += s
            n -= v
    return result

def from_roman(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = vals[ch]
        total += v if v >= prev else -v
        prev = v
    return total

for n in [1, 4, 9, 14, 42, 400, 1776, 2026]:
    r = to_roman(n)
    print(f"{n:6} → {r:12} → {from_roman(r)}")
