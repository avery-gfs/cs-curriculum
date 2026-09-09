# Write a program to calculate and print the prime factors of the numbers
# 2 through 50 using recursion. You may not use for or while loops. Your
# program output should have the following format:
#
# 2 [2]
# 3 [3]
# 4 [2, 2]
# 5 [5]
# ...


def getFactors(n, d):
    if n == 1:
        return []

    if n % d == 0:
        return [d] + getFactors(n // d, d)

    else:
        return getFactors(n, d + 1)


def loopNums(n):
    factors = getFactors(n, 2)
    print(n, factors)

    if n < 100:
        loopNums(n + 1)


loopNums(2)
