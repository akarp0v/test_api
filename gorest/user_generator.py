from essential_generators import DocumentGenerator

gen = DocumentGenerator()


class User:
    def __init__(self):
        self.id = None
        self.name = gen.name()
        self.email = gen.email()
        self.gender = "Male"
        self.status = "Active"
