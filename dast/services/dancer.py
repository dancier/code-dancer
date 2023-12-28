import requests
import json
import config


class RestClient:
    hostname = config.DANCER_HOSTNAME

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

    def get_own_profile(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/profile", headers=headers)
        return r

    def get_profile(self, dancer_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/profile/" + dancer_id, headers=headers)
        return r

    def auth_whoami(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/authentication/whoami", headers=headers)
        return r

    def auth_logout(self):
        r = requests.get(self.hostname + "/authentication/logout")
        if r.status_code == 200:
            print("removing cookie")
            self.cached_token = None

    def auth_login(self, email, password):
        print("Login in with:" + email)
        headers = {
            "Content-Type": "application/json",
        }
        payload = {
            "email": email,
            "password": password
        }
        r = requests.post(self.hostname + "/authentication/login", headers=headers, data=json.dumps(payload))
        if r.status_code == 200:
            print("Login successful: ")
            print("Token stored for further reference")
            print(r.headers["Set-Cookie"])
            self.cached_token = r.json()["accessToken"]
        return r

    def auth_login_as_human(self, captcha_token):
        headers = {
            "X-Captcha-Token": captcha_token
        }
        r = requests.post(self.hostname + "/authentication/loginAsHuman", headers=headers)
        if r.status_code == 200:
            print ("foo: " + str(r.headers))
            print("Login as Human successful: ")
            print("Token stored for further reference")
            print(r.headers["Set-Cookie"])
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
        r = requests.put(self.hostname + "/profile", headers=headers, data=json.loads(payload))
        return r

    def auth_set_validation_status(self, email, validated=True):
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

    # chats

    def get_recommendations(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/recommendations", headers=headers)
        return r

    def get_chats(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/chats", headers=headers)
        return r

    def get_chat(self, chat_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/chats/" + chat_id, headers=headers)
        return r

    def get_messages(self, chat_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        r = requests.get(self.hostname + "/chats/" + chat_id + "/messages", headers=headers)
        return r

    def post_message(self, chat_id, text, author_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        payload = {
            "text": text,
            "authorId": author_id
        }
        r = requests.post(self.hostname + "/chats/" + chat_id + "/messages", headers=headers, data=json.dumps(payload))
        return r

    def post_chat(self, participantIds):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }
        payload = {
            "participantIds": participantIds
        }
        r = requests.post(self.hostname + "/chats", headers=headers, data=json.dumps(payload))
        return r

    def set_read(self, message_id, read):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.cached_token
        }

        payload = {
            "read": read
        }

        res = requests.put(self.hostname + "/messages/" + message_id, headers=headers,
                           data=json.dumps(payload))
        return res
