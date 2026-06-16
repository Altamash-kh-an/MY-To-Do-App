import tkinter as tk
import sqlite3

# Database Connection
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Window
root = tk.Tk()
root.title("Todo App")
root.geometry("700x500")

# Task Entry
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

# Search Entry
search_entry = tk.Entry(root, width=40)
search_entry.pack(pady=5)

# Task List
task_list = tk.Listbox(root, width=80, height=15)
task_list.pack(pady=10)


# =====================
# View Tasks
# =====================

def load_tasks():

    task_list.delete(0, tk.END)

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    for row in rows:
        task_list.insert(
            tk.END,
            f"{row[0]}. {row[1]} - {row[2]}"
        )


# =====================
# Add Task
# =====================

def add_task():

    task = task_entry.get().strip()

    if task == "":
        return

    cursor.execute(
        "INSERT INTO tasks (task, status) VALUES (?, ?)",
        (task, "Pending")
    )

    conn.commit()

    task_entry.delete(0, tk.END)

    load_tasks()


# =====================
# Delete Task
# =====================

def delete_task():

    selected = task_list.curselection()

    if not selected:
        return

    item = task_list.get(selected[0])

    task_id = int(item.split(".")[0])

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    load_tasks()


# =====================
# Edit Task
# =====================

def edit_task():

    selected = task_list.curselection()

    if not selected:
        return

    new_task = task_entry.get().strip()

    if new_task == "":
        return

    item = task_list.get(selected[0])

    task_id = int(item.split(".")[0])

    cursor.execute(
        "UPDATE tasks SET task = ? WHERE id = ?",
        (new_task, task_id)
    )

    conn.commit()

    task_entry.delete(0, tk.END)

    load_tasks()


# =====================
# Search Task
# =====================

def search_task():

    search = search_entry.get().strip()

    task_list.delete(0, tk.END)

    cursor.execute(
        "SELECT * FROM tasks WHERE task LIKE ?",
        (f"%{search}%",)
    )

    rows = cursor.fetchall()

    for row in rows:
        task_list.insert(
            tk.END,
            f"{row[0]}. {row[1]} - {row[2]}"
        )


# =====================
# Mark Done
# =====================

def mark_done():

    selected = task_list.curselection()

    if not selected:
        return

    item = task_list.get(selected[0])

    task_id = int(item.split(".")[0])

    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        ("Done", task_id)
    )

    conn.commit()

    load_tasks()


# =====================
# Exit
# =====================

def exit_app():

    conn.close()

    root.destroy()


# =====================
# Buttons
# =====================

tk.Button(
    root,
    text="Add Task",
    command=add_task
).pack(pady=3)

tk.Button(
    root,
    text="View Tasks",
    command=load_tasks
).pack(pady=3)

tk.Button(
    root,
    text="Delete Task",
    command=delete_task
).pack(pady=3)

tk.Button(
    root,
    text="Edit Task",
    command=edit_task
).pack(pady=3)

tk.Button(
    root,
    text="Search Task",
    command=search_task
).pack(pady=3)

tk.Button(
    root,
    text="Mark Done",
    command=mark_done
).pack(pady=3)

tk.Button(
    root,
    text="Exit",
    command=exit_app
).pack(pady=3)



# Load Existing Tasks
load_tasks()

# Start GUI
root.mainloop()



