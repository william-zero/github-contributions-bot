"""
Roman Numeral Converter
Because sometimes you just need to feel like it's 42 AD.
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
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        result += curr if curr >= prev else -curr
        prev = curr
    return result

tests = [1, 4, 9, 14, 42, 99, 400, 1999, 2024, 3888]
for n in tests:
    r = to_roman(n)
    print(f"{n:5d} → {r:15s} → {from_roman(r)}")
