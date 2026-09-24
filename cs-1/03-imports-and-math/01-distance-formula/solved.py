# Write a program that gets the coordinates of two points as input from the
# user, and prints the distance between them, using the math library.
#
# The distance between two points is:
#
# distance = sqrt((x₂ - x₁)² + (y₂ - y₁)²)
#
# Round the distance to two decimal places.
#
# Examples:
#
# x1: 1
# y1: 2
# x2: 4
# y2: 6
# Distance: 5.0
#
# x1: 0
# y1: 0
# x2: 1
# y2: 1
# Distance: 1.41

import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

dx = x2 - x1
dy = y2 - y1
distance = math.sqrt(dx**2 + dy**2)  # Could also use math.hypot(dx, dy)

print(f"Distance: {round(distance, 2)}")
