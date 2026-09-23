# Roman numeral converter — because sometimes you need to date your monuments

def to_roman(n):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
            (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for value, numeral in vals:
        while n >= value:
            result += numeral
            n -= value
    return result

def from_roman(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        curr = roman[ch]
        total += curr if curr >= prev else -curr
        prev = curr
    return total

if __name__ == '__main__':
    for n in [1, 4, 9, 14, 40, 90, 399, 1999, 2024, 3999]:
        roman = to_roman(n)
        back = from_roman(roman)
        status = "✓" if back == n else "✗"
        print(f"{n:>5} = {roman:<15} (back: {back}) {status}")
