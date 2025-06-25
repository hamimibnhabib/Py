import tkinter as tk
from tkinter import messagebox

# Main app window
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x500")
root.config(bg="#1e1e1e")

tasks = []

# -------- Functions ----------
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()
        index = selected[0]
        tasks.pop(index)
        update_list()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete.")

def update_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ---------- UI -------------
title = tk.Label(root, text="🗂️ My To-Do List", font=("Segoe UI", 18, "bold"), bg="#1e1e1e", fg="#ffffff")
title.pack(pady=20)

task_entry = tk.Entry(root, font=("Segoe UI", 14), width=25, bg="#2d2d2d", fg="white", border=0, insertbackground='white')
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="➕ Add Task", command=add_task,
                    bg="#4CAF50", fg="white", font=("Segoe UI", 12, "bold"),
                    activebackground="#45a049", relief="flat")
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="🗑️ Delete Task", command=delete_task,
                    bg="#f44336", fg="white", font=("Segoe UI", 12, "bold"),
                    activebackground="#e53935", relief="flat")
delete_btn.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, height=10, width=40, font=("Segoe UI", 12),
                     bg="#292929", fg="white", selectbackground="#555", yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# ---------- Run app ----------
root.mainloop()
