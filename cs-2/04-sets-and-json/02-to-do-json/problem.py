import os
import json

with open("tasks.json") as file:
    data = json.load(file)

    # Make `undone` and `done` sets from JSON data

    # undone = ??  Your code goes here
    # done = ??  Your code goes here

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

    # Make dictionary with `undone` and `done` fields (lists of task names)
    # for conversion to JSON

    data = {
        # Your code goes here
    }

    with open("tasks.json", "w") as file:
        json.dump(data, file)
