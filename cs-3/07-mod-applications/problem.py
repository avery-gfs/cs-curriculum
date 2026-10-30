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
    pass


test(lastDigit(5678), 8)


# ---------------------------------------------------------


def isEven(n):
    # Check whether an integer `n` is even
    pass


test(isEven(-4), True)
test(isEven(5), False)


# ---------------------------------------------------------


def isWhole(n):
    # Check whether a number `n` is an integer
    pass


test(isWhole(2), True)
test(isWhole(2.5), False)


# ---------------------------------------------------------


def gcd(a, b):
    # Get the greatest common divisor of two integers `a` and `b`
    pass


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

    pass


test(calcDay("monday", 100), "wednesday")


# ---------------------------------------------------------


def showHeight(totalInches):
    # Display a height (given in inches) as feet and inch components
    pass


test(showHeight(66), "5'06\"")


# ---------------------------------------------------------


def factors(n):
    # Get a list of the factors of an integer `n`
    pass


test(factors(40), [1, 2, 4, 5, 8, 10, 20, 40])


# ---------------------------------------------------------


def loading():
    # Display an animated loading bar
    pass


loading()


# ---------------------------------------------------------


def randomNums(seed):
    # Generate a list of 10 paeuso-random numbers using the LCG algorithm
    # https://en.wikipedia.org/wiki/Linear_congruential_generator

    n = seed
    m = 2**32
    a = 1664525
    c = 1013904223

    pass


print(randomNums(17))
