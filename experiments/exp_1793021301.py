# Fibonacci spiral ratio checker
# Computes ratios of consecutive Fibonacci numbers and shows convergence to golden ratio

def fibonacci_ratios(n=20):
    a, b = 1, 1
    ratios = []
    for _ in range(n):
        ratios.append(b / a)
        a, b = b, a + b
    return ratios

PHI = (1 + 5 ** 0.5) / 2

print(f"Golden ratio (phi): {PHI:.10f}")
print()
print(f"{'Step':>4}  {'Ratio':>14}  {'Error':>14}")
print("-" * 36)
for i, r in enumerate(fibonacci_ratios()):
    print(f"{i+1:>4}  {r:>14.10f}  {abs(r - PHI):>14.2e}")
