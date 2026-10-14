class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r = Rectangle(3, 4)

print(r)  # Rectangle(3, 4)
print(r.width)  # 3
print(r.height)  # 4
print(r.area())  # 12
print(r.perimeter())  # 14
