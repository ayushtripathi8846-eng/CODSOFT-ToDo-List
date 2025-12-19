import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("420x450")
root.resizable(False, False)

tasks = []

def add_task():
    task = task_entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    tasks.append({"task": task, "status": "Pending"})
    task_entry.delete(0, tk.END)
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, f"{task['task']}  [{task['status']}]")

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks[index]["status"] = "Completed"
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task")

tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

task_entry = tk.Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

tk.Button(root, text="Add Task", width=25, command=add_task).pack(pady=5)
tk.Button(root, text="Mark as Completed", width=25, command=complete_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=25, command=delete_task).pack(pady=5)

listbox = tk.Listbox(root, width=50, height=12)
listbox.pack(pady=15)

root.mainloop()
