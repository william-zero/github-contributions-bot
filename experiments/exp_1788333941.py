# Fibonacci Fizzbuzz: Because normal fizzbuzz was too easy
# Prints Fibonacci numbers, but with fizzbuzz rules applied

def fibonacci_fizzbuzz(n):
    a, b = 0, 1
    for _ in range(n):
        if a % 15 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
        a, b = b, a + b

fibonacci_fizzbuzz(20)
