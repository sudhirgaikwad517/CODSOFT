#Name Sudhir Gaikwad
#CodSoft Internship 
# Task 1

import json
import tkinter as tk
from tkinter import messagebox
import os

def load_tasks():
    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def update_task_status(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks(tasks)
    update_listbox()

def delete_task(index):
    del tasks[index]
    save_tasks(tasks)
    update_listbox()

def add_task():
    description = entry_task.get()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    update_listbox()
    entry_task.delete(0, tk.END)

def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = "[ ]" if not task["completed"] else "[X]"
        listbox.insert(tk.END, f"{i}. {status} {task['description']}")

def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        update_task_status(selected_index)

def on_delete():
    selected_index = listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        delete_task(selected_index)

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry_task = tk.Entry(root, width=30)
entry_task.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=on_delete)
delete_button.pack(pady=5)

listbox.bind("<<ListboxSelect>>", on_select)

update_listbox()

root.mainloop()
