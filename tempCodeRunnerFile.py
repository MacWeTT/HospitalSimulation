import simpy
import tkinter as tk
from entitles.entitles import Patient
from utils.utils import askPatient

class HospitalSimulator:
    '''
    Entry point for the hospital simulation.
    '''
    def __init__(self,patient: Patient):
        
        self.patient = patient
        
        self.root = tk.Tk()
        self.root.title("Hospital Simulator")
        self.root.geometry("1920x1080") 
        
        self.title_label = tk.Label(self.root, text="Hospital Simulator")
        self.title_label.grid(row=0, column=2, pady=10,padx=10)
        
        self.question_label = tk.Label(self.root, text=f"Hi {self.patient.name}! How may I help you?")
        self.question_label.grid(row=1, column=2, pady=10,padx=10)


if __name__ == "__main__":
    patient = askPatient()
    print(patient)
    simulator = HospitalSimulator(patient=patient)
    simulator.root.mainloop()