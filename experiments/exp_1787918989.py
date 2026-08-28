# Fun experiment: Fibonacci sequence with memoization
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

# Print first 20 Fibonacci numbers
print("First 20 Fibonacci numbers:")
for i in range(20):
    print(f"  fib({i:2d}) = {fib(i)}")

# Fun fact: The ratio of consecutive Fibonacci numbers approaches the golden ratio
import math
phi = (1 + math.sqrt(5)) / 2
print(f"\nGolden ratio φ ≈ {phi:.10f}")
print(f"fib(20)/fib(19)  = {fib(20)/fib(19):.10f}")
