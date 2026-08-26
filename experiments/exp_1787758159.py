"""
Collatz conjecture visualizer.
Take any positive integer, if even divide by 2, if odd multiply by 3 and add 1.
Repeat. Conjecture: you always eventually reach 1. (Nobody has proven it.)
"""

def collatz_steps(n):
    steps = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps.append(n)
    return steps

if __name__ == "__main__":
    # Find the starting number under 100 with the most steps
    longest = max(range(1, 101), key=lambda n: len(collatz_steps(n)))
    seq = collatz_steps(longest)
    print(f"Starting at {longest} takes {len(seq)-1} steps to reach 1")
    print(f"Peak value reached: {max(seq)}")
    print(f"First 10 steps: {seq[:10]}")
