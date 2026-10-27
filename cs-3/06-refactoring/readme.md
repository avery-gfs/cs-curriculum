# Refactoring

## What is Refactoring?

<img src="/assets/refactoring.png" height="400px" />

...

Make code better written...

...

**Without** changing its behavior

...

This is a somewhat subjective process, but there are also norms within software
engineering about what constitutes "well-written" code.

## Example

```py
def sign(num):
    if num > 0 == True:
        return "positive"

    elif num < 0 == True:
        return "negative"

    elif num == 0 == True:
        return "zero"
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

    elif num < 0:
        return "negative"

    elif num == 0:
        return "zero"
```

---

```py
def sign(num):
    if num > 0:
        return "positive"

    elif num < 0:
        return "negative"

    else:
        return "zero"
```

---

```py
def sign(num):
    if num > 0:
        return "positive"

    if num < 0:
        return "negative"

    return "zero"
```

# Refactoring isn't Code Golf!

...

```py
def sign(num):
    return ["zero", "positive", "negative"][num // (abs(num) or 1)]
```

...

Don't do this.
