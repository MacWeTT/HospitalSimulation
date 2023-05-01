import tkinter as tk
from entitles.entitles import Patient

def askPatient() -> Patient:
    """
    Ask the user for their name, and then proceed further.
    """
    root = tk.Tk()
    root.title("Enter your name")
    name_label = tk.Label(root, text="Enter your name:")
    name_label.grid(row=0, column=0, pady=10,padx=10)
    
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, pady=10,padx=10)
    
    problem_label = tk.Label(root, text="Enter your problem:")
    problem_label.grid(row=1, column=0, pady=10,padx=10)
    
    problem_entry = tk.Entry(root)
    problem_entry.grid(row=1, column=1, pady=10,padx=10)
    
    wait_time_label = tk.Label(root, text="Enter your wait time:")
    wait_time_label.grid(row=2, column=0, pady=10,padx=10)
    
    wait_time_entry = tk.Entry(root)
    wait_time_entry.grid(row=2, column=1, pady=10,padx=10)
    
    patient = None
    
    def submit():
        nonlocal patient
        name = name_entry.get()
        wait_time = wait_time_entry.get()
        problem = problem_entry.get()
        patient = Patient(name=name, problem=problem, wait_time=wait_time)
        root.destroy()
    
    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=3, column=0, pady=10,padx=10)
    root.mainloop()
    
    return patient


