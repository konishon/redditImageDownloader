import os


class StorageManager:
    def __init__(self, full_directory_path=""):
        self.full_directory_path = full_directory_path

    def createRootStorageDir(self):
        if not os.path.exists(self.full_directory_path):
            os.makedirs(self.full_directory_path)

    def count_files(self):
        files = os.listdir(self.full_directory_path)
        return len(files)


