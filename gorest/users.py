from essential_generators import DocumentGenerator

gen = DocumentGenerator()


class User:
    id = ''
    name = gen.name()
    email = gen.email()
    gender = "Male"
    status = "Active"

    def info(self) -> dict:
        return {"name": self.name, "gender": self.gender, "email": self.email, "status": self.status}
