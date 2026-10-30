import os
import time


# ---------------------------------------------------------


def test(result, expected):
    if result != expected:
        print("!!!!! FAIL !!!!!\n")

    else:
        print("----- PASS -----\n")

    print(result)
    print()


# ---------------------------------------------------------


def lastDigit(n):
    # Return the last digit of an integer `n`
    return n % 10


test(lastDigit(5678), 8)


# ---------------------------------------------------------


def isEven(n):
    # Check whether an integer `n` is even
    return n % 2 == 0


test(isEven(-4), True)
test(isEven(5), False)


# ---------------------------------------------------------


def isWhole(n):
    # Check whether a number `n` is an integer
    return n % 1 == 0


test(isWhole(2), True)
test(isWhole(2.5), False)


# ---------------------------------------------------------


def gcd(a, b):
    # Get the greatest common divisor of two integers `a` and `b`

    # There are more efficient ways to do this, such as
    # the euclidean algorithm

    result = 1

    for div in range(1, min(a, b)):
        if a % div == 0 and b % div == 0:
            result = div

    return result


test(gcd(12, 20), 4)


# ---------------------------------------------------------


def calcDay(today, n):
    # Figure out what day it will be `n` days from now
    #
    # Hint: use the `.index()` method of list

    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]

    index = days.index(today)
    return days[(index + n) % 7]


test(calcDay("monday", 100), "wednesday")


# ---------------------------------------------------------


def showHeight(totalInches):
    # Display a height (given in inches) as feet and inch components

    inches = totalInches % 12
    feet = totalInches // 12
    return f"{feet}'{inches:02}\""


test(showHeight(66), "5'06\"")


# ---------------------------------------------------------


def factors(n):
    # Get a list of the factors of an integer `n`

    return [f for f in range(1, n + 1) if n % f == 0]


test(factors(40), [1, 2, 4, 5, 8, 10, 20, 40])


# ---------------------------------------------------------


def loading():
    # Display an animated loading bar

    for n in range(10):
        print("loading" + "." * (n % 5))
        time.sleep(0.2)

        # This code to clears the current line:
        print("\x1b[1A\x1b[2K", end="")


loading()


# ---------------------------------------------------------


def randomNums(seed):
    # Generate a list of 10 paeuso-random numbers using the LCG algorithm
    # https://en.wikipedia.org/wiki/Linear_congruential_generator

    n = seed
    m = 2**32
    a = 1664525
    c = 1013904223

    result = []

    for _ in range(10):
        result.append(n / m)
        n = (n * a + c) % m

    return result


print(randomNums(17))
