# Number base converter: decimal to anything up to base 36
def to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while n > 0:
        result.append(digits[n % base])
        n //= base
    return ''.join(reversed(result))

for num in [42, 255, 1024, 65535]:
    print(f"{num} in base 2:  {to_base(num, 2)}")
    print(f"{num} in base 8:  {to_base(num, 8)}")
    print(f"{num} in base 16: {to_base(num, 16)}")
    print(f"{num} in base 36: {to_base(num, 36)}")
    print()
