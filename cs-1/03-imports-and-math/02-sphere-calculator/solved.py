# Write a program that gets the radius of a sphere as input from the user, and
# prints the sphere's volume and surface area, using the math library.
#
# volume = (4 / 3) * pi * radius³
# surface area = 4 * pi * radius²
#
# Round both results to two decimal places.
#
# Examples:
#
# Radius: 2
# Volume: 33.51
# Surface area: 50.27
#
# Radius: 3
# Volume: 113.1
# Surface area: 113.1

import math

radius = float(input("Radius: "))

volume = (4 / 3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

print(f"Volume: {round(volume, 2)}")
print(f"Surface area: {round(surface_area, 2)}")
