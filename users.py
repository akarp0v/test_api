from essential_generators import DocumentGenerator


class User:
    id = ''

    @staticmethod
    def info():
        gen = DocumentGenerator()
        return {"name": gen.name(), "gender": "Male",  "email": gen.email(), "status": "Active"}
