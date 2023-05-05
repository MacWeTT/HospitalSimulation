# Processes
# All the processes used in the simulation are defined here.

import tkinter as tk
import simpy, simpy.rt
import entitles.entitles as entitles


def departmentDentist(patient, nurse) -> None:
    # Tkinter GUI
    window = tk.Tk()
    window.title("Dentist Department")
    window.geometry("800x500")

    header = tk.Label(
        window, text=f"Hello {patient.name}! Welcome to the Dentist Department."
    )
    header.grid(row=0, column=1, pady=10, padx=10)

    simulatorBox = tk.Text(window, height=20, width=90)
    simulatorBox.grid(row=1, column=1, pady=10)
    simulationTimeBox = tk.Text(window, height=20, width=3)
    simulationTimeBox.grid(row=1, column=0, pady=10, padx=10)

    start_button = tk.Button(
        window, text="Examine", command=lambda: patient_process(patient)
    )
    start_button.grid(row=3, column=1, pady=10, padx=10)

    text_1 = tk.Label(window, text="Press Examine to start the procedure...")
    text_1.grid(row=4, column=1, pady=10, padx=10)

    def patient_process(patient) -> None:
        def start_simulation(env, patient: entitles.Patient) -> None:
            text_1.config(text="Please wait while the examination is in progress...")
            start_button.config(state=tk.DISABLED)
            # Start the examination
            simulatorBox.insert(tk.END, f"Starting {patient.name}'s examination.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            yield env.timeout(1)
            window.update()

            # Report the issues
            problems = patient.problems["dental"]
            simulatorBox.insert(
                tk.END, f"Dentist found the following issues: {problems}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            yield env.timeout(2)
            window.update()

            simulatorBox.insert(tk.END, "Starting the treatment\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            # If cavities exist, perform fillings and root canal
            if problems.count("caries"):
                simulatorBox.insert(tk.END, "Treating dental caries...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(0)
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(1)
                window.update()

                simulatorBox.insert(tk.END, "~Performing root canal\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(2)
                window.update()

                simulatorBox.insert(tk.END, "~Filling the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(2)
                window.update()

                simulatorBox.insert(tk.END, "~Polishing the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(1)
                window.update()

                simulatorBox.insert(tk.END, "Treatment for dental caries successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["dental"].append("Ketrol DT")
                patient.prescriptions["dental"].append("IBUPROFEN")
                patient.bill["dental"]["RCT + filling charges"] += 2500
                patient.bill["dental"]["Medication charges"] += 220
                patient.bill_total += 2720

            # If tooth is broken, perform extraction
            if problems.count("brokentooth"):
                simulatorBox.insert(tk.END, "Treating broken tooth...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(0)
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(1)
                window.update()

                simulatorBox.insert(tk.END, "~Extracting the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(2)
                window.update()

                simulatorBox.insert(tk.END, "Treatment for broken tooth successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["dental"].append("Ketrol DT")
                patient.prescriptions["dental"].append("Acetaminophen")
                patient.bill["dental"]["Extraction charges"] += 1000
                patient.bill["dental"]["Medication charges"] += 1070
                patient.bill_total += 2070

            # If gums are bleeding, perform cleaning and apply medication
            if problems.count("bleedinggums"):
                simulatorBox.insert(tk.END, "Treating bleeding gums...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(0)
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(1)
                window.update()

                simulatorBox.insert(tk.END, "~Cleaning the gums\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(2)
                window.update()

                simulatorBox.insert(tk.END, "~Applying medication\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                yield env.timeout(1)
                window.update()

                simulatorBox.insert(tk.END, "Treatment for bleeding gums successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                patient.prescriptions["dental"].append("Amoxycillin")
                patient.bill["dental"]["Gum treatment charges"] += 1000
                patient.bill["dental"]["Medication charges"] += 30
                patient.bill_total += 1030

            # Prescription
            yield env.timeout(1)
            simulatorBox.insert(tk.END, "Prescribing medication...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            window.update()

            patient.bill["dental"]["Examination charges"] += 500
            patient.bill_total += 500

            # Payment
            yield env.timeout(2)
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            yield env.timeout(2)
            start_button.config(
                state=tk.NORMAL,
                text="Pay Bill",
                command=payment_window,
            )
            text_1.config(text="Thank you for visiting the Dentist Department!")
            window.update()

        def payment_window() -> None:
            window_pay = tk.Toplevel(window)
            window_pay.title("Pay Bill")

            text_main = tk.Label(window_pay, text="Dentist Bill Summary")
            text_main.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

            bill_box = tk.Text(window_pay, height=10, width=30, padx=10, pady=10)
            bill_box.grid(row=1, column=0, columnspan=2)

            amount_box = tk.Text(window_pay, height=10, width=5, padx=10, pady=10)
            amount_box.grid(row=1, column=2)

            for key, value in patient.bill["dental"].items():
                bill_box.insert(tk.END, f"{key}\n")
                amount_box.insert(tk.END, f"{value}\n")
                window_pay.update()

            def pay() -> None:
                simulatorBox.insert(tk.END, "Payment successful.\n")
                simulationTimeBox.insert(tk.END, f"{dentistenv.now}\n")
                window.update()

                simulatorBox.insert(
                    tk.END, "Thank you for visiting the Dentist Department!\n"
                )
                simulationTimeBox.insert(tk.END, f"{dentistenv.now}\n")
                window.update()

                window_pay.destroy()

            pay_button = tk.Button(window_pay, text="Pay Bill", command=pay)
            pay_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

            window_pay.mainloop()

        # Start the simulation environment
        dentistenv = simpy.rt.RealtimeEnvironment(factor=1, initial_time=0)
        # Start the patient process
        dentist = dentistenv.process(start_simulation(dentistenv, patient))
        # Run the simulation
        dentistenv.run(until=dentist)
