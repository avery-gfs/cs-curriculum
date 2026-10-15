import os

done = []
undone = []

while True:
    os.system("clear")
    print("tasks:\n")

    for task in undone:
        print("[ ]", task)

    for task in done:
        print("[x]", task)

    task = input("\ntask name: ")

    if task in done:
        done.remove(task)

    elif task in undone:
        done.append(task)
        undone.remove(task)

    else:
        undone.append(task)

    done.sort()
    undone.sort()
