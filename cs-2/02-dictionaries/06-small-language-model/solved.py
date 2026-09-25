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
# Example:
#
# {
#   ...
#   'falling': ['down', 'through'],
#   'deep': ['well', 'or', 'and', 'hollow', 'sigh', 'voice', 'voice'],
#   'fell': ['very', 'past', 'off', 'on', 'upon', 'asleep'],
#   'slowly': ['for', 'back', 'back', 'beginning', 'opened', 'followed', 'after', 'and'],
#   'plenty': ['of', 'of'],
#   ...
# }

for index, word in enumerate(words):
    if index < len(words) - 1:
        nextWord = words[index + 1]
        successors.setdefault(word, [])
        successors[word].append(nextWord)

print(
    successors["deep"]
)  # Should print ['well', 'or', 'and', 'hollow', 'sigh', 'voice', 'voice']

output = []
current = random.choice(words)

# The variable `current` is initialized as a random word from the story.
# Repeat the following steps 100 times:
#
# 1) Add the current word to the list `output`
#
# 2) Choose a new word at random from the list of words in `successors`
#    for the key `current`. Set this new word as the new value for `current`.

for _ in range(100):
    output.append(current)
    current = random.choice(successors[current])

print(" ".join(output))
