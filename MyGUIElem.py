import tkinter as tk

from PIL import ImageTk, Image
import PIL

import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class MyButton(tk.Button):

    def __init__(self, *args, **kwargs):
        tk.Button.__init__(self, *args, **kwargs)
        self.bind("<Enter>", self.changeBGEnter)
        self.bind("<Leave>", self.changeBGLeave)
        self.configure(fg="black",borderwidth=6, height=1, width=15, font="Helvetica 20 bold",cursor="hand1")

    def changeBGEnter(self, event):
        self.config(background="orange2")

    def changeBGLeave(self, event):
        self.config(background="SystemButtonFace")




class MyLabel(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(height=3, width=20, font="Helvetica 20 bold",background='LightYellow2')

class MyLabelListElem(tk.Label):
    listElem=[]
    choiceElem=None
    textElem="Emma"

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(height=2, width=13, font="Helvetica 15 bold",background='LightYellow2',borderwidth=2, relief="groove",cursor="hand1")

        self.bind("<Button-1>", lambda e: self.changeColor())
        MyLabelListElem.listElem.append(self)

    def setColorBackgroundNoActive(self):
        self.configure(background="LightYellow2")




    def setColoroActive(self):
        self.configure(background="powder blue")
        choiceElem=self


    def changeColor(self):
        self.configure(background="powder blue")
        choiceElem=self
        MyLabelListElem.textElem=self.cget("text")



        for elem in MyLabelListElem.listElem:
            if(elem!=self):
                elem.setColorBackgroundNoActive()

class MyLabelStartRecord(tk.Label):
    listElem = []


    def __init__(self, *args, **kwargs):
            tk.Label.__init__(self, *args, **kwargs)
            self.configure(height=2, width=15, font="Helvetica 15 bold", background='LightYellow2', borderwidth=2,
                           relief="groove")




            MyLabelStartRecord.listElem.append(self)

            MyLabelStartRecord.listElem[0].setColoroDefault()


    def setColorBackgroundNoActive(self):
        self.configure(background="LightYellow2")


    def setColoroDefault(self):
         self.configure(background="red2")

    def setColorEmpty(self):
         self.configure(background="LightYellow2")



    def changeColorToActive(self):
         self.configure(background="green1")






class MyLabelPhoto(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(background='LightYellow2')

    def addPhotoNewRecord(self):
       self.photo = ImageTk.PhotoImage(Image.open(resource_path("img/addNewRecordImage.png")))
       self.configure(image=self.photo)

    def addPhotoRecordSound(self):
        self.photo = ImageTk.PhotoImage(Image.open(resource_path("img/recordSoundImage.png")))
        self.configure(image=self.photo)

    def addPhotoSettingsAndInfo(self):
        self.photo = ImageTk.PhotoImage(Image.open(resource_path("img/settingsAndInfoImage.png")))
        self.configure(image=self.photo)

    def addBackgroundImage(self):
        self.photo = ImageTk.PhotoImage(Image.open(resource_path("img/zs4logo.png")))
        self.configure(image=self.photo)

    def addPhotoExit(self):
        self.photo=ImageTk.PhotoImage(Image.open(resource_path("img/exitImage.png")))
        self.configure(image=self.photo)


class MyLabelReturnMenu(tk.Label):

    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(background='LightYellow2',width=64,height=64,pady=3)
        self.photo=ImageTk.PhotoImage(Image.open(resource_path("img/returnMenuButton.png")))
        self.configure(image=self.photo,cursor="hand1")


class EmptyLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.configure(height=2, width=13, font="Helvetica 15 bold", background='LightYellow2',
                        )




class MyEntry(tk.Entry):
    def __init__(self, *args, **kwargs):
        tk.Entry.__init__(self, *args, **kwargs)
        self.textNewRecord = tk.StringVar()
        self.textNewRecord.set("Default value")
        from tkinter import font
        small_font = font.Font(size=25)
        self.configure(background='LightYellow2', width=19,textvariable=self.textNewRecord,justify='center',font=small_font)


    def checkValidateName(self):
        if (self.textNewRecord.get() == "Default value"):
            return False
        if (len(self.textNewRecord.get()) == 0):
            return False
        import Sounds
        if self.modifyNameRecordToFormat(self.textNewRecord.get()) in Sounds.SOUND_RECORD:
            return False

        return True

    def modifyNameRecordToFormat(self, nameSound):
        changeTextFormat = lambda s: s[:1].upper() + s[1:].lower() if s else ''
        return changeTextFormat(nameSound)

    def getInfoMessageAfterClickAddRecord(self):
        if(self.textNewRecord.get()=="Default value"):
            return "Enter name new record"
        if(len(self.textNewRecord.get())==0):
            return "Enter text"
        import Sounds
        if self.modifyNameRecordToFormat(self.textNewRecord.get()) in Sounds.SOUND_RECORD:
            return "This name record exist"

        return "Add "+self.modifyNameRecordToFormat(self.textNewRecord.get())


    def getNameNewRecord(self):
        return self.textNewRecord



class MyLabelInfo(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)

        from tkinter import font
        small_font = font.Font(size=13)
        self.configure(background='LightYellow2', width=38,height=2,justify='center',font=small_font,fg="red",text="")


    def setErrorMessage(self,errorText):
        self.configure(text=errorText,fg="red")

    def setInfoMessage(self,infoText):
        self.configure(text=infoText,fg="green")





