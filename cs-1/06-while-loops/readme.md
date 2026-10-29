# Conditionals

## Variable Updates

```py
n = 1

print(n)
n *= 2

print(n)
n *= 2

print(n)
n *= 2

print(n)
n *= 2

print(n)
```

...

```
1
2
4
8
16
```

## While Loops

```
while <condition>:
    <code block
```

---

```
1
2
4
8
16
```

...

```py
n = 1

while n < 20:
    print(n)
    n *= 2
```

---

```
Hello!
Hello!
Hello!
Hello!
Hello!
```

...

```py
n = 5

while n > 0:
    print("Hello!")
    n -= 1
```

---

```
5
6
7
8
9
10
```

...

```py
n = 5

while n <= 10:
    print(n)
    n += 1
```

---

```
10
100
1000
10000
100000
```

...

```py
n = 1

while n <= 5:
    print(10 ** n)
    n += 1
```

## Infinite Loops

```py
while True:
    # ...
```

---

```
Enter a number: 5
5
Enter a number: 10
15
Enter a number: -4
11
Enter a number: 33
44
...
```

...

```py
total = 0

while True:
    n = int(input("Enter a number: "))
    total += n
    print(total)
```

...

**Accumulator pattern**

## Break

```py
while True:
    name = input("Enter a name: ")

    if name == "":
        break

    print(f"Hello {name}!")
```

...

```
Enter a name: Avery
Hello Avery!
Enter a name: Clementine
Hello Clementine!
Enter a name:
```

## Nested Loops

```py
x = 1

while x <= 4:
    y = 1

    while y <= 4:
        print(f"{x} x {y} = {x * y}")
        y += 1

    x += 1
```

...

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
```

**Problems**

- Prime test
- Prime factors
- Simplify fractions
- Running sum of inputs
- Running average of inputs
- 99 bottles of beer
