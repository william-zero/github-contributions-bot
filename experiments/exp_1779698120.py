# Luhn algorithm - credit card number validator

def luhn_check(number):
    digits = [int(d) for d in str(number) if d.isdigit()]
    digits.reverse()
    total = 0
    for i, d in enumerate(digits):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

def luhn_generate(partial):
    partial = str(partial)
    digits = [int(d) for d in partial]
    digits.append(0)  # placeholder
    digits.reverse()
    total = sum(
        d * 2 - (9 if d * 2 > 9 else 0) if i % 2 == 0 else d
        for i, d in enumerate(digits[1:], 1)
    )
    check = (10 - (total % 10)) % 10
    return partial + str(check)

test_numbers = ['4532015112830366', '4532015112830367', '79927398713', '79927398714']
for n in test_numbers:
    valid = luhn_check(n)
    print(f"{n}: {'VALID' if valid else 'INVALID'}")

print(f"\nGenerated: {luhn_generate('453201511283036')}")
