# Imports and Math

## Global Numeric Functions

Python provides functions for common numeric tasks.

| Function   | Operation                                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------------------------- |
| `round(x)` | Round to the nearest whole number (using [banker's rounding](https://en.wikipedia.org/wiki/Rounding#Rounding_half_to_even)) |
| `abs(x)`   | Absolute value (convert negatives to positives)                                                                             |

```py
round(3.7)  # 4
abs(-8)     # 8
```

## Rounding

What value does this expression produce?

```py
round(2.4)
```

...

```
2
```

---

What value does this expression produce?

```py
round(-2.4)
```

...

```
-2
```

---

What value does this expression produce?

```py
round(2.5)
```

...

Halfway cases round to the nearest _even_ number, not always up (banker's
rounding).

```
2
```

---

What value does this expression produce?

```py
round(3.5)
```

...

```
4
```

---

`round` takes an optional second argument: the number of decimal places to keep.

What value does this expression produce?

```py
round(1234.5678, 2)
```

...

```
1234.57
```

---

What value does this expression produce?

```py
round(1234.5678, -2)
```

...

```
1200.0
```

## Absolute Value

What value does this expression produce?

```py
abs(-2.5)
```

...

```
2.5
```

---

What value does this expression produce?

```py
abs(3 - 10)
```

...

`abs` is useful for finding the difference between two numbers, no matter which
one is bigger.

```
7
```

## Imports

Python has more useful mathematical functions in the `math` **module**. We have
to **import** modules to use them using the `import` statement.

```py
import math
```

Import statements go at the top of the file, before the rest of the code. Once a
module is imported, we use a dot to access the functionality inside it.

```py
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

- **Module**: a library of pre-written code that we can use in our own programs.

- **Import**: loading a module so that our program can use it.

## The Math Module

Useful definitions in the `math` module.

| Name               | Meaning                                      |
| ------------------ | -------------------------------------------- |
| `math.pi`          | The constant $\pi$ (`3.14159...`)            |
| `math.sqrt(x)`     | Square root of `x`                           |
| `math.floor(x)`    | Round down to the nearest whole number       |
| `math.ceil(x)`     | Round up to the nearest whole number         |
| `math.hypot(x, y)` | Length of the hypotenuse, $\sqrt{x^2 + y^2}$ |

The full list is in the
[Python documentation](https://docs.python.org/3/library/math.html).

## Problem: Distance Formula

Write a program that asks the user for the coordinates of two points and prints
the distance between them, using the `math` library.

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

Round the distance to two decimal places.

```
x1: 1
y1: 2
x2: 4
y2: 6
```

```
Distance: 5.0
```

```
x1: 0
y1: 0
x2: 1
y2: 1
```

```
Distance: 1.41
```

## Problem: Sphere Calculator

Write a program that asks the user for the radius of a sphere and prints its
volume and surface area, each rounded to two decimal places.

$$
V = \frac{4}{3} \pi r^3
$$

$$
A = 4 \pi r^2
$$

```
Radius: 2
```

```
Volume: 33.51
Surface area: 50.27
```
