import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import os

TASKS_FILE = "tasks.txt"

CATEGORIES = ["School", "Work", "Personal", "Other"]

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file,)

def add_task():
    task_text = task_entry.get()
    due_date = due_date_entry.get()
    category = category_var.get()
    if task_text:
        tasks.append({"task": task_text, "completed": False, "due": due_date, "category": category})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task description.")

def update_task_list(filtered=None):
    task_listbox.delete(0, tk.END)
    display_tasks = filtered if filtered is not None else tasks
    for task in display_tasks:
        status = "Complete" if task["completed"] else "Incomplete"
        task_str = f"{task['task']} [{status}] - Due: {task['due']} - Category: {task['category']}"
        task_listbox.insert(tk.END, task_str)

def complete_task():
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        tasks[index] ["completed"] = True
        save_tasks(tasks)
        update_task_list()

def delete_task():
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        del tasks[index]
        save_tasks(tasks)
        update_task_list()

def filter_tasks_category(category):
    filtered = []
    for task in tasks:
        if task["category"] == category and not task["completed"]:
            filtered.append(task)
    return filtered

def sort_category():
    selected_category = category_var.get()
    if selected_category in CATEGORIES:
        filtered_tasks = filter_tasks_category(selected_category)
        update_task_list(filtered_tasks)
    else:
        messagebox.showwarning("Category Error", "Please select a valid category.")

root = tk.Tk()
root.title("Daily Planner")
root.resizable(True, True)

task_entry = tk.Entry(root, width=40)
task_entry.insert(0, "Enter New Task")
task_entry.pack(pady=5)

due_date_entry = tk.Entry(root, width=40)
due_date_entry.pack(pady=5)
due_date_entry.insert(0, "(MM-DD-YYYY)")

category_var = tk.StringVar()
category_dropdown = ttk.Combobox(root, textvariable=category_var)
category_dropdown['values'] = ("School", "Work", "Personal", "Other")
category_dropdown.set("Select Category")
category_dropdown.pack(pady=5)

reset_button = tk.Button(root, text="Show All Tasks", command=update_task_list)
reset_button.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

sort_button = tk.Button(root, text="Sort by Category", command=sort_category)
sort_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=70, height=15)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark As Completed", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

tasks = load_tasks()
update_task_list() 

root.mainloop()