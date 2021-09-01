import requests


def process(url):
    try:
        response = requests.get(url)
    except:
        return "Bad Query"
    books = response.json()
    status = response.status_code
    shell_cat = ""
    if status != 200:
        return "Bad Query"
    if len(books) == 0 or books==Nu:
        return "I can't recognize it"
    else:
        shell_cat = books[0]["category"]
    for book in books:
        if shell_cat != book["category"]:
            return "I can't recognize it"
    return shell_cat
