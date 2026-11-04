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
    # Move a single disc from the top of tower `src` to tower `dest`.
    #
    # For example, if `towers` is
    #
    #     [[6, 5, 4], [3, 2, 1], []]
    #
    # and we run
    #
    #     moveSingle(0, 2)
    #
    # then `towers` will become
    #
    #     [[6, 5], [3, 2, 1], [4]]

    showTowers()


def solve(src, dest, depth):
    # Using recursion, move the top `depth` discs from tower `src` to tower `dest`.
    #
    # For example, if `towers` is
    #
    #     [[6, 5, 4, 3, 2, 1], [], []]
    #
    # and we run
    #
    #     solve(0, 2, 3)
    #
    # then `towers` will become
    #
    #     [[6, 5, 4], [], [3, 2, 1]]

    tmp = 3 - src - dest

    # Your code goes here

    pass


# The game state is represented as a list of three stacks. Each stack represents a
# tower. The numbers on the stack represent the discs in the tower, where 1 is the
# smallest and 6 is the largest.

towers = [[6, 5, 4, 3, 2, 1], [], []]

# Test moveSingle
# Remove this once moveSingle is working before you start implementing solve
moveSingle(0, 2)

showTowers()
solve(0, 2, 6)
