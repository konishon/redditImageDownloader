from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# http://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib2
from NetworkRequest import NetworkRequest


class DocumentParser:
    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_images_from_reddit(self):
        list_of_images = list()
        potential_image_tags = self.soup.findAll('div')

        for tag in potential_image_tags:
            if tag.parent.get('id') == "siteTable" and tag.has_attr('data-url'):
                image_url = tag['data-url']
                # isValidImage = NetworkRequest().check_if_valid_image(image_url)
                # if isValidImage:
                #     print ("Added "+image_url+" to the list")
                #     list_of_images.append(image_url)

                print("Added " + image_url + " to the list")
                list_of_images.append(image_url)

        return list_of_images
