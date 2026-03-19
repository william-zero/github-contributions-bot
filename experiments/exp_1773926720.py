# Bubble Sort Contemplation

def bubble_sort_of_chaos(arr):
    """A sorting algorithm that questions its own existence."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Early exit - why sort if already sorted?
    return arr

# Test the philosophy
chaos = [64, 34, 25, 12, 22, 11, 90]
print(f"Before: {chaos}")
print(f"After: {bubble_sort_of_chaos(chaos)}")
print("Order from chaos. Beauty in simplicity.")
