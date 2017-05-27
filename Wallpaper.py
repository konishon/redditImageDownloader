import ctypes


class Wallpaper:

    def setWindowsWallpaper(self, image_path):
        SPI_SETDESKWALLPAPER = 20
        print("Setting wallpaper " + image_path)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0x2)
