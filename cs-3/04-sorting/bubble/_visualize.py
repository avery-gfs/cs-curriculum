items = list("🦀🥦🫖🐼🧲🐼")


def render(index):
    left = "   ".join(items[:index])

    if left:
        left = "   " + left

    right = "   ".join(items[index + 2 :])

    if right:
        right += "   "

    middle = f" ( {items[index]}   {items[index + 1]} ) "
    print("[" + left + middle + right + "]")


for end in range(len(items) - 1, 0, -1):
    for index in range(end):
        render(index)

        if items[index] > items[index + 1]:
            tmp = items[index]
            items[index] = items[index + 1]
            items[index + 1] = tmp
            render(index)
