# Classes

## Functions Review

https://www.w3schools.com/python/python_functions.asp

```py
def greeting(name, school):
    return f"Hello {name} from {school}!"
```

...

What are `name` and `school` called here?

...

**Parameters**

...

```py
greeting("Avery", "gfs")
```

...

```py
"Hello Avery from gfs!"
```

...

What are "Avery" and "gfs" called here?

...

**Arguments**

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

```py
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

```py
3
```

## Object Oriented Programming

**Objects** are **data** + **functionality**.

```py
nums = [1, 2, 3, 4]
```

...

```py
nums[0]
```

...

```py
1
```

...

```py
nums.index(2)
```

...

```py
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
r = Rectangle(3, 4)
```

```py
r
r.width
r.height
r.area()
r.perimeter()
```

```
Rectangle(3, 4)
3
4
12
14
```

- **Objects**: Structures that combine data and functionality (methods)

- **Methods**: Functions that are attached to a value

- **Classes**: The categories that objects belong to

- **Instance**: An object is an "instance" of a class if the object belongs to
  that class category

- **Fields**: Variables that are stored inside an object

- **Self**: A special variable used to keep track of an object's fields and
  methods, within the methods of that object's class.

## Making Classes

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

## Repr

```py
r = Rectangle(3, 4)
print(r)
```

```
<__main__.Rectangle object at 0x710f081cf380>
```

---

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

```
Rectangle(3, 4)
```

## Methods

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * width
        self.perimeter = 2 * (width + height)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
```

...

```py
r = Rectangle(3, 4)
```

...

```py
r.width = 5
```

...

```py
r.area()
```

...

```py
12
```

---

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

---

```py
r = Rectangle(3, 4)
```

...

```py
r.width = 5
```

...

```py
r.area()
```

...

```py
20
```

## Self

The `self` variable helps us keep track of which data and functionality is
inside of the objects of our class (that is, which variables and functions are
fields and methods).

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

It's a questionable design decision, in my opinion. If you find it confusing,
it's because it is.

https://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
