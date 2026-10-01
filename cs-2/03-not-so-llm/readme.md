# Not-So-Large Language Model

## Text Prediction Intro

Large language models generate text by repeatedly predicting what token is most
likely to come next, based on the text that came before it.

This problem builds a much simpler version of that idea. Instead of considering
an entire conversation, the model looks at the most recent word generated and
randomly chooses one of the words that follows it in the text of the story
_Alice in Wonderland_.

For example, if the word `alice` is often followed by `said`, `was`, or
`thought`, this model can choose one of those words as its prediction. Repeating
that process creates an original sequence of text.

## Source Text

The source text file `alice-punct.txt` contains the text of Alice in wonderland,
in lowercase, including spaces, line breaks, periods (with spaces added before
them), hyphens, and apostrophes.

```
please ma'am is this new zealand or australia and she tried to curtsey as she
spoke fancy curtseying as you're falling through the air do you think you
could manage it and what an ignorant little girl she'll think me for asking
no it'll never do to ask perhaps i shall see it written up somewhere . down
down down . there was nothing else to do so alice soon began talking again .
dinah'll miss me very much to-night i should think dinah was the cat . i hope
they'll remember her saucer of milk at tea-time . dinah my dear i wish you
were down here with me there are no mice in the air i'm afraid but you might
catch a bat and that's very like a mouse you know .
```

## Problem: Language Model

Use the text of _Alice in Wonderland_ to probabilistically generate a sequence
of words to make a new piece of text.

First, create a dictionary `successors` that maps each word to a list of the
words that immediately follow it in the story (duplicate words are allowed).

For example, given this text:

```txt
the rabbit was late and the rabbit ran away .
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
    "away": ["."],
}
```

_Note: you may want to use the
[setdefault](https://www.w3schools.com/python/ref_dictionary_setdefault.asp)
dictionary method._

---

Next, choose one of the successors of the `.` character. This is the first word
in the output sequence. Then, choose the next word at random from the list of
words that follow the current word from the dictionary. Repeat this process to
choose subsequent words for the output sequence. For example, using the
following `successors` dictionary:

```py
{
    ".": ["sun"],
    "sun": ["shines", "shines", "sets"],
    "shines": ["brightly", "warmly"],
    "sets": ["slowly", "today"],
    "brightly": ["today", "again"],
    "warmly": ["today"],
    "slowly": ["today"],
    "again": ["sun"],
    "today": ["sun", "ends", "."],
    "ends": ["today"],
}
```

1. Choose a random word from `successors["."]` -> `sun`
2. Choose a random word from `successors["sun"]` -> `sets`
3. Choose a random word from `successors["sets"]` -> `slowly`
4. Choose a random word from `successors["slowly"]` -> `today`
5. Choose a random word from `successors["today"]` -> `sun`
6. Choose a random word from `successors["sun"]` -> `shines`
7. Choose a random word from `successors["shines"]` -> `warmly`
8. Choose a random word from `successors["warmly"]` -> `today`
9. Choose a random word from `successors["today"]` -> `.`

Final Output:

```
sun sets slowly today sun shines warmly today .
```

---

You should stop the generation process when these two conditions are true:

1. The output sequence is at least 100 words long, **and**
2. The final word in the sequence is `.`

---

You can choose a random value from a list using `random.choice()`.

```py
import random

words = ["well", "or", "and", "hollow", "sigh", "voice", "voice"]

random.choice(words)  # A random word from the list
```

---

Example output from the final model:

> alice went on everybody minded their faces and say creatures argue . first
> remark with hearts . they both go after that is sure what i can't remember
> half no no wise fish came first she said the king and said alice when she
> thought alice . no use denying it goes on which word two said the roof off .
> you to the creatures order one as it over their forepaws to the little
> crocodile improve his confusion of tears . first speech caused a line along
> the hatter and wag my own children who were silent for the caterpillar
> decidedly and then alice could see after her own feet high said alice .
