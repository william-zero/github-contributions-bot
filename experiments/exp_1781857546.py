"""
Luhn algorithm validator — checks if a credit card number passes the Luhn checksum.
Classic use case: client-side validation before hitting the network.
"""

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


test_cases = [
    ("4532015112830366", True),   # valid Visa
    ("1234567890123456", False),  # made-up garbage
    ("79927398713", True),        # Wikipedia's classic example
    ("79927398714", False),       # one digit off
]

for number, expected in test_cases:
    result = luhn_check(number)
    status = "✓" if result == expected else "✗"
    print(f"{status} {number}: {'valid' if result else 'invalid'}")
