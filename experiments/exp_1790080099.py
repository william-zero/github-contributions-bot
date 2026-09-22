"""Number base converter — because decimal is just one option."""

def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append("0123456789ABCDEF"[n % base])
        n //= base
    return ''.join(reversed(digits))

demos = [
    (42, 2, "binary"),
    (42, 8, "octal"),
    (42, 16, "hex"),
    (255, 2, "binary"),
    (1000, 3, "ternary"),
]

for num, base, name in demos:
    print(f"{num:5d} in {name:8s} (base {base:2d}): {to_base(num, base)}")
