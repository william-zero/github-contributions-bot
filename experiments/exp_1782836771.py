"""
Number base converter playground — converts integers to binary, octal, hex, and base-36
"""

def to_base(n: int, base: int, digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> str:
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    result = []
    while n:
        result.append(digits[n % base])
        n //= base
    if negative:
        result.append("-")
    return "".join(reversed(result))


if __name__ == "__main__":
    test_numbers = [0, 1, 42, 255, 1024, 65535, 1_000_000]
    print(f"{'N':>10}  {'BIN':>20}  {'OCT':>8}  {'HEX':>8}  {'BASE36':>8}")
    print("-" * 62)
    for n in test_numbers:
        print(f"{n:>10}  {to_base(n, 2):>20}  {to_base(n, 8):>8}  {to_base(n, 16):>8}  {to_base(n, 36):>8}")
