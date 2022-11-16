import requests
import json
from tkinter import simpledialog

class CustomRequester:
    """HTTPAPI Requester"""
    def __init__(self, url):
        self.url = url
        

    def get():
        """Website Getter"""
        # ask what website to get
        url = simpledialog.askstring("Website", "Enter Website")
        r = [requests.get(url).headers]
        print(r)
        with open("Return.txt", "w") as f:
            # write to file nicely
            f.writelines(str(r))
        # print the website
        return 0
    def post(self, data):
        r = requests.post(self.url, data=json.dumps(data))
        return r.json()

    def put(self, data):
        r = requests.put(self.url, data=json.dumps(data))
        return r.json()

    def delete(self, data):
        r = requests.delete(self.url, data=json.dumps(data))
        return r.json()

