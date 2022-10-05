import json

from services.dancer import RestClient as DancerClient


class JsonImporter:

    dc = DancerClient()

    def __init__(self):
        self.dc.login("marc@gorzala.de", "secret")

    def import_dancer(self, dancer):
        email = dancer["email"]
        password = dancer["password"]
        self.dc.registrations(email, password)
        self.dc.setValidationStatus(email, True)

    def import_from_file(self, filename):
        f = open(filename)
        data = json.load(f)
        for dancer in data["dancer"]:
            self.import_dancer(dancer)
