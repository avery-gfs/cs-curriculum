# Conditionals

## Control Flow

```py
tempF = 75

print("Water is solid: ice")
print("Water is liquid: water")
print("Water is gas: steam")
```

...

```
Water is solid: ice
Water is liquid: water
Water is gas: steam
```

---

```py
tempF = 75

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")

else:
    print("Water is gas: steam")
```

...

```
Water is liquid: water
```

## If Statements

If statements contain a condition and an indented code block. The code block
runs only if the condition is `True`.

```
if <condition>:
    <code block>
    ...
```

---

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
