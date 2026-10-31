# Roman Numeral Converter
# Because sometimes you want to feel ancient and important

def to_roman(num):
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for i in range(len(val)):
        while num >= val[i]:
            result += syms[i]
            num -= val[i]
    return result

for n in [1, 4, 9, 14, 42, 99, 2024, 3999]:
    print(f"{n:4d} = {to_roman(n)}")
