"""Fibonacci sequence via recursion, memoization, and generator — three ways, one result."""

from functools import lru_cache

def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

def fib_generator(limit: int):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    n = 10
    print(f"Recursive fib({n})  = {fib_memo(n)}")
    print(f"Memoized  fib({n})  = {fib_memo(n)}")
    print(f"Generator up to 100: {list(fib_generator(100))}")
