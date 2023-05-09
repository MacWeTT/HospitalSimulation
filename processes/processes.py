# Processes
# All the processes used in the simulation are defined here.

import tkinter as tk
import simpy, simpy.rt
import entitles.entitles as entitles


def departmentDentist(patient: entitles.Patient, nurse: entitles.Nurse) -> None:
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
        def start_simulation(
            env: simpy.rt.RealtimeEnvironment, patient: entitles.Patient
        ) -> None:
            text_1.config(text="Please wait while the examination is in progress...")
            start_button.config(state=tk.DISABLED)

            # Start the examination
            simulatorBox.insert(tk.END, f"Starting {patient.name}'s examination.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(2)

            # Report the issues
            problems = patient.problems["dental"]
            simulatorBox.insert(
                tk.END, f"Dentist found the following issues: {problems}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            simulatorBox.insert(tk.END, "Starting the treatment\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)

            # If cavities exist, perform fillings and root canal
            if problems.count("caries"):
                simulatorBox.insert(tk.END, "Treating dental caries...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Performing root canal\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Filling the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Polishing the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

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
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Extracting the tooth\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

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
                window.update()

                simulatorBox.insert(tk.END, "~Injecting anaesthesia\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Cleaning the gums\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Applying medication\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Treatment for bleeding gums successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                patient.prescriptions["dental"].append("Amoxycillin")
                patient.bill["dental"]["Gum treatment charges"] += 1000
                patient.bill["dental"]["Medication charges"] += 30
                patient.bill_total += 1030

            # Prescription
            simulatorBox.insert(tk.END, "Prescribing medication...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)
            simulatorBox.insert(
                tk.END, f"Prescribed: {patient.prescriptions['dental']}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            window.update()

            patient.bill["dental"]["Examination charges"] += 500
            patient.bill_total += 500

            # Payment
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
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

            bill_box = tk.Text(window_pay, height=10, width=30)
            bill_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            amount_box = tk.Text(window_pay, height=10, width=5)
            amount_box.grid(row=1, column=2, padx=10, pady=10)

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
                start_button.config(tk.DISABLED)
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


def departmentPhysician(patient: entitles.Patient, nurse: entitles.Nurse) -> None:
    window = tk.Tk()
    window.title("Physician Department")
    window.geometry("800x500")

    header = tk.Label(
        window, text=f"Hello {patient.name}! Welcome to the Physician Department."
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
        def start_simulation(
            env: simpy.rt.RealtimeEnvironment, patient: entitles.Patient
        ) -> None:
            text_1.config(text="Please wait while the examination is in progress...")
            start_button.config(state=tk.DISABLED)

            # Start the examination
            simulatorBox.insert(tk.END, f"Starting {patient.name}'s examination.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(2)

            # Report the issues
            problems = patient.problems["illness"]
            simulatorBox.insert(
                tk.END, f"Physician found the following issues: {problems}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            simulatorBox.insert(tk.END, "Checking patient’s history.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)

            # If Hepatitis exist, perform ultrasound and liver biopsy
            if problems.count("Hepatitis"):
                simulatorBox.insert(tk.END, "Taking blood samples ...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Performing Ultrasound\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Checking reports for ultrasound\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Performing Liver biopsy\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Recommending medicines\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Treatment for hepatitis caries successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["illness"].append("tenofovir disoproxil fumarate (TDF)")
                patient.prescriptions["illness"].append("entecavir (ETV)")
                patient.bill["illness"]["Test Charges"] += 2000
                patient.bill["illness"]["Medication charges"] += 250
                patient.bill_total += 2250

            # If Hypertension, perform the following
            if problems.count("Hypertension"):
                simulatorBox.insert(tk.END, "Checking blood pressure...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Performing ambulatory blood pressure monitoring\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Performing Blood and urine tests\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Performing electrocardiogram\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Checking reports and prescribing medicines\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Checkup for hypertension successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["illness"].append("hydrochlorothiazide (Microzide)")
                patient.prescriptions["illness"].append(" benazepril (Lotensin)")
                patient.bill["illness"]["Test charges"] += 1000
                patient.bill["illness"]["Medication charges"] += 1070
                patient.bill_total += 2070

            # If asthma, perform tests and prescribe medicines
            if problems.count("asthma"):
                simulatorBox.insert(tk.END, "Checking asthma...\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Performing Spirometry\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Tracking and dealing with low peak flow readings\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Prescribing medication\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Checkup for asthma successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                patient.prescriptions["illness"].append("Fluticasone (Flovent HFA)")
                patient.prescriptions["illness"].append("Budesonide (Pulmicort Flexhaler)")
                patient.bill["illness"]["Tests charges"] += 1500
                patient.bill["illness"]["Medication charges"] += 400
                patient.bill_total += 1900

            # Prescription
            simulatorBox.insert(tk.END, "Prescribing medication...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)
            simulatorBox.insert(
                tk.END, f"Prescribed: {patient.prescriptions['illness']}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            window.update()

            patient.bill["illness"]["Examination charges"] += 500
            patient.bill_total += 500

            # Payment
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            start_button.config(
                state=tk.NORMAL,
                text="Pay Bill",
                command=payment_window,
            )
            text_1.config(text="Thank you for visiting the Physician Department!")
            window.update()

        def payment_window() -> None:
            window_pay = tk.Toplevel(window)
            window_pay.title("Pay Bill")

            text_main = tk.Label(window_pay, text="Physician Bill Summary")
            text_main.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

            bill_box = tk.Text(window_pay, height=10, width=30)
            bill_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            amount_box = tk.Text(window_pay, height=10, width=5)
            amount_box.grid(row=1, column=2, padx=10, pady=10)

            for key, value in patient.bill["illness"].items():
                bill_box.insert(tk.END, f"{key}\n")
                amount_box.insert(tk.END, f"{value}\n")
                window_pay.update()

            def pay() -> None:
                simulatorBox.insert(tk.END, "Payment successful.\n")
                simulationTimeBox.insert(tk.END, f"{physicianenv.now}\n")
                window.update()

                simulatorBox.insert(
                    tk.END, "Thank you for visiting the Physician Department!\n"
                )
                start_button.config(tk.DISABLED)
                simulationTimeBox.insert(tk.END, f"{physicianenv.now}\n")
                window.update()

                window_pay.destroy()

            pay_button = tk.Button(window_pay, text="Pay Bill", command=pay)
            pay_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

            window_pay.mainloop()

        # Start the simulation environment
        physicianenv = simpy.rt.RealtimeEnvironment(factor=1, initial_time=0)
        # Start the patient process
        physician = physicianenv.process(start_simulation(physicianenv, patient))
        # Run the simulation
        physicianenv.run(until=physician)



def departmentOphthalmologist(patient: entitles.Patient, nurse: entitles.Nurse) -> None:
    # Tkinter GUI
    window = tk.Tk()
    window.title("Ophthalomologist Department")
    window.geometry("800x500")

    header = tk.Label(
        window, text=f"Hello {patient.name}! Welcome to the Ophthalmologist Department."
    )
    header.grid(row=0, column=1, pady=10, padx=10)

    simulatorBox = tk.Text(window, height=20, width=90)
    simulatorBox.grid(row=1, column=1, pady=10)
    simulationTimeBox = tk.Text(window, height=20, width=3)
    simulationTimeBox.grid(row=1, column=0, pady=10, padx=10)

    start_button = tk.Button(
        window, text="Enter", command=lambda: patient_process(patient)
    )
    start_button.grid(row=3, column=1, pady=10, padx=10)

    text_1 = tk.Label(window, text="Press Enter to start the procedure...")
    text_1.grid(row=4, column=1, pady=10, padx=10)

    def patient_process(patient) -> None:
        def start_simulation(
            env: simpy.rt.RealtimeEnvironment, patient: entitles.Patient
        ) -> None:
            text_1.config(text="Please wait while the examination is in progress...")
            start_button.config(state=tk.DISABLED)

            # Start the examination
            simulatorBox.insert(tk.END, f"Starting {patient.name}'s examination.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(2)

            # Report the issues
            problems = patient.problems["weakeyesight"]
            simulatorBox.insert(
                tk.END, f"Ophthalmologist found the following issues: {problems}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            simulatorBox.insert(tk.END, "Checking patient’s history.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)

            # If cavities exist, perform fillings and root canal
            if problems.count("myopia"):
                simulatorBox.insert(tk.END, "Proceeding with vision test\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Asked to read the eye chart\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Performing eye exam \n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Checking health of the eyes\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Preparing diagnosis and treatment plan\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Treatment for myopia carries successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["weakeyesight"].append("Atropine")
                patient.bill["weakeyesight"]["eye test charges"] += 2100
                patient.bill["weakeyesight"]["contact lens charges"] += 3220
                patient.bill_total += 5320

            # If hyperopia, perform following
            if problems.count("conjunctivitis"):
                simulatorBox.insert(tk.END, "Proceeding with conjunctivitis\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Rinsing the eyes\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Preparing treatment\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Applying ointment\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Treatment for conjunctivitis carries successful.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                # Add prescriptions and bill
                patient.prescriptions["weakeyesight"].append("Antivirals")
                patient.bill["weakeyesight"]["Test charges"] += 1000
                patient.bill["weakeyesight"]["Medication charges"] += 1070
                patient.bill_total += 2070

            # If gums are bleeding, perform cleaning and apply medication
            if problems.count("cataract"):
                simulatorBox.insert(tk.END, "Proceeding with the eye surgery\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                simulatorBox.insert(tk.END, "~Performing comprehensive eye exam\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "~Discussing surgical options\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Removing the clouded lens.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(2)

                simulatorBox.insert(tk.END, "~Monitoring the eye condition\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()
                yield env.timeout(1)

                simulatorBox.insert(tk.END, "Surgery performed successfully.\n")
                simulationTimeBox.insert(tk.END, f"{env.now}\n")
                window.update()

                patient.prescriptions["weakeyesight"].append("Zeaxanthin")
                patient.bill["weakeyesight"]["Surgery charges"] += 3000
                patient.bill["weakeyesight"]["Medication charges"] += 300
                patient.bill_total += 3300

            # Prescription
            simulatorBox.insert(tk.END, "Prescribing medication...\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)
            simulatorBox.insert(
                tk.END, f"Prescribed: {patient.prescriptions['weakeyesight']}\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            window.update()

            patient.bill["weakeyesight"]["Examination charges"] += 500
            patient.bill_total += 500

            # Payment
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            start_button.config(
                state=tk.NORMAL,
                text="Pay Bill",
                command=payment_window,
            )
            text_1.config(text="Thank you for visiting the Ophthalmologist Department!")
            window.update()

        def payment_window() -> None:
            window_pay = tk.Toplevel(window)
            window_pay.title("Pay Bill")

            text_main = tk.Label(window_pay, text="Ophthalmologist Bill Summary")
            text_main.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

            bill_box = tk.Text(window_pay, height=10, width=30)
            bill_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            amount_box = tk.Text(window_pay, height=10, width=5)
            amount_box.grid(row=1, column=2, padx=10, pady=10)

            for key, value in patient.bill["weakeyesight"].items():
                bill_box.insert(tk.END, f"{key}\n")
                amount_box.insert(tk.END, f"{value}\n")
                window_pay.update()

            def pay() -> None:
                simulatorBox.insert(tk.END, "Payment successful.\n")
                simulationTimeBox.insert(tk.END, f"{ophthalmologistenv.now}\n")
                window.update()

                simulatorBox.insert(
                    tk.END, "Thank you for visiting the ophthalmologist Department!\n"
                )
                start_button.config(tk.DISABLED)
                simulationTimeBox.insert(tk.END, f"{ophthalmologistenv.now}\n")
                window.update()

                window_pay.destroy()

            pay_button = tk.Button(window_pay, text="Pay Bill", command=pay)
            pay_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

            window_pay.mainloop()

        # Start the simulation environment
        ophthalmologistenv = simpy.rt.RealtimeEnvironment(factor=1, initial_time=0)
        # Start the patient process
        ophthalmologist = ophthalmologistenv.process(start_simulation(ophthalmologistenv, patient))
        # Run the simulation
        ophthalmologistenv.run(until=ophthalmologist)


def departmentUltrasound(patient: entitles.Patient, nurse: entitles.Nurse) -> None:
    window = tk.Tk()
    window.title("Ultrasound")
    header = tk.Label(
        window, text=f"Hello {patient.name}! Welcome to the Ultrasound Department."
    )
    header.grid(row=0, column=0, pady=10, padx=10, columnspan=6)

    text_2 = tk.Label(window, text="Please select the organs you want to examine:")
    text_2.grid(row=1, column=1, pady=10, padx=10, columnspan=5)

    start_button = tk.Button(
        window, text="Examine", command=lambda: patient_process(patient)
    )
    start_button.grid(row=5, column=1, pady=10, padx=10, columnspan=5)

    organs = []

    def select_organs(organ) -> None:
        if organ not in organs:
            organs.append(organ)
            simulatorBox.insert(tk.END, f"Selected: {organ}\n")

    organ_1 = tk.Button(window, text="Heart", command=lambda: select_organs("heart"))
    organ_1.grid(row=2, column=1, pady=10, padx=10)

    organ_2 = tk.Button(window, text="Liver", command=lambda: select_organs("liver"))
    organ_2.grid(row=2, column=2, pady=10, padx=10)

    organ_3 = tk.Button(window, text="Kidney", command=lambda: select_organs("kidney"))
    organ_3.grid(row=2, column=3, pady=10, padx=10)

    organ_4 = tk.Button(window, text="Lungs", command=lambda: select_organs("lungs"))
    organ_4.grid(row=2, column=4, pady=10, padx=10)

    organ_5 = tk.Button(
        window, text="Stomach", command=lambda: select_organs("stomach")
    )
    organ_5.grid(row=2, column=5, pady=10, padx=10)

    simulatorBox = tk.Text(window, height=20, width=80)
    simulatorBox.grid(row=3, column=1, pady=10, padx=10, columnspan=5)

    simulationTimeBox = tk.Text(window, height=20, width=5)
    simulationTimeBox.grid(row=3, column=0, pady=10, padx=10, columnspan=1)

    text_1 = tk.Label(window, text="Press Examine to start your examination...")
    text_1.grid(row=4, column=1, pady=10, padx=10, columnspan=5)

    def patient_process(patient) -> None:
        def start_simulation(
            env: simpy.rt.RealtimeEnvironment,
            patient: entitles.Patient,
            ultrasoundMachine: simpy.Resource,
            organs: list,
        ) -> None:
            text_1.config(text="Please wait while the examination is in progress...")
            start_button.config(state=tk.DISABLED)

            # Clear the text box
            simulatorBox.delete("1.0", tk.END)
            # Start the examination
            simulatorBox.insert(tk.END, f"Starting {patient.name}'s examination.\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(2)

            # Report the issues
            simulatorBox.insert(
                tk.END, f"Starting ultrasound on the selected organs..\n"
            )
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()

            simulatorBox.insert(tk.END, "Starting the treatment\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            window.update()
            yield env.timeout(1)

            for organ in organs:
                with ultrasoundMachine.request() as req:
                    yield req
                    yield env.timeout(1)
                    simulatorBox.insert(tk.END, f"Starting ultrasound on {organ}\n")
                    simulationTimeBox.insert(tk.END, f"{env.now}\n")
                    window.update()
                patient.bill["ultrasound"]["Examination charges"] += 800
                patient.bill["ultrasound"]["Examined organs"] += 1
                patient.bill_total += 800

            # Payment
            simulatorBox.insert(tk.END, f"Payment due: {patient.bill_total}\n")
            simulationTimeBox.insert(tk.END, f"{env.now}\n")
            simulatorBox.see(tk.END)
            simulationTimeBox.see(tk.END)
            start_button.config(
                state=tk.NORMAL,
                text="Pay Bill",
                command=payment_window,
            )
            text_1.config(text="Thank you for visiting Ultrasound Department!")
            window.update()

        def payment_window() -> None:
            window_pay = tk.Toplevel(window)
            window_pay.title("Pay Bill")

            text_main = tk.Label(window_pay, text="Ultrasound Bill Summary")
            text_main.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

            bill_box = tk.Text(window_pay, height=10, width=30)
            bill_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

            amount_box = tk.Text(window_pay, height=10, width=5)
            amount_box.grid(row=1, column=2, padx=10, pady=10)

            for key, value in patient.bill["ultrasound"].items():
                bill_box.insert(tk.END, f"{key}\n")
                amount_box.insert(tk.END, f"{value}\n")
                window_pay.update()

            def pay() -> None:
                simulatorBox.insert(tk.END, "Payment successful.\n")
                simulationTimeBox.insert(tk.END, f"{ultrasoundenv.now}\n")
                window.update()

                simulatorBox.insert(
                    tk.END, "Thank you for visiting the Ultrasound Department!\n"
                )
                start_button.config(tk.DISABLED)
                simulationTimeBox.insert(tk.END, f"{ultrasoundenv.now}\n")
                window.update()

                window_pay.destroy()

            pay_button = tk.Button(window_pay, text="Pay Bill", command=pay)
            pay_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

            window_pay.mainloop()

        # Start the simulation environment
        ultrasoundenv = simpy.rt.RealtimeEnvironment(factor=1, initial_time=0)
        # Create the ultrasound machine resource
        ultrasoundMachine = simpy.Resource(ultrasoundenv, capacity=1)
        # Start the patient process
        ultrasound = ultrasoundenv.process(
            start_simulation(ultrasoundenv, patient, ultrasoundMachine, organs)
        )
        # Run the simulation
        ultrasoundenv.run(until=ultrasound)
