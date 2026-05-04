"""
Collatz conjecture explorer — pick any positive integer,
apply n/2 if even, 3n+1 if odd, repeat until you reach 1.
Nobody has proven it always works. It always works.
"""

def collatz(n):
    steps = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps.append(n)
    return steps

def find_longest_sequence(limit=1000):
    champion = (0, 0, [])
    for start in range(1, limit + 1):
        seq = collatz(start)
        if len(seq) > champion[1]:
            champion = (start, len(seq), seq)
    return champion

if __name__ == "__main__":
    n, steps, seq = find_longest_sequence(1000)
    print(f"Most stubborn number under 1000: {n}")
    print(f"Takes {steps} steps to surrender and reach 1")
    print(f"Peak value reached: {max(seq)}")
    print(f"\nFirst 10 steps from {n}: {seq[:10]}...")
    print("\nSome quick examples:")
    for num in [6, 27, 42, 97]:
        s = collatz(num)
        print(f"  {num} → {len(s)} steps, peak={max(s)}")
