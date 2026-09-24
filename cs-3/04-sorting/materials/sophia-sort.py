import os
import time


def render():
    os.system("clear")
    print(" ".join(map(str, items)))
    print("  " * j + "^")
    print("  " * i + "^")
    time.sleep(0.5)


items = [5, 3, 2, 5, 1, 4, 1]

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        render()
        if items[i] > items[j]:
            tmp = items[i]
            items[i] = items[j]
            items[j] = tmp
            render()
