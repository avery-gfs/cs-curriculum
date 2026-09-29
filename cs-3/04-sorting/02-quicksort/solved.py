def quicksort(items):
    if items == []:
        return []

    pivot = items[0]

    lo = [item for item in items if item < pivot]
    eq = [item for item in items if item == pivot]
    hi = [item for item in items if item > pivot]

    return quicksort(lo) + eq + quicksort(hi)


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

print(quicksort(numbers))

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

print(quicksort(emojis))

words = "Mayday Mayday watch the needle leave the dial".split()

print(quicksort(words))
