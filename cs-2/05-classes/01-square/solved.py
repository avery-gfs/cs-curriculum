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

print(s)  # Square(10)
print(s.width)  # 10
print(s.area())  # 100
print(s.perimeter())  # 40
