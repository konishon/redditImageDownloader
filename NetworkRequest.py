import requests
import os
import urllib.request


class NetworkRequest:
    code_request_success = 200
    code_too_many_requests = 429
    returned_status_code = 0;

    programExitMsg = "Reddit server has stopped responding to our request."

    def get_with_retry(self, max_retry_count=3, url=""):
        for num in range(1, max_retry_count):
            if (NetworkRequest.returned_status_code == NetworkRequest.code_request_success):
                return page
                break
            page = NetworkRequest.perform_get_request(self, url)
        if (NetworkRequest.returned_status_code != NetworkRequest.code_request_success):
            print(NetworkRequest.programExitMsg)
            exit()

    def perform_get_request(self, url):
        page = requests.get(url)
        print("Status retured by server " + str(page.status_code))
        if page.status_code == NetworkRequest.code_request_success:
            NetworkRequest.returned_status_code = page.status_code
            return page
        if page.status_code == NetworkRequest.code_too_many_requests:
            NetworkRequest.returned_status_code = page.status_code

    def check_if_valid_image(self, url=""):
        response = requests.head(url)
        response_header = response.headers
        if response_header.__contains__('Content-Type'):
            maintype = response.headers['Content-Type'].split(';')[0].lower()
            if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
                return False
            return True
        return False

    def startImageDownload(self, image_url="",full_save_path=""):
        filename = "wallpaper"
        filenameAndHeader = urllib.request.urlretrieve(image_url, full_save_path + filename)
        header = filenameAndHeader[1]
        content_type = header['Content-Type']
        content_type_split = str.split(content_type, "/")
        file_format = "." + content_type_split[1]
        os.rename(full_save_path + filename, full_save_path + filename + file_format)
