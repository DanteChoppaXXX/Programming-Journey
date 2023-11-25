#!./env/bin/python3
"""Build a simple To Do list program that allows user to add task, view task, mark task as done and also delete tasks"""
# Display the program name
app_name = "Super To-Do App"
print(app_name)
print("="*len(app_name))
# Display the menu to the user with options to add task, view task, mark task as done and also delete tasks.
menu = "1. Add a task\n2. View tasks\n3. Mark task as done\n4. Delete task\n5. Exit"
print(menu)
print("(Select Option 1 - 5)\n")
# CREATE A LIST TO STORE TASKS
tasks = []

# Create a function to add tasks to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully.")
    return tasks

# Create a function to view tasks in the list
def view_tasks():
    print("Tasks")
    print("="*5)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Create a function to mark task as done in the list
def mark_task_done(task_number):
    if task_number > len(tasks):
        print("Invalid task number. Please enter a valid task number.")
    else:
        task = tasks[task_number-1]
        tasks.remove(task)
        print(f"Task '{task}' marked as done.")
        return tasks
    
# Create a function to delete tasks from the list
def delete_task(task_number):
    if task_number > len(tasks):
        print("Invalid task number. Please enter a valid task number.")
    else:
        task = tasks[task_number-1]
        tasks.remove(task)
        print(f"Task '{task}' deleted.")
        return tasks

keep_going = True
while keep_going:
    # Ask the user to enter the option
    option = input("\nEnter option: ")
    # Check if the user entered a valid option
    if option not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please enter a valid option.")
    else:
        if option == "1":
            # Ask the user to enter the task
            task = input("Enter task: ")
            # Call the add_task function to add the task to the list
            add_task(task)
        elif option == "2":
            # Call the view_tasks function to view the tasks in the list
            view_tasks()
        elif option == "3":
            # Ask the user to enter the task number
            task_number = int(input("Enter task number: "))
            # Call the mark_task_done function to mark the task as done in the list
            mark_task_done(task_number)
        elif option == "4":
            # Ask the user to enter the task number
            task_number = int(input("Enter task number: "))
            # Call the delete_task function to delete the task from the list
            delete_task(task_number)
            while keep_going:
                # Ask the user if they want to delete another task
                delete_another = input("Delete another task (y/n)? ")
                if delete_another.lower() == "y":
                    # Ask the user to enter the task number
                    task_number = int(input("Enter task number: "))
                    # Call the delete_task function to delete the task from the list
                    delete_task(task_number)
                else:
                    keep_going = False
        elif option == "5":
            # Exit the program
            print("Exiting program.")
            keep_going = False
            break
