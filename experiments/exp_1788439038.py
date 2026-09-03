"""
Mandelbrot Set renderer in ASCII — because pixels are overrated
"""
import sys

def mandelbrot(c, max_iter=80):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def render(x_min=-2.5, x_max=1.0, y_min=-1.2, y_max=1.2, width=60, height=30):
    chars = " .:-=+*#%@"
    for row in range(height):
        line = ""
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            y = y_min + (y_max - y_min) * row / height
            m = mandelbrot(complex(x, y))
            line += chars[m * (len(chars) - 1) // 80]
        print(line)

if __name__ == "__main__":
    print("Mandelbrot Set (ASCII)")
    print("=" * 60)
    render()
