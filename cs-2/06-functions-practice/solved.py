def test(result, expected):
    if result != expected:
        print("!!!!! FAIL !!!!!\n")

    else:
        print("----- PASS: -----\n")

    print(result)
    print()


# ----------------------------------------------------------

# Write cToF(c), which converts a temperature in Celsius to Fahrenheit.


def cToF(c):
    return 32 + 9 / 5 * c


test(cToF(25), 77)
test(cToF(0), 32)
test(cToF(100), 212)

# ----------------------------------------------------------

# Write absValue(n), which returns the absolute value of n.
# Don't use the built-in abs function.


def absValue(n):
    if n < 0:
        return -n

    return n


# def absValue(n):
# 	return -n if n < 0 else n

test(absValue(-5), 5)
test(absValue(5), 5)
test(absValue(0), 0)

# ----------------------------------------------------------

# Write grayscale(r, g, b), which returns the average of r, g, and b,
# rounded to the nearest whole number.


def grayscale(r, g, b):
    return round((r + g + b) / 3)


test(grayscale(0, 0, 0), 0)
test(grayscale(255, 255, 255), 255)
test(grayscale(10, 20, 30), 20)

# ----------------------------------------------------------

# Write clamp(n, low, hi), which returns n if it is between low and hi,
# low if n is too small, and hi if n is too big. Assume low <= hi.


def clamp(n, low, hi):
    if n < low:
        return low

    if n > hi:
        return hi

    return n


# def clamp(n, low, hi):
# 	return min(hi, max(low, n))

test(clamp(5, 0, 10), 5)
test(clamp(-1, 0, 10), 0)
test(clamp(11, 0, 10), 10)

# ----------------------------------------------------------

# Write letterGrade(points), which returns "A" for 90 and up, "B" for
# 80-89, "C" for 70-79, "D" for 60-69, and "F" for anything lower.


def letterGrade(points):
    if points >= 90:
        return "A"

    if points >= 80:
        return "B"

    if points >= 70:
        return "C"

    if points >= 60:
        return "D"

    return "F"


# def letterGrade(points):
# 	return { 10: "A", 9: "A", 8: "B", 7: "C", 6: "D" }.get(points // 10, "F")

test(letterGrade(100), "A")
test(letterGrade(90), "A")
test(letterGrade(89), "B")
test(letterGrade(70), "C")
test(letterGrade(60), "D")
test(letterGrade(59), "F")

# ----------------------------------------------------------

# Write product(numbers), which returns all the numbers multiplied together.
# Assume numbers is not empty.


def product(numbers):
    result = 1

    for n in numbers:
        result *= n

    return result


test(product([1, 2, 3, 4]), 24)
test(product([4, 5, 6, 0]), 0)

# ----------------------------------------------------------

# Write middle(values), which returns a new list with the first and
# last items removed. Assume values has at least 2 items.


def middle(values):
    return values[1:-1]


test(middle([1, 2, 3, 4, 5]), [2, 3, 4])

# ----------------------------------------------------------

# Write countEven(numbers), which returns how many of the numbers are even.


def countEven(numbers):
    result = 0

    for n in numbers:
        if n % 2 == 0:
            result += 1

    return result


# def countEven(numbers):
# 	return sum(n % 2 == 0 for n in numbers)

test(countEven([]), 0)
test(countEven([1, 2, 3, 4, -2, 0]), 4)

# ----------------------------------------------------------

# Write negate(numbers), which changes the list so that every number is
# negated. It should change the original list and not return anything.


def negate(numbers):
    for i in range(len(numbers)):
        numbers[i] *= -1


numbers = [1, -2, 0]
negate(numbers)
test(numbers, [-1, 2, 0])

# ----------------------------------------------------------

# Write negateCopy(numbers), which returns a new list with every number
# negated. The original list should not change.


def negateCopy(numbers):
    result = []

    for n in numbers:
        result.append(-n)

    return result


# def negateCopy(numbers):
# 	return [-n for n in numbers]

numbers = [2, -4, 0]
test(negateCopy(numbers), [-2, 4, 0])
test(numbers, [2, -4, 0])

# ----------------------------------------------------------

# Write filterNegs(numbers), which returns a new list with the negative
# numbers removed, keeping the rest in the same order.


def filterNegs(numbers):
    result = []

    for n in numbers:
        if n >= 0:
            result.append(n)

    return result


# def filterNegs(numbers):
# 	return [n for n in numbers if n >= 0]

test(filterNegs([]), [])
test(filterNegs([3, -1, 0, -4, 2]), [3, 0, 2])

# ----------------------------------------------------------

# Write areUnique(values), which returns True if no value appears more
# than once, and False otherwise.


def areUnique(values):
    return len(set(values)) == len(values)


test(areUnique([]), True)
test(areUnique([1, 2, 3]), True)
test(areUnique([1, 2, 1]), False)

# ----------------------------------------------------------

# Write isSorted(numbers), which returns True if the numbers are in
# increasing order (equal neighbors are fine), and False otherwise.


def isSorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i - 1] > numbers[i]:
            return False

    return True


# def isSorted(numbers):
# 	return all(numbers[i - 1] <= numbers[i] for i in range(1, len(numbers)))

test(isSorted([]), True)
test(isSorted([1, 2, 2, 3]), True)
test(isSorted([1, 3, 2, 4]), False)

# ----------------------------------------------------------

# Write swap(values, i, j), which swaps the items at indexes i and j.
# It should change the original list and not return anything.
# Assume i and j are valid indexes.


def swap(values, i, j):
    tmp = values[i]
    values[i] = values[j]
    values[j] = tmp


# def swap(values, i, j):
# 	values[i], values[j] = values[j], values[i]

values = ["a", "b", "c"]
swap(values, 0, 2)
test(values, ["c", "b", "a"])

# ----------------------------------------------------------

# Write strongPassword(password), which returns True if the password
# has at least 8 characters, at least one digit, and at least one
# uppercase letter, and False otherwise.
#
# Hint: look up the string methods isdigit and isupper.


def strongPassword(password):
    if len(password) < 8:
        return False

    hasDigit = False
    hasUpper = False

    for c in password:
        if c.isdigit():
            hasDigit = True

        if c.isupper():
            hasUpper = True

    return hasDigit and hasUpper


# def strongPassword(password):
# 	return (
# 		len(password) >= 8 and
# 		any(c.isupper() for c in password) and
# 		any(c.isdigit() for c in password)
# 	)

test(strongPassword("Abcdefg1"), True)
test(strongPassword("Abcde1"), False)
test(strongPassword("abcdefg1"), False)
test(strongPassword("Abcdefgh"), False)

# ----------------------------------------------------------

# Write isPalindrome(text), which returns True if text reads the same
# forwards and backwards, and False otherwise.


def isPalindrome(text):
    for i in range(len(text) // 2):
        if text[i] != text[-1 - i]:
            return False

    return True


# def isPalindrome(text):
# 	return text == text[::-1]

test(isPalindrome(""), True)
test(isPalindrome("a"), True)
test(isPalindrome("racecar"), True)
test(isPalindrome("abba"), True)
test(isPalindrome("abca"), False)
