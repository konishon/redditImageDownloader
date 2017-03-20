from DocumentParser import DocumentParser
from NetworkRequest import NetworkRequest
from StorageManager import StorageManager

wallpaper = "https://www.reddit.com/r/wallpapers/"
gmb = "https://www.reddit.com/r/gmbwallpapers/"

request = NetworkRequest(wallpaper)
page = request.get_with_retry(3)
parser = DocumentParser(page)
listofImages = parser.get_images_from_reddit()

storageManager = StorageManager()
storageManager.createRootStorageDir()

for index in range(len(listofImages)):
    print('Current Image :', listofImages[index], len(listofImages))

#
# storagemanager = StorageManager
# storagemanager.createRootStorageDir()
#
# #
