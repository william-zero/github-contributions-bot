# Collatz conjecture explorer: pick any number, keep halving evens and tripling+1 odds
# It always reaches 1. Always. (We think.)

def collatz(n):
    steps = []
    while n != 1:
        steps.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps.append(1)
    return steps

def find_longest(limit=1000):
    best_n, best_len = 1, 1
    for n in range(2, limit + 1):
        seq = collatz(n)
        if len(seq) > best_len:
            best_n, best_len = n, len(seq)
    return best_n, best_len

if __name__ == "__main__":
    champion, length = find_longest()
    print(f"Among 1-1000, n={champion} takes the longest Collatz journey: {length} steps")
    print("Sequence:", collatz(27)[:10], "...")
