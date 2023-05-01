from main import env
from simpy import Resource
from entitles.entitles import Patient

class Dentist(env):
    """
    A simple dentist, who examines the patient and, if necessary, sends them to the surgeon.
    """
    def __init__(self, env):
        self.env = env
        self.dentist = Resource(env, capacity=1)
        self.patient = Patient()
        
    def examine(self, patient):
        print(f"Dentist is examining {patient.name}...")
        # if ()
    
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