def product(numbers):
    # Calculate the product of the numbers in a list recursively
    # Return `1` if the list is empty

    if numbers == []:
        return 1

    return numbers[0] * product(numbers[1:])


print(product([9, 4, 5, 6, 8, 10]))  # Should print 86400


def hasSeven(numbers):
    # Check if a list of numbers contains the number 7

    if numbers == []:
        return False

    if numbers[0] == 7:
        return True

    return hasSeven(numbers[1:])


print(hasSeven([9, 4, 5, 6, 8, 10, 7]))  # Should print True
print(hasSeven([9, 4, 5, 6, 8, 10]))  # Should print False


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
