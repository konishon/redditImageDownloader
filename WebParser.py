import os
import random

import re

from DocumentParser import DocumentParser
from ImageDownloader import ImageDownloader
from NetworkRequest import NetworkRequest
from StorageManager import StorageManager

url_wallpaper = "https://www.reddit.com/r/wallpapers/"
url_gmb = "https://www.reddit.com/r/gmbwallpapers/"
default_retry_count = 3
image_pattern = "/\Ahttp.*(jpeg|jpg|gif|png)\Z/"

# network request
request = NetworkRequest()
page = request.get_with_retry(default_retry_count, url_wallpaper)

# # parsing page for images
parser = DocumentParser(page)
listofImages = parser.get_images_from_reddit()

# creating folder for storing image
currentWorkingDir = os.getcwd()
full_directory_path = currentWorkingDir + "\wallpaper\\"
storageManager = StorageManager(full_directory_path)
storageManager.createRootStorageDir()

# # downloading image
selected_image = random.choice(listofImages)
request.startImageDownload(selected_image, full_directory_path)


def print_image_list():
    for index in range(len(listofImages)):
        print('Current Image :', listofImages[index], len(listofImages))
