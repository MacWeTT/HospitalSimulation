import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import entitles.entitles as entitles
import processes.processes as processes
from utils.utils import askPatient
from dotenv import load_dotenv
import os

load_dotenv()


class HospitalSimulator:
    """
    Entry point for the hospital simulation.
    """

    def __init__(self, patient: entitles.Patient):
        self.patient = patient

        # Tkinter GUI
        self.root = tk.Tk()
        self.root.configure(bg="skyblue")
        self.department = "None"
        self.root.title("Hospital Simulator")
        self.title_label = tk.Label(
            self.root,
            text="Hospital Simulator",
            font=("Verdana bold", 40),
            bg="skyblue",
        )
        self.title_label.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

        self.question_label = tk.Label(
            self.root,
            text=f"Hi {self.patient.name}! How may I help you?",
            font=("Verdana", 15),
            bg="skyblue",
        )
        self.question_label.grid(row=1, column=1, pady=10, columnspan=2)

        # Now, we have 4 options to choose from, regarding the patient's problem.
        self.image = Image.open(os.getenv("ROOT_DIR") + r"\assets\dentistImage.png")
        self.image = self.image.resize((300, 200))
        self.dentist_image = ImageTk.PhotoImage(self.image)
        self.Labelimg = tk.Label(self.root, image=self.dentist_image).grid(
            row=2, column=0, pady=10, padx=10
        )
        self.department1 = tk.Label(self.root, text="Dentist")
        self.department1.grid(row=3, column=0, pady=10, padx=10)
        self.department1_button = tk.Button(
            self.root,
            text="Go to dentist",
            command=lambda: self.run("dentist"),
            bg="Dodgerblue",
            fg="white",
            font=("Verdana bold", 10),
        )
        self.department1_button.grid(row=3, column=0, pady=10, padx=10)

        self.image2 = Image.open(
            os.getenv("ROOT_DIR") + r"\assets\Ophthalmologists.png"
        )
        self.image2 = self.image2.resize((300, 200))
        self.ophthalmologist_image = ImageTk.PhotoImage(self.image2)
        self.Labelimg = tk.Label(self.root, image=self.ophthalmologist_image).grid(
            row=2, column=1, pady=10, padx=10
        )
        self.department2 = tk.Label(self.root, text="ophthalmologist")
        self.department2.grid(row=3, column=1, pady=10, padx=10)
        self.department2_button = tk.Button(
            self.root,
            text="Go to ophthalmologist",
            command=lambda: self.run("ophthalmologist"),
            bg="Dodgerblue",
            fg="white",
            font=("Verdana bold", 10),
        )
        self.department2_button.grid(row=3, column=1, pady=10, padx=10)

        self.image3 = Image.open(os.getenv("ROOT_DIR") + r"\assets\physician.png")
        self.image3 = self.image3.resize((300, 200))
        self.physician_image = ImageTk.PhotoImage(self.image3)
        self.Labelimg = tk.Label(self.root, image=self.physician_image).grid(
            row=2, column=2, pady=10, padx=10
        )
        self.department3 = tk.Label(self.root, text="Physician")
        self.department3.grid(row=3, column=2, pady=10, padx=10)
        self.department3_button = tk.Button(
            self.root,
            text="Go to physician",
            command=lambda: self.run("physician"),
            bg="Dodgerblue",
            fg="white",
            font=("Verdana bold", 10),
        )
        self.department3_button.grid(row=3, column=2, pady=10, padx=10)

        self.image4 = Image.open(os.getenv("ROOT_DIR") + r"\assets\ultrasound.png")
        self.image4 = self.image4.resize((300, 200))
        self.ultrasound_image = ImageTk.PhotoImage(self.image4)
        self.Labelimg = tk.Label(self.root, image=self.ultrasound_image).grid(
            row=2, column=3, pady=10, padx=10
        )
        self.department4 = tk.Label(self.root, text="Ultrasound")
        self.department4.grid(row=3, column=3, pady=10, padx=10)
        self.department4_button = tk.Button(
            self.root,
            text="Go to ultrasound",
            command=lambda: self.run("ultrasound"),
            bg="Dodgerblue",
            fg="white",
            font=("Verdana bold", 10),
        )
        self.department4_button.grid(row=3, column=3, pady=10, padx=10)

        self.exit_button = tk.Button(
            self.root,
            text="Exit The Simulation",
            command=self.root.destroy,
            bg="red",
            fg="white",
            font=("Verdana bold", 10),
        )
        self.exit_button.grid(row=4, column=1, pady=10, padx=10, columnspan=2)

    def run(self, department):
        selected_department = department
        if selected_department != "None":
            if selected_department == "dentist":
                processes.departmentDentist(patient=self.patient)
            elif selected_department == "ophthalmologist":
                processes.departmentOphthalmologist(patient=self.patient)
            elif selected_department == "ultrasound":
                processes.departmentUltrasound(patient=self.patient)
            elif selected_department == "physician":
                processes.departmentPhysician(patient=self.patient)
            else:
                print("Invalid department selected")
        else:
            message = tk.Message(self.root, text="Please select a department")
            message.grid(row=4, column=0, pady=10, padx=10)


if __name__ == "__main__":
    # Initialize the objects
    # patient = askPatient()
    patient = entitles.Patient(
        name="Manas",
        # problems={"dental": ["caries", "bleedinggums", "brokentooth"]},
        problems={
            "eyes": ["myopia", "conjunctivitis", "cataract"],
            "illness": ["hepatitis", "hypertension"],
        },
    )
    simulator = HospitalSimulator(patient=patient)

    # Run the simulation window
    simulator.root.mainloop()
