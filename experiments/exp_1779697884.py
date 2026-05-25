# Roman numeral encoder/decoder

def to_roman(num):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
            (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for v, s in vals:
        while num >= v:
            result += s
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

for n in [1, 4, 9, 14, 40, 90, 1999, 2024, 3999]:
    r = to_roman(n)
    print(f"{n:5} -> {r:15} -> {from_roman(r)}")
