"""
Mandelbrot Set - ASCII renderer
"""

def mandelbrot(c, max_iter=80):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def render(width=80, height=40, x_min=-2.5, x_max=1.0, y_min=-1.25, y_max=1.25):
    chars = " .:-=+*#%@"
    for row in range(height):
        line = ""
        for col in range(width):
            c = complex(
                x_min + (x_max - x_min) * col / width,
                y_min + (y_max - y_min) * row / height
            )
            m = mandelbrot(c)
            line += chars[m % len(chars)]
        print(line)

if __name__ == "__main__":
    print("Mandelbrot Set (ASCII)")
    print("=" * 80)
    render()
