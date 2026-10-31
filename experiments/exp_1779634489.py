# Number base converter with commentary

def convert_to_base(n, base):
    """Convert integer n to a given base (2-36). Returns string representation."""
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    negative = n < 0
    n = abs(n)
    while n:
        result.append(digits[n % base])
        n //= base
    if negative:
        result.append('-')
    return ''.join(reversed(result))

if __name__ == "__main__":
    test_numbers = [42, 255, 1024, 31337]
    for num in test_numbers:
        print(f"{num} in binary:  {convert_to_base(num, 2)}")
        print(f"{num} in octal:   {convert_to_base(num, 8)}")
        print(f"{num} in hex:     {convert_to_base(num, 16)}")
        print(f"{num} in base-36: {convert_to_base(num, 36)}")
        print()
