def factorial(n):
    # Calculate the factorial of `n` recursively

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(10))  # Should print 3628800


def power2(n):
    # Calculate the `2 ** n` recursively, without using the
    # built-in exponentiation functionality

    if n == 0:
        return 1

    return 2 * power2(n - 1)


print(power2(10))  # Should print 1024


def fibonacci(n):
    # Calculate the nth fibonacci number recursively

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Should print 55


def total(numbers, index):
    # Calculate the sum of the numbers in a list recursively

    if index == len(numbers):
        return 0

    return numbers[index] + total(numbers, index + 1)


print(total([5, 6, 7, 8, 9], 0))  # Should print 35


def product(numbers, index):
    # Calculate the product of the numbers in a list recursively
    # Return `1` if the list is empty

    if index == len(numbers):
        return 1

    return numbers[index] * product(numbers, index + 1)


print(product([1, 2, 3, 4, 5], 0))  # Should print 120


def contains(items, value, index):
    # Check if a list of items contains a value recursively

    if index == len(items):
        return False

    if items[index] == value:
        return True

    return contains(items, value, index + 1)


print(contains(["a", "s", "d", "f"], "d", 0))  # Should print True
print(contains(["a", "s", "d", "f"], "g", 0))  # Should print False


def minimum(numbers, index):
    # Find the minimum among the numbers in a list recursively
    # Return `None` if the list is empty

    if index == len(numbers):
        return None

    minTail = minimum(numbers, index + 1)

    if minTail == None or minTail > numbers[index]:
        return numbers[index]

    return minTail


print(minimum([68, 10, 13, 2, 13, 10, 57, 12, 80, 82], 0))  # Should print 2
