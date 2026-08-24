# Roman numeral converter with a twist: supports subtraction notation
def to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result

def from_roman(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        result += curr if curr >= prev else -curr
        prev = curr
    return result

# Fun test: what year did things happen?
years = [1066, 1492, 1776, 1969, 2001]
for y in years:
    roman = to_roman(y)
    back = from_roman(roman)
    print(f"{y} → {roman} → {back} {'✓' if back == y else '✗'}")
