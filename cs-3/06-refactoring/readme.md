# Refactoring

## What is Refactoring?

<img src="/assets/refactoring.png" height="400px" />

...

Make code better...

...

**Without** changing its behavior

## Example

```py
def sign(num):
    if num > 0 == True:
        return "positive"

    elif num == 0:
        return "zero"

    elif num < 0 == True:
        return "negative"
```

...

```py
sign(8)   # "positive"
sign(0)   # "zero"
sign(-7)  # "negative"
```

---

```py
def sign(num):
    if num > 0:
        return "positive"

    elif num == 0:
        return "zero"

    elif num < 0:
        return "negative"
```

---

```py
def sign(num):
    if num > 0:
        return "positive"

    elif num == 0:
        return "zero"

    else:
        return "negative"
```

---

```py
def sign(num):
    if num > 0:
        return "positive"

    if num == 0:
        return "zero"

    return "negative"
```

---

```py
def sign(num):
    return ["zero", "positive", "negative"][num // (abs(num) or 1)]
```

Don't do this. Refactoring is not code golf!
