import time
import random
from contextlib import contextmanager


@contextmanager
def timer(title):
    print(title)
    start = time.time_ns()
    yield
    end = time.time_ns()
    print(end - start)


def search(lst, low, high, target):
    if low > high:
        return False

    mid = (low + high) // 2

    if lst[mid] == target:
        return True

    if lst[mid] < target:
        return search(lst, mid + 1, high, target)

    return search(lst, low, mid - 1, target)


count = 100_000
maxNum = 200_000

numbers = sorted([random.randrange(1, maxNum + 1) for _ in range(count)])
target = random.randrange(1, maxNum + 1)

with timer("linear search"):
    target in numbers

with timer("binary search"):
    search(numbers, 0, len(numbers) - 1, target)

# import time

# with open("words-sorted.txt") as file:
# 	words = file.read().splitlines()

# def search(lst, target):
#     if lst == []:
#         return False

#     mid = len(lst) // 2

#     if lst[mid] == target:
#         return True

#     if lst[mid] < target:
#         return search(lst[mid + 1 :], target)

#     return search(lst[:mid], target)

# start = time.time_ns()

# print("asdf" in words)

# end = time.time_ns()

# print(end - start)

# import time
# import random

# count = 10**8
# maxNum = 10**9

# numbers = []

# for _ in range(count):
# 	n = random.randrange(1, maxNum + 1)
# 	numbers.append(n)

# numbers.sort()

# def search(lst, target):
#     if lst == []:
#         return False

#     mid = len(lst) // 2

#     if lst[mid] == target:
#         return True

#     if lst[mid] < target:
#         return search(lst[mid + 1 :], target)

#     return search(lst[:mid], target)

# target = random.randrange(1, maxNum + 1)

# start = time.time()

# for i in numbers:
# 	if i == target:
# 		print(True)

# end = time.time()

# print(end - start)

# start = time.time()

# print(search(numbers, target))

# end = time.time()

# print(end - start)
