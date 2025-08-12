file = open("tasks.txt")
tasks = file.read().split("\n")

for task in tasks:
    print(f"{tasks.index(task) + 1}. {task}") #displays the index of the tasks and the tasks in a line.

