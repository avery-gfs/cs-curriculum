import os
import json

with open("tasks.json") as file:
    data = json.load(file)

    # Make `undone` and `done` sets from JSON data

    # undone = ??  Your code goes here
    # done = ??  Your code goes here

# Loop forever
while True:
    # Your to-do code from part 01 here

    # Make dictionary with `undone` and `done` fields (lists of task names)
    # for conversion to JSON

    data = {
        # Your code goes here
    }

    with open("tasks.json", "w") as file:
        json.dump(data, file)
