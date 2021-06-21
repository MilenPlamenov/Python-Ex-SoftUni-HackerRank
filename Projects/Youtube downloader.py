from tkinter import *
from pytube import YouTube


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(text="Downloaded")


window = Tk()
window.geometry("370x170")
window.title("YouTube downloader")
link = StringVar()


Label(window, text="Enter your link here: ").grid(row=0, column=0)
Entry(window, text="link", width=30, textvariable=link).grid(row=0, column=1)
Button(window, text="Download",
       command=downloader).grid(row=0, column=2)
window.mainloop()