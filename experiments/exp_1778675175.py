"""
Mandelbrot Set ASCII renderer - explore fractal complexity with just text!
"""

def mandelbrot(c, max_iter=50):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def render(x_min=-2.5, x_max=1.0, y_min=-1.25, y_max=1.25, width=70, height=30):
    chars = " .:-=+*#%@"
    for row in range(height):
        line = ""
        y = y_min + (y_max - y_min) * row / height
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            m = mandelbrot(complex(x, y))
            line += chars[m % len(chars)]
        print(line)

if __name__ == "__main__":
    print("=== Mandelbrot Set ===")
    render()
    print("\nZoomed into seahorse valley:")
    render(x_min=-0.8, x_max=-0.6, y_min=0.0, y_max=0.2, width=70, height=25)
