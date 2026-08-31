"""
Mandelbrot set renderer in ASCII - outputs a tiny fractal to the terminal
"""

def mandelbrot(c, max_iter=50):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def render(width=60, height=25, x_min=-2.5, x_max=1.0, y_min=-1.1, y_max=1.1):
    chars = " .:-=+*#%@"
    for row in range(height):
        line = ""
        for col in range(width):
            c = complex(
                x_min + col * (x_max - x_min) / width,
                y_min + row * (y_max - y_min) / height
            )
            m = mandelbrot(c)
            line += chars[m % len(chars)]
        print(line)

if __name__ == "__main__":
    print("Mandelbrot Set:\n")
    render()
