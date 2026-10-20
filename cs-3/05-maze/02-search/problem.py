import os
import time

maze = """
█████████████████████████████████
█A█     █B█         █         █ █
█ █ ███ █ █ ███ █████ █ █████ █ █
█ █ █ █ █     █       █ █   █   █
█ █ █ █ ███████████ ███ █ █ █████
█   █ █     █     █ █ █   █     █
█ ███ █████ █ ███ █ █ ███████ █ █
█ █     █ █ █ █ █ █       █ █ █ █
█ █ ███ █ █ █ █ █ █████████ ███ █
█ █   █   █ █   █   █       █   █
█ ███ ███ █ ███ ███ █ ███████ █ █
█ █   █ █ █     █ █   █   █   █ █
█ █ ███ █ ███████ █████ █ █ ███ █
█ █   █ █       █   █   █ █ █ █ █
█ ███ █ ███████ █ █ █ ███ █ █ █ █
█     █           █   █     █   █
█████████████████████████████████
"""

board = [list(row) for row in maze.strip().split("\n")]


def update(r, c, symbol):
    board[r][c] = symbol
    os.system("clear")
    print("\n".join("".join(row) for row in board))
    time.sleep(0.05)


def search(r, c):
    # Edit the code below to make a function that fully searches the board
    # Build from your solution to the probe problem

    pass


search(1, 1)
