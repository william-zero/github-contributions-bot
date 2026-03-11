"""
FizzBuzz Variants Collection
============================
Because the world needs more ways to solve FizzBuzz.
Each variant is increasingly unnecessary.
"""


def classic_fizzbuzz(n: int) -> str:
    """The OG. Respect the classics."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def one_liner_fizzbuzz(n: int) -> str:
    """For when readability is overrated."""
    return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)


def dramatic_fizzbuzz(n: int) -> str:
    """FizzBuzz with feelings."""
    if n % 15 == 0:
        return "FIZZBUZZ! (the crowd goes wild)"
    if n % 3 == 0:
        return "fizz... (whispered softly)"
    if n % 5 == 0:
        return "BUZZ! (an air horn sounds)"
    return f"{n} (silence)"


def reverse_fizzbuzz(n: int) -> str:
    """zzuBzziF"""
    result = classic_fizzbuzz(n)
    return result[::-1] if not result.isdigit() else result


def emoji_fizzbuzz(n: int) -> str:
    """For the modern era."""
    if n % 15 == 0:
        return "🥤🐝"
    if n % 3 == 0:
        return "🥤"
    if n % 5 == 0:
        return "🐝"
    return str(n)


# --- Run all variants for 1..20 ---
if __name__ == "__main__":
    variants = [
        ("Classic", classic_fizzbuzz),
        ("One-Liner", one_liner_fizzbuzz),
        ("Dramatic", dramatic_fizzbuzz),
        ("Reverse", reverse_fizzbuzz),
        ("Emoji", emoji_fizzbuzz),
    ]
    for name, func in variants:
        print(f"\n=== {name} FizzBuzz ===")
        print(", ".join(func(i) for i in range(1, 21)))
