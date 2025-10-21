import tkinter as tk 
 
# Function to add a task to the list 
def add_task(): 
    task = task_entry.get() 
    if task != "": 
        task_listbox.insert(tk.END, task)  # Add task to Listbox 
        task_entry.delete(0, tk.END)  # Clear the Entry widget 
 
# Function to delete a selected task from the list 
def delete_task(): 
    try: 
        task_index = task_listbox.curselection()  # Get selected task 
        task_listbox.delete(task_index)  # Remove the selected task 
    except IndexError: 
        pass  # If no task is selected, do nothing 
 


# Create the main window 
root = tk.Tk() 
root.title("To-Do List") 
root.geometry("300x300") 
 
# Create a Label 
task_label = tk.Label(root, text="Enter a Task:") 
task_label.pack(pady=10) 
 
# Create an Entry widget to input tasks 
task_entry = tk.Entry(root, width=30) 
task_entry.pack(pady=5) 
 
# Create a Button to add a task 
add_button = tk.Button(root, text="Add Task", command=add_task) 
add_button.pack(pady=5) 
 
# Create a Listbox to display tasks 
task_listbox = tk.Listbox(root, width=30, height=10) 
task_listbox.pack(pady=5) 
 
# Create a Button to delete selected task 
delete_button = tk.Button(root, text="Delete Task", command=delete_task) 
delete_button.pack(pady=5) 
 
# Start the Tkinter event loop 
root.mainloop() 