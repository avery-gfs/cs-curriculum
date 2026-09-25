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

for index, word in enumerate(words):
    if index < len(words) - 1:
        nextWord = words[index + 1]
        successors.setdefault(word, [])
        successors[word].append(nextWord)

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
#
# For example, using the following `successors` dictionary:
#
# {
#     "sun": ["shines", "shines", "sets"],
#     "shines": ["brightly", "warmly"],
#     "sets": ["slowly", "today"],
#     "brightly": ["today", "again"],
#     "warmly": ["today"],
#     "slowly": ["today"],
#     "again": ["sun"],
#     "today": ["sun", "ends"],
#     "ends": ["today"],
# }
#
# Possible result:
#
# "sun sets slowly today sun shines warmly today"

for _ in range(100):
    output.append(current)
    current = random.choice(successors[current])

print(" ".join(output))
