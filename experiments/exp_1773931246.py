# Chaotic number printer
def chaos_printer(n):
    """Print n in increasingly chaotic formats."""
    print(f"Binary: {bin(n)}")
    print(f"Hex: {hex(n)}")
    print(f"Reversed: {str(n)[::-1]}")
    print(f"Sum of digits: {sum(int(d) for d in str(n))}")

chaos_printer(42)
