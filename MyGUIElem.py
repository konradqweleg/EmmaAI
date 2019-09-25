import tkinter as tk
from PIL import ImageTk, Image
import PIL

class MyButton(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.bind("<Enter>", self.changeBGEnter)
        self.bind("<Leave>", self.changeBGLeave)
        self.configure(fg="black",borderwidth=6, height=1, width=15, font="Helvetica 20 bold",cursor="hand1")

    def changeBGEnter(self, event):
        self.config(background="lavender")

    def changeBGLeave(self, event):
        self.config(background="SystemButtonFace")


class MyLabel(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(height=3, width=20, font="Helvetica 20 bold",background='LightYellow2')


class MyLabelPhoto(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(background='LightYellow2')

    def addPhotoNewRecord(self):
       self.photo = ImageTk.PhotoImage(Image.open("img/addNewRecordImage.png"))
       self.configure(image=self.photo)

    def addPhotoRecordSound(self):
        self.photo = ImageTk.PhotoImage(Image.open("img/recordSoundImage.png"))
        self.configure(image=self.photo)

    def addPhotoSettingsAndInfo(self):
        self.photo = ImageTk.PhotoImage(Image.open("img/settingsAndInfoImage.png"))
        self.configure(image=self.photo)

    def addBackgroundImage(self):
        self.photo = ImageTk.PhotoImage(Image.open("img/zs4logo.png"))
        self.configure(image=self.photo)




