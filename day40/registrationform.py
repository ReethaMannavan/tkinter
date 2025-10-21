import tkinter as tk
from tkinter import messagebox
import re
import os

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    # Validation
    if not name:
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        name_entry.focus_set()
        return
    if not email:
        messagebox.showerror("Validation Error", "Email cannot be empty.")
        email_entry.focus_set()
        return
    if not is_valid_email(email):
        messagebox.showerror("Validation Error", "Please enter a valid email address.")
        email_entry.focus_set()
        return
    if not password:
        messagebox.showerror("Validation Error", "Password cannot be empty.")
        password_entry.focus_set()
        return

    # If all valid — print to terminal
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")  # be cautious showing password in real apps

    messagebox.showinfo("Success", "Registration completed successfully!")

    # Clear fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x250")

# Set icon (if you have .ico file)
if os.path.exists("myicon.ico"):
    root.iconbitmap("myicon.ico")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill='both', expand=True)

# Name
tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='e', pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Email
tk.Label(frame, text="Email:").grid(row=1, column=0, sticky='e', pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

# Password
tk.Label(frame, text="Password:").grid(row=2, column=0, sticky='e', pady=5)
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.grid(row=2, column=1, pady=5)

# Submit button (using pack())
submit_button = tk.Button(root, text="Submit", command=submit_form, width=15)
submit_button.pack(pady=15)

name_entry.focus_set()

root.mainloop()
