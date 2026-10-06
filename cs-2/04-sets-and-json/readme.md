# Sets and JSON

## Data Structures

Primitives: represent a single piece of information

numbers, booleans, strings

Data structures: contain multiple pieces of information

lists, tuples, **sets**, dictionaries

## What are Sets

A set is a collection of unique values that allows us to quickly check
membership.

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

## Add a value

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

...

```py
states.add("TX")
states.add("FL")
```

...

```py
{"NY", "CA", "IL", "TX", "AZ", "PA", "FL"}
```

**A set can only contain a single copy of a given value.**

## Remove a Value

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

...

```py
states.remove("CA")
```

...

```py
{"NY", "IL", "TX", "AZ", "PA"}
```

...

```py
states.remove("FL")
```

...

```
Traceback (most recent call last):
  File "<python-input-3>", line 2, in <module>
    states.remove("FL")
    ~~~~~~~~~~~~~^^^^^^
KeyError: 'FL'
```

## Count Values

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

...

```py
len(states)
```

...

```py
6
```

## Set From a List

```py
statesList = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "TX"]
```

...

```py
set(statesList)
```

...

```py
{"CA", "TX", "AZ", "NY", "IL", "PA"}
```

_Notice that the order has changed_

## Empty Set

...

```py
states = set()
```

Why not `{}`?

## Check membership

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

...

```py
"TX" in states
"FL" in states
```

...

```py
True
False
```

---

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

...

```py
"TX" not in states
"FL" not in states
```

...

```py
False
True
```

## Iterate Over Values

```py
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}

for state in states:
    print(state)
```

...

```
PA
CA
AZ
TX
IL
NY
```

## Set of Words

How many distinct words are there in Alice in Wonderland?

```py
with open("alice.txt") as file:
    words = file.read().split()  # Get words from file
```

...

```py
wordSet = set()

for word in words:
    wordSet.add(word)

print(len(wordSet))
```

...

```py
wordSet = set(words)
print(len(wordSet))
```

## Why Use Sets?

Why use sets instead of lists?

1. To work with deduplicated data
2. To efficiently check set membership

## Membership Check Efficiency

```py
statesList = ["NY", "CA", "IL", "TX", "AZ", "PA"]
states = {"NY", "CA", "IL", "TX", "AZ", "PA"}
```

```py
"NY" in statesList
"NY" in states
```

Checking set membership is much more efficient than checking list membership.

- List membership checking scales with the **size of the list**.

- Set membership checking stays (relatively) **constant**.

## Problem: To Do App

- Entering a new task name adds the task to the list in an undone state.

- Entering the task name a second time sets the task's state to done.

- Entering the task name a third time removes the task from the to do app list.

- Display the total number of tasks, and the number currently undone.

<img height="400" src="/assets/to-do.gif" />

## JSON (JavaScript Object Notation)

JSON is a data serialization format, which allows us to convert structured data
(strings, numbers, lists, etc) into text format. This allows us to easily save
the data to a file, load it from a file, send it over the internet, open it with
other programs, etc. It is a simple but immensely useful and widely used tool
that every software engineer should be familiar with.

https://www.json.org/json-en.html

```
Python program -> Text file (JSON)

Text file (JSON) -> Python program

Python program -> Network (JSON) -> Python program (another computer)

Python program -> Text file (JSON) -> Program in another language
```
