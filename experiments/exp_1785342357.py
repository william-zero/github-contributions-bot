# Roman numeral converter
def to_roman(n):
    vals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for v, s in vals:
        while n >= v:
            result += s
            n -= v
    return result

def from_roman(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        val = roman[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

for n in [1, 4, 9, 14, 40, 42, 99, 400, 1999, 2024, 3999]:
    roman = to_roman(n)
    back = from_roman(roman)
    status = "OK" if back == n else "FAIL"
    print(f"{n:4} -> {roman:12} -> {back:4} [{status}]")
