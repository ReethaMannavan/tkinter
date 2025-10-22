import tkinter as tk
from tkinter import messagebox
import re  # for email validation

def validate_fields(*args):
    """Validate fields and control submit button + error messages."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    valid = True

    # --- Validate Name ---
    if not name:
        name_error.config(text="Name is required", fg="red")
        valid = False
    elif not name.replace(" ", "").isalpha():
        name_error.config(text="Name must contain only letters", fg="red")
        valid = False
    else:
        name_error.config(text="")  # clear error

    # --- Validate Email ---
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not email:
        email_error.config(text="Email is required", fg="red")
        valid = False
    elif not re.match(email_pattern, email):
        email_error.config(text="Invalid email format", fg="red")
        valid = False
    else:
        email_error.config(text="")

    # --- Enable or disable Submit ---
    if valid:
        submit_button.config(state=tk.NORMAL)
    else:
        submit_button.config(state=tk.DISABLED)


def submit_form():
    """Handle successful form submission."""
    name = name_entry.get().strip()
    email = email_entry.get().strip()

    messagebox.showinfo("Success", f"Form submitted!\n\nName: {name}\nEmail: {email}")
    print(f"Form Submitted:\nName: {name}\nEmail: {email}")

    # Reset form
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    name_error.config(text="")
    email_error.config(text="")
    submit_button.config(state=tk.DISABLED)


# --- Main Window ---
root = tk.Tk()
root.title("Dynamic Form with Validation")
root.geometry("420x300")
root.resizable(False, False)

# --- Name Field ---
tk.Label(root, text="Name:", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=(20, 5), sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=(20, 5))
name_error = tk.Label(root, text="", fg="red", font=("Arial", 9))
name_error.grid(row=1, column=1, sticky="w")

# --- Email Field ---
tk.Label(root, text="Email:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=(10, 5), sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, pady=(10, 5))
email_error = tk.Label(root, text="", fg="red", font=("Arial", 9))
email_error.grid(row=3, column=1, sticky="w")

# --- Submit Button ---
submit_button = tk.Button(root, text="Submit", state=tk.DISABLED, command=submit_form,
                          bg="#4CAF50", fg="white", width=15)
submit_button.grid(row=4, column=1, pady=25)

# --- Info Label ---
status_label = tk.Label(root, text="Fill all fields correctly to enable Submit", fg="gray")
status_label.grid(row=5, column=0, columnspan=2, pady=(5, 0))

# --- Bind Validation to Key Release ---
name_entry.bind("<KeyRelease>", validate_fields)
email_entry.bind("<KeyRelease>", validate_fields)

# --- Run the App ---
root.mainloop()
