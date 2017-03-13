from DocumentParser import DocumentParser
from Request import Request
import requests

wallpaper = "https://www.reddit.com/r/wallpapers/"
gmb = "https://www.reddit.com/r/gmbwallpapers/"


request = Request(gmb)
page = request.get_request()

parser = DocumentParser(page)
listofImages = parser.get_images()

for index in range(len(listofImages)):
    print('Current Image :', listofImages[index],len(listofImages))
