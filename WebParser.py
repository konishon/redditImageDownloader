import random

from DocumentParser import DocumentParser
from ImageDownloader import ImageDownloader
from Request import Request
import requests

from StorageManager import StorageManager

wallpaper = "https://www.reddit.com/r/wallpapers/"
gmb = "https://www.reddit.com/r/gmbwallpapers/"

request = Request(wallpaper)
page = request.perform_get_request()

parser = DocumentParser(page)
listofImages = parser.get_images_from_reddit()
for index in range(len(listofImages)):
    print('Current Image :', listofImages[index], len(listofImages))

#
# storagemanager = StorageManager
# storagemanager.createRootStorageDir()
#
# #


