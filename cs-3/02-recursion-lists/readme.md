# Recursion with Lists

## Head and Tail

```py
numbers = [5, 6, 7, 8, 9]
```

Head:

```py
numbers[0]  # 5
```

Tail:

```py
numbers[1:]  # [6, 7, 8, 9]
```

## Printing Values

```py
def printEach(numbers):
    # Print each of the number in the list `numbers`, one at a time
    # on separate lines

    # ???
```

```py
printEach([9, 4, 5, 6, 8, 10])
```

```
9
4
5
6
8
10
```

---

```py
def printEach(numbers):
    # Print each of the number in the list `numbers`, one at a time
    # on separate lines

    if numbers != []:
        print(numbers[0])
        printEach(numbers[1:])
```

```
printEach([9, 4, 5, 6, 8, 10])  # Prints 9
printEach([4, 5, 6, 8, 10])     # Prints 4
printEach([5, 6, 8, 10])        # Prints 5
printEach([6, 8, 10])           # Prints 6
printEach([8, 10])              # Prints 8
printEach([10])                 # Prints 10
printEach([])                   # Does nothing
```

## Summing Values

```py
def total(numbers):
    # Calculate the sum of the numbers in a list recursively

    if numbers == []:
        return 0

    return numbers[0] + total(numbers[1:])
```

```py
total([9, 4, 5, 6, 8, 10])
```

| Head | Tail               | Sub-result | Result |
| :--: | ------------------ | :--------: | :----: |
| `9`  | `[4, 5, 6, 8, 10]` |    `33`    |  `42`  |
| `4`  | `[5, 6, 8, 10]`    |    `29`    |  `33`  |
| `5`  | `[6, 8, 10]`       |    `24`    |  `29`  |
| `6`  | `[8, 10]`          |    `18`    |  `24`  |
| `8`  | `[10]`             |    `10`    |  `18`  |
| `10` | `[]`               |    `0`     |  `10`  |

## Checking Values

```py
def countEven(numbers):
    # Count how many numbers in a list are even, recursively

    if numbers == []:
        return 0

    isEven = numbers[0] % 2 == 0
    return isEven + countEven(numbers[1:])
```

```py
countEven([9, 4, 5, 6, 8, 10])
```

| Head | Tail               | Sub-result | Result |
| :--: | ------------------ | :--------: | :----: |
| `9`  | `[4, 5, 6, 8, 10]` |    `4`     |  `4`   |
| `4`  | `[5, 6, 8, 10]`    |    `3`     |  `4`   |
| `5`  | `[6, 8, 10]`       |    `3`     |  `3`   |
| `6`  | `[8, 10]`          |    `2`     |  `3`   |
| `8`  | `[10]`             |    `1`     |  `2`   |
| `10` | `[]`               |    `0`     |  `1`   |
