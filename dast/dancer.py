import requests


def get_api():
    r = requests.get("http://localhost:8080/api")
    return r
