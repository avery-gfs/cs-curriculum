import os

done = set()
undone = set()

# Loop forever
while True:
    os.system("clear")  # Clear the screen

    numTasks = len(done) + len(undone)
    print(f"{numTasks} tasks, {len(undone)} undone\n")

    for name in undone:
        print(f"[ ] {name}")

    for name in done:
        print(f"[x] {name}")

    task = input("\nEnter a task: ")  # Get a task name as input

    if task in done:
        done.remove(task)

    elif task in undone:
        undone.remove(task)
        done.add(task)

    else:
        undone.add(task)
