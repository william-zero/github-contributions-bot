"""Binary search — find a target in a sorted list efficiently."""

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

nums = list(range(0, 100, 2))  # even numbers 0-98
for t in [42, 57, 0, 98]:
    idx = binary_search(nums, t)
    print(f"search({t}) -> index {idx}" + ("" if idx == -1 else f" (value={nums[idx]})"))
