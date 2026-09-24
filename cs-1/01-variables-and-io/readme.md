# Output, Variables, and Input

## Hello World!

There's an old tradition among computer programmers: when learning a new
language, we start by writing a little program that prints out the message
"Hello world!". Type out the code below and run it.

```py
print("Hello world!")
```

When you run the code, it should print out the following message.

```
Hello world!
```

Congratulations, you are now a computer programmer!

## Type out these examples!

You can't learn to play piano just by watching videos of other people playing.
At some point you've got to put your fingers on the keyboard.

![](https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg)

Similarly, you should type the code in these examples into your editor, rather
than copying and pasting it. It's tedious, but it will better prepare you to
write your own code in the future.

## What is a Program?

A **program** is a sequence of instructions that tells a computer how to perform
a task. We call these instructions **code**. Our "hello world" program contains
a single instruction.

```py
print("Hello world!")
```

- **Program**: a sequence of instructions that tells a computer how to perform a
  task.

- **Code**: the instructions in a program.

## Running Code

When we **run** a computer program, the computer goes through the instructions
in our code in order from the start of the program to the end.

- **Running** a program: having a computer follow the instructions in a program.

What will this code display?

```py
print("Hello world!")
print("Greetings from Python")
print("Let's write some code")
```

...

This program displays the three messages in the `print` instructions, in the
order that they are written.

```
Hello world!
Greetings from Python
Let's write some code
```

## Programming Languages

In the same way that there are many spoken languages (English, Mandarin, Hindi,
etc), there are many **programming languages**. Different languages have
different strengths and weaknesses.

In this course we'll be writing our programs using **Python**, a popular,
general-purpose programming language.

That being said, the concepts we'll learn will be relevant when using a wide
variety of programming languages.

- **Programming Language**: a way of writing code, using a specific set of
  instructions and following certain rules.

- **Python**: the programming language that we'll be using in this course.

---

Different spoken languages have different vocabulary (words) and different rules
for how those words can fit together (grammar).

Similarly, different programming languages provide different instructions, and
have different rules about how those instructions can be used.

![](/assets/lang-comparison.png)

## Comments

Comments start with a hash `#` symbol and are ignored when the code runs.
Comments are used for two purposes:

Adding notes to pieces of code:

```py
speed_limit = 35  # Speed limit in miles per hour
```

Temporarily disabling pieces of code:

```py
# print("Hello!")
print("Bonjour!")
```

You can toggle commends on/off for a block of code by selecting it and pressing
<kbd>Ctrl + /</kbd> or <kbd>Command + /</kbd>.

## Calling Print

Python code uses **functions**: instructions that tell Python to perform a
certain task.

We can use the `print` function to print out **strings** (pieces of text).

```py
print("Hello world!")  # Prints `Hello world!`
```

When we use a function to perform a task in our code, programmers say that we
**call** the function.

- **Function**: an instruction that tells our program to perform a certain task.
- **Calling** a function: writing the name of a function followed by
  parentheses, which tells the computer to perform the action associated with
  that function.
- **String**: a piece of text.

## Multiple Arguments

The values that we give a function when we call it are known as **arguments**.

Some functions like `print` can accept a flexible number of arguments, separated
by commas `,`. Others require a fixed number of arguments.

If we call `print` with multiple strings, Python will display these strings
together, with a space in between.

```py
print("Hello", "Avery")  # Prints `Hello Avery`
```

- **Arguments**: zero or more values placed between the parentheses when calling
  a function, that provide the function with information on how to perform its
  task. Multiple arguments require commas in between.

## No Arguments

What happens if we call `print` with no arguments?

```py
print()
```

...

It prints an empty line.

## Print Practice

What will this code print?

```py
print("Hello")
print()
print("a", "b", "c")
```

...

```
Hello

a b c
```

## Errors

When we write code, we inevitably make mistakes that cause **errors**.

- **Error**: an error occurs when a computer receives instructions that it can't
  understand.

- **Syntax Error**: an error caused by leaving out or adding extra symbols in
  code.

- **Name Error**: an error caused by an incorrect or misspelled name.

- **Crash**: when a computer encounters an error while running a program, the
  computer will typically crash (stop running) the program.

## Errors Practice

What's the issue?

```py
print "Hello world!"
```

...

Issue: missing parentheses.

```
  File "/tmp/demo.py", line 1
    print "Hello world!"
    ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

---

What's the issue?

```py
print(Hello world!)
```

...

Issue: missing quotes.

```
  File "/tmp/demo.py", line 1
    print(Hello world!)
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

---

What's the issue?

```py
print("Hello world!)
```

...

Issue: missing closing quote.

```
  File "/tmp/demo.py", line 1
    print("Hello world!)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

---

What's the issue?

```py
Print("Hello world!")
```

...

Issue: incorrect function name. Programming languages are picky about spelling
and capitalization.

```
Traceback (most recent call last):
  File "/tmp/demo.py", line 1, in <module>
    Print("Hello world!")
    ^^^^^
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

## Variables

**Variables** give us a way to associate a value with a name. Using variables is
integral to programming.

- **Variables**: names that are attached to values.

To define a variable, we put the name of the variable we're defining on the left
hand side of an `=` sign, and the value we're giving the variable on the right
hand side.

```py
name = "Avery"
print("Hello", name)  # Prints `Hello Avery`
```

What will this code print out?

```py
time = "morning"
name = "Avery"
print("Good", time, name)
```

...

```
Good morning Avery
```

## Format Strings

What will this code print out?

```py
time = "morning"
name = "Avery"
print("Good", time, ",", name, "!")
```

...

```
Good morning , Avery !
```

...

We can use **format strings** (f-strings) to be more precise about how we
display variables.

```py
time = "morning"
name = "Avery"
print(f"Good {time}, {name}!")
```

```
Good morning, Avery!
```

Format strings start with an `f` and can contain variable names wrapped in curly
brackets `{}`. These bracketed variable names get replaced with the values of
the variables.

---

What does this code print out?

```py
time = "morning"
name = "Avery"
print(f"Good {time}, name!")
```

...

Second variable isn't in brackets, so it doesn't get filled in.

```
Good morning, name!
```

---

What does this code print out?

```py
time = "morning"
name = "Avery"
print("Good {time}, {name}!")
```

...

The string is missing the `f` prefix, so it's treated as a normal string, not a
format string, and no variables get filled in.

```
Good {time}, {name}!
```

## Variable Names

Variable names may contain letters, digits, and underscores (`_`), but must not
start with a digit. Names are case sensitive.

```py
first_name = "Avery"  # OK
first name = "Avery"  # ERROR: names must not contain spaces
1stname = "Avery"     # ERROR: names must not start with a digit
```

_Come up with some examples of valid and invalid variables names._

## Variables Practice

What will this code print out?

```py
color = "green"
print(color)
color = "red"
print(color)
```

...

```
green
red
```

---

What will this code print out?

```py
color = "green"
color = "red"
print(color)
```

...

```
red
```

---

What will this code print out?

```py
color = "green"
# color = "red"
print(color)
```

...

```
green
```

---

What will this code print out?

```py
print(color)
color = "green"
```

...

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'color' is not defined
```

## String Input

We can use the `input` function to get text input from the **user** (a person
who is using our program). We can call `input` with a prompt argument that it
will show to the user.

```py
name = input("What is your name? ")  # Prompts the user for their name
print(f"Hello {name}")  # Greets the user
```

User input

```
What is your name? Avery
```

Output

```
Hello Avery
```

- **user**: a person who is using our program.

## Prompt Trailing Space

Notice that the prompt string has an extra space at the end.

```py
name = input("What is your name? ")
```

What would happen if we left this space out?

```py
name = input("What is your name?")
```

...

There would be no space between the prompt and the user input.

```
What is your name?Avery
```

## Problem: Name and Age

Write code that asks the user for their name and age and prints a message
containing both.

```
What is your name? Avery
What is your age? 12
```

```
Avery is 12 years old
```

## Problem: Citations

Write code that builds an APA book citation given:

- Author
- Title
- Publication year
- Publisher

Format: `Author. (Year). Title of Book. Publisher.`

Example:

```
Author: Tate, Bruce
Title: Seven Languages in Seven Weeks
Year: 2010
Publisher: The Pragmatic Bookshelf
```

```
Tate, Bruce. (2010). Seven Languages in Seven Weeks. The Pragmatic Bookshelf.
```

## Problem: Mad Libs

Write a Mad Libs generator.

Inputs

```
verb: cook
adjective: spicy
plural noun: frogs
number: 2
number: 200
substance: rice pudding
```

...

Output

```
When operating a used car, remember: never cook the engine if the car is spicy.
Before driving, make sure the gas tank is free of frogs.
Used cars perform best when driven between 2 and 200 miles per hour.
Always keep a large supply of rice pudding in your car for passengers to enjoy.
```
