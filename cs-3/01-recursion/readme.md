# Recursion

## Recursive Functions

What does this code do?

```py
def hello():
    print("Hello world!")


hello()
```

---

What does this code do?

```py
def hello():
    print("Hello world!")
    hello()


hello()
```

---

What does this code do?

```py
def hello():
    hello()
    print("Hello world!")


hello()
```

---

What does this code do?

```py
def hello(n):
    if n < 10:
        print("Hello world!")
        hello(n + 1)


hello(0)
```

---

What does this code do?

```py
def hello(n):
    if n < 10:
        print("Hello world!")
        hello(n + 1)
    else:
        print("Done")


hello(0)
```

---

What does this code do?

```py
def hello(n):
    if n < 10:
        print("Hello world!")
        hello(n + 1)
        print("Goodbye")


hello(0)
```

## Koan

Recursive functions: functions which call themselves

> To understand recursion, you must first understand recursion.

<img width="600" src="/assets/nesting-dolls.jpg" />

<img width="600" src="/assets/nesting-doll-cutaway.jpg" />

## Factorial Definition

$n! = n \cdot (n - 1) \cdot (n - 2) \cdot ... \cdot 1$

$5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$

$0! = 1$

```txt
factorial(n)
```

## Iterative Factorial

```py
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))  # Prints 120
```

```py
def factorial(n):
    result = 1

    while n > 0:
        result *= n
        n -= 1

    return result


print(factorial(5))  # Prints 120
```

## Recursive Factorial

```txt
factorial(0) = 1
factorial(n) = n * factorial(n - 1)
```

```txt
factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
```

```txt
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 * factorial(0)
5 * 4 * 3 * 2 * 1 * 1
```

---

```py
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))  # Prints 120
```

...

```txt
factorial(5)
5 * factorial(4)
5 * 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 * factorial(1)
5 * 4 * 3 * 2 * 1 * factorial(0)
5 * 4 * 3 * 2 * 1 * 1
```

---

```py
def factorial(n):
    if n == 0:
        return 1
        
    else:
        return n * factorial(n - 1)
```

```py
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)
```

## Base Case

```py
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))  # Prints 120
```

Case in which the function doesn't call itself recursively

```txt
0! = 1
```

```py
if n == 0:
    return 1
```

## Recursive Case

```py
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))  # Prints 120
```

Case in which the function calls itself recursively

```txt
n! = n * (n - 1)!
```

```py
return n * factorial(n - 1)
```

## Tracing Recursion

```py
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))  # Prints 120
```

|    Problem     | Sub-problem    | Sub-result | Result |
| :------------: | -------------- | :--------: | :----: |
| `factorial(5)` | `factorial(4)` |    `24`    | `120`  |
| `factorial(4)` | `factorial(3)` |    `6`     |  `24`  |
| `factorial(3)` | `factorial(2)` |    `2`     |  `6`   |
| `factorial(2)` | `factorial(1)` |    `1`     |  `2`   |
| `factorial(1)` | `factorial(0)` |    `1`     |  `1`   |
| `factorial(0)` |                |            |  `1`   |

## Recursive Summation

```py
def summation(n):
    if n == 0:
        return 0

    return n + summation(n - 1)


print(summation(5))  # Prints 15
```

|    Problem     | Sub-problem    | Sub-result | Result |
| :------------: | -------------- | :--------: | :----: |
| `summation(5)` | `summation(4)` |    `10`    |  `15`  |
| `summation(4)` | `summation(3)` |    `6`     |  `10`  |
| `summation(3)` | `summation(2)` |    `3`     |  `6`   |
| `summation(2)` | `summation(1)` |    `1`     |  `3`   |
| `summation(1)` | `summation(0)` |    `0`     |  `1`   |
| `summation(0)` |                |            |  `0`   |

## Fibonacci is Recursive

```txt
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...
```

$$
F_0 = 0
$$

$$
F_1 = 1
$$

$$
F_n = F_{n - 1} + F_{n - 2}
$$

![](/assets/fibonacci-tree.png)

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

## Recursion with Lists

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

---

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

```
total([9, 4, 5, 6, 8, 10])
9 + total([4, 5, 6, 8, 10])
9 + 4 + total([5, 6, 8, 10])
9 + 4 + 5 + total([6, 8, 10])
9 + 4 + 5 + 6 + total([8, 10])
9 + 4 + 5 + 6 + 8 + total([10])
9 + 4 + 5 + 6 + 8 + 10 + total([])
9 + 4 + 5 + 6 + 8 + 10 + 0
```
