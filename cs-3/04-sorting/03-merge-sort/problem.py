def mergeSort(items):
    # Add base case

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    result = []

    # Add merging code

    return result


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

print(mergeSort(numbers))

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

print(mergeSort(emojis))

words = "Mayday Mayday watch the needle leave the dial".split()

print(mergeSort(words))
