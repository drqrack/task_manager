import tkinter as tk
from tkinter import messagebox
from functools import partial
import commands

def handle_delete(id, app):
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
        commands.delete_task(id)
        show_all_tasks_frame(app)

def submit_task(title, app):
    if not title:
        messagebox.showerror(title="Add Task", message="Cannot add empty task!", parent=app)
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app) 

def handle_update(id, title, app):
    if not title:
        messagebox.showerror(title="Edit Task", message="Cannot update with empty task!", parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)

def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    label = tk.Label(master=frame, text=f"Edit task: {task["title"]}", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    # Add an entry widget and show the task title
    entry = tk.Entry(master=frame, width=30)
    entry.insert(0, task["title"])
    entry.grid(row=1, column=0, columnspan=2, pady=5)

    # Add a button with text update for saving the changes
    update_button = tk.Button(master=frame, width=12, text="Update", command=lambda: handle_update(task["_id"], entry.get(), app))
    update_button.grid(row=2, column=1, pady=10, sticky="e")
    # Add a button with text Back/Cancel for 
    cancel_button = tk.Button(master=frame, text="Cancel", command=lambda: frame.destroy())
    cancel_button.grid(row=3, column=2)

    frame.tkraise()

def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    label = tk.Label(master=frame, text="Add New Task", font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    entry = tk.Entry(master=frame)
    entry.grid()
    
    btn = tk.Button(master=frame, text="Submit", command=lambda:submit_task(entry.get(), app))
    btn.grid()
    btn_cancel = tk.Button(master=frame, text="Cancel", command=lambda: frame.destroy())
    btn_cancel.grid(row=2, column=1)

    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)

        edit_btn = tk.Button(master=frame, text="Edit", command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task), column=1)

        delete_btn = tk.Button(master=frame, text="Delete", command=partial(handle_delete, task["_id"], app))
        delete_btn.grid(row=tasks.index(task), column=2)

    add_btn = tk.Button(master=frame, text="Add Task", command=lambda: show_add_task_frame(app))
    add_btn.grid(row=len(tasks) + 1, column=0, padx=10, pady=10)

    frame.tkraise()

