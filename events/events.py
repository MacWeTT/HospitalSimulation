import simpy

def dentistEvent(env):
    yield simpy.Timeout(env, 10)    