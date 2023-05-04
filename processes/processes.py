#Processes
#All the processes used in the simulation are defined here.

import tkinter as tk
import simpy

#debug
# from entitles import entitles

def departmentDentist(env, patient, nurse):
    """
    The patient is sent to the dentist department.
    Patient is then examined, and if the patient needs a surgery, he is sent to the surgeon department.
    Otherwise, he is taken care of by the dentist itself.
    The patient will be provided the necessary treatment and prescribed the necessary medicines.
    The patient is then sent to the cashier, where he pays the bill.
    """
    window = tk.Tk()
    window.title("The Dentist")
    window.title_label = tk.Label(window, text="Welcome to the Dentist's department!")
    window.title_label.grid(row=0, column=0, padx=10, pady=10)
    print(patient)
    print(nurse)
    print("Doctor ka hogaya")
    yield env.timeout(10)  # Time for examination
    
    window.mainloop()


def departmentUltrasound(env, nurse, patient):
    pass

# env = simpy.RealtimeEnvironment(factor=1)
# patient = entitles.Patient(name="Manas", problem="Dental", wait_time=10)
# dentistNurse = entitles.Nurse(name="Dentist's Nurse", patient=patient)
# env.process(departmentDentist(env,patient,nurse=dentistNurse))
# env.run(until=20)