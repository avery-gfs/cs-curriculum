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
print(True)
```

```
True
```

...

```py
print(true)
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
error message. If you find this confusing, it's because it is: Python makes a
bad design choice here; programming languages are full of them.

## Comparisons

One way to get booleans in Python is by comparing values using the equality `==`
operator.

```py
print(1 == 1)
print(1 == 7)
```

```py
True
False
```

## Equality Song

**Comparing values**

```py
name == "Avery"
```

**Assigning variables**

```py
name = "Avery"
```

...

> Double equals, double equals for comparing Single equals for assigning

_(In C Major)_

```
mi-mi mi-mi, mi-mi mi-mi fa re mi mi
do-do do-do  la    so    do do
```
