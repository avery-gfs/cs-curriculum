# Keep track of the largest integer entered so far. Assume that the largest
# number is 0 to start.
#
# Example:
#
# Enter a number: 9
# Maximum: 9
# Enter a number: 90
# Maximum: 90
# Enter a number: 7
# Maximum: 90
# Enter a number: 100
# Maximum: 100
# ...

maximum = 0

while True:
    n = int(input("Enter a number: "))
    maximum = max(maximum, n)

    print(f"Maximum: {maximum}")
