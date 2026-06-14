"""
prime_rain.py — visualize primes falling like rain in the terminal
"""
import time
import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_rain(width=40, count=20):
    primes = [n for n in range(2, 300) if is_prime(n)]
    for _ in range(count):
        pos = random.randint(0, width - 5)
        p = random.choice(primes)
        line = " " * pos + str(p)
        print(line)
        time.sleep(0.07)

if __name__ == "__main__":
    print("=== Prime Rain ===")
    prime_rain()
    print("=== done ===")
