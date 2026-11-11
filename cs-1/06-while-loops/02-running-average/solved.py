# Keep track of the average of the integers entered so far.
#
# Example:
#
# Enter a number: 10
# Average: 10.0
# Enter a number: 4
# Average: 7.0
# Enter a number: 4
# Average: 6.0
# Enter a number: 0
# Average: 4.5
# Enter a number: 100
# Average: 23.6
# ...

count = 0
total = 0

while True:
    n = int(input("Enter a number: "))
    total += n
    count += 1

    average = total / count
    print(f"Average: {average}")
