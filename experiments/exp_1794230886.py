"""Roman numeral converter with style."""

def to_roman(num):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for v, s in zip(vals, syms):
        while num >= v:
            result += s
            num -= v
    return result

for n in [1, 4, 9, 14, 42, 1999, 2024, 3999]:
    print(f"{n:>5} = {to_roman(n)}")
