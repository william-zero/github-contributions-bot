#!/usr/bin/env python3
"""Mandelbrot Set ASCII Renderer"""

def mandelbrot(c, max_iter=100):
    """Calculate Mandelbrot set iterations for a complex number"""
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Render a tiny Mandelbrot fractal
width, height = 60, 20
for y in range(height):
    row = ""
    for x in range(width):
        # Map pixel to complex plane
        real = (x / width) * 3.5 - 2.5
        imag = (y / height) * 2 - 1
        c = complex(real, imag)
        
        iterations = mandelbrot(c)
        chars = " .:-=+*#%@"
        row += chars[min(iterations // 10, len(chars) - 1)]
    print(row)
