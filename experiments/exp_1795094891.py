"""Number base converter: convert between binary, octal, decimal, hex."""

def to_base(n: int, base: int) -> str:
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = []
    negative = n < 0
    n = abs(n)
    while n:
        result.append(digits[n % base])
        n //= base
    if negative:
        result.append("-")
    return "".join(reversed(result))


def from_base(s: str, base: int) -> int:
    return int(s, base)


examples = [42, 255, 1024, 0, -7]
bases = {"bin": 2, "oct": 8, "dec": 10, "hex": 16}

for num in examples:
    conversions = {name: to_base(num, b) for name, b in bases.items()}
    print(f"{num:6d}  =>  " + "  |  ".join(f"{k}: {v}" for k, v in conversions.items()))
