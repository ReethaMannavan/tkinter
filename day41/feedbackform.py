import tkinter as tk

def submit_feedback():
    feedback = feedback_text.get("1.0", "end-1c").strip()
    
    if feedback == "":
        result_label.config(text="Please enter your feedback.", fg="red")
    else:
        # Print to terminal
        print("Feedback submitted:")
        print(feedback)
        
        result_label.config(text=f"Feedback Received:\n{feedback}", fg="green")

def clear_feedback():
    feedback_text.delete("1.0", "end")
    result_label.config(text="")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")

instr_label = tk.Label(root, text="Please enter your feedback below:")
instr_label.pack(pady=(10,5))

feedback_text = tk.Text(root, height=8, width=40)
feedback_text.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

submit_button = tk.Button(btn_frame, text="Submit", command=submit_feedback)
submit_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(btn_frame, text="Clear", command=clear_feedback)
clear_button.grid(row=0, column=1, padx=5)

result_label = tk.Label(root, text="", justify="left", wraplength=380)
result_label.pack(pady=10)

root.mainloop()
