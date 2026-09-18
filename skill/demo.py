board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def solveRec(r, c):
    if c == 9:
        c = 0
        r += 1

    if r == 9:
        return True

    if board[r][c] > 0:
        return solveRec(r, c + 1)

    br = r // 3
    bc = c // 3

    for n in range(1, 10):
        if n not in rows[r] and n not in cols[c] and n not in blocks[br][bc]:
            board[r][c] = n
            rows[r].add(n)
            cols[c].add(n)
            blocks[br][bc].add(n)

            if solveRec(r, c + 1):
                return True

            board[r][c] = 0
            rows[r].remove(n)
            cols[c].remove(n)
            blocks[br][bc].remove(n)


rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
blocks = [[set() for _ in range(3)] for _ in range(3)]

for r, row in enumerate(board):
    for c, n in enumerate(row):
        rows[r].add(n)
        cols[c].add(n)
        blocks[r // 3][c // 3].add(n)

solveRec(0, 0)

print("\n".join(str(row) for row in board))
