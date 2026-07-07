# fibonacci but make it dramatic
import time

def fib_dramatic(n):
    """Generate fibonacci numbers with theatrical flair."""
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def announce(nums):
    adjectives = [
        "humble", "slightly larger", "suspiciously large",
        "alarmingly large", "astronomically large", "incomprehensibly vast"
    ]
    for i, n in enumerate(nums):
        adj = adjectives[min(i, len(adjectives) - 1)]
        print(f"  And next we have... the {adj} number {n}!")
        time.sleep(0.05)

if __name__ == "__main__":
    print("Ladies and gentlemen, the Fibonacci sequence!")
    print("(Please hold your applause until the end)")
    print()
    nums = fib_dramatic(12)
    announce(nums)
    print()
    print(f"Total drama: {sum(nums)} units")
    print("Thank you, goodnight.")
