# Example input:
#
# width (meters): 6
# height (meters): 7
#
# Example output:
#
# area: 42.0m²
# perimiter: 26.0m

width = float(input("width (meters): "))
height = float(input("height (meters): "))

area = width * height
perimiter = 2 * (width + height)

print(f"area: {area}m²")
print(f"perimiter: {perimiter}m")
