import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    selected_task_index = listbox.curselection()
    updated_task = entry_update.get()

    if selected_task_index and updated_task:
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, updated_task)
        entry_update.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task and enter an update.")

def clear_tasks():
    listbox.delete(0, tk.END)

def on_task_select(event):
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = listbox.get(selected_task_index)
        entry_update.delete(0, tk.END)
        entry_update.insert(tk.END, selected_task)

root = tk.Tk()
root.title("To-Do List")
root.geometry("570x550")
root.config(background="black")


title_label = tk.Label(root, text="To-Do List", font=("Ubuntu", 20), fg="white", bg="black")
title_label.grid(row=0, column=0, columnspan=2, pady=10)


entry = tk.Entry(root, width=50, font=("Ubuntu", 15))
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

add_button = tk.Button(root,
                       text="Add Task",
                       command=add_task,
                       font=("Ubuntu", 15),
                       bg="#3c3c45",
                       fg="White",
                       activebackground="#3c3c45",
                       activeforeground="White")
add_button.grid(row=2, column=0, padx=10, pady=10)

update_button = tk.Button(root,
                          text="Update Task",
                          command=update_task,
                          font=("Ubuntu", 15),
                          bg="#3c3c45",
                          fg="White",
                          activebackground="#3c3c45",
                          activeforeground="White")
update_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = tk.Button(root,
                          text="Delete Task",
                          command=delete_task,
                          font=("Ubuntu", 15),
                          bg="#3c3c45",
                          fg="White",
                          activebackground="#3c3c45",
                          activeforeground="White")
delete_button.grid(row=3, column=0, padx=10, pady=10)

clear_button = tk.Button(root,
                         text="Clear All",
                         command=clear_tasks,
                         font=("Ubuntu", 15),
                         bg="#3c3c45",
                         fg="White",
                         activebackground="#3c3c45",
                         activeforeground="White")
clear_button.grid(row=3, column=1, padx=10, pady=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=("Ubuntu", 15))
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
listbox.bind("<ButtonRelease-1>", on_task_select)

entry_update = tk.Entry(root, width=50, font=("Ubuntu", 15))
entry_update.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
