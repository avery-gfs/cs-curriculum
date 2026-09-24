with open("alice.txt") as file:
    words = file.read().split()  # Get words from file

letterPoints = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

# For each letter of the alphabet, find the highest scoring word
# that starts with that letter. Don't loop through the list of
# words more than once!

bestWords = {}  # Keep track of the highest scoring word for each letter
bestScores = {}  # Keep track of the scores for bestWords

# Find the word with the highest Scrabble score

for word in words:
    # Score variable for the current word
    score = 0

    # Loop through each letter in the current word
    # Look up the points for the letter and add it to the word score

    pass

    # After summing the points for each letter, get the first letter
    # of the word.
    #
    #   - If this is the first word we've seen that starts with this
    #     first letter, then update bestWord and bestScore to contain
    #     this word and its score
    #
    #   - If we already have a best word that starts with this first
    #     letter, check if the score for this word is better than the
    #     score for the old best word. If it is then update bestWord
    #     and bestScore to contain this new word and its score

    pass

# Display the highest scoring word for each letter along with its score

pass
