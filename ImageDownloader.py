import urllib.request


class ImageDownloader:
    def __init__(self, image_path="", download_url=""):
        self.download_url = download_url
        self.image_path = image_path



    def imageDownloader(self):
        urllib.request.urlretrieve(self.url, self.image_path)


