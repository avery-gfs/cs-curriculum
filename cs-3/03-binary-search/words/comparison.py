import time
import random
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time_ns()
    yield
    end = time.time_ns()
    print(end - start)


def linear_search(lst, target):
    return target in lst


def binary_search_indexed_iter(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return True

        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


def binary_search_indexed_rec(lst, low, high, target):
    if low > high:
        return False

    mid = (low + high) // 2

    if lst[mid] == target:
        return True

    if lst[mid] < target:
        return binary_search_indexed_rec(lst, mid + 1, high, target)

    return binary_search_indexed_rec(lst, low, mid - 1, target)


def binary_search_sliced_rec(lst, target):
    if lst == []:
        return False

    mid = len(lst) // 2

    if lst[mid] == target:
        return True

    if lst[mid] < target:
        return binary_search_sliced_rec(lst[mid + 1 :], target)

    return binary_search_sliced_rec(lst[:mid], target)


def binary_search_sliced_iter(lst, target):
    while lst != []:
        mid = len(lst) // 2

        if lst[mid] == target:
            return True

        if lst[mid] < target:
            lst = lst[mid + 1 :]
        else:
            lst[:mid]

    return False


count = 10**6
maxNum = 10**7

numbers = sorted([random.randrange(1, maxNum + 1) for _ in range(count)])
target = random.randrange(1, maxNum + 1)

with timer():
    print("linear search")
    target in numbers

with timer():
    print("binary search: indexed, iterative")
    binary_search_indexed_iter(numbers, target)

with timer():
    print("binary search: indexed, recursive")
    binary_search_indexed_rec(numbers, 0, len(numbers) - 1, target)

with timer():
    print("binary search: sliced, iterative")
    binary_search_sliced_rec(numbers, target)

with timer():
    print("binary search: sliced, recursive")
    binary_search_sliced_iter(numbers, target)
