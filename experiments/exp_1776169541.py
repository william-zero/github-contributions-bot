#!/usr/bin/env python3
"""
Prime Spiral Generator
Generates a visual spiral of prime numbers using ASCII art.
Perfect for turning math into pixels!
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_spiral(size=7):
    """Generate a square spiral matrix"""
    matrix = [[0] * size for _ in range(size)]
    num = 1
    top, bottom, left, right = 0, size - 1, 0, size - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1
        
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    
    return matrix

if __name__ == "__main__":
    spiral = generate_spiral(7)
    print("Prime Spiral (7x7):\n")
    for row in spiral:
        line = ""
        for num in row:
            marker = "✨" if is_prime(num) else "  "
            line += f"{num:2d}{marker} "
        print(line)
