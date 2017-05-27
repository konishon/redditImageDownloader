import ctypes

import requests
import os
import urllib.request

from StorageManager import StorageManager
import Wallpaper


class NetworkRequest:
    code_request_success = 200
    code_too_many_requests = 429
    returned_status_code = 0

    programExitMsg = "Reddit server has stopped responding to our request."

    def get_with_retry(self, max_retry_count=3, url=""):
        # todo this needs more work
        attempts = 0
        while True:
            page = NetworkRequest.perform_get_request(self, url)
            if attempts == max_retry_count:
                print(NetworkRequest.programExitMsg)
                break
            elif NetworkRequest.returned_status_code == NetworkRequest.code_request_success:
                print(NetworkRequest.programExitMsg)
                break
        attempts += 1
        return page

    def perform_get_request(self, url):
        page = requests.get(url)
        print("Status retured by server " + str(page.status_code))
        if page.status_code == NetworkRequest.code_request_success:
            NetworkRequest.returned_status_code = page.status_code
            return page
        elif page.status_code == NetworkRequest.code_too_many_requests:
            NetworkRequest.returned_status_code = page.status_code
            exit()
        else:
            exit()

    def check_if_valid_image(self, url=""):
        response = requests.head(url)
        response_header = response.headers
        if response_header.__contains__('Content-Type'):
            maintype = response.headers['Content-Type'].split(';')[0].lower()
            if maintype not in ('image/png', 'image/jpeg', 'image/gif'):
                return False
            return True
        return False

    def startImageDownload(self, image_url="", full_save_path=""):

        print(full_save_path + " full save path")
        filename = self.getImageName(image_url, full_save_path)
        filenameAndHeader = urllib.request.urlretrieve(image_url, full_save_path + filename)

        image_path = NetworkRequest.setFileExtenstion(filenameAndHeader, full_save_path, filename)


        # todo setting wallpaper
        Wallpaper


    def setFileExtenstion(self, filenameAndHeader, full_save_path, filename):

        header = filenameAndHeader[1]
        content_type = header['Content-Type']
        content_type_split = str.split(content_type, "/")
        file_format = "." + content_type_split[1]

        os.rename(full_save_path + filename, full_save_path + filename + file_format)

        return full_save_path + filename + file_format

    def getImageName(self, image_url, full_save_path):
        print("Starting download for " + image_url)
        numberOfPresentWallpapers = StorageManager(full_save_path).count_files()
        filename = "wallpaper_" + str(numberOfPresentWallpapers)
        return filename
