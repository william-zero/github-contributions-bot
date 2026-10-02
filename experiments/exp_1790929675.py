"""Fibonacci sequence variants: classic, memoized, and matrix exponentiation."""

from functools import lru_cache


def fib_classic(n):
    """Classic iterative Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=None)
def fib_memo(n):
    """Memoized recursive Fibonacci."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_matrix(n):
    """Matrix exponentiation Fibonacci — O(log n)."""
    def mat_mul(A, B):
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]],
        ]

    def mat_pow(M, p):
        if p == 1:
            return M
        if p % 2 == 0:
            half = mat_pow(M, p // 2)
            return mat_mul(half, half)
        return mat_mul(M, mat_pow(M, p - 1))

    if n == 0:
        return 0
    result = mat_pow([[1, 1], [1, 0]], n)
    return result[0][1]


if __name__ == "__main__":
    print("n  | classic | memo | matrix")
    print("-" * 35)
    for n in [0, 1, 5, 10, 20, 30]:
        print(f"{n:2} | {fib_classic(n):7} | {fib_memo(n):4} | {fib_matrix(n)}")
