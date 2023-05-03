from main import env
from simpy import Resource

class Patient:
    """Patient's Name, Problem, and Wait Time"""
    def __init__(self,name, problem, wait_time):
        self.name = name
        self.problem = problem
        self.wait_time = wait_time
        
    def __str__(self):
        return f"Patient(name={self.name}, problem={self.problem}, wait_time={self.wait_time})"

class Nurse:
    """A model of a nurse, who generally aids the doctor and performs other tasks which a doctor does not have time for."""
    def __init__(self, name, patient: Patient):
        self.name = name
        self.patient = patient if patient else None
        self.busy = "not busy" if not patient else f"busy with {patient.name}."
        
    def __str__(self):
        return f"Nurse {self.name} is currently {self.busy}."

    def assign(self, patient):
        """Assigns a patient to the nurse."""
        self.busy = f"Busy with {patient.name}."
        
    def free(self):
        """Frees the nurse from the patient."""
        self.busy = "Not busy"
        
class Dentist(env):
    """
    A simple dentist, who examines the patient and, if necessary, sends them to the surgeon.
    """
    def __init__(self, env, patient:Patient):
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