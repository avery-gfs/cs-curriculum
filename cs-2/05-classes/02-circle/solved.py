import math


class Square:
    def __init__(self, width):
        self.width = width

    def __repr__(self):
        return f"Square({self.width})"

    def area(self):
        return self.width**2

    def perimeter(self):
        return 4 * self.width


s = Square(10)

print(s)
print(s.width)
print(s.area())
print(s.perimeter())
