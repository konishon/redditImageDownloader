import urllib.request


class ImageDownloader:
    directory = "C:\wallpaper"

    def __init__(self, download_url=""):
        self.download_url = download_url

    def imageDownloader(self):
        urllib.request.urlretrieve(self.download_url, ImageDownloader.directory)
