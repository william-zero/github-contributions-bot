"""Gray code generator — converts between binary and Gray code.

Gray code has the property that consecutive values differ by exactly one bit,
useful in rotary encoders and error correction.
"""


def binary_to_gray(n: int) -> int:
    return n ^ (n >> 1)


def gray_to_binary(g: int) -> int:
    mask = g >> 1
    while mask:
        g ^= mask
        mask >>= 1
    return g


def show_table(limit: int = 16) -> None:
    print(f"{'Decimal':>8} {'Binary':>8} {'Gray':>8} {'Gray(bin)':>10}")
    print("-" * 40)
    for i in range(limit):
        g = binary_to_gray(i)
        print(f"{i:>8} {i:>08b} {g:>8} {g:>010b}")


if __name__ == "__main__":
    show_table()
    # Round-trip check
    for i in range(256):
        assert gray_to_binary(binary_to_gray(i)) == i
    print("\nAll round-trip checks passed!")
