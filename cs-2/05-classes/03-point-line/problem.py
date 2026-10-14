import math


class Point:
    def __init__(self, x, y):
        pass

    def __repr__(self):
        pass

    def distance_to(self, other):
        pass


p = Point(3, 4)

print(p)  # (3, 4)
print(p.x)  # 3
print(p.y)  # 4

origin = Point(0, 0)
print(p.distance_to(origin))  # 5.0


class Line:
    def __init__(self, p1, p2):
        pass

    def __repr__(self):
        pass

    def length(self):
        pass

    def slope(self):
        pass


l = Line(Point(0, 0), Point(3, 4))

print(l)  # Line((0, 0), (3, 4))
print(l.p1)  # (0, 0)
print(l.p2)  # (3, 4)
print(l.length())  # 5.0
print(l.slope())  # 1.3333333333333333
