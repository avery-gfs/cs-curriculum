def bubbleSort(items):
    for limit in range(len(items) - 1, 0, -1):
        for index in range(limit):
            if items[index] > items[index + 1]:
                tmp = items[index]
                items[index] = items[index + 1]
                items[index + 1] = tmp


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

bubbleSort(numbers)
print(numbers)

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

bubbleSort(emojis)
print(emojis)

words = "Mayday Mayday watch the needle leave the dial I am reckless I am telling myself the story of my life".split()

bubbleSort(words)
print(words)
