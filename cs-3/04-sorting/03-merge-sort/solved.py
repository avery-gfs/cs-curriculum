def mergeSort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    result = []

    while sortedLeft != [] and sortedRight != []:
        if sortedLeft[0] < sortedRight[0]:
            result.append(sortedLeft.pop(0))
        else:
            result.append(sortedRight.pop(0))

    result.extend(sortedLeft)
    result.extend(sortedRight)

    return result


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

print(mergeSort(numbers))

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

print(mergeSort(emojis))

words = "Mayday Mayday watch the needle leave the dial".split()

print(mergeSort(words))
