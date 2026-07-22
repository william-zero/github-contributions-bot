# Luhn algorithm - credit card number validator
def luhn_check(number: str) -> bool:
    digits = [int(d) for d in number if d.isdigit()]
    digits.reverse()
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

test_numbers = [
    ("4532015112830366", True),   # valid Visa
    ("1234567890123456", False),  # invalid
    ("79927398713", True),        # classic test number
]

for number, expected in test_numbers:
    result = luhn_check(number)
    status = "✓" if result == expected else "✗"
    print(f"{status} {number}: {'valid' if result else 'invalid'}")
