import tkinter
from tkinter import messagebox

from WebParser import WebParser


class MainGUI:
    webparser = WebParser()

    def __init__(self):
        top = tkinter.Tk()
        B = tkinter.Button(top, text="GET WALLPAPER", padx=50, pady=50, command=MainGUI.webparser.start_task)
        B.pack()
        top.mainloop()

    def showErrorMsg(self, title, msg):
        messagebox.showinfo(title, msg)
