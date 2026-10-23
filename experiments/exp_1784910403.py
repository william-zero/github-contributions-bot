# Fibonacci spiral: print first N Fibonacci numbers with ASCII art bar
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

def bar(val, max_val, width=40):
    filled = int(val / max_val * width) if max_val else 0
    return '█' * filled + '░' * (width - filled)

nums = fibonacci(15)
max_val = max(nums) if nums else 1
print("Fibonacci Sequence (first 15):\n")
for i, n in enumerate(nums):
    print(f"  F({i:2d}) = {n:5d}  {bar(n, max_val)}")
