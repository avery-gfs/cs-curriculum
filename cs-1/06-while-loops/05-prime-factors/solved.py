# Print the prime factors of a given number, from smallest to largest.
#
# Example:
#
# Enter a number: 60
# 2
# 2
# 3
# 5
#
# Example:
#
# Enter a number: 17
# 17

n = int(input("Enter a number: "))

factor = 2

while n > 1:
    if n % factor == 0:
        print(factor)
        n //= factor
    else:
        factor += 1
