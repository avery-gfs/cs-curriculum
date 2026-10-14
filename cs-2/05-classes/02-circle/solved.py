import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(10)

print(c)  # Circle(10)
print(c.radius)  # 10
print(c.area())  # 314.1592653589793
print(c.perimeter())  # 62.83185307179586
