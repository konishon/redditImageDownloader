import os


class StorageManager:
    directory = os.path.realpath(__file__)
    os = "Hi ! I am OS"

    def __init__(self):
        self.createRootStorageDir()

    def createRootStorageDir(self):
        print("Storage Manager")
        print(StorageManager.directory)
        # if not os.path.exists(StorageManager.directory):
        #     os.makedirs(StorageManager.directory)
