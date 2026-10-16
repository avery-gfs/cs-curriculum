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

# ??
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

...

Write a program that calculates and displays the parity of an integer that the
user inputs using two `if` statements. "Parity" refers to whether a number is
even or odd.

...

```py
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")

if n % 2 != 0:
    print("Odd")
```

## Independent Ifs

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

## Control Flow Ordering

Will this code

```py
if n < 0:
    print("n is negative")

if n % 2 == 0:
    print("n is even")
```

ever print

```
n is even
n is negative
```

for some value of `n`?

## Syntax

What will this code print?

```py
n = 10

if n % 2 == 0:
print("Even")

if n % 2 != 0:
print("Odd")
```

...

```
  File "<python-input-0>", line 4
    print("Even")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 3
```

---

What will this code print?

```py
n = 10

if n % 2 == 0
    print("Even")

if n % 2 != 0
    print("Odd")
```

...

```
  File "<python-input-1>", line 3
    if n % 2 == 0
                 ^
SyntaxError: expected ':'
```

---

What will this code print?

```py
n = 10

if n % 2 == 0:

if n % 2 != 0:
    print("Odd")
```

...

```
  File "<python-input-2>", line 5
    if n % 2 != 0:
    ^^
IndentationError: expected an indented block after 'if' statement on line 3
```

---

What will this code print?

```py
n = 10

if n % 2 = 0:
    print("Even")

if n % 2 != 0:
    print("Odd")
```

...

```
  File "<python-input-3>", line 3
    if n % 2 = 0:
       ^^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
```

## Indentation

What will this code print?

```py
greet = True

if greet:
    print("Hello")
    print("World")
```

...

```
Hello
World
```

---

What will this code print?

```py
greet = False

if greet:
    print("Hello")
    print("World")
```

...

```
```

---

What will this code print?

```py
greet = False

if greet:
    print("Hello")
print("World")
```

...

```
World
```

## Else Clauses

Else clauses can be added to if statements to write code that runs when the if
condition is `False`.

```
if <condition>:
    <code block>
    ...

else:
    <code block>
    ...
```

...

Rewrite using an `if` statement with an `else` clause.

```py
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")

if n % 2 != 0:
    print("Odd")
```

...

```py
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")

else:
    print("Odd")
```

---

What will this code print?

```py
n = 4

if n % 2 == 0:
    print("Even")

else:
    print("Odd")
```

...

```
Even
```

---

What will this code print?

```py
n = 5

if n % 2 == 0:
    print("Even")

else:
    print("Odd")
```

...

```
Odd
```

---
Will this code even print both "Even" and "Odd" for some value of `n`? Will it
ever print neither?

```py
if n % 2 == 0:
    print("Even")

else:
    print("Odd")
```
---

No. Exactly one of the code blocks will run.

## Elif Clauses

Elif clauses can be used to add existing conditional checks to an if statement.
In a conditional statement combining `if`, `elif`, and `else`, no more than one
code block will be run.

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

---

What will this code print?

```py
tempF = 300

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")

else:
    print("Water is gas: steam")
```

...

```
Water is gas: steam
```

---

What will this code print?

```py
tempF = 10

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")

else:
    print("Water is gas: steam")
```

...

```
Water is solid: ice
```

---

What will this code print?

```py
tempF = 300

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")
```

...

```
```

---

What will this code print?

```py
tempF = 75

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")
```

...

```
Water is liquid: water
```

---

What will this code print?

```py
tempF = 10

if tempF <= 212:
    print("Water is liquid: water")

elif tempF < 32:
    print("Water is solid: ice")

else:
    print("Water is gas: steam")
```

...

```
Water is liquid: water
```

Ordering matters!

## Exclusivity

What will this code print?

```py
n = -8

if n < 0:
    print("n is negative")

elif n % 2 == 0:
    print("n is even")
```

...

```
n is negative
```

...

Only one code block will run.

## Multiple Elifs

What will this code print?

```py
tempF = 67

if tempF < 32:
    print("Water is solid: ice")

elif tempF == 67:
    print("THE PERFECT TEMPERATURE!")

elif tempF <= 212:
    print("Water is liquid: water")

else:
    print("Water is gas: steam")
```

...

```
THE PERFECT TEMPERATURE!
```

## Nested Conditionals

What will this code print?

```py
languages = "Spanish"
n = -7

if language == "Spanish":
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("cero")

elif language == "English":
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")
```

...

```
negativo
```

---

What will this code print?

```py
languages = "English"
n = 0

if language == "Spanish":
    if n > 0:
        print("positivo")
    elif n < 0:
        print("negativo")
    else:
        print("cero")

elif language == "English":
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")
```

...

```
zero
```

---

What will this code print?

```py
languages = "French"
n = 10

if language == "Spanish":
    if n > 0:
        print("positivo")
        
    elif n < 0:
        print("negativo")
        
    else:
        print("cero")

        
elif language == "English":
    if n > 0:
        print("positive")
        
    elif n < 0:
        print("negative")
        
    else:
        print("zero")
```

...

```
```
