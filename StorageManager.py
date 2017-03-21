import os


class StorageManager:
    wallpaper_dir = "\wallpaper"

    def __init__(self):
        self.createRootStorageDir()

    def createRootStorageDir(self):
        if not os.path.exists(os.getcwd() + StorageManager.wallpaper_dir):
            os.makedirs(os.getcwd() + StorageManager.wallpaper_dir)
