file = open("tasks.txt")
tasks = file.read().split("\n")

for task in tasks:
    print(task)