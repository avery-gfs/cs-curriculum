# Probabilistically generate a sequence of words based on the text of
# Alice in Wonderland

import random

with open("alice.txt") as file:
    words = file.read().split()  # Get words from file

successors = {}

# Loop over the list of words. For each word, create an entry in the successors
# dictionary. The value for each entry should be the list of words that
# come immediately after the given key word in the story (with duplicates).
#
# For example, given this text:
#
# "the rabbit was late and the rabbit ran away"
#
# The `successors` dictionary would contain:
#
# {
#     "the": ["rabbit", "rabbit"],
#     "rabbit": ["was", "ran"],
#     "was": ["late"],
#     "late": ["and"],
#     "and": ["the"],
#     "ran": ["away"],
# }

# You code goes here

# Should print ['well', 'or', 'and', 'hollow', 'sigh', 'voice', 'voice']
print(successors["deep"])

output = []
current = random.choice(words)

# The variable `current` is initialized as a random word from the story.
# Repeat the following steps 100 times:
#
# 1) Add the current word to the list `output`
#
# 2) Choose a new word at random from the list of words in `successors`
#    for the key `current`. Set this new word as the new value for `current`.

# You code goes here

print(" ".join(output))
