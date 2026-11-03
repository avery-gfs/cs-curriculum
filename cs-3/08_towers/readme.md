# Towers of Hanoi

## Puzzle

<img src="/assets/towers.gif" height="600px" />

## Tower Representation

```txt
Tower Labels:

    ░             ░             ░
    ░             ░             ░
    ░             ░             ░
    ░             ░             ░
    ░             ░             ░
    ░             ░             ░
    ░             ░             ░
   
    0             1             2
```

...

```py
towers = [[6, 5, 4, 3, 2, 1], [], []]
```

...

```py
towers[0]  # [6, 5, 4, 3, 2, 1]
```

...

```py
towers[1]  # []
```

...

```py
towers[0][-1]  # 1
```

## Stacks

"Last in, first out"

- Push (add value) `append`

```py
values.append(something)
```

- Pop (remove last) `pop`

```py
values.pop()
```

- Check last (without removing)

```py
values[-1]
```

What are some real-life examples of stacks?

<!-- browser history, loading truck (shelf before books) -->

## Functions

```py
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

moveSingle(src, dest)
```

## Functions

```py
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

solve(src, dest, depth)
```

## Algorithm

To move `n` discs from the `src` tower to the `dest` tower:

- Move `n - 1` discs from the `src` tower to the `tmp` tower
- Move the next `n`th disc from the `src` tower to the `dest` tower
- Move `n - 1` discs from the `tmp` tower to the `dest` tower

Draw tree diagram

Where does `* 2 + 1` pattern in step counts come from?

---

## Towers

```txt
steps(n + 1) = 2 * steps(n) + 1
```

## World Record

https://www.youtube.com/watch?v=TTKwx1xIx6g

---
