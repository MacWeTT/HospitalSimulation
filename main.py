import tkinter as tk
import entitles.entitles as entitles
import processes.processes as processes

# from utils.utils import askPatient


class HospitalSimulator:
    """
    Entry point for the hospital simulation.
    """

    def __init__(self, patient: entitles.Patient):
        self.patient = patient

        # Tkinter GUI
        self.root = tk.Tk()
        self.department = "None"
        self.root.title("Hospital Simulator")
        # self.root.geometry("1920x1080")

        self.title_label = tk.Label(self.root, text="Hospital Simulator")
        self.title_label.grid(row=0, column=1, pady=10, padx=10, columnspan=2)

        self.question_label = tk.Label(
            self.root, text=f"Hi {self.patient.name}! How may I help you?"
        )
        self.question_label.grid(row=1, column=0, pady=10, columnspan=2)

        # Now, we have 4 options to choose from, regarding the patient's problem.
        self.department1 = tk.Label(self.root, text="Dentist")
        self.department1.grid(row=2, column=0, pady=10, padx=10)
        self.department1_button = tk.Button(
            self.root, text="Go to dentist", command=lambda: self.run("dentist")
        )
        self.department1_button.grid(row=3, column=0, pady=10, padx=10)

        self.department2 = tk.Label(self.root, text="Emergency")
        self.department2.grid(row=2, column=1, pady=10, padx=10)
        self.department2_button = tk.Button(
            self.root, text="Go to emergency", command=lambda: self.run("emergency")
        )
        self.department2_button.grid(row=3, column=1, pady=10, padx=10)

        self.department3 = tk.Label(self.root, text="Physician")
        self.department3.grid(row=2, column=2, pady=10, padx=10)
        self.department3_button = tk.Button(
            self.root, text="Go to physician", command=lambda: self.run("physician")
        )
        self.department3_button.grid(row=3, column=2, pady=10, padx=10)

        self.department4 = tk.Label(self.root, text="Ultrasound")
        self.department4.grid(row=2, column=3, pady=10, padx=10)
        self.department4_button = tk.Button(
            self.root, text="Go to ultrasound", command=lambda: self.run("ultrasound")
        )
        self.department4_button.grid(row=3, column=3, pady=10, padx=10)

        self.exit_button = tk.Button(
            self.root, text="Exit The Simulation", command=self.root.destroy
        )
        self.exit_button.grid(row=4, column=1, pady=10, padx=10, columnspan=2)

    def run(self, department):
        selected_department = department
        if selected_department != "None":
            if selected_department == "dentist":
                dentistNurse = entitles.Nurse(
                    name="Dentist's Nurse", patient=self.patient
                )
                processes.departmentDentist(patient=self.patient, nurse=dentistNurse)
            elif selected_department == "emergency":
                surgeonNurse = entitles.Nurse(name="ICU's Nurse", patient=self.patient)
                processes.departmentSurgeon(self.patient, surgeonNurse)
            elif selected_department == "ultrasound":
                radiologyTech = entitles.Nurse(
                    name="Radiology Technician", patient=self.patient
                )
                processes.departmentUltrasound(self.patient, radiologyTech)
            elif selected_department == "physician":
                Nurse = entitles.Nurse(
                    name="Nurse", patient=self.patient
                )
                processes.departmentPhysician(self.patient, Nurse)
            else:
                print("Invalid department selected")
        else:
            message = tk.Message(self.root, text="Please select a department")
            message.grid(row=4, column=0, pady=10, padx=10)


if __name__ == "__main__":
    # Initialize the objects
    patient = entitles.Patient(
        name="Manas",
        problems={"dental": ["caries", "bleedinggums", "brokentooth"]},
    )
    simulator = HospitalSimulator(patient=patient)

    # Run the simulation window
    simulator.root.mainloop()
