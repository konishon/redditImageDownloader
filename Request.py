import requests


class Request:
    code_request_success = 200
    code_too_many_requests = 429
    programExitMsg = "Reddit server has stopped responding to our request."

    def __init__(self, url=0):
        self.url = url

    def perform_get_request(self):
        page = requests.get(self.url)

        print ("Status retured by server "+str(page.status_code))
        if page.status_code == Request.code_request_success:
            return page
        if page.status_code == Request.code_too_many_requests:
            print(Request.programExitMsg)
            exit
