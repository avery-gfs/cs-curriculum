import time
import random
from contextlib import contextmanager


@contextmanager
def timer(name):
    print(name)
    start = time.time_ns()
    yield
    end = time.time_ns()
    print(end - start)


def search(lst, low, high, target):
    pass


count = 100_000
maxNum = 200_000

numbers = sorted([random.randrange(1, maxNum + 1) for _ in range(count)])
target = random.randrange(1, maxNum + 1)

with timer("linear search"):
    target in numbers

with timer("binary search"):
    search(numbers, 0, len(numbers), target)
