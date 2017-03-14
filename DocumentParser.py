from bs4 import BeautifulSoup
import requests


class DocumentParser:
    def __init__(self, page):
        self.page = page
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

    def get_images_from_reddit(self):
        list_of_images = list()
        potential_image_tags = self.soup.findAll('div')

        for tag in potential_image_tags:

           if tag.parent.get('id') == 'siteTable' and tag.has.attr('data-url'):
                image_url = tag['data-url']
                list_of_images.append(image_url)
        return list_of_images
