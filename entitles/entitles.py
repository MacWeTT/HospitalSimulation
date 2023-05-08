from simpy import Resource


class Patient:
    """Patient's Name, Problem, and Wait Time"""

    def __init__(
        self,
        name,
        problems={"dental": [], "surgery": [], "physical": [], "pharmacy": []},
        prescriptions={"dental": [], "surgery": [], "physical": [], "pharmacy": []},
        bill={
            "dental": {
                "Medication charges": 0,
                "Examination charges": 0,
                "RCT + filling charges": 0,
                "Gum treatment charges": 0,
                "Extraction charges": 0,
            },
            "surgery": {
                "Medication charges": 0,
                "Examination charges": 0,
                "surgery charges": 0,
            },
            "physical": {
                "Medication charges": 0,
                "physical examination charges": 0,
            },
            "ultrasound": {
                "Medication charges": 0,
            },
        },
        bill_total=0,
    ):
        self.name = name
        self.problems = problems
        self.prescriptions = prescriptions
        self.bill = bill
        self.bill_total = bill_total

    def __str__(self):
        return f"Patient(name={self.name}\n problem={self.problems} \n prescriptions={self.prescriptions} \n bill={self.bill})"


class Nurse:
    """A model of a nurse, who generally aids the doctor and performs other tasks which a doctor does not have time for."""

    def __init__(self, name, patient: Patient):
        self.name = name
        self.patient = patient if patient else None
        self.busy = "not busy" if not patient else f"busy with {patient.name}."

    def __str__(self):
        return f"{self.name} is currently {self.busy}."

    def assign(self, patient):
        """Assigns a patient to the nurse."""
        self.busy = f"Busy with {patient.name}."

    def free(self):
        """Frees the nurse from the patient."""
        self.busy = "Not busy"


class Dentist:
    """
    A simple dentist, who examines the patient and, if necessary, sends them to the surgeon.
    """

    def __init__(self, env, patient: Patient):
        self.env = env
        self.dentist = Resource(env, capacity=1)
        self.patient = patient if patient else None

    def examine(self, patient):
        print(f"Dentist is examining {patient.name}...")
        yield self.env.timeout(10)  # Time for examination
        print(f"Dentist has finished examining {patient.name}.")

    def clean_teeth(self, patient):
        # Perform teeth cleaning procedure
        print(f"Dentist is cleaning the teeth of {patient}...")
        yield self.env.timeout(15)  # Time for teeth cleaning
        print(f"Dentist has finished cleaning the teeth of {patient}.")

    def extract_tooth(self, patient):
        # Perform tooth extraction procedure
        print(f"Dentist is extracting a tooth from {patient}...")
        yield self.env.timeout(60)  # Time for tooth extraction
        print(f"Dentist has finished extracting a tooth from {patient}.")

    def __str__(self) -> str:
        print("You requested a dentist.")


class RadiologyTechnician:
    pass
