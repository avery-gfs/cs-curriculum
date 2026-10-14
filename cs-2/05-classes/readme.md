# Classes

## Functions Review

https://www.w3schools.com/python/python_functions.asp

```py
def greeting(name, school):
    return f"Hello {name} from {school}!"
```

...

```py
print(greeting("Avery", "gfs"))
```

...

```
Hello Avery from gfs!
```

---

```py
def average(numbers):
    total = 0

    for n in numbers:
        total += n

    return total / len(numbers)
```

...

```py
average([1, 4, 2, 7, 3, 1])
```

...

```
3.0
```

## Early returns

```py
def smallest(a, b):
    if a < b:
        return a

    return b
```

...

```py
smallest(3, 4)
```

...

```
3
```

## Object Oriented Programming

**Objects** are **data** + **functionality**.

```py
nums = [1, 2, 3, 4]
```

...

```py
nums
```

...

```
[1, 2, 3, 4]
```

...

```py
nums[0]
```

...

```
1
```

...

```py
nums.index(2)
```

...

```
1
```

...

```py
nums.append(5)
```

...

```py
[1, 2, 3, 4, 5]
```

## Classes

We use **classes** to make custom objects.

https://www.w3schools.com/python/python_classes.asp

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

...

```py
r = Rectangle(3, 4)
```

...

```py
r.width
```

...

```
3
```

...

```py
r.height
```

...

```
4
```

---

<img src="/assets/init-meme.png" />

## Terms

- **Objects**: Structures that combine data and functionality (methods)

- **Methods**: Functions that are attached to a value

- **Classes**: The categories that objects belong to

- **Instance**: An object is an "instance" of a class if the object belongs to
  that class category

- **Fields**: Variables that are stored inside an object

## Repr

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
```

...

```py
r = Rectangle(3, 4)
print(r)
```

...

```py
print(r)
```

...

```
Rectangle(3, 4)
```

## Methods

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

...

```py
r = Rectangle(3, 4)
```

...

```py
r.area()
```

...

```
12
```

...

```py
r.perimeter()
```

...

```
14
```

...

Why use methods vs extra fields?

---

```py
r = Rectangle(3, 4)
r.width = 5
```

...

What does this give us?

```py
r.area()
```

...

```py
20
```

## Self

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

The `self` variable helps us keep track of which data and functionality is
inside of the objects of our class (that is, which variables and functions are
fields and methods).
