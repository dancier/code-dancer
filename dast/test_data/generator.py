class SimpleGenerator:
    number_of_dancer = 100

    def generate(self):
        result = {}
        all_dancer = list()
        result["dancer"] = all_dancer
        for x in range(self.number_of_dancer):
            dancer = {
                "email": str(x) + "test@dancier.net",
                "password": "secret"
            }
            all_dancer.append(dancer)
        return result
