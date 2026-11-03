import os
import time


def showRow(radius, sym):
    padding = " " * (6 - radius)
    width = radius * 2 + 1
    return padding + sym * width + padding


def showRows(tower):
    numBlanks = 6 - len(tower) + 1
    blanks = [showRow(0, "░")] * numBlanks
    discs = [showRow(row, "▇") for row in reversed(tower)]
    return blanks + discs


def showTowers():
    combined = [" "] * 7

    for tower in towers:
        rows = showRows(tower)

        for index, row in enumerate(rows):
            combined[index] += row + " "

    os.system("clear")

    for row in combined:
        print(row)

    time.sleep(0.2)


# https://en.wikipedia.org/wiki/Tower_of_Hanoi#Recursive_solution


# Tower Labels:
#
#        ░             ░             ░
#       ▇▇▇            ░             ░
#      ▇▇▇▇▇           ░             ░
#     ▇▇▇▇▇▇▇          ░             ░
#    ▇▇▇▇▇▇▇▇▇         ░             ░
#   ▇▇▇▇▇▇▇▇▇▇▇        ░             ░
#  ▇▇▇▇▇▇▇▇▇▇▇▇▇       ░             ░
#
#        0             1             2


def moveSingle(src, dest):
    towers[dest].append(towers[src].pop())
    showTowers()


def solve(src, dest, depth):
    if depth:
        tmp = 3 - src - dest
        solve(src, tmp, depth - 1)
        moveSingle(src, dest)
        solve(tmp, dest, depth - 1)


towers = [[6, 5, 4, 3, 2, 1], [], []]

showTowers()
solve(0, 2, 6)
