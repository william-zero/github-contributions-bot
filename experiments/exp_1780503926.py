# Collatz Conjecture Explorer
# Take any positive integer. If even, divide by 2. If odd, multiply by 3 and add 1.
# Repeat. The conjecture: you always reach 1. Nobody has proven it yet.

def collatz_steps(n):
    steps = 0
    path = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        path.append(n)
        steps += 1
    return steps, path

# Find which numbers under 100 take the most steps
results = [(collatz_steps(i)[0], i) for i in range(2, 101)]
results.sort(reverse=True)

print("Top 5 most stubborn numbers (1-100):")
for steps, num in results[:5]:
    print(f"  {num}: takes {steps} steps to reach 1")

# The champion of champions under 100
worst_steps, worst_num = results[0]
_, path = collatz_steps(worst_num)
print(f"\nFull journey of {worst_num}:")
print(" → ".join(map(str, path[:15])) + ("..." if len(path) > 15 else ""))
print(f"Peak value reached: {max(path)}")
