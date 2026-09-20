with open("alice.txt") as file:
    words = file.read().split()  # Get words from file

longest = {}

for word in words:
    firstLetter = word[0]

    if len(word) > len(longest.get(firstLetter, "")):
        longest[firstLetter] = word

for word in longest.values():
    print(word)
