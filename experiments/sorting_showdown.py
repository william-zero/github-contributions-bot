"""
Sorting Showdown
================
Implementing sorting algorithms nobody asked for.
May the best O(n) win. (spoiler: none of these are O(n))
"""

import random
import time


def sleep_sort(arr: list[int]) -> list[int]:
    """Sort by sleeping. O(max(arr)) time. Genius or insanity?"""
    import threading

    result = []
    lock = threading.Lock()

    def sleep_and_append(val):
        time.sleep(val * 0.001)
        with lock:
            result.append(val)

    threads = [threading.Thread(target=sleep_and_append, args=(v,)) for v in arr]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result


def bogo_sort(arr: list[int], max_attempts: int = 10000) -> list[int]:
    """The Monte Carlo of sorting. Shuffle until sorted."""
    arr = arr.copy()
    attempts = 0
    while arr != sorted(arr) and attempts < max_attempts:
        random.shuffle(arr)
        attempts += 1
    return arr


def gravity_sort(arr: list[int]) -> list[int]:
    """Also known as Bead Sort. Let gravity do the work."""
    if not arr:
        return []
    max_val = max(arr)
    grid = [[0] * max_val for _ in range(len(arr))]
    for i, val in enumerate(arr):
        for j in range(val):
            grid[i][j] = 1
    for j in range(max_val):
        count = sum(grid[i][j] for i in range(len(arr)))
        for i in range(len(arr)):
            grid[i][j] = 1 if i >= len(arr) - count else 0
    return [sum(row) for row in grid]


def pancake_sort(arr: list[int]) -> list[int]:
    """Sort by flipping pancakes. A real algorithm. Seriously."""
    arr = arr.copy()
    n = len(arr)
    for size in range(n, 1, -1):
        max_idx = arr.index(max(arr[:size]))
        if max_idx != size - 1:
            arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
            arr[:size] = reversed(arr[:size])
    return arr


def benchmark(sort_func, arr, name):
    start = time.perf_counter()
    result = sort_func(arr.copy())
    elapsed = time.perf_counter() - start
    is_sorted = result == sorted(arr)
    print(f"  {name:20s} | {elapsed:8.4f}s | {'OK' if is_sorted else 'FAIL'}")
    return elapsed


if __name__ == "__main__":
    test_data = [random.randint(1, 50) for _ in range(10)]
    print(f"Input: {test_data}\n")
    print(f"  {'Algorithm':20s} | {'Time':>8s} | Status")
    print(f"  {'-'*20} | {'-'*8} | ------")

    benchmark(gravity_sort, test_data, "Gravity Sort")
    benchmark(pancake_sort, test_data, "Pancake Sort")
    benchmark(sleep_sort, test_data, "Sleep Sort")
    # bogo_sort intentionally last - it might take a while
    small_data = test_data[:5]
    benchmark(bogo_sort, small_data, "Bogo Sort (5 items)")
