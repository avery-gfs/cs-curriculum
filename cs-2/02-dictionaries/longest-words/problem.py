# Find the longest word starting with each letter of the alphabet in
# the text of Alice in Wonderland
#
# Expected output:
#
# affectionately
# beautifully
# contemptuously
# disappointment
# extraordinary
# frontispiece
# generally
# hippopotamus
# inquisitively
# judging
# knowledge
# longitude
# multiplication
# nevertheless
# occasionally
# processions
# quarrelling
# refreshments
# straightening
# thoughtfully
# uncomfortable
# variations
# wonderland
# xii
# yesterday
# zealand

with open("alice.txt") as file:
    words = file.read().split()  # Get words from file

longWords = {}
wordLengths = {}

pass

for word in sorted(longWords.values()):
    print(word)
