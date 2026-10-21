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

How do we **call** a function?

...

```py
greeting("Avery", "gfs")
```

...

```py
"Hello Avery from gfs!"
```

...

What are `"Avery"` and `"gfs"` called here?

...

**Arguments**

---

Write a function named `average` that takes a list of numbers as an argument,
and returns the average of those numbers.

...

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

Write a function named `smallest` that takes two numbers as arguments and
returns the smaller of the two numbers.

...

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
people = ["Luna", "Marty", "Mercedes", "Judy"]
```

...

```py
people[0]
```

...

```py
"Luna"
```

...

```py
people.index("Marty")
```

...

```py
1
```

...

```py
people.append("DeVondre")
```

...

```py
["Luna", "Marty", "Mercedes", "Judy", "DeVondre"]
```

## Classes

We use **classes** to make custom objects.

https://www.w3schools.com/python/python_classes.asp

...

```py
r = Rectangle(3, 4)
```

...

```py
r.width
r.area()
```

...

```
3
12
```

...

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

## Repr

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

...

```py
r = Rectangle(3, 4)
print(r)
```

...

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
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height
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
r.area
```

...

```py
12
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

```py
Rectangle(4, 5, 6)
```

...

```
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    Rectangle(4, 5, 6)
    ~~~~~~~~~^^^^^^^^^
TypeError: Rectangle.__init__() takes 3 positional arguments but 4 were given
```

...

It's a questionable design decision, in my opinion. If you find it confusing,
it's because it is.

https://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html

## Problem: Square

```py
s = Square(10)
```

```py
print(s)       # Square(10)
s.width        # 10
s.area()       # 100
s.perimeter()  # 40
```

## Problem: Circle

```py
c = Circle(10)
```

```py
print(c)       # Circle(10)
c.radius       # 10
c.area()       # 314.1592653589793
c.perimeter()  # 62.83185307179586
```

## Problem: Point

```py
p = Point(3, 4)
```

```py
print(p)  # (3, 4)
p.x       # 3
p.y       # 4

origin = Point(0, 0)
p.distance_to(origin)  # 5.0
```

## Problem: Line

```py
l = Line(Point(0, 0), Point(3, 4))
```

```py
print(l)    # Line((0, 0), (3, 4))
l.p1        # (0, 0)
l.p2        # (3, 4)
l.length()  # 5.0
l.slope()   # 1.3333333333333333
```

## Roster Demo

```py
class Player:
    def __init__(self, name):
        # ...

    def percent(self):
        # ...

    def __repr__(self):
        # ...


class Team:
    def __init__(self):
        # ...

    def addPlayer(self, name):
        # ...

    def addBasket(self, name):
        # ...

    def addMiss(self, name):
        # ...

    def removePlayer(self, name):
        # ...

    def average(self):
        # ...

    def __repr__(self):
        # ...
```

https://github.com/avery-gfs/cs-curriculum/blob/public/cs-2/05-classes/04-receipt/roster-demo.py

---

```py
team = Team()

team.addPlayer("Luna")
team.addPlayer("Marty")
team.addPlayer("Mercedes")

team.addBasket("Luna")
team.addMiss("Luna")

team.addBasket("Marty")
team.addBasket("Marty")
team.addBasket("Marty")
team.addMiss("Marty")
team.addMiss("Marty")

team.addBasket("Mercedes")
```

...

```py
print(team)
```

...

```
Luna 1/2 (50.00)
Marty 3/5 (60.00)
Mercedes 1/1 (100.00)
----------
average: 70.00
```

---

```py
class Item:
    def __init__(self, name, price, quantity):
        # ...

    def total(self):
        # ...

    def __repr__(self):
        # ...



class Receipt:
    def __init__(self):
        # ...

    def addItem(self, name, price, quantity):
        # ...

    def updateQuantity(self, name, newQuantity):
        # ...

    def removeitem(self, name):
        # ...

    def total(self):
        # ...

    def __repr__(self):
        # ...
```

---

```py
receipt = Receipt()

receipt.addItem("juice", 5, 3)
receipt.addItem("salad", 10, 3)
receipt.addItem("brownie", 4, 1)
receipt.updateQuantity("brownie", 2)
receipt.removeitem("juice")
receipt.addItem("yogurt", 2, 1)
```

...

```py
print(receipt)
```

...

```
salad 30.00 ($3 x $10.00)
brownie 8.00 ($2 x $4.00)
yogurt 2.00 ($1 x $2.00)
----------
total: $40.00
```
