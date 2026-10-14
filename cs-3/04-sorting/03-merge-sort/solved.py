def mergeSort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = mergeSort(items[:mid])
    right = mergeSort(items[mid:])

    result = []

    while left != [] and right != []:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    return result


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

print(mergeSort(numbers))

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

print(mergeSort(emojis))

words = "Mayday Mayday watch the needle leave the dial".split()

print(mergeSort(words))
