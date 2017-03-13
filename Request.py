import requests


class Request:
    def __init__(self, url=0):
        self.url = url

    def get_request(self):
        page = requests.get(self.url)
        print(page.status_code)
        if page.status_code == 200:
            return page

