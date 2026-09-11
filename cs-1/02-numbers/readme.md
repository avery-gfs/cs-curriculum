# Numbers

## Ints and Floats

Numbers in Python come in two main forms: **ints** (integers, aka whole numbers)
and **floats** (floating-point numbers, aka numbers with decimal points).

```py
speed_limit = 35    # An int (a whole number)
temperature = 98.6  # A float (a number with a decimal point)
```

- **Ints**: whole numbers.
- **Floats**: numbers with decimal points.

## Math Operators

| Symbol | Operation      |
| ------ | -------------- |
| `+`    | Addition       |
| `-`    | Subtraction    |
| `*`    | Multiplication |
| `/`    | Division       |
| `//`   | Floor division |
| `**`   | Exponentiation |
| `%`    | Modulo         |

These operators work on ints, floats, or a combination of both.

```py
1 + 2      # 3
1.2 + 5.5  # 6.7
-4 + 0.01  # -3.99
```

## Operator Precedence

These operators follow standard math order of operations, with parentheses used
for grouping.

```py
1 + 2 * 3    # 7
(1 + 2) * 3  # 9
```

## Addition

What value does this expression produce?

```py
7 + 2
```

...

```
9
```

## Subtraction

What value does this expression produce?

```py
7.1 - 2.5
```

...

```
4.6
```

## Multiplication

What value does this expression produce?

```py
7.1 * -2
```

...

```
-14.2
```

## Division

What value does this expression produce?

```py
7 / 2
```

...

```
3.5
```

---

What value does this expression produce?

```py
7 / 7
```

...

Division produces a float!

```
1.0
```

## Floor Division

What value does this expression produce?

```py
7 // 7
```

...

Floor division rounds down to the nearest whole number.

```
1
```

---

What value does this expression produce?

```py
7 // 2
```

...

```
3
```

---

What value does this expression produce?

```py
-7 // 2
```

...

Floor division rounds _down_, not _towards zero_.

```
-4
```

## Exponentiation

What value does this expression produce?

```py
7**2
```

...

```
49
```

## Modulo

What value does this expression produce?

```py
11 % 2
```

...

The modulo operator in Python computes the remainder using
[floored division](https://en.wikipedia.org/wiki/Modulo#Variants_of_the_definition).

```
1
```

---

What value does this expression produce?

```py
14 % 1
```

...

```
0
```

---

What value does this expression produce?

```py
14 % 2
```

...

```
0
```

---

What value does this expression produce?

```py
14 % 5
```

...

```
4
```

---

What value does this expression produce?

```py
-14 % 5
```

...

```
1
```

---

What value does this expression produce?

```py
14 % 14
```

...

```
0
```

---

What value does this expression produce?

```py
14 % 20
```

...

```
14
```

## Type Errors

What's the issue?

```py
3 / "4"
```

...

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

The division operator expects two numbers, not a number and a string. We're
trying to do division on the wrong **type** of value, and getting a **type
error**.

- **Type**: the kind of value something is (int, float, string, etc).

- **Type Error**: an error caused by using a value of the wrong type.

## Numeric Variables

We can store numbers in variables, and use these variables with math operators.

```py
x = 5
```

What value does this expression produce?

```py
x * 4
```

...

```
20
```

---

```py
x = 5
y = 6
```

What value does this expression produce?

```py
x * y
```

...

```
30
```

## Variables From Variables

We can use existing variables to define new variables.

What will this code print out?

```py
score = 58
bonus = 3
print(score + bonus)
```

...

```
61
```

---

A variable can even be defined using its own old value. Python computes the
right hand side first, then stores the result back in the variable.

What will this code print out?

```py
score = 92
score = score + 5
print(score)
```

...

```
97
```

---

What will this code print out?

```py
x = 2
y = x * 3
print(y)
x = 10
print(y)
```

...

```
6
6
```

Changing `x` after we've defined `y` doesn't change the value of `y`.

## Compound Assignment

Python provides a shorthand for updating a variable based on its current value.
The two lines below are equivalent.

```py
score = score + 5
score += 5
```

Each math operator has a matching compound assignment operator.

| Symbol | Example   | Meaning      |
| ------ | --------- | ------------ |
| `+=`   | `x += y`  | `x = x + y`  |
| `-=`   | `x -= y`  | `x = x - y`  |
| `*=`   | `x *= y`  | `x = x * y`  |
| `/=`   | `x /= y`  | `x = x / y`  |
| `//=`  | `x //= y` | `x = x // y` |
| `**=`  | `x **= y` | `x = x ** y` |
| `%=`   | `x %= y`  | `x = x % y`  |

---

What will this code print out?

```py
count = 3
count += 1
count *= 10
print(count)
```

...

```
40
```

## Numeric Input

What's the issue with this code?

```py
x = input("x: ")
print(x / 2)
```

...

Issue: `input` always gives us a string, even when the user types digits.

```
x: 10
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

---

The `int` and `float` functions convert a string into a number.

```py
int("12")     # 12
float("1.5")  # 1.5
```

We can fix our code by wrapping our call to `input` in a call to `int`.

```py
x = int(input("x: "))
print(x / 2)
```

```
x: 10
5.0
```

## Problem: Temperature Conversion

Write code that asks the user for a temperature in degrees Celsius and prints
the temperature in degrees Fahrenheit.

To convert Celsius to Fahrenheit, multiply by `9`, divide by `5`, and add `32`.

```
Enter degrees C: 25
```

```
Temp in degrees F: 77.0
```

## Problem: Dog Years

Write a program that gets two numbers as input from the user:

- Their birth year
- Their dog's birth year

And calculates:

- The user's age in years
- The dog's age in years
- The dog's age in dog-years

```
Enter your birth year: 1996
Enter your dog's birth year: 2016
```

```
Your age (years): 30
Your dog's age (years): 10
Your dog's age (dog-years): 70
```

## Problem: Line Equation

Write code that asks the user for the coordinates of two points and prints the
equation of the line that passes through them.

![](/assets/line-equation.png)

---

The slope $m$ and y-intercept $b$ of the line are:

$$
m = \frac{y_2 - y_1}{x_2 - x_1}
$$

$$
b = y_1 - m x_1
$$

The equation of the line is $y = mx + b$.

```
x1: 1
y1: 3
x2: 3
y2: 7
```

```
y = 2.0x + 1.0
```
