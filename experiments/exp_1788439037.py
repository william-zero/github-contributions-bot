"""
Fibonacci but make it dramatic.
"""

def fib_dramatic(n):
    """Generate Fibonacci numbers with commentary."""
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        if a > 1000:
            print(f"  #{i}: {a} (getting wild...)")
        elif a > 100:
            print(f"  #{i}: {a} (heating up)")
        else:
            print(f"  #{i}: {a}")
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    print("The Fibonacci Sequence: A Journey\n")
    result = fib_dramatic(15)
    print(f"\nFinal total: {sum(result)}")
    print(f"Peak value: {max(result)}")
