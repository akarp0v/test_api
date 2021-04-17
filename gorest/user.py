from essential_generators import DocumentGenerator as Gen


class User:
    def __init__(self):
        self.id = None
        self.name = Gen().name()
        self.email = Gen().email()
        self.gender = "Male"
        self.status = "Active"
