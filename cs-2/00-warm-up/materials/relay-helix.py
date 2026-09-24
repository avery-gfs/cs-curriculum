import math
import time


def height(n):
    return round(10 + 10 * math.cos(n / 4))


for n in range(60):
    a = height(n)
    b = height(n + 6)
    before = " " * min(a, b)
    between = "." * abs(a - b)
    print(f"{before}*{between}*")
    time.sleep(0.04)
