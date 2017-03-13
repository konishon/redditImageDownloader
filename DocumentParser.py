from bs4 import BeautifulSoup
import requests


class DocumentParser:
    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_images(self):
        image_list = list()
        for ana in self.soup.findAll('div'):
            if ana.parent.get('id') == "siteTable":
                if ana.has_attr('data-url'):
                     image_list.append(ana['data-url'])

        return image_list
