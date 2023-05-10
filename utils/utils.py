import tkinter as tk
from entitles.entitles import Patient


def askPatient() -> Patient:
    """
    Ask the user for their name, and then proceed further.
    """
    root = tk.Tk()
    root.title("Enter your name")
    name_label = tk.Label(root, text="Enter your name:")
    name_label.grid(row=0, column=0, pady=10, padx=10)

    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, pady=10, padx=10)

    dental_problem_label = tk.Label(root, text="Enter your dental problems:")
    dental_problem_label.grid(row=1, column=0, pady=10, padx=10)

    dental_problem_entry = tk.Entry(root)
    dental_problem_entry.grid(row=1, column=1, pady=10, padx=10)

    dental_available_entry = tk.Label(
        root, text="Available diagnosis: Dental caries, Broken tooth, Bleeding gums."
    )
    dental_available_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    eye_problem_label = tk.Label(root, text="Enter your eye problems:")
    eye_problem_label.grid(row=3, column=0, padx=10, pady=10)

    eye_problem_entry = tk.Entry(root)
    eye_problem_entry.grid(row=3, column=1, padx=10, pady=10)

    eye_available_entry = tk.Label(
        root,
        text="Available diagnosis: myopia, conjunctivitis, cataract.",
    )
    eye_available_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    physical_problem_label = tk.Label(root, text="Enter your physical problems:")
    physical_problem_label.grid(row=5, column=0, padx=10, pady=10)

    physical_problem_entry = tk.Entry(root)
    physical_problem_entry.grid(row=5, column=1, padx=10, pady=10)

    physical_available_entry = tk.Label(
        root,
        text="Available diagnosis: hepatitis, hypertension, asthma.",
    )
    physical_available_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    patient = None

    def submit():
        nonlocal patient
        name = name_entry.get()
        dental_problem = dental_problem_entry.get().split(",")
        eye_problem = eye_problem_entry.get().split(",")
        problems = {"dental": dental_problem, "eyes": eye_problem}
        patient = Patient(name=name, problems=problems)
        root.destroy()

    submit_button = tk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=7, column=0, pady=10, padx=10, columnspan=2)

    note_label = tk.Label(root, text="Enter your issues seperated by commas.")
    note_label.grid(row=8, column=0, columnspan=2)

    root.mainloop()

    return patient
