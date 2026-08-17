"""
Fibonacci sequence with memoization vs naive recursion — speed comparison
"""
import time

def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

cache = {}
def fib_memo(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return cache[n]

def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

for n in [10, 20, 30]:
    t0 = time.time()
    naive = fib_naive(n)
    t_naive = time.time() - t0

    t0 = time.time()
    memo = fib_memo(n)
    t_memo = time.time() - t0

    t0 = time.time()
    it = fib_iter(n)
    t_iter = time.time() - t0

    print(f"fib({n}) = {naive}")
    print(f"  naive: {t_naive:.6f}s | memo: {t_memo:.8f}s | iter: {t_iter:.8f}s")
    print()
