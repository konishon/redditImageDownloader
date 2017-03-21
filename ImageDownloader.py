import os
import urllib.request


class ImageDownloader:
    wallpaper_dir = "\wallpaper\\"
    full_directory = os.getcwd() + wallpaper_dir

    def __init__(self, download_url=""):
        self.download_url = download_url

    def startDownload(self):
        filename = "wallpaper"
        filenameAndHeader = urllib.request.urlretrieve(self.download_url, ImageDownloader.full_directory + filename)
        header = filenameAndHeader[1]
        content_type = header['Content-Type']
        content_type_split = str.split(content_type, "/")
        file_format = "." + content_type_split[1]
        os.rename(ImageDownloader.full_directory + filename, ImageDownloader.full_directory + filename + file_format)
