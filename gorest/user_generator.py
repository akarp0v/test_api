from essential_generators import DocumentGenerator

gen = DocumentGenerator()


class User:
    id = ''
    name = gen.name()
    email = gen.email()
    gender = "Male"
    status = "Active"

    @staticmethod
    def info():
        return User()
