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

print(l)
print(l.p1)
print(l.p2)
print(l.length())
print(l.slope())
