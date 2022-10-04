import requests
import json

class RestClient:

    hostname = "https://test-dancer.dancier.net"

    def __init__(self) -> None:
        pass

    def eventLog(self) :
        headers = {
            "Content-Type": "application/json",
        }

        payload = {
        	"topic": "test123",
	        "metaData" : {"hallo" : "jan"},
	        "payload": {"engles": "schick doch auch mal was"}
        }
        r = requests.post(self.hostname + "/eventlog", headers = headers, data=json.dumps(payload))
        return r