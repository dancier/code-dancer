import json
import config

from services.dancer import RestClient as DancerClient


class JsonImporter:
    dc = DancerClient()

    def __init__(self):
        pass

    def register_dancer(self, dancer):
        print("Admin login")
        self.dc.auth_login(config.DANCER_ADMIN_USER, config.DANCER_ADMIN_PASS)
        email = dancer["email"]
        password = dancer["password"]
        print("Perform Registration")
        self.dc.auth_registrations(email, password)
        self.dc.auth_setValidationStatus(email, True)

    def put_profile(self, dancer):
        print("User Login")
        self.dc.auth_login(dancer["email"], dancer["password"])
        print("Profile update")

        payload = {
            "aboutMe": dancer["aboutMe"],
            "gender": dancer["gender"],
            "dancerName": dancer["dancerName"],
            "birthDate": dancer["birthDate"],
            "ableTo": dancer["ableTo"],
            "wantsTo": dancer["wantsTo"],
            "zipCode": dancer["zipCode"],
            "country": dancer["country"],
            "size": dancer["size"]
        }

        r = self.dc.profile_put(payload)
        print(r)

    def import_from_file(self, filename):
        f = open(filename)
        data = json.load(f)
        for dancer in data["dancer"]:
            self.register_dancer(dancer)
            self.put_profile(dancer)
