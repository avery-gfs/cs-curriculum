import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)


p = Point(3, 4)

print(p)  # (3, 4)
print(p.x)  # 3
print(p.y)  # 4

origin = Point(0, 0)
print(p.distance_to(origin))  # 5.0


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

    def length(self):
        return self.p1.distance_to(self.p2)

    def slope(self):
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        return dy / dx


l = Line(Point(0, 0), Point(3, 4))

print(l)  # Line((0, 0), (3, 4))
print(l.p1)  # (0, 0)
print(l.p2)  # (3, 4)
print(l.length())  # 5.0
print(l.slope())  # 1.3333333333333333
