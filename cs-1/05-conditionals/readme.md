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

What will this code print?

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

What will this code print?

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

What will this code print?

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

What will this code print?

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

...

No, that ordering is not possible.

## Syntax Issues

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

```py
n = int(input("Enter a number: "))

if n < 0:
    print("Negative")

else:
    print("Not negative")
```

---

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

What will this code print?

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

## Ordering

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

## Elif Without Else

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
tempF = 300

if tempF < 32:
    print("Water is solid: ice")

elif tempF <= 212:
    print("Water is liquid: water")
```

...

```
```

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

Only the first branch whose condition matches is evaluated.

## Nested Conditionals

What will this code print?

```py
language = "Spanish"
n = -7

if language == "Spanish":
    if n > 0:
        print("Positivo")
        
    elif n < 0:
        print("Negativo")
        
    else:
        print("Cero")

        
elif language == "English":
    if n > 0:
        print("Positive")
        
    elif n < 0:
        print("Negative")
        
    else:
        print("Zero")
```

...

```
Negativo
```

---

What will this code print?

```py
language = "English"
n = 0

if language == "Spanish":
    if n > 0:
        print("Positivo")
        
    elif n < 0:
        print("Negativo")
        
    else:
        print("Cero")

        
elif language == "English":
    if n > 0:
        print("Positive")
        
    elif n < 0:
        print("Negative")
        
    else:
        print("Zero")
```

...

```
Zero
```

---

What will this code print?

```py
language = "French"
n = 10

if language == "Spanish":
    if n > 0:
        print("Positivo")

    elif n < 0:
        print("Negativo")

    else:
        print("Cero")


elif language == "English":
    if n > 0:
        print("Positive")

    elif n < 0:
        print("Negative")

    else:
        print("Zero")
```

...

```
```

## Problem: Grades

```py
points = int(input("Enter assignment points: "))

# Print a letter grade (A, B, C, D, or F) based on
# the points earned for an assignment
```

## Problem: Positive Even Whole

```py
n = float(input("Enter a number: "))

# Print "Positive" if `n` greater than or equal to 0
# Print "Even" if `n` is even
# Print "Whole" if `n` is a whole number
#
# For numbers that satisfy multiple conditions, print all relavant messages
```

## Problem: Discount

```py
age = float(input("Enter age: "))

# Print "Youth discount" for users aged below 18
# Print "Senior discount" for users aged 65 or above
# Print "No discount" for all other users
```

## Problem: Rock Paper Scissors

```py
import random

move = input("Enter a move (rock, paper, or scissors): ")

computerMove = random.choice(["rock", "paper", "scissors"])

print(f"Computer's move: {computerMove}")

# Print "You win!", "You lose!" or "You tie!" for a rock-paper-scissors
# game depending on the user's input and the computer's random move. Print
# "Invalid move. You lose!" for invalid user move inputs
#
# Examples:
#
# Enter a move (rock, paper, or scissors): paper
# Computer's move: rock
# You win!
#
# Enter a move (rock, paper, or scissors): rock
# Computer's move: paper
# You lose!
#
# Enter a move (rock, paper, or scissors): scissors
# Computer's move: scissors
# You tie!
#
# Enter a move (rock, paper, or scissors): towel
# Computer's move: rock
# Invalid move. You lose!
```

## Problem: Time Conversion

```py
totalSeconds = int(input("Enter a duration in seconds: "))

seconds = totalSeconds % 60
minutes = totalSeconds // 60 % 60
hours = totalSeconds // (60 * 60) % 24
days = totalSeconds // (60 * 60 * 24)

# Calculate the days, hours, minutes, and seconds in the total
# number of seconds entered by the user. Print these values,
# omitting zero values, with correct pluralization
#
# Examples:
#
# Enter a duration in seconds: 1234561
#
# 14 days
# 6 hours
# 56 minutes
# 1 second
#
# Enter a duration in seconds: 3605
#
# 1 hour
# 5 seconds
```
