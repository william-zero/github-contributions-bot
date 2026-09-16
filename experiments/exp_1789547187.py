"""
Roman numeral converter - because sometimes you need to pretend it's 44 BC.
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
    total = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        if curr < prev:
            total -= curr
        else:
            total += curr
        prev = curr
    return total

if __name__ == '__main__':
    tests = [1, 4, 9, 14, 42, 99, 2024, 3999]
    for n in tests:
        roman = to_roman(n)
        back = from_roman(roman)
        print(f"{n:4d} → {roman:15s} → {back}")
