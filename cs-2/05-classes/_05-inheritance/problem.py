import math


class Triangle:
    # two sides and the angle between them, in degrees
    def __init__(self, side1, angle, side2):
        self.side1 = side1
        self.angle = angle
        self.side2 = side2

    def __repr__(self):
        return f"Triangle({self.side1}, {self.angle}, {self.side2})"

    def side3(self):
        return math.sqrt(
            self.side1**2
            + self.side2**2
            - 2 * self.side1 * self.side2 * math.cos(math.radians(self.angle))
        )

    def area(self):
        return 0.5 * self.side1 * self.side2 * math.sin(math.radians(self.angle))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3()


t = Triangle(3, 60, 3)

print(t)
print(t.side3())
print(t.area())
print(t.perimeter())


class RightTriangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __repr__(self):
        return f"RightTriangle({self.side1}, {self.side2})"

    def side3(self):
        return math.sqrt(self.side1**2 + self.side2**2)

    def area(self):
        return 0.5 * self.side1 * self.side2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3()


rt = RightTriangle(3, 4)

print(rt)
print(rt.side3())
print(rt.area())
print(rt.perimeter())


class IsoscelesTriangle:
    def __init__(self, side, angle):
        self.side1 = side
        self.angle = angle
        self.side2 = side

    def __repr__(self):
        return f"IsoscelesTriangle({self.side1}, {self.angle})"

    def side3(self):
        return math.sqrt(
            self.side1**2
            + self.side2**2
            - 2 * self.side1 * self.side2 * math.cos(math.radians(self.angle))
        )

    def area(self):
        return 0.5 * self.side1 * self.side2 * math.sin(math.radians(self.angle))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3()


it = IsoscelesTriangle(5, 40)

print(it)
print(it.side1 == it.side2)
print(it.area())
print(it.perimeter())


class EquilateralTriangle:
    def __init__(self, side):
        self.side1 = side
        self.angle = 60
        self.side2 = side

    def __repr__(self):
        return f"EquilateralTriangle({self.side1})"

    def side3(self):
        return math.sqrt(
            self.side1**2
            + self.side2**2
            - 2 * self.side1 * self.side2 * math.cos(math.radians(self.angle))
        )

    def area(self):
        return 0.5 * self.side1 * self.side2 * math.sin(math.radians(self.angle))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3()


et = EquilateralTriangle(2)

print(et)
print(et.angle)
print(et.side3())
print(et.area())
print(et.perimeter())


class Parallelogram:
    # two adjacent sides and the angle between them, in degrees
    def __init__(self, side1, angle, side2):
        self.side1 = side1
        self.angle = angle
        self.side2 = side2

    def __repr__(self):
        return f"Parallelogram({self.side1}, {self.angle}, {self.side2})"

    def area(self):
        return self.side1 * self.side2 * math.sin(math.radians(self.angle))

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


p = Parallelogram(4, 30, 3)

print(p)
print(p.area())
print(p.perimeter())


class Rectangle:
    def __init__(self, width, height):
        self.side1 = width
        self.angle = 90
        self.side2 = height
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


r = Rectangle(3, 4)

print(r)
print(r.width)
print(r.height)
print(r.angle)
print(r.area())
print(r.perimeter())


class Square:
    def __init__(self, side):
        self.side1 = side
        self.angle = 90
        self.side2 = side
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square({self.width})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.side1 + self.side2)


s = Square(10)

print(s)
print(s.width)
print(s.area())
print(s.perimeter())
