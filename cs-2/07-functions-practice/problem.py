def test(result, expected):
    if result != expected:
        print("!!!!! FAIL !!!!!\n")

    else:
        print("----- PASS -----\n")

    print(result)
    print()


# ----------------------------------------------------------

# Write cToF(c), which converts a temperature in Celsius to Fahrenheit.


def cToF():
    pass


test(cToF(25), 77)
test(cToF(0), 32)
test(cToF(100), 212)

# ----------------------------------------------------------

# Write absValue(n), which returns the absolute value of n.
# Don't use the built-in abs function.


def absValue():
    pass


test(absValue(-5), 5)
test(absValue(5), 5)
test(absValue(0), 0)

# ----------------------------------------------------------

# Write grayscale(r, g, b), which returns the average of r, g, and b,
# rounded to the nearest whole number.


def grayscale():
    pass


test(grayscale(0, 0, 0), 0)
test(grayscale(255, 255, 255), 255)
test(grayscale(10, 20, 30), 20)

# ----------------------------------------------------------

# Write clamp(n, low, hi), which returns n if it is between low and hi,
# low if n is too small, and hi if n is too big. Assume low <= hi.


def clamp():
    pass


test(clamp(5, 0, 10), 5)
test(clamp(-1, 0, 10), 0)
test(clamp(11, 0, 10), 10)

# ----------------------------------------------------------

# Write letterGrade(points), which returns "A" for 90 and up, "B" for
# 80-89, "C" for 70-79, "D" for 60-69, and "F" for anything lower.


def letterGrade():
    pass


test(letterGrade(99), "A")
test(letterGrade(88), "B")
test(letterGrade(77), "C")
test(letterGrade(66), "D")
test(letterGrade(55), "F")

# ----------------------------------------------------------

# Write product(numbers), which returns all the numbers multiplied together.
# Assume numbers is not empty.


def product():
    pass


test(product([1, 2, 3, 4]), 24)
test(product([4, 5, 6, 0]), 0)

# ----------------------------------------------------------

# Write middle(values), which returns a new list with the first and
# last items removed. Assume values has at least 2 items.


def middle():
    pass


test(middle([1, 2, 3, 4, 5]), [2, 3, 4])

# ----------------------------------------------------------

# Write countEven(numbers), which returns how many of the numbers are even.


def countEven():
    pass


test(countEven([]), 0)
test(countEven([1, 2, 3, 4, -2, 0]), 4)

# ----------------------------------------------------------

# Write negate(numbers), which changes the list so that every number is
# negated. It should change the original list and not return anything.


def negate():
    pass


numbers = [1, -2, 0]
negate(numbers)
test(numbers, [-1, 2, 0])

# ----------------------------------------------------------

# Write negateCopy(numbers), which returns a new list with every number
# negated. The original list should not change.


def negateCopy():
    pass


numbers = [2, -4, 0]
test(negateCopy(numbers), [-2, 4, 0])
test(numbers, [2, -4, 0])

# ----------------------------------------------------------

# Write filterNegs(numbers), which returns a new list with the negative
# numbers removed, keeping the rest in the same order.


def filterNegs():
    pass


test(filterNegs([]), [])
test(filterNegs([3, -1, 0, -4, 2]), [3, 0, 2])

# ----------------------------------------------------------

# Write areUnique(values), which returns True if no value appears more
# than once, and False otherwise.


def areUnique():
    pass


test(areUnique([]), True)
test(areUnique([1, 2, 3]), True)
test(areUnique([1, 2, 1]), False)

# ----------------------------------------------------------

# Write isSorted(numbers), which returns True if the numbers are in
# increasing order (equal neighbors are fine), and False otherwise.


def isSorted():
    pass


test(isSorted([]), True)
test(isSorted([1, 2, 2, 3]), True)
test(isSorted([1, 3, 2, 4]), False)

# ----------------------------------------------------------

# Write swap(values, i, j), which swaps the items at indexes i and j.
# It should change the original list and not return anything.
# Assume i and j are valid indexes.


def swap():
    pass


values = ["a", "b", "c"]
swap(values, 0, 2)
test(values, ["c", "b", "a"])

# ----------------------------------------------------------

# Write strongPassword(password), which returns True if the password
# has at least 8 characters, at least one digit, and at least one
# uppercase letter, and False otherwise.
#
# Hint: look up the string methods isdigit and isupper.


def strongPassword():
    pass


test(strongPassword("Abcdefg1"), True)
test(strongPassword("Abcde1"), False)
test(strongPassword("abcdefg1"), False)
test(strongPassword("Abcdefgh"), False)

# ----------------------------------------------------------

# Write isPalindrome(text), which returns True if text reads the same
# forwards and backwards, and False otherwise.


def isPalindrome():
    pass


test(isPalindrome(""), True)
test(isPalindrome("a"), True)
test(isPalindrome("racecar"), True)
test(isPalindrome("abca"), False)
