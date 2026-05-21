"""
Luhn Algorithm Validator - the secret handshake of credit card numbers.
Every valid credit card number passes this check. Try your own!
"""

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

def luhn_generate_check_digit(number: str) -> int:
    """Given a partial number, compute the check digit to make it valid."""
    digits = [int(d) for d in number if d.isdigit()]
    digits.reverse()
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 0:  # positions flip since we're adding one more
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return (10 - (total % 10)) % 10

test_cases = [
    ("4532015112830366", True),   # Visa test number
    ("79927398713", True),        # Wikipedia example
    ("1234567890123456", False),  # Obviously fake
    ("0000000000000000", True),   # All zeros, technically valid
]

print("=== Luhn Algorithm Validator ===\n")
for number, expected in test_cases:
    result = luhn_check(number)
    status = "PASS" if result == expected else "FAIL"
    print(f"  {number}: {'VALID' if result else 'INVALID'} [{status}]")

print("\n=== Check Digit Generator ===\n")
partials = ["453201511283036", "7992739871"]
for p in partials:
    check = luhn_generate_check_digit(p)
    full = p + str(check)
    print(f"  {p} + {check} => {full} (valid: {luhn_check(full)})")

print("\nFun fact: The Luhn algorithm was invented by Hans Peter Luhn at IBM in 1954.")
print("It wasn't designed to catch fraud — just typos. Simpler times.")
