# Find the longest word starting with each letter of the alphabet in
# the text of Alice in Wonderland
#
# Expected output:
#
# affectionately 25
# beautifully 19
# contemptuously 23
# difficulty 22
# extraordinary 24
# frontispiece 19
# geography 19
# hjckrrh 26
# inquisitively 28
# jumping 19
# knocking 19
# lazily 18
# multiplication 20
# neighbouring 19
# occasionally 19
# puzzling 29
# quickly 25
# refreshments 20
# squeezed 27
# thoughtfully 25
# uncomfortably 25
# vanishing 16
# whiskers 18
# xii 10
# yesterday 16
# zigzag 26

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

bestWords = {}
bestScores = {}

for word in words:
    score = 0

    for letter in word:
        score += letterPoints[letter]

    firstLetter = word[0]
    bestScores.setdefault(firstLetter, 0)

    if bestScores[firstLetter] < score:
        bestWords[firstLetter] = word
        bestScores[firstLetter] = score

for letter in sorted(bestWords.keys()):
    print(bestWords[letter], bestScores[letter])
