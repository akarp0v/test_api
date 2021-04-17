from essential_generators import DocumentGenerator as Gen
from random import choice


class User:
    def __init__(self):
        self.id = None
        self.name = Gen().name()
        self.email = Gen().email()
        self.gender = choice(["Male", "Female"])
        self.status = "Active"
