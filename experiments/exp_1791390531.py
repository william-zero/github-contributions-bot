"""
Roman numeral converter - because sometimes you need to tell people
what year a movie was made in the credits.
"""

def to_roman(num):
    if not 0 < num < 4000:
        raise ValueError("Roman numerals only go from 1 to 3999. Sorry, year 0 and the future don't exist.")
    
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    
    result = ""
    for v, s in zip(vals, syms):
        while num >= v:
            result += s
            num -= v
    return result

def from_roman(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    prev = 0
    for c in reversed(s.upper()):
        curr = roman[c]
        result += curr if curr >= prev else -curr
        prev = curr
    return result

# Some fun facts in Roman numerals
years = [1776, 1969, 2001, 42, 666]
print("Famous years in Roman numerals:")
for y in years:
    print(f"  {y} = {to_roman(y)}")

print("\nDecode: MMXXVI =", from_roman("MMXXVI"))
print("Decode: XLII =", from_roman("XLII"))
