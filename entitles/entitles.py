class Patient:
    """Patient's Name, Problem, and Wait Time"""
    def __init__(self,name, problem, wait_time):
        self.name = name
        self.problem = problem
        self.wait_time = wait_time
        
    def __str__(self):
        return f"Patient(name={self.name}, problem={self.problem}, wait_time={self.wait_time})"