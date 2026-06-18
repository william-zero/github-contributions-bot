# Gray code generator — adjacent values differ by exactly 1 bit
def gray_code(n):
    return [i ^ (i >> 1) for i in range(1 << n)]

def to_binary(num, bits):
    return format(num, f'0{bits}b')

def print_gray_table(n):
    codes = gray_code(n)
    print(f"Gray code for {n} bits:")
    print(f"{'Index':<8} {'Binary':<12} {'Gray':<12} {'Gray (bin)'}")
    print("-" * 44)
    for i, g in enumerate(codes):
        b = to_binary(i, n)
        gb = to_binary(g, n)
        print(f"{i:<8} {b:<12} {g:<12} {gb}")

if __name__ == "__main__":
    print_gray_table(4)
    print()
    # Verify: each consecutive pair differs by exactly 1 bit
    codes = gray_code(4)
    for a, b in zip(codes, codes[1:]):
        diff = bin(a ^ b).count('1')
        assert diff == 1, f"Oops: {a} and {b} differ by {diff} bits"
    print("Verified: all adjacent values differ by exactly 1 bit.")
