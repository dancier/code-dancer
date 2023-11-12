import requests
import json
import config


class RestClient:
    hostname = config.CHAT_DANCER_HOSTNAME

    cached_token = None

    def __init__(self) -> None:
        pass

    def create_chat(self, participant_ids):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "dancerIds": participant_ids
        }
        res = requests.post(self.hostname + "/h/chats", headers=headers, data=json.dumps(payload))
        return res

    def get_chats_by_participant(self, dancer_id):
        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "dancerId": dancer_id
        }
        res = requests.get(self.hostname + "/h/chats", params=params, headers=headers)
        return res

    def post_message(self, chat, text, author):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "text": text,
            "authorId": author
        }

        res = requests.post(self.hostname + "/h/chats/" + chat + "/messages", headers=headers, data=json.dumps(payload))
        return res
