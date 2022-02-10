import requests
import json


def fetch_data(URL):
    res = requests.get(URL)
    response = json.loads(res.text)
    return response
