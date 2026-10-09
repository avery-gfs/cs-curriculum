# Booleans and Conditionals

## Python Types (So Far)

- Strings
- Ints
- Floats
- **Booleans**

Booleans are a simple type, but they are key to unlocking a vast array of new
possibilities for our programs.

## Booleans

Booleans are true/false values. We can write them using the keywords `True` and
`False`.

```py
True
False
```

- **Booleans**: true/false values

## Keyword Case

```py
True
```

...

```py
true
```

```
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    print(true)
          ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
```

In Python the first letters of these keywords are capitalized. Virtually every
other mainstream language writes booleans in lowercase, but Python writes them
in uppercase. If you find forget to capitalize the first letter, you'll get an
error message. If you find this confusing, it's because it is.

## Equality

One way to get booleans in Python is by comparing values using the equality `==`
operator.

```py
1 == 1
```

...

```py
True
```

...

```py
1 == 7
```

...

```py
False
```

---

```py
5 == 5
```

...

```py
True
```

---

```py
5 == 5.0
```

...

```py
True
```

---

```py
5 == "5"
```

...

```py
False
```

Values of different types are _usually_ not equal.

---

```py
"Avery" == "Avery"
```

...

```py
True
```

In some languages this would give us `False` (yikes!). Python is being nice to
us here.

---

```py
"Avery" == " Avery"
```

...

```py
False
```

---

```py
"Avery" == "avery"
```

...

```py
False
```

---

```py
True == "True"
```

...

```py
False
```

---

```py
True == 2
```

...

```py
False
```

---

```py
True == 1
```

...

```py
True
```

In Python, `True` is equal to `1` and `False` is equal to `0`. If you find this
confusing, it's because it is.

---

```py
1 + 2 == 3
```

...

```py
True
```

---

```py
0.1 + 0.2 == 0.3
```

...

```py
False
```

...

```py
0.1 + 0.2
```

```py
0.30000000000000004
```

In general, math with floating-point numbers is inexact. Be careful when
comparing decimal results to specific values. If you find this confusing, it's
because it is.

---

```py
[1, 2, 3] == [1, 2, 3]
```

...

```py
True
```

In many other languges this comparison would give us `False`. Python is being
nice to us here.

---

```py
n = 5
```

...

```py
n == 5
```

...

```py
True
```

## The Equals Song

**Comparing values**

```py
name == "Avery"
```

...

**Assigning variables**

```py
name = "Avery"
```

...

<img src="/assets/equals-song.png" />

## Not Equals

We can use the not equal operators `!=` to check whether two values are not
equal.

```py
1 != 1
```

...

```py
False
```

...

```py
1 != 7
```

...

```py
True
```

## Inequality

We can use the not following inequaliy operators to test whether a value is
larger or smaller than another.

| Symbol | Operation                |
| ------ | ------------------------ |
| `<`    | Less Than                |
| `<=`   | Less than or equal to    |
| `>`    | Greater than             |
| `>=`   | Greater than or equal to |

...

```py
1 <= 1
```

...

```py
True
```

...

```py
1 > 7
```

...

```py
False
```

---

```py
5 < 5
```

...

```py
False
```

---

```py
5 <= 5
```

...

```py
True
```

---

```py
5 < 10
```

...

```py
True
```

---

```py
5 > 10
```

...

```py
False
```

---

```py
"banana" < "peach"
```

...

```py
True
```

---

```py
"banana" < "apple"
```

...

```py
False
```

---

```py
"app" < "apple"
```

...

```py
True
```

---

```py
"apple" < "Apple"
```

...

```py
False
```

## Comparison Operators

| Symbol | Operation                |
| ------ | ------------------------ |
| `==`   | Equal                    |
| `!=`   | Not equal                |
| `<`    | Less than                |
| `<=`   | Less than or equal to    |
| `>`    | Greater than             |
| `>=`   | Greater than or equal to |

## Boolean Operators

Python includes the following boolean operators: `and`, `or`, `not`.

| Operator | Usage     | Operation                                              |
| -------- | --------- | ------------------------------------------------------ |
| `and`    | `a and b` | Check that both `a` and `b` are `True`                 |
| `or`     | `a or b`  | Check that either `a` or `b` is `True`                 |
| `not`    | `not a`   | Flip a `True` value to `False`, or a `False` to `True` |

---

```py
"a" == "b" and 10 < 5
```

...

```py
False
```

---

```py
"a" == "b" or 10 > 5
```

...

```py
True
```

---

```py
"a" == "a" or 10 < 5
```

...

```py
True
```

---

```py
"a" == "b" or 10 < 5
```

...

```py
False
```

---

```py
not 2 > 1
```

...

```py
False
```

---

```py
not "a" == "b"
```

...

```py
True
```

## Boolean Operator Precedence

```py
False and (True or True)
```

...

```py
False
```

...

```py
(False and True) or True
```

...

```py
True
```

...

```py
False and True or True
```

...

```py
True
```
