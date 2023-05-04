#Processes
#All the processes used in the simulation are defined here.

import tkinter as tk
import simpy, simpy.rt
import time

def departmentDentist(patient, nurse) -> None:
    #Tkinter GUI
    window = tk.Tk()
    window.title("Dentist Department")
    window.geometry("500x500")
    header = tk.Label(window, text=f"Hello {patient.name}! Welcome to the Dentist Department.")
    header.grid(row=0, column=1, pady=10,padx=10)
    simulatorBox = tk.Text(window, height=15, width=50)
    simulatorBox.grid(row=1, column=1, pady=10)
    simulationTimeBox= tk.Text(window, height=15, width=3)
    simulationTimeBox.grid(row=1, column=0, pady=10, padx=10)
    start_button = tk.Button(window, text="Start", command=lambda: patient_process(patient))
    start_button.grid(row=3, column=1, pady=10, padx=10)
    text_1 = tk.Label(window, text="Please wait while the examination is in progress...")
    text_1.grid(row=4, column=1, pady=10, padx=10)
    
    def patient_process(patient):
        def start_simulation(env,patient):
            # Start the exam
            yield env.timeout(1)
            simulatorBox.insert(tk.END, "Starting exam...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Clean the teeth
            yield env.timeout(2)
            simulatorBox.insert(tk.END, "Cleaning teeth...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Check for cavities
            yield env.timeout(3)
            # if patient.has_cavities:
            #     simulatorBox.insert(tk.END, "Cavities found. Referring to surgeon...\n")
            #     patient.department = "surgeon"
            #     # events.surgeon.put(patient)
            #     return
            # else:
                
            simulatorBox.insert(tk.END, "No cavities found. Proceeding with treatment...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Fillings
            yield env.timeout(2)
            simulatorBox.insert(tk.END, "Performing fillings...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Root Canal
            # if patient.has_root_canal:
            #     yield env.timeout(3)
            #     simulatorBox.insert(tk.END, "Performing root canal...\n")
            # else:
            simulatorBox.insert(tk.END, "No root canal required...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Prescription
            yield env.timeout(1)
            simulatorBox.insert(tk.END, "Prescribing medication...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # Payment
            yield env.timeout(2)
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            yield env.timeout(2)
            text_1.config(text="Thank you for visiting the Dentist Department!")
            window.update()

        # Start the simulation environment
        dentistenv = simpy.rt.RealtimeEnvironment(factor=1)
        # Start the patient process
        dentist = dentistenv.process(start_simulation(dentistenv, patient))
        # Run the simulation
        dentistenv.run(until=dentist)
