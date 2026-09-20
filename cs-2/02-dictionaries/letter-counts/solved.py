with open("alice.txt") as file:
    # Get text from file
    text = file.read()

    # Remove spaces and newlines
    text = text.replace(" ", "").replace("\n", "")

counts = {}
total = len(text)

for letter in text:
    counts.setdefault(letter, 0)
    counts[letter] += 1

for letter, count in counts.items():
    print(letter, round(count / total * 100, 1))
