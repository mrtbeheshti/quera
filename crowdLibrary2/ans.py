import requests
import json


def process(book):
    default_url = "http://127.0.0.1:8000/"
    category = book["category"]
    books = requests.get(default_url + category + "/").json()
    for bk in books:
        if bk["name"] == book["name"]:
            return "bad query"
    requests.post(default_url + category + "/", data=book)
