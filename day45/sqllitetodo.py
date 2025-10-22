import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
import os
import traceback

DB_PATH = "todo.db"

# ------------------ Database Setup ------------------
def init_db():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                status TEXT DEFAULT 'Pending'
            )''')
        conn.commit()
    finally:
        conn.close()

def fetch_tasks():
    conn = sqlite3.connect(DB_PATH)
    try:
        c = conn.cursor()
        c.execute("SELECT id, task FROM tasks ORDER BY id ASC")
        return c.fetchall()
    finally:
        conn.close()

def add_task_to_db(task):
    conn = sqlite3.connect(DB_PATH)
    try:
        c = conn.cursor()
        c.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
    finally:
        conn.close()

def update_task_in_db(task_id, new_task):
    conn = sqlite3.connect(DB_PATH)
    try:
        c = conn.cursor()
        c.execute("UPDATE tasks SET task=? WHERE id=?", (new_task, task_id))
        conn.commit()
        return c.rowcount  # number of rows updated
    finally:
        conn.close()

def delete_task_from_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    try:
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        return c.rowcount
    finally:
        conn.close()

# ------------------ UI Functions ------------------
tasks_data = []  # list of (id, task)

def refresh_task_list():
    global tasks_data
    try:
        tasks_data = fetch_tasks()
        listbox.delete(0, tk.END)
        for t in tasks_data:
            listbox.insert(tk.END, f"{t[0]}. {t[1]}")
        print("REFRESHED tasks_data (index: id, task):")
        for i, t in enumerate(tasks_data):
            print(f"  [{i}] {t}")
    except Exception:
        print("Error during refresh_task_list:\n" + traceback.format_exc())

def get_selected_index():
    sel = listbox.curselection()
    if not sel:
        print("get_selected_index: no selection")
        return None
    idx = sel[0]
    print(f"get_selected_index -> {idx}")
    return idx

def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    try:
        add_task_to_db(task)
        print(f"Added Task: {task}")
        task_entry.delete(0, tk.END)
        refresh_task_list()
    except Exception:
        print("Error in add_task:\n" + traceback.format_exc())
        messagebox.showerror("Error", "Failed to add task. See terminal for details.")

def update_task():
    try:
        idx = get_selected_index()
        if idx is None:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return

        if idx >= len(tasks_data):
            messagebox.showerror("Error", "Selection index out of range.")
            print(f"Index {idx} >= len(tasks_data) {len(tasks_data)}")
            return

        task_id, old_text = tasks_data[idx]
        new_task = task_entry.get().strip()
        if not new_task:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
            return

        print(f"Attempting to update ID {task_id}: '{old_text}' -> '{new_task}'")
        rows = update_task_in_db(task_id, new_task)
        if rows == 0:
            messagebox.showwarning("Update", "No rows updated (maybe task was removed).")
            print("update_task_in_db returned 0 rows")
        else:
            print(f"Updated Task ID {task_id} → {new_task}")

        refresh_task_list()

        # re-select the updated item (if still present)
        for new_idx, t in enumerate(tasks_data):
            if t[0] == task_id:
                listbox.selection_clear(0, tk.END)
                listbox.selection_set(new_idx)
                listbox.see(new_idx)
                break

        task_entry.delete(0, tk.END)

    except Exception:
        print("Error in update_task:\n" + traceback.format_exc())
        messagebox.showerror("Error", "Failed to update task. See terminal for details.")

def delete_task():
    try:
        idx = get_selected_index()
        if idx is None:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        if idx >= len(tasks_data):
            messagebox.showerror("Error", "Selection index out of range.")
            return

        task_id, task_text = tasks_data[idx]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete task:\n\n{task_text}")
        if not confirm:
            return

        rows = delete_task_from_db(task_id)
        if rows == 0:
            messagebox.showwarning("Delete", "No rows deleted (maybe already removed).")
            print("delete_task_from_db returned 0 rows")
        else:
            print(f"Deleted Task ID {task_id}: {task_text}")

        refresh_task_list()
        task_entry.delete(0, tk.END)

    except Exception:
        print("Error in delete_task:\n" + traceback.format_exc())
        messagebox.showerror("Error", "Failed to delete task. See terminal for details.")

def export_tasks():
    try:
        tasks = fetch_tasks()
        if not tasks:
            messagebox.showinfo("No Data", "There are no tasks to export.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Task List As"
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                for task in tasks:
                    file.write(f"{task[0]}. {task[1]}\n")
            messagebox.showinfo("Export Successful", f"Tasks exported to:\n{os.path.basename(file_path)}")
            print(f"Tasks exported to {file_path}")
    except Exception:
        print("Error in export_tasks:\n" + traceback.format_exc())
        messagebox.showerror("Error", "Failed to export tasks. See terminal for details.")

def on_task_select(event):
    try:
        idx = get_selected_index()
        if idx is None:
            return
        if idx < len(tasks_data):
            _id, text = tasks_data[idx]
            task_entry.delete(0, tk.END)
            task_entry.insert(0, text)
            print(f"on_task_select: idx={idx}, id={_id}, text='{text}'")
    except Exception:
        print("Error in on_task_select:\n" + traceback.format_exc())

# ------------------ Main Window ------------------
init_db()

root = tk.Tk()
root.title("SQLite Todo App - debug")
root.geometry("640x480")

# Header
tk.Label(root, text="📝 SQLite To-Do Application (debug mode)", font=("Arial", 14, "bold")).pack(pady=10)

# Entry Field
entry_frame = tk.Frame(root)
entry_frame.pack(pady=5)
tk.Label(entry_frame, text="Enter Task:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
task_entry = tk.Entry(entry_frame, width=50)
task_entry.pack(side=tk.LEFT, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Add", width=12, command=add_task).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="Update", width=12, command=update_task).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="Delete", width=12, command=delete_task).grid(row=0, column=2, padx=6)
tk.Button(btn_frame, text="Export", width=12, command=export_tasks).grid(row=0, column=3, padx=6)

# Listbox + Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(list_frame, orient="vertical")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(list_frame, width=90, height=15, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)
listbox.bind("<<ListboxSelect>>", on_task_select)

# initial load
refresh_task_list()

root.mainloop()
