# Modulo Applications

## Modulo Review

The modulo operator in Python computes the remainder using
[floored division](https://en.wikipedia.org/wiki/Modulo#Variants_of_the_definition).

```py
a % b
```

Means:

> Subtract (or add) zero or more copies of `b` from `a` in order to get the
> smallest number possible that is `>= 0`

...

(Or, if `a` is negative)

> Subtract (or add) zero or more copies of `b` from `a` in order to get the
> highest (least negative) number possible that is `<= 0`

---

What value does this expression produce?

```py
11 % 2
```

...

```
11 -> 9 -> 7 -> 5 -> 3 -> 1
```

---

What value does this expression produce?

```py
14 % 1
```

...

```
14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0
```

---

What value does this expression produce?

```py
14 % 2
```

...

```
14 -> 12 -> 10 -> 8 -> 6 -> 4 -> 2 -> 0
```

---

What value does this expression produce?

```py
14 % 5
```

...

```
14 -> 9 -> 4
```

---

What value does this expression produce?

```py
-14 % 5
```

...

```
-14 -> -9 -> -4 -> 1
```

---

What value does this expression produce?

```py
14 % 14
```

...

```
14 -> 0
```

---

What value does this expression produce?

```py
14 % 20
```

...

```
14
```
