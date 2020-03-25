from essential_generators import DocumentGenerator


class GenerateData:

    @staticmethod
    def data():
        gen = DocumentGenerator()
        data = {"first_name": "Johny Z",
                "last_name": "Rocket",
                "gender": "male",
                "dob": "1970-08-12",
                "email": gen.email(),
                "phone": gen.phone(),
                "website": gen.url(),
                "address": "Platform 3/4 end of rainbow street",
                "status": "active"}
        return data
