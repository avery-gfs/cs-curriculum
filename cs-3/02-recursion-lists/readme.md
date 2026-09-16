# Recursion with Lists

## Head and Tail

```py
numbers = [5, 6, 7, 8, 9]
```

...

Head: the first value in a list

...

```py
numbers[0]  # 5
```

...

Tail: everything after the first value in a list

...

```py
numbers[1:]  # [6, 7, 8, 9]
```

## Printing Values

```py
def printEach(numbers):
    # Print each of the number in the list `numbers`, one at a time
    # on separate lines

    # ???


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


printEach([9, 4, 5, 6, 8, 10])
```

...

```
printEach([9, 4, 5, 6, 8, 10])  # Prints 9
printEach([4, 5, 6, 8, 10])     # Prints 4
printEach([5, 6, 8, 10])        # Prints 5
printEach([6, 8, 10])           # Prints 6
printEach([8, 10])              # Prints 8
printEach([10])                 # Prints 10
printEach([])                   # Does nothing
```

## Base Case

What's the base case?

```py
def printEach(numbers):
    # Print each of the number in the list `numbers`, one at a time
    # on separate lines

    if numbers != []:
        print(numbers[0])
        printEach(numbers[1:])


printEach([9, 4, 5, 6, 8, 10])
```

...

```
numbers == []
```

---

```py
def printEach(numbers):
    # Print each of the number in the list `numbers`, one at a time
    # on separate lines

    if numbers == []:
        return 

    print(numbers[0])
    printEach(numbers[1:])


printEach([9, 4, 5, 6, 8, 10])
```

## Summing Values

```py
def total(numbers):
    # Calculate the sum of the numbers in a list recursively

    if numbers == []:
        return 0

    return numbers[0] + total(numbers[1:])


total([9, 4, 5, 6, 8, 10])
```

...

| Head | Tail               | Sub-result | Result |
| :--: | ------------------ | ---------: | -----: |
| `9`  | `[4, 5, 6, 8, 10]` |       `33` |   `42` |
| `4`  | `[5, 6, 8, 10]`    |       `29` |   `33` |
| `5`  | `[6, 8, 10]`       |       `24` |   `29` |
| `6`  | `[8, 10]`          |       `18` |   `24` |
| `8`  | `[10]`             |       `10` |   `18` |
| `10` | `[]`               |        `0` |   `10` |

## Averaging Values

```py
def average(numbers):
    # Count how many numbers in a list are even, recursively

    if numbers == []:
        return 0

    tailAvg = average(numbers[1:])
    return (numbers[0] + tailAvg * (len(numbers) - 1)) / len(numbers)

average([9, 4, 5, 6, 8, 10])
```

...

| Head | Tail               | Sub-result | Result |
| :--: | ------------------ | ---------: | -----: |
| `9`  | `[4, 5, 6, 8, 10]` |      `6.6` |    `7` |
| `4`  | `[5, 6, 8, 10]`    |     `7.25` |  `6.6` |
| `5`  | `[6, 8, 10]`       |        `8` | `7.25` |
| `6`  | `[8, 10]`          |        `9` |    `8` |
| `8`  | `[10]`             |       `10` |    `9` |
| `10` | `[]`               |        `0` |   `10` |

## Base Case conditions

All equivalent

```py
if numbers == []:
    # ...
```

```py
if len(numbers) == 0:
    # ...
```

```py
if not numbers:
    # ...
```

## Key Concepts

Head

```py
numbers[0]
```

Tail

```py
numbers[1:]
```

Base case

```py
if numbers == []:
    # ...
```
