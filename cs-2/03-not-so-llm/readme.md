# Not-So-Large Language Model

## Text Prediction Intro

Large language models generate text by repeatedly predicting what token is most
likely to come next, based on the text that came before it.

This problem builds a much simpler version of that idea. Instead of considering
an entire conversation, at the current word and randomly chooses one of the
words that followed it in _Alice in Wonderland_.

For example, if the word `alice` is often followed by `said`, `was`, or
`thought`, this model can choose one of those words as its prediction. Repeating
that process creates an original sequence of text.

## Source Text

Alice in wonderland, lowercase, including spaces, line breaks, periods, hyphens,
and apostrophes.

```
in another moment down went alice after it never once considering how in
the world she was to get out again . the rabbit-hole went straight on like a
tunnel for some way and then dipped suddenly down so suddenly that alice had
not a moment to think about stopping herself before she found herself falling
down a very deep well . either the well was very deep or she fell very slowly
for she had plenty of time as she went down to look about her and to wonder
what was going to happen next .
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

---

Next, choose one of the successors of the `.` character. This is the first word
in the output sequence. Then, choose the next word at random from the list of
words that follow the current word from the dictionary. Repeat this process to
choose subsequence words in the output sequence. For example, using the
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

1. Choose a random word from the story: `sun`
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
