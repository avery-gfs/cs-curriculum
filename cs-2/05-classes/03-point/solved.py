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


p = Point(1, 2)

print(p)
print(p.x)
print(p.y)

origin = Point(0, 0)
print(p.distance_to(origin))
