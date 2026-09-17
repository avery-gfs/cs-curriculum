# Dictionaries

## What are Dictionaries

A dictionary is a collection of key/value pairs that allows us to look up the
value associated with each key.

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 1}
```

_Note that the correct name for this data structure is a "map" (or more
specifically a "hashmap"). The name "object" is also acceptable. Python's
decision to name these data structures "dictionaries" is idiosyncratic, and a
silly and confusing choice imo._

## Look up a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 1}
```

...

```py
votes["strawberry"]
```

...

```
1
```

## Add a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 1}
```

...

```py
votes["mint"] = 1
```

...

```py
{"strawberry": 1, "chocolate": 1, "vanilla": 1, "mint": 1}
```

## Update a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 1}
```

...

```py
votes["strawberry"] = 2
```

...

```py
{"strawberry": 2, "chocolate": 1, "vanilla": 1}
```

**A dictionary can only contain a single entry for a given key.**

## Increment a value

```py
votes = {"strawberry": 1, "chocolate": 1, "vanilla": 1}
```

...

```py
votes["chocolate"] += 1
```

...

```py
{"strawberry": 1, "chocolate": 2, "vanilla": 1}
```

## Check membership

...

```py
"mint" in votes  # True
"pineapple" in votes  # False
```

## Iterate over keys

```py
{"strawberry": 2, "chocolate": 1, "vanilla": 1, "mint": 1}

for flavor in votes:
    print(flavor, votes[flavor])
```

...

```
strawberry 2
chocolate 2
vanilla 1
mint 1
```

## Ice cream flavor voting

```py
votes = {"strawberry": 1}

while True:  # Loop forever
    flavor = input("Enter for your favorite flavor: ")

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

## Fining a Maximizing Value

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

## Problem: Alice in Wonderland Best Word Score

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
