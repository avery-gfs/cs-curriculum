import os

done = set()
undone = set()

while True:
    os.system("clear")

    numTasks = len(done) + len(undone)
    print(f"{numTasks} tasks, {len(undone)} undone")

    for name in undone:
        print(f"[ ] {name}")

    for name in done:
        print(f"[x] {name}")

    task = input("\nEnter a task: ")

    if task in done:
        done.remove(task)

    elif task in undone:
        undone.remove(task)
        done.add(task)

    else:
        undone.add(task)
