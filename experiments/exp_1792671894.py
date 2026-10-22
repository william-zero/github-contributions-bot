# Fibonacci sequence with a twist: also prints if the number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_prime_hunt(limit=20):
    a, b = 0, 1
    results = []
    for _ in range(limit):
        label = " <-- PRIME!" if is_prime(a) else ""
        results.append(f"{a}{label}")
        a, b = b, a + b
    return results

if __name__ == "__main__":
    print("Fibonacci numbers with prime spotting:")
    for line in fibonacci_prime_hunt():
        print(line)
