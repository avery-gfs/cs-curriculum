def render(items, i, j):
    print("```")
    print(" ".join(map(str, items)))
    print("  " * j + "^")
    print("  " * i + "^")
    print("```\n---\n")


def sofiaSort(items):
    for i in range(len(items)):
        for j in range(i, len(items)):
            if items[i] > items[j]:
                tmp = items[i]
                items[i] = items[j]
                items[j] = tmp


sofiaSort([5, 3, 2, 5, 1, 4, 1])
