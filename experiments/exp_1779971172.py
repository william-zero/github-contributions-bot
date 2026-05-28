"""
Roman numeral converter — because sometimes you need to know
what year MMXXVI is without counting on your fingers.
"""

def to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for i, v in enumerate(val):
        while num >= v:
            result += syms[i]
            num -= v
    return result

def from_roman(s):
    vals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        if i+1 < len(s) and vals[s[i]] < vals[s[i+1]]:
            result -= vals[s[i]]
        else:
            result += vals[s[i]]
    return result

if __name__ == '__main__':
    for year in [2026, 1984, 42, 1776, 3999]:
        roman = to_roman(year)
        print(f"{year:>5} → {roman:<15} → {from_roman(roman)}")
