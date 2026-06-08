"""Mandelbrot set ASCII renderer with zoom and iteration control."""

def mandelbrot(c, max_iter=80):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def render(x_min=-2.5, x_max=1.0, y_min=-1.25, y_max=1.25, width=70, height=35):
    chars = " .,:;i+hHM#@"
    for row in range(height):
        line = ""
        for col in range(width):
            x = x_min + (x_max - x_min) * col / width
            y = y_min + (y_max - y_min) * row / height
            m = mandelbrot(complex(x, y))
            line += chars[min(m * len(chars) // 81, len(chars) - 1)]
        print(line)

if __name__ == "__main__":
    print("Mandelbrot Set (full view)")
    render()
    print("\nZoomed into the seahorse valley")
    render(x_min=-0.76, x_max=-0.74, y_min=0.09, y_max=0.11, width=70, height=35)
