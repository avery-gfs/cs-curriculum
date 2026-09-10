def product(numbers):
    # Calculate the product of the numbers in a list recursively
    # Return `1` if the list is empty

    if numbers == []:
        return 1

    return numbers[0] * product(numbers[1:])


print(product([9, 4, 5, 6, 8, 10]))  # Should print 86400


def totalEven(numbers):
    # Calculate if the sum of the numbers in a list is even, recursively
    # Return `True` if the list is empty

    if numbers == []:
        return True

    isEven = numbers[0] % 2 == 0
    return isEven == totalEven(numbers[1:])


print(totalEven([9, 4, 5, 6, 8, 10]))  # Should print True
print(totalEven([9, 4, 5, 6, 8, 10, 1]))  # Should print False


def contains(items, value):
    # Check if a list of items contains a value recursively

    if items == []:
        return False

    if items[0] == value:
        return True

    return contains(items[1:], value)


print(contains([9, 4, 5, 6, 8, 10], 8))  # Should print True
print(contains([9, 4, 5, 6, 8, 10], 7))  # Should print False


def minimum(numbers):
    # Find the minimum among the numbers in a list recursively
    # Return `None` if the list is empty

    if numbers == []:
        return None

    minTail = minimum(numbers[1:])

    if minTail == None or minTail > numbers[0]:
        return numbers[0]

    return minTail


print(minimum([9, 4, 5, 6, 8, 10]))  # Should print 4
