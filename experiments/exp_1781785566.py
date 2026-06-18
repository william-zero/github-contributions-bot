"""
Collatz sequence explorer — how many steps to reach 1?
"""

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def find_longest_under(limit):
    best_n, best_steps = 1, 0
    for i in range(2, limit):
        s = collatz_steps(i)
        if s > best_steps:
            best_steps = s
            best_n = i
    return best_n, best_steps

if __name__ == "__main__":
    print("Collatz sequence lengths (n → steps to reach 1):")
    for n in [6, 11, 27, 97, 100]:
        print(f"  {n:>4}: {collatz_steps(n)} steps")

    print()
    champion, steps = find_longest_under(1000)
    print(f"Under 1000, longest chain: n={champion} ({steps} steps)")
