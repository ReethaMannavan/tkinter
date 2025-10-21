import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    # basic regex for email format
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def submit_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    message = message_text.get("1.0", "end-1c").strip()

    # Validation
    if not name:
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        name_entry.focus_set()
        return
    if not email:
        messagebox.showerror("Validation Error", "Email cannot be empty.")
        email_entry.focus_set()
        return
    if not validate_email(email):
        messagebox.showerror("Validation Error", "Please enter a valid email address.")
        email_entry.focus_set()
        return
    if not message:
        messagebox.showerror("Validation Error", "Message cannot be empty.")
        message_text.focus_set()
        return

    # If we reach here, validation passed
    print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    result_label.config(text="Form Submitted Successfully!", fg="green")

    # Clear the fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    message_text.delete("1.0", tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Form")
root.geometry("450x350")
root.resizable(False, False)

# Using a Frame to improve layout
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill="both")

# Name
name_label = tk.Label(frame, text="Name:")
name_label.grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(frame, width=35)
name_entry.grid(row=0, column=1, pady=5, padx=5)

# Email
email_label = tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, sticky="e", pady=5)
email_entry = tk.Entry(frame, width=35)
email_entry.grid(row=1, column=1, pady=5, padx=5)

# Message
message_label = tk.Label(frame, text="Message:")
message_label.grid(row=2, column=0, sticky="ne", pady=5)
message_text = tk.Text(frame, width=35, height=7)
message_text.grid(row=2, column=1, pady=5, padx=5)

# Submit Button
submit_button = tk.Button(frame, text="Submit", command=submit_form, width=15)
submit_button.grid(row=3, column=1, sticky="e", pady=10)

# Result Label
result_label = tk.Label(frame, text="", font=("Arial", 10, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Optionally set focus to name entry on start
name_entry.focus_set()

root.mainloop()
