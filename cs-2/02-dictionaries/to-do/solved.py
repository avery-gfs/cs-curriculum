import os

done = {}
undone = {}

while True:
    os.system("clear")

    for name in undone:
        print(f"[ ] {name}")

    for name in done:
        print(f"[x] {name}")

    taskName = input("\nEnter a task: ")

    if taskName not in tasks:
        tasks[taskName] = False
    elif tasks[taskName]:
        del tasks[taskName]
    else:
        tasks[taskName] = True
