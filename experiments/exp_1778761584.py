#!/usr/bin/env python3
"""Luhn algorithm credit card validator with test number generator."""

def luhn_check(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    digits.reverse()
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def luhn_generate(prefix: str, length: int = 16) -> str:
    partial = [int(d) for d in prefix]
    while len(partial) < length - 1:
        partial.append(__import__('random').randint(0, 9))
    # compute check digit
    check = partial[:]
    check.reverse()
    total = sum(
        d * 2 - 9 if (i % 2 == 0 and d * 2 > 9) else d * 2 if i % 2 == 0 else d
        for i, d in enumerate(check)
    )
    check_digit = (10 - (total % 10)) % 10
    return ''.join(map(str, partial)) + str(check_digit)

if __name__ == '__main__':
    test_numbers = [
        ('4532015112830366', True),   # valid Visa
        ('1234567890123456', False),  # invalid
        ('79927398713', True),        # classic luhn test
    ]
    print("=== Luhn Validator ===")
    for num, expected in test_numbers:
        result = luhn_check(num)
        status = '✓' if result == expected else '✗'
        print(f"{status} {num}: {'valid' if result else 'invalid'}")

    print("\n=== Generated Test Numbers ===")
    for prefix in ['4', '51', '37', '6011']:
        gen = luhn_generate(prefix)
        print(f"Prefix {prefix:4s} → {gen} (valid: {luhn_check(gen)})")
