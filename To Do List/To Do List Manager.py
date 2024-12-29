import json
import os

# Load tasks from file if exists
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
else:
    tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i + 1}. {task['task']} - {status}")

def mark_done():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("tasks.json", "w") as task_file:
        json.dump(tasks, task_file)
    print("Tasks saved!")

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        save_tasks()
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
