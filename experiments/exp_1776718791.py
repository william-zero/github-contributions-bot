# weekend experiment: a tiny spirograph pattern generator using turtle-style math
import math

def spirograph(R, r, d, steps=1000):
    points = []
    for i in range(steps):
        t = 2 * math.pi * i / steps
        x = (R - r) * math.cos(t) + d * math.cos((R - r) * t / r)
        y = (R - r) * math.sin(t) - d * math.sin((R - r) * t / r)
        points.append((round(x, 4), round(y, 4)))
    return points

if __name__ == "__main__":
    pts = spirograph(R=5, r=3, d=5)
    print(f"spirograph with {len(pts)} points")
    print(f"first: {pts[0]}, last: {pts[-1]}")
    span_x = max(p[0] for p in pts) - min(p[0] for p in pts)
    span_y = max(p[1] for p in pts) - min(p[1] for p in pts)
    print(f"bounding box: {span_x:.2f} x {span_y:.2f}")
