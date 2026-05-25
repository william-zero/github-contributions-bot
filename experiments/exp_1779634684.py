# Collatz conjecture explorer

def collatz_sequence(n):
    """Returns the full Collatz sequence starting from n."""
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

if __name__ == "__main__":
    test_values = [27, 97, 871, 6171]
    print("Collatz Conjecture Explorer")
    print("(Every sequence eventually reaches 1 — probably. Nobody's proven it yet.)\n")
    for start in test_values:
        seq = collatz_sequence(start)
        print(f"Start: {start:6d}  |  Steps: {len(seq)-1:4d}  |  Peak: {max(seq)}")
