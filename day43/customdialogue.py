import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

def new_file():
    # ask user if they want to save before creating new
    if messagebox.askyesno("Confirm", "Discard current content and create new file?"):
        text_area.delete("1.0", tk.END)
        root.title("Untitled - Application")

def open_file():
    # ask for filename via simpledialog
    fname = simpledialog.askstring("Open File", "Enter filename to open:")
    if fname:
        # in a real app you'd open the file. Here just simulate.
        messagebox.showinfo("Opening", f"Would open file: {fname}")
        print(f"Opened file: {fname}")
        root.title(f"{fname} - Application")

def save_file():
    # ask for filename via simpledialog
    fname = simpledialog.askstring("Save File", "Enter filename to save as:")
    if fname:
        # simulate save
        messagebox.showinfo("Saving", f"Would save to file: {fname}")
        print(f"Saved file: {fname}")
        root.title(f"{fname} - Application")

def exit_app():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# Main window
root = tk.Tk()
root.title("Untitled - Application")
root.geometry("600x400")

# Menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Toolbar
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
btn_new = tk.Button(toolbar, text="New", command=new_file)
btn_new.pack(side=tk.LEFT, padx=2, pady=2)
btn_open = tk.Button(toolbar, text="Open", command=open_file)
btn_open.pack(side=tk.LEFT, padx=2, pady=2)
btn_save = tk.Button(toolbar, text="Save", command=save_file)
btn_save.pack(side=tk.LEFT, padx=2, pady=2)
toolbar.pack(side=tk.TOP, fill=tk.X)

# Text area (just for demonstration)
text_area = tk.Text(root, wrap=tk.WORD)
text_area.pack(expand=True, fill=tk.BOTH)

root.mainloop()
