import requests
import json


def get_api():
    r = requests.get("http://localhost:8080/api")
    return r


def get_dancers():
    r = requests.get("http://localhost:8080/api/dancers")
    return r


def get_dancer(id):
    r = requests.get("http://localhost:8080/api/dancers/{}".format(id))
    return r


def post_dancer(first_name, last_name, public_name, dance):
    data = {
        "firstName": first_name,
        "lastName": last_name,
        "publicName": public_name,
        "dance": dance
    }
    json_string = json.dumps(data)
    r = requests.post("http://localhost:8080/api/dancers", data=json_string)
    return r
