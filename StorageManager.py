import os


class StorageManager:
    directory = "C:\wallpaper"

    def __init__(self):
        self.createRootStorageDir()

    def createRootStorageDir(self):
        if not os.path.exists(StorageManager.directory):
            os.makedirs(StorageManager.directory)
