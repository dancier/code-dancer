import json

from services.dancer import RestClient as DancerClient


class JsonImporter:

    dc = DancerClient()

    admin_user = "marc@gorzala.de"
    admin_pass = "secret"

    def __init__(self):
        pass

    def import_dancer(self, dancer):
        print("Admin login")
        self.dc.auth_login(self.admin_user, self.admin_pass)
        email = dancer["email"]
        password = dancer["password"]
        print("Perform Registration")
        self.dc.auth_registrations(email, password)
        self.dc.auth_setValidationStatus(email, True)
        print("User Login")
        self.dc.auth_login(email, password)
        print("Profile update")
        self.dc.profile_put("")

    def import_from_file(self, filename):
        f = open(filename)
        data = json.load(f)
        for dancer in data["dancer"]:
            self.import_dancer(dancer)
