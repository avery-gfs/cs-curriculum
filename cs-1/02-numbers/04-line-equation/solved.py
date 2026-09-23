# Write a program that gets the coordinates of two points as input from the
# user, and prints the equation of the line that passes through them.
#
# The slope m and y-intercept b of the line are:
#
#     y₂ - y₁
# m = -------
#     x₂ - x₁
#
# b = y₁ - m * x₁
#
# The equation of the line is y = mx + b.
#
# Example:
#
# x1: 1
# y1: 3
# x2: 3
# y2: 7
# y = 2.0x + 1.0

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

slope = (y2 - y1) / (x2 - x1)
intercept = y1 - slope * x1

print(f"y = {slope}x + {intercept}")
