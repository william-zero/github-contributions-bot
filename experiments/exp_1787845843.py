"""Roman numeral converter — because sometimes you want to feel ancient."""

def to_roman(n):
    vals = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
            (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for v, s in vals:
        while n >= v:
            result += s
            n -= v
    return result

for i in [1, 4, 9, 14, 40, 90, 399, 1999, 2024, 2026]:
    print(f"{i:>5} → {to_roman(i)}")
