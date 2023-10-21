#!../../bin/python3
tasks = []

def add_task():
    print('Enter New Task Description')
    task_description = input()
    tasks.append(task_description)

add_task()
print(tasks)