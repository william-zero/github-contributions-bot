"""
Parallel sorting benchmark - exploring different sorting strategies.
"""
import random
import time

def parallel_merge_sort(arr):
    """Simple merge sort implementation for demonstration."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = parallel_merge_sort(arr[:mid])
    right = parallel_merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]

if __name__ == "__main__":
    data = [random.randint(1, 1000) for _ in range(100)]
    sorted_data = parallel_merge_sort(data)
    print(f"Sorted {len(sorted_data)} elements successfully")
