# Find the word with the highest scrabble score starting with each letter
# of the alphabet in the text of Alice in Wonderland

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

bestWord = None
bestScore = 0

for word in words:
    score = 0

    for letter in word:
        score += letterPoints[letter]

    if score > bestScore:
        bestScore = score
        bestWord = word

print(bestWord)
print(bestScore)
