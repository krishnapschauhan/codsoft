import tkinter as tk
from tkinter import messagebox

# Functionality
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected!")

def clear_all_tasks():
    task_listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("To-Do List")

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Task List
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks)
clear_button.pack(side=tk.LEFT, padx=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
exit_button.pack(side=tk.LEFT, padx=5)

# Run Application
root.mainloop()
