# Conditionals

## Control Flow

```py
tempF = 75

print("Ice")
print("Water")
print("Steam")
```

...

```
Ice
Water
Steam
```

---

```py
tempF = 75

if tempF < 32:
    print("Ice")

elif tempF <= 212:
    print("Water")

else:
    print("Steam")
```

...

```
Water
```

## If Statements

If statements contain a condition and an indented code block. The code block
runs only if the condition is `True`.

```py
n = -7

if n < 0:
    print("n is negative")

if n % 2 == 0:
    print("n is even")
```

...

```
n is negative
```

---

```py
n = 6

if n < 0:
    print("n is negative")

if n % 2 == 0:
    print("n is even")
```

...

```
n is even
```

---

```py
n = 7

if n < 0:
    print("n is negative")

if n % 2 == 0:
    print("n is even")
```

...

```
```

---

```py
n = -8

if n < 0:
    print("n is negative")

if n % 2 == 0:
    print("n is even")
```

...

```
n is negative
n is even
```
