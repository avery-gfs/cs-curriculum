class Task:
    def __init__(self, name):
        # Keep track of task name and status (done or not done). Tasks should
        # start out not done
        self.name = name
        self.isDone = False

    def __repr__(self):
        # Display the name and status of task
        if self.isDone:
            return f"[x] {self.name}"

        return f"[ ] {self.name}"


class TodoList:
    def __init__(self):
        # Keep track of a tasks list, which starts out empty
        self.tasks = []

    def add(self, name):
        # Add a new task with a given name
        self.tasks.append(Task(name))

    def finish(self, name):
        # Update the status of the task that matches `name` to be done
        for task in self.tasks:
            if task.name == name:
                task.isDone = True

    def remove(self, name):
        # Filter out the task that matches `name`
        newTasks = []

        for task in self.tasks:
            if task.name != name:
                newTasks.append(task)

        self.tasks = newTasks

    def __repr__(self):
        # Return a representation of the to do list that shows each task (name
        # and status), the total number of tasks, and the number of undone
        # tasks.

        numTasks = len(self.tasks)
        numUnDone = 0
        taskRows = ""

        for task in self.tasks:
            taskRows += f"\n{task}"

            # Count number of undone tasks
            if task.isDone:
                numUnDone += 1

        return f"{numTasks} tasks, {numUnDone} undone{taskRows}"


print("Test tasks:\n")

hw = Task("do homework")

print(hw.name)  # "do homework"
print(hw.isDone)  # False

hw.isDone = True
print(hw)  # [x] do homework

print("\nTest to do list:\n")

todo = TodoList()

todo.add("do homework")
todo.add("feed dog")
todo.add("water plants")
todo.finish("feed dog")
todo.remove("do homework")

print(todo)

# Prints
#
# 2 tasks, 1 undone
# [x] feed dog
# [ ] water plants
