# Find the percentage frequency for each letter in the text of
# Alice in Wonderland
#
# Expected output:
#
# a 8.2
# b 1.4
# c 2.2
# d 4.6
# e 12.6
# f 1.9
# g 2.4
# h 6.8
# i 7.0
# j 0.1
# k 1.1
# l 4.4
# m 2.0
# n 6.5
# o 7.6
# p 1.4
# q 0.2
# r 5.0
# s 6.0
# t 9.9
# u 3.2
# v 0.8
# w 2.5
# x 0.1
# y 2.1
# z 0.1

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

for letter in sorted(counts.keys()):
    print(letter, round(counts[letter] / total * 100, 1))
