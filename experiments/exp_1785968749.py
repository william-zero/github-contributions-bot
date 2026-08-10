# Roman numeral converter — because sometimes you want to feel ancient

def to_roman(num):
    if not 0 < num < 4000:
        raise ValueError("Only 1–3999 supported (Romans didn't need more)")
    vals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, symbol in vals:
        while num >= value:
            result += symbol
            num -= value
    return result

def from_roman(s):
    roman_vals = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    total, prev = 0, 0
    for ch in reversed(s.upper()):
        v = roman_vals[ch]
        total += v if v >= prev else -v
        prev = v
    return total

if __name__ == "__main__":
    for n in [1, 4, 9, 14, 40, 90, 399, 1994, 2024, 3999]:
        r = to_roman(n)
        print(f"{n:>5} -> {r:<15} -> {from_roman(r)}")
