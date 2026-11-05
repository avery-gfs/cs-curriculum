# Determine whether a given number is prime. Assume the number is at least 2.
#
# A number is prime if it has no factors other than 1 and itself.
#
# Example:
#
# Enter a number: 17
# Prime
#
# Example:
#
# Enter a number: 51
# Not prime

n = int(input("Enter a number: "))

isPrime = True
factor = 2

while factor < n:
    if n % factor == 0:
        isPrime = False

    factor += 1

if isPrime:
    print("Prime")
else:
    print("Not prime")
