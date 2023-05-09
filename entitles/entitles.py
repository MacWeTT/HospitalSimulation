from simpy import Resource


class Patient:
    """Patient's Name, Problem, and Wait Time"""

    def __init__(
        self,
        name,
        problems={"dental": [], "eyes": [], "physical": [], "ultrasound": []},
        prescriptions={"dental": [], "eyes": [], "physical": [], "ultrasound": []},
        bill={
            "dental": {
                "Medication charges": 0,
                "Examination charges": 0,
                "RCT + filling charges": 0,
                "Gum treatment charges": 0,
                "Extraction charges": 0,
            },
            "eyes": {
                "Medication charges": 0,
                "Test charges": 0,
                "Surgery charges": 0,
                "eye test charges": 0,
                "contact lens charges": 0,
                "Examination charges": 0,
            },
            "physical": {
                "Medication charges": 0,
                "physical examination charges": 0,
            },
            "ultrasound": {
                "Examined organs": 0,
                "Medication charges": 0,
                "Examination charges": 0,
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
