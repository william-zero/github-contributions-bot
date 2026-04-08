"""
Fibonacci Sequence Generator with Memoization

A simple but elegant demonstration of how memoization can dramatically
improve performance for recursive functions. This script generates Fibonacci
numbers and shows the time difference between memoized and non-memoized approaches.
"""

def fib_memo(n, cache={}):
    """Fibonacci with memoization - O(n) time complexity"""
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

# Generate first 20 Fibonacci numbers
print("First 20 Fibonacci numbers (with memoization):")
for i in range(20):
    print(f"F({i}) = {fib_memo(i)}")
