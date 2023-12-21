import requests
import json
import config


class RestClient:
    hostname = config.CHAT_DANCER_HOSTNAME

    cached_token = None

    def __init__(self) -> None:
        pass

    def get_chat_by_id(self, id):
        headers = {
            "Content-Type": "application/json"
        }
        res = requests.get(self.hostname + "/chats/" + id, headers=headers)
        return res

    def get_chats_by_participant(self, participant_id):
        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "participantId": participant_id
        }
        res = requests.get(self.hostname + "/chats", params=params, headers=headers)
        return res

    def create_chat(self, participant_ids):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "participantIds": participant_ids
        }
        res = requests.post(self.hostname + "/chats", headers=headers, data=json.dumps(payload))
        return res

    def post_message(self, chat, text, author):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "authorId": author
        }

        res = requests.post(self.hostname + "/chats/" + chat + "/messages", headers=headers, data=json.dumps(payload))
        return res

    def get_messages(self, chat_id):
        headers = {
            "Content-Type": "application/json"
        }
        res = requests.get(self.hostname + "/chats/" + chat_id + "/messages", headers=headers)
        return res

    def set_read(self, message_id, participant_id, read):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "read": True
        }

        res = requests.put(self.hostname + "/messages/" + message_id + "/read-by/" + participant_id, headers=headers, data=json.dumps(payload))
        return res
