"""
Kaprekar's Constant: any 4-digit number (with at least 2 different digits)
reaches 6174 within 7 iterations of this process.
"""

def kaprekar(n):
    steps = 0
    while n != 6174:
        digits = sorted(f"{n:04d}")
        ascending = int("".join(digits))
        descending = int("".join(reversed(digits)))
        n = descending - ascending
        steps += 1
        print(f"  {descending} - {ascending:04d} = {n:04d}")
        if n == 0:
            print("  (number has all identical digits, skip it!)")
            return steps
    return steps

print("=== Kaprekar's Constant (6174) ===")
for start in [1234, 9999, 1111, 4321, 5050]:
    print(f"\nStarting with {start}:")
    steps = kaprekar(start)
    print(f"  → Reached 6174 in {steps} step(s)")
