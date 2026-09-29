def quicksort(items):
    if items == []:
        return []

    lo = [item < pivot for item in items]
    eq = [item == pivot for item in items]
    hi = [item > pivot for item in items]

    quicksort(lo)
    quicksort(hi)

    return lo + eq + hi


numbers = [8, 7, 12, 4, 10, 4, 3, 12, 11, 5, 2, 1, 6, 7, 9, 12]

quicksort(numbers)
print(numbers)

emojis = list("🦀🥦🫖🐼🧲🐼🏀🫖🪭💩🍄⚽🥑🥦🦘🫖")

quicksort(emojis)
print(emojis)

words = "Mayday Mayday watch the needle leave the dial".split()

quicksort(words)
print(words)
