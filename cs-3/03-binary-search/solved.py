def search(lst, target):
    if lst == []:
        return False

    mid = len(lst) // 2

    if lst[mid] == target:
        return True

    if lst[mid] < target:
        return search(lst[mid + 1 :], target)

    return search(lst[:mid], target)


lst = [2, 5, 24, 32, 33, 34, 35, 38, 38, 41, 49, 74, 79, 87, 91, 98, 98, 99]

print(search(lst, 74))  # Should print True
print(search(lst, 75))  # Should print False
