"""
Fibonacci Feud: Three algorithms walk into a bar and race to the nth number.
"""

import time


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def fib_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


def race(n):
    print(f"Fibonacci({n}) race:")
    
    for name, fn in [("recursive", fib_recursive), ("iterative", fib_iterative), ("memoized", fib_memoized)]:
        start = time.perf_counter()
        result = fn(n)
        elapsed = time.perf_counter() - start
        print(f"  {name:12s}: {result} in {elapsed:.6f}s")


if __name__ == "__main__":
    for n in [10, 20, 30]:
        race(n)
        print()
