# Example input:
#
# width (meters): 6
# height (meters): 7
#
# Example output:
#
# area: 42.0m²
# perimeter: 26.0m

width = float(input("width (meters): "))
height = float(input("height (meters): "))

area = width * height
perimeter = 2 * (width + height)

print(f"area: {area}m²")
print(f"perimeter: {perimeter}m")
