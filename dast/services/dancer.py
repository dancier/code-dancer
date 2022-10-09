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
        print("Loggin in:" + email)
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

    def profile_put(self, payload):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        print("Putting: " + str(payload))
        r = requests.put(self.hostname + "/profile", headers=headers, data=json.dumps(payload))
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
