"""
Roman numeral converter - converts between integers and Roman numerals
"""

def to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result

def from_roman(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
            result -= roman[s[i]]
        else:
            result += roman[s[i]]
    return result

for n in [1, 4, 9, 14, 40, 90, 399, 1999, 2024, 3999]:
    r = to_roman(n)
    print(f"{n:5} = {r:15} -> back = {from_roman(r)}")
