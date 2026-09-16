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


with open("words-sorted.txt") as file:
    words = file.read().splitlines()

with timer("linear search"):
    "asdf" in words

with timer("binary search"):
    search(words, 0, len(words) - 1, "asdf")
