# Binary search visualizer with step counter
def binary_search_verbose(arr, target):
    left, right = 0, len(arr) - 1
    steps = 0
    while left <= right:
        mid = (left + right) // 2
        steps += 1
        print(f"Step {steps}: checking index {mid} (value={arr[mid]}), range=[{left},{right}]")
        if arr[mid] == target:
            print(f"Found {target} at index {mid} in {steps} steps!")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Target {target} not found after {steps} steps.")
    return -1

data = list(range(0, 100, 2))  # even numbers 0-98
binary_search_verbose(data, 42)
binary_search_verbose(data, 77)
