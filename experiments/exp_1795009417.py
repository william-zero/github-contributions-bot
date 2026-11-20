"""Roman numeral converter — because sometimes you need to know what MCMXCIX means."""

def to_roman(num: int) -> str:
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, numeral in vals:
        while num >= value:
            result += numeral
            num -= value
    return result

def from_roman(s: str) -> int:
    roman_vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev = 0
    for ch in reversed(s):
        curr = roman_vals[ch]
        result += curr if curr >= prev else -curr
        prev = curr
    return result

if __name__ == "__main__":
    test_nums = [1, 4, 9, 14, 42, 1999, 2024]
    for n in test_nums:
        roman = to_roman(n)
        back = from_roman(roman)
        print(f"{n:5d} → {roman:<12} → {back}")
