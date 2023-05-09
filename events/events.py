import simpy

class DentistEvent:
    """
    The patient is sent to the dentist department.
    If the patient needs a surgery, he is sent to the surgeon department.
    Otherwise, he is taken care of by the dentist itself.
    The patient will be provided the necessary treatment and prescribed the necessary medicines.
    The patient is then sent to the cashier, where he pays the bill.
    """
    def __init__(self, env):
        self.env = env
        self.dentist = simpy.Resource(env, capacity=1)
        self.surgeon = simpy.Resource(env, capacity=1)
        self.cashier = simpy.Resource(env, capacity=1)

    def run(self, patient):
        with self.dentist.request() as request:
            yield request

            # Patient is examined by the dentist
            print(f"Patient {patient.name} is being examined by the dentist")
            yield self.env.timeout(5)

            if patient.needSurgery:
                # Patient needs surgery, so send to surgeon department
                print(f"Patient {patient.name} needs surgery and is being sent to surgeon department")
                with self.surgeon.request() as request:
                    yield request
                    print(f"Patient {patient.name} is being operated on by the surgeon")
                    yield self.env.timeout(10)
            else:
                # Patient is treated by the dentist
                print(f"Patient {patient.name} is being treated by the dentist")
                yield self.env.timeout(10)

            # Patient is sent to the cashier department
            print(f"Patient {patient.name} is being sent to the cashier")
            with self.cashier.request() as request:
                yield request
                print(f"Patient {patient.name} is paying the bill")
                yield self.env.timeout(5)
                print(f"Patient {patient.name} has paid the bill and is leaving the dentist department")

class OphthalmologistEvent:
    """
    The patient is sent to the ophthalmologist department.
    If the patient needs a surgery, he is sent to the surgeon department.
    Otherwise, he is taken care of by the ophthalmologist itself.
    The patient will be provided the necessary treatment and prescribed the necessary medicines.
    The patient is then sent to the cashier, where he pays the bill.
    """
    def __init__(self, env):
        self.env = env
        self.ophthalmologist = simpy.Resource(env, capacity=1)
        self.surgeon = simpy.Resource(env, capacity=1)
        self.cashier = simpy.Resource(env, capacity=1)

    def run(self, patient):
        with self.ophthalmologist.request() as request:
            yield request

            # Patient is examined by the ophthalmologist
            print(f"Patient {patient.name} is being examined by the ophthalmologist")
            yield self.env.timeout(5)

            if patient.needSurgery:
                # Patient needs surgery, so send to surgeon department
                print(f"Patient {patient.name} needs surgery and is being sent to surgeon department")
                with self.surgeon.request() as request:
                    yield request
                    print(f"Patient {patient.name} is being operated on by the surgeon")
                    yield self.env.timeout(10)
            else:
                # Patient is treated by the ophthalmologist
                print(f"Patient {patient.name} is being treated by the ophthalmologist")
                yield self.env.timeout(10)

            # Patient is sent to the cashier department
            print(f"Patient {patient.name} is being sent to the cashier")
            with self.cashier.request() as request:
                yield request
                print(f"Patient {patient.name} is paying the bill")
                yield self.env.timeout(5)
                print(f"Patient {patient.name} has paid the bill and is leaving the ophthalmologist department")

