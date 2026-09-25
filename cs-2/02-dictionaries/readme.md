# Dictionaries

## Data Structures

Primitives: represent a single piece of information

numbers, booleans, strings

Data structures: contain multiple pieces of information

lists, tuples, sets, **dictionaries**

## What are Dictionaries

A dictionary is a collection of key/value pairs that allows us to look up the
value associated with each key.

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

_Note that the correct name for this data structure is a "map" (or more
specifically a "hashmap"). The name "record" or "object" is potentially
acceptable. Python's decision to name these data structures "dictionaries" is
idiosyncratic, and a silly and confusing choice imo._

## Look up a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

...

```py
votes["strawberry"]
```

...

```
1
```

## Missing Key

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

```py
votes["garlic"]
```

...

```
Traceback (most recent call last):
  File "<python-input-23>", line 1, in <module>
    votes["garlic"]
    ~~~~~^^^^^^^^^^
KeyError: 'garlic'
```

## Add a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

...

```py
votes["mint"] = 1
```

...

```py
{"strawberry": 1, "chocolate": 1, "vanilla": 2, "mint": 1}
```

## Update a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

...

```py
votes["strawberry"] = 3
```

...

```py
{"strawberry": 3, "chocolate": 1, "vanilla": 2}
```

**A dictionary can only contain a single entry for a given key.**

## Increment a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

...

```py
votes["strawberry"] += 1
```

...

```py
{"strawberry": 2, "chocolate": 1, "vanilla": 2}
```

## Remove a Value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
```

...

```py
del votes["chocolate"]
```

...

```py
{"strawberry": 1, "vanilla": 2}
```

## Empty Dictionary

...

```py
votes = {}
```

## Check membership

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2, "mint": 3}
```

...

```py
"mint" in votes
"pineapple" in votes
```

...

```py
True
False
```

## Iterate over keys

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2, "mint": 3}

for flavor in votes:
    print(flavor, votes[flavor])
```

...

```
strawberry 1
chocolate 1
vanilla 2
mint 3
```

## Ice cream flavor voting

```py
votes = {}

# Loop forever

while True:
    flavor = input("Enter your favorite flavor: ")

    if flavor in votes:
        votes[flavor] += 1  # Increase vote count by one
    else:
        votes[flavor] = 1  # Set initial vote count to one

    print(votes)  # Print out vote data after each new vote
```

## Scrabble Points

```txt
a:  1, b:  3, c:  3, d:  2, e:  1, f:  4, g:  2, h:  4,
i:  1, j:  8, k:  5, l:  1, m:  3, n:  1, o:  1, p:  3,
q: 10, r:  1, s:  1, t:  1, u:  1, v:  4, w:  4, x:  8,
y:  4, z: 10
```

What is the score for "apple"?

...

```
9
```

...

What is the score for "quaker"?

...

```
19
```

## Looping Over Characters

```py
word = "hello"

for c in word:
    print(c)
```

...

Note that you can use a `for` loop to loop over the characters in a string.

```
h
e
l
l
o
```

## Problem: Scrabble Score

```
Enter a word: germantown
16
```

## Finding a Maximizing Value

```py
words = [
    "chapter", "i", "down", "the", "rabbit", "hole", "alice",
    "was", "beginning", "to", "get", "very", "tired",
]
```

How do we find the longest word in a list?

...

```py
maxLen = 0
maxWord = None

for word in words:
    if len(word) > maxLen:
        maxLen = len(word)
        maxWord = word

print(maxWord)
print(maxLen)
```

```
beginning
9
```

What happens if we have multiple words with the same length?

## Problem: Best Word Score

```txt
chapter i down the rabbit hole alice was beginning to get very tired
of sitting by her sister on the bank and of having nothing to do once
or twice she had peeped into the book her sister was reading but it
had no pictures or conversations in it and what is the use of a book
thought alice without pictures or conversations so she was
considering in her own mind as well as she could for the hot day made
her feel very sleepy and stupid whether the pleasure of making a
daisy chain would be worth the trouble of getting up and picking the
daisies when suddenly a white rabbit with pink eyes ran close by her
there was nothing so very remarkable in that nor did alice think it
so very much out of the way to hear the rabbit say to itself oh dear
oh dear i shall be late when she thought it over afterwards it...
```

Find the word with the highest Scrabble score.

## `dict.keys()`

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}

for k in votes.keys():
    print(k)
```

...

```
strawberry
chocolate
vanilla
```

## `dict.values()`

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}

for v in votes.values():
    print(v)
```

...

```
1
1
2
```

## `dict.items()`

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}

for (k, v) in votes.items():
    print(k, v)
```

...

```
strawberry 1
chocolate 1
vanilla 2
```

## `dict.get()`

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}

votes.get("chocolate", 0)
votes.get("mint", 0)
```

...

```
1
0
```

## Using `dict.get()`

```py
votes = {}

while True:
    flavor = input("Enter your favorite flavor: ")

    if flavor in votes:
        votes[flavor] += 1
    else:
        votes[flavor] = 1

    print(votes)
```

...

```py
votes = {}

while True:
    flavor = input("Enter your favorite flavor: ")
    votes[flavor] = votes.get(flavor, 0) + 1
    print(votes)
```

## `dict.setdefault()`

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 2}
votes.setdefault("chocolate", 0)
votes.setdefault("mint", 0)
```

...

```py
{"strawberry": 1, "chocolate": 1, "vanilla": 2, "mint": 0}
```

## Using `dict.setdefault()`

```py
votes = {}

while True:
    flavor = input("Enter your favorite flavor: ")

    if flavor in votes:
        votes[flavor] += 1
    else:
        votes[flavor] = 1

    print(votes)
```

...

```py
votes = {}

while True:
    flavor = input("Enter your favorite flavor: ")
    votes.setdefault(flavor, 0)
    votes[flavor] += 1
    print(votes)
```

## Problem: Letter Frequency

Find the percentage frequency for each letter in the text of Alice in
Wonderland.

```
a 8.2
b 1.4
c 2.2
d 4.6
e 12.6
...
```

---

`counts`

```py
{
    "a": 8788,
    "b": 1476,
    "c": 2396,
    "d": 4927,
    "e": 13571,
    # ...
}
```

## Problem: Longest Words

Find the longest word starting with each letter of the alphabet in the text of
Alice in Wonderland.

```
affectionately
beautifully
contemptuously
disappointment
extraordinary
...
```

---

`longWords`

```py
{
    "a": "affectionately",
    "b": "beautifully",
    "c": "contemptuously",
    "d": "disappointment",
    "e": "extraordinary",
    # ...
}
```

`wordLengths`

```py
{
    "a": 14,
    "b": 11,
    "c": 14,
    "d": 14,
    "e": 13,
    # ...
}
```

## Problem: Best Word Each Letter

Find the word with the highest scrabble score starting with each letter of the
alphabet in the text of Alice in Wonderland.

```
affectionately 25
beautifully 19
contemptuously 23
difficulty 22
extraordinary 24
...
```

---

`bestWords`

```py
{
    "a": "affectionately",
    "b": "beautifully",
    "c": "contemptuously",
    "d": "difficulty",
    "e": "extraordinary",
    # ...
}
```

`bestScores`

```py
{
    "a": 25,
    "b": 19,
    "c": 23,
    "d": 22,
    "e": 24,
    # ...
}
```

## Challenge: Not-So-Large Language Model

Use the text of _Alice in Wonderland_ to probabilistically generate a sequence
of 100 words.

First, create a dictionary `successors` that maps each word to a list of the
words that immediately follow it in the story. Keep duplicate words in each
list.

For example, given this text:

```txt
the rabbit was late and the rabbit ran away
```

The `successors` dictionary would contain:

```py
{
    "the": ["rabbit", "rabbit"],
    "rabbit": ["was", "ran"],
    "was": ["late"],
    "late": ["and"],
    "and": ["the"],
    "ran": ["away"],
}
```

---

Next, choose a random word from the story. This is the first word in the output
sequence. Then, choose the next word at random from the list of words that
follow the current word from the dictionary. Repeat this process to choose
subsequence words in the output sequence. For example, using the following
`successors` dictionary:

```py
{
    "sun": ["shines", "shines", "sets"],
    "shines": ["brightly", "warmly"],
    "sets": ["slowly", "today"],
    "brightly": ["today", "again"],
    "warmly": ["today"],
    "slowly": ["today"],
    "again": ["sun"],
    "today": ["sun", "ends"],
    "ends": ["today"],
}
```

1. Choose a random word from the story: `sun`
2. Choose a random word from `successors["sun"]` -> `sets`
3. Choose a random word from `successors["sets"]` -> `slowly`
4. Choose a random word from `successors["slowly"]` -> `today`
5. Choose a random word from `successors["today"]` -> `sun`
6. Choose a random word from `successors["sun"]` -> `shines`
7. Choose a random word from `successors["shines"]` -> `warmly`
8. Choose a random word from `successors["warmly"]` -> `today`

Final Output:

```
sun sets slowly today sun shines warmly today
```

---

You can choose a random value from a list using `random.choice`.

```py
import random

words = ['well', 'or', 'and', 'hollow', 'sigh', 'voice', 'voice']

random.choice(words)  # A random word from the list
```

---

Example output from the final model:

> his claws and off you getting its head do next peeped into a pair of more i
> tell you make out who is like the refreshments but why is the gryphon the
> meaning of course not becoming and barking hoarsely all about them a sound of
> white kid gloves and say presently the distance and in wonderland of tarts on
> like a graceful zigzag and oh how the jurors she had not make it pleaded poor
> child said alice added the things that i think it muttered to speak but i
> could think i beg pardon said the little nervous

> business there seemed to come on it does it occurred to alice cautiously
> replied alice but why i mentioned before and repeat you like it was a moment
> and waving of march hare alice called softly after the game the eaglet bent
> down and stupid but they draw you dont believe you my tail but youre falling
> through into the king said the fifth bend i beg for such a thick wood to find
> them and she took the temper of trees a very queer indeed the way which word i
> could and the sea but said the right size

> and tillie and then unrolled the moment she had made of his head how she
> walked off this time said alice im glad she began dreaming after a little
> timidly saying lessons youd rather alarmed at the march hare sixteenth added
> the moral of boots and looked round on messages for having the reason to him
> sighing in but she left her to take me see you manage on they were silent the
> judge ill set dinah tell you our cat said alice went alice that she could not
> a poor man said alice that to set out again no
