# Maze Solving

## Hidden Maze

<img src="/assets/maze-manson.webp" height="550px" />

https://avery-gfs.github.io/cs-curriculum/apps/hidden-maze.html

1. Solve the maze
2. Write an algorithm for solving the maze

Note that this maze has **no loops**

## Maze Algorithm

1. Choose an unexplored (white) path if there is one

2. Backtrack (green) otherwise

## Maze Data

```
███████████████
█A█     █B█   █
█ █ ███ █ ███ █
█ █ █ █ █     █
█ █ █ █ █████ █
█   █ █     █ █
█ ███ █████ █ █
█     █       █
███████████████
```

---

```py
maze = """
███████████████
█A█     █B█   █
█ █ ███ █ ███ █
█ █ █ █ █     █
█ █ █ █ █████ █
█   █ █     █ █
█ ███ █████ █ █
█     █       █
███████████████
"""
```

...

```py
board = [list(row) for row in maze.strip().split("\n")]
```

...

```
[
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
    ['█', 'A', '█', ' ', ' ', ' ', ' ', ' ', '█', 'B', '█', ' ', ' ', ' ', '█'],
    ['█', ' ', '█', ' ', '█', '█', '█', ' ', '█', ' ', '█', '█', '█', ' ', '█'],
    ['█', ' ', '█', ' ', '█', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█'],
    ['█', ' ', '█', ' ', '█', ' ', '█', ' ', '█', '█', '█', '█', '█', ' ', '█'],
    ['█', ' ', ' ', ' ', '█', ' ', '█', ' ', ' ', ' ', ' ', ' ', '█', ' ', '█'],
    ['█', ' ', '█', '█', '█', ' ', '█', '█', '█', '█', '█', ' ', '█', ' ', '█'],
    ['█', ' ', ' ', ' ', ' ', ' ', '█', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '█'],
    ['█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█', '█'],
]
```

---

```
███████████████
█A█     █B█   █
█ █ ███ █ ███ █
█ █ █ █ █     █
█ █ █ █ █████ █
█   █ █     █ █
█ ███ █████ █ █
█     █       █
███████████████
```

...

```py
board[0][0]
```

...

```py
"█"
```

...

```py
board[1][1]
```

...

```py
"A"
```

...

```py
board[1][9]
```

...

```py
"B"
```

## Update Maze

```
███████████████
█A█     █B█   █
█ █ ███ █ ███ █
█ █ █ █ █     █
█ █ █ █ █████ █
█   █ █     █ █
█ ███ █████ █ █
█     █       █
███████████████
```

...

```py
update(1, 1, "▒")
update(2, 1, "▒")
```

...

```
███████████████
█▒█     █B█   █
█▒█ ███ █ ███ █
█ █ █ █ █     █
█ █ █ █ █████ █
█   █ █     █ █
█ ███ █████ █ █
█     █       █
███████████████
```

## Maze Probe

<img src="/assets/probe.gif" height="400px" />

- Recursively "probe" every path in the maze

- Don't worry about stopping when you find the goal ("B")

- Make sure your probe accesses each cell of the maze

- Make your probe erase previous path characters as it backtracks from exploring
  a branch

## Starter Code

```py
def probe(r, c):
    # Edit the code below to make a function that fully probes the board

    cell = board[r][c]

    if cell == "█":
        return

    update(r, c, "▒")
    probe(r + 1, c)
```

## Backtracking

```py
def hello(n):
    if n < 5:
        print("Hello world!")
        hello(n + 1)
        print("Goodbye")
```

...

```py
hello(0)
```

...

```
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Goodbye
Goodbye
Goodbye
Goodbye
Goodbye
```

## Probe Algorithm

To probe from position `(r, c)`:

- If the cell at `(r, c)` is a wall, or in the currently probed path, then do
  nothing. Otherwise:

- Mark the cell at `(r, c)` as being on the current path.

- Probe each of the neighbor cells `(r + 1, c)`, `(r - 1, c)`, `(r, c + 1)`,
  `(r, c - 1)`.

- Once the four neighbor probes have completed, mark the cell at `(r, c)` as
  empty.

- No need to do anything else to handle backtracking: the structure of recursion
  does it for us!

## Search

<img src="/assets/search.gif" height="400" />

---

```py
def search(r, c):
    # if ??:
        return True

    # if ??:
        return False
```

`search` is similar to `probe`, except that it returns `True` or `False`
depending on whether the current path found the goal `B`.

## Trees

<img src="/assets/tree.svg" height="500" />
