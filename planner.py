import json
import os

FILE_PATH = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file)

tasks = load_tasks()

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks()
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, t in enumerate(tasks):
            status = "✅" if t["completed"] else "❌"
            print(f"{i+1}. {t['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            print("Task marked as completed.")
        else: 
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number for deletion: "))
        if 0 <= task_num < len(tasks): 
            removed = tasks.pop(task_num)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("|n--- Daily Planner ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose a valid option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the application, Goodbye!")
            break
        else:
            print("Invalid option.")

main()