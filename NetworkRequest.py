import requests


class NetworkRequest:
    code_request_success = 200
    code_too_many_requests = 429
    returned_status_code = 0;

    programExitMsg = "Reddit server has stopped responding to our request."

    def __init__(self, url=0):
        self.url = url

    def get_with_retry(self, max_retry_count=3):
        for num in range(1, max_retry_count):
            if (NetworkRequest.returned_status_code == NetworkRequest.code_request_success):
                return page
                break
            page = NetworkRequest.perform_get_request(self)
        if (NetworkRequest.returned_status_code != NetworkRequest.code_request_success):
            print(NetworkRequest.programExitMsg)
            exit()

    def perform_get_request(self):
        page = requests.get(self.url)
        print("Status retured by server " + str(page.status_code))
        if page.status_code == NetworkRequest.code_request_success:
            NetworkRequest.returned_status_code = page.status_code
            return page
        if page.status_code == NetworkRequest.code_too_many_requests:
            NetworkRequest.returned_status_code = page.status_code

    def check_if_valid_image(self):
        response = requests.head(self.url)
        maintype = response.headers['Content-Type'].split(';')[0].lower()
        if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
            return False
        return True
