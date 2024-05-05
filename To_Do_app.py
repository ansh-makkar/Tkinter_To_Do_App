import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

def mark_task():
    try:
        index = listbox.curselection()[0]
        listbox.itemconfig(index, {'bg': 'light green', 'fg': 'black'})
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark as Completed", font=("Helvetica", 12), command=mark_task)
mark_button.pack(pady=5)

listbox = tk.Listbox(root, height=15, width=40, font=("Helvetica", 12))
listbox.pack(padx=10, pady=5)

root.mainloop()


# TO Run this TO_DO_APP in terminal Press "python To_Do_app.py"