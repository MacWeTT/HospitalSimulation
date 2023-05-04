import simpy
import tkinter as tk
import entitles.entitles as entitles
import processes.processes as processes
from utils.utils import askPatient

class HospitalSimulator:
    '''
    Entry point for the hospital simulation.
    '''
    def __init__(self, env: simpy.RealtimeEnvironment, patient: entitles.Patient):
        
        self.env = env
        self.patient = patient
        
        #Tkinter GUI
        self.root = tk.Tk()
        self.department = tk.StringVar()
        self.department.initialize("dentist")
        self.action = env.process(self.run())
        self.root.title("Hospital Simulator")
        # self.root.geometry("1920x1080") 
        
        self.title_label = tk.Label(self.root, text="Hospital Simulator")
        self.title_label.grid(row=0, column=0, pady=10,padx=10)
        
        self.question_label = tk.Label(self.root, text=f"Hi {self.patient.name}! How may I help you?")
        self.question_label.grid(row=1, column=0, pady=10,padx=10)
        
        #Now, we have 5 options to choose from, regarding the patient's problem.
        self.department1 = tk.Label(self.root, text="Dentist")
        self.department1.grid(row=2, column=0, pady=10,padx=10)
        self.department1_button = tk.Button(self.root, text="Go to dentist", command=lambda: self.assignDepartment("dentist"))
        self.department1_button.grid(row=3, column=0, pady=10,padx=10)

        self.department2 = tk.Label(self.root, text="Surgeon")
        self.department2.grid(row=2, column=1, pady=10,padx=10)
        self.department2_button = tk.Button(self.root, text="Go to surgeon", command=lambda: self.assignDepartment("surgeon"))
        self.department2_button.grid(row=3, column=1, pady=10,padx=10)
        
        self.department3 = tk.Label(self.root, text="Physician")
        self.department3.grid(row=2, column=2, pady=10,padx=10)
        self.department3_button = tk.Button(self.root, text="Go to physician", command=lambda: self.assignDepartment("physician"))
        self.department3_button.grid(row=3, column=2, pady=10,padx=10)
        
        self.department4 = tk.Label(self.root, text="Psychiatrist")
        self.department4.grid(row=2, column=3, pady=10,padx=10)
        self.department4_button = tk.Button(self.root, text="Go to psychiatrist", command=lambda: self.assignDepartment("psychiatrist"))
        self.department4_button.grid(row=3, column=3, pady=10,padx=10)
        
        self.department5 = tk.Label(self.root, text="Ultrasound")
        self.department5.grid(row=2, column=4, pady=10,padx=10)
        self.department5_button = tk.Button(self.root, text="Go to ultrasound", command=lambda: self.assignDepartment("ultrasound"))
        self.department5_button.grid(row=3, column=4, pady=10,padx=10)
        
    def assignDepartment(self,department):
        self.department.set(department)
        print(self.department.get())
            
    def run(self):
        while True:
            selected_department = self.department.get()
            print(selected_department)
            if selected_department:
                print(f"Selected department: {selected_department}")
                if selected_department == "dentist":
                    print("Dentist's Nurse")
                    dentistNurse = entitles.Nurse(name="Dentist's Nurse", patient=self.patient)
                    yield self.env.process(processes.departmentDentist(self.env, self.patient, dentistNurse))
                elif selected_department == "surgeon":
                    surgeonNurse = entitles.Nurse(name="Surgeon's Nurse", patient=self.patient)
                    yield self.env.process(processes.departmentSurgeon(self.env, self.patient, surgeonNurse))
                elif selected_department == "physician":
                    physicianNurse = entitles.Nurse(name="Physician's Nurse", patient=self.patient)
                    yield self.env.process(processes.departmentPhysician(self.env, self.patient, physicianNurse))
                elif selected_department == "psychiatrist":
                    psychiatristNurse = entitles.Nurse(name="Psychiatrist's Nurse", patient=self.patient)
                    yield self.env.process(processes.departmentPsychiatrist(self.env, self.patient, psychiatristNurse))
                elif selected_department == "ultrasound":
                    radiologyTech = entitles.RadiologyTechnician(name="Radiology Technician", patient=self.patient)
                    yield self.env.process(processes.departmentUltrasound(self.env, self.patient, radiologyTech))
                else:
                    print("Invalid department selected")
                    yield self.env.timeout(1)
            else:
                yield self.env.timeout(1)
            
            yield self.env.timeout(1)


if __name__ == "__main__":
    patient = entitles.Patient(name="Manas", problem="Dental", wait_time=10)
    print(patient)
    env = simpy.RealtimeEnvironment(factor=1)
    simulator = HospitalSimulator(env,patient=patient)
    env.run(until=1)
    simulator.root.mainloop()