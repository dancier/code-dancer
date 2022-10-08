import requests
import json


class RestClient:
    hostname = "http://localhost:8080"

    cached_token = None

    def __init__(self) -> None:
        pass

    def event_log(self):
        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "topic": "test123",
            "metaData": {"hallo": "jan"},
            "payload": {"engles": "schick doch auch mal was"}
        }
        r = requests.post(self.hostname + "/eventlog", headers=headers, data=json.dumps(payload))
        return r

    def auth_whoami(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/authentication/whoami", headers=headers)
        return r

    def auth_login(self, email, password):
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "email": email,
            "password": password
        }
        r = requests.post(self.hostname + "/authentication/login", headers=headers, data=json.dumps(payload))
        if r.status_code == 200:
            print("Login successfull: ")
            print("Token stored for further reference")
            self.cached_token = r.json()["accessToken"]
        return r

    def auth_registrations(self, email, password):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        payload = {
            "email": email,
            "password": password,
            "acceptTermsAndConditions": True
        }
        r = requests.post(self.hostname + "/authentication/registrations", headers=headers, data=json.dumps(payload))
        return r

    def profile_put(self, body):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        body = {
            "size": 120,
            "aboutMe": "Ich TAnzen lernen, egal wie hauptsache schnell.",
            "gender": "DIVERS",
            "dancerName": "dominik",
            "birthDate": "1987-07-30",
            "zipCode": "44139",
            "country": "GER",
            "profileImageHash": "60820f9f49c51232dca11cf582e8cee0b6e2fe086b69bfc7fb10597db9ff4589",
            "ableTo": [
                {
                    "dance": "Tango",
                    "level": "ADVANCED",
                    "leading": "LEAD"
                }
            ],
            "wantsTo": [
                {
                    "dance": "Lindi Hop",
                    "level": "INTERMEDIATE",
                    "leading": "FOLLOW"
                },
                {
                    "dance": "Tango",
                    "level": "INTERMEDIATE",
                    "leading": "FOLLOW"
                },
                {
                    "dance": "Bed Dance",
                    "level": "ADVANCED",
                    "leading": "FOLLOW"
                }
            ]
        }
        r = requests.put(self.hostname + "/profile", headers=headers, data=json.dumps(body))
        return r

    def auth_setValidationStatus(self, email, validated=True):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        payload = {
            "emailAddress": email,
            "validated": validated
        }
        r = requests.put(self.hostname + "/authentication/email-validations", headers=headers, data=json.dumps(payload))
        return r
