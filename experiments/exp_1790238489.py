# Luhn algorithm — validates credit card numbers with pure math guilt
def luhn_check(card_number: str) -> bool:
    digits = [int(d) for d in card_number if d.isdigit()]
    digits.reverse()
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    return sum(digits) % 10 == 0

test_cards = [
    ("4532015112830366", True),   # valid Visa
    ("1234567890123456", False),  # decidedly not valid
    ("79927398713", True),        # classic test number
]

for num, expected in test_cards:
    result = luhn_check(num)
    status = "✓" if result == expected else "✗"
    print(f"{status} {num}: {'valid' if result else 'invalid'}")
