import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    
    # Validate Name
    if not name:
        messagebox.showwarning("Input Error", "Name cannot be empty.")
        name_entry.focus_set()
        return
    if not name.isalpha():
        messagebox.showwarning("Input Error", "Name must contain letters only.")
        name_entry.focus_set()
        return
    
    # Validate Phone
    if not phone:
        messagebox.showwarning("Input Error", "Phone number cannot be empty.")
        phone_entry.focus_set()
        return
    if not phone.isdigit():
        messagebox.showwarning("Input Error", "Phone number must contain digits only.")
        phone_entry.focus_set()
        return
    if len(phone) != 10:
        messagebox.showwarning("Input Error", "Phone number must be exactly 10 digits.")
        phone_entry.focus_set()
        return
    
    # Validate Email
    if not email:
        messagebox.showwarning("Input Error", "Email cannot be empty.")
        email_entry.focus_set()
        return
    if not is_valid_email(email):
        messagebox.showwarning("Input Error", "Please enter a valid email address.")
        email_entry.focus_set()
        return
    
    # All validations passed
    contact = f"{name} | {phone} | {email}"
    contact_listbox.insert(tk.END, contact)
    print(f"Added contact: {contact}")  # terminal output
    
    # Clear the entry fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def remove_contact():
    selected_indices = contact_listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Selection Error", "No contact selected.")
        return
    for index in reversed(selected_indices):
        removed = contact_listbox.get(index)
        contact_listbox.delete(index)
        print(f"Removed contact: {removed}")  # terminal output

# Main window
root = tk.Tk()
root.title("Contact Book with Validation")
root.geometry("500x400")

# Frame for inputs
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.grid(row=0, column=0, sticky="ew")

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, pady=5, padx=5)

tk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky="e", pady=5)
phone_entry = tk.Entry(input_frame, width=30)
phone_entry.grid(row=1, column=1, pady=5, padx=5)

tk.Label(input_frame, text="Email:").grid(row=2, column=0, sticky="e", pady=5)
email_entry = tk.Entry(input_frame, width=30)
email_entry.grid(row=2, column=1, pady=5, padx=5)

# Buttons Frame
buttons_frame = tk.Frame(root, padx=10, pady=5)
buttons_frame.grid(row=1, column=0, sticky="ew")

add_button = tk.Button(buttons_frame, text="Add Contact", command=add_contact, width=15)
add_button.pack(side="left", padx=5)
remove_button = tk.Button(buttons_frame, text="Remove Contact", command=remove_contact, width=15)
remove_button.pack(side="left", padx=5)

# Listbox + Scrollbar
list_frame = tk.Frame(root, padx=10, pady=10)
list_frame.grid(row=2, column=0, sticky="nsew")

contact_listbox = tk.Listbox(list_frame, width=50, height=10, selectmode=tk.EXTENDED)
contact_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=contact_listbox.yview)
scrollbar.pack(side="right", fill="y")

contact_listbox.configure(yscrollcommand=scrollbar.set)

# Make window resizable in list area
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

# Set focus
name_entry.focus_set()

root.mainloop()
