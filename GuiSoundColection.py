import tkinter as tk
import MyGUIElem as mg
import Sounds
import os

from PIL import Image
from PIL import ImageTk, Image
import MyGUIFrame as myFrame
import tkinter, sys
from tkinter import *
import tkinter.messagebox as messagebox


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.createWidget()
        self.configure(background='LightYellow2')


    def createWidget(self):
        self.readOptionToRecordFromFile()
        self.clearGraphicInterface()

        self.descriptionApp = mg.MyLabel(self,text="Emma Sound Collections \n")


        self.imageRecordSound = mg.MyLabelPhoto(self, height=64, width=64)
        self.imageRecordSound.addPhotoRecordSound()
        self.recordSoundButton = mg.MyButton(self, text="Record sound",
                                             command=self.setFrameRecordSound)


        self.imageAddNewRecord=mg.MyLabelPhoto(self,height=64,width=64)
        self.imageAddNewRecord.addPhotoNewRecord()
        self.addNewRecordButton = mg.MyButton(self, text="Add new record",command=self.setFrameAddNewRecord )


        self.imageSettingsAndInfo = mg.MyLabelPhoto(self, height=64, width=64)
        self.imageSettingsAndInfo.addPhotoSettingsAndInfo()
        self.settingsAndInfoButton = mg.MyButton(self, text="Settings & info")

        self.exitFromPrograme = mg.MyLabelPhoto(self, height=64, width=64)
        self.exitFromPrograme.addPhotoExit()
        self.exitFromPgrogramButton = mg.MyButton(self, text="Exit",command=root.destroy)



        self.descriptionApp.grid(row=1, columnspan=3)

        self.imageRecordSound.grid(row=2, column=0, padx=20, pady=20)
        self.recordSoundButton.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        self.imageAddNewRecord.grid(row=3, column=0)
        self.addNewRecordButton.grid(row=3,column=2,columnspan=2,padx=20,pady=20)

        self.imageSettingsAndInfo.grid(row=4, column=0)
        self.settingsAndInfoButton.grid(row=4, column=1, columnspan=2, padx=20, pady=20)

        self.exitFromPrograme.grid(row=5,column=0)
        self.exitFromPgrogramButton.grid(row=5,column=1,columnspan=2, padx=20, pady=20)

        try:
            self.backgroundPhoto == None


        except AttributeError:
            self.backgroundPhoto = mg.MyLabelPhoto()
            self.backgroundPhoto.addBackgroundImage()
            self.backgroundPhoto.pack(pady=20,side="bottom",anchor="center")




    def setFrameRecordSound(self):
        self.clearGraphicInterface()
        self.createWidgetTwoPart()

    def setFrameAddNewRecord(self):
        self.clearGraphicInterface()
        self.createWidgetAddNewRecord()



    def readOptionToRecordFromFile(self):
        records=open(resource_path("records.txt"),"r",encoding="utf-8")
        Sounds.SOUND_RECORD.clear()
        line = records.readline()

        while line:
            line = line.replace('\n','')
            Sounds.SOUND_RECORD[line]=Sounds.Sound(line)
            line = records.readline()

        records.close()



    def createWidgetTwoPart(self):
        from tkinter import font

        self.recordSoundText = mg.MyLabel(self, text="Record Sound \n",anchor='w')
        self.recordSoundText.grid(column=1,row=0,columnspan=10)

        self.returnMenulLabel=mg.MyLabelReturnMenu(self)
        self.returnMenulLabel.grid(column=0,row=0,sticky='wn',padx=10,pady=5)
        self.returnMenulLabel.bind("<Button-1>",lambda x:( self.createWidget()))



        mg.MyLabelListElem.listElem=[]
        mg.MyLabelListElem.choiceElem=[]
        mg.MyLabelStartRecord.listElem=[]






        row=1
        column=0
        self.recordElem=[]



       # self.soundEmma=mg.MyLabelListElem(self,text="Emma")
       # self.soundEmma.grid(row=1,column=0,padx=3,pady=2)
       # self.soundEmma.setColoroActive()

        self.recordElem.append(mg.MyLabelListElem(self,text="Emma"))
        self.recordElem[0].grid(row=1,column=0,padx=3)
        self.recordElem[0].setColoroActive()

        index=1
        for key, value in Sounds.SOUND_RECORD.items():

            if(key!="Emma"):

                if(column<7):
                    column+=1

                else:
                    column=0
                    row+=1


                self.recordElem.append( mg.MyLabelListElem(self, text=key))
                self.recordElem[index].grid(row=row, column=column,padx=3,pady=2)
                index += 1


       # self.soundPogoda = mg.MyLabelListElem(self, text="Pogoda")
       # self.soundPogoda.grid(row=2, column=0,padx=3,pady=2)

        self.offRecordInfo = mg.MyLabelStartRecord(self, text="Off")
        self.offRecordInfo.grid(row=(row+1), column=3, columnspan=3, pady=20,sticky="w")

        self.onRecordInfo = mg.MyLabelStartRecord(self, text="On")
        self.onRecordInfo.grid(row=(row+1), column=4, columnspan=3, pady=20,sticky="w")

        small_font = font.Font(size=25)  #
        self.recordButton = mg.MyButton(self, text="Recording")
        self.recordButton.configure(width=20)
        self.recordButton.bind("<ButtonRelease-1>", lambda e: self.recording())
        self.recordButton.grid(row=(row+2), column=3, columnspan=3, pady=10,sticky="w")



    def setRecordColor(self):
        self.offRecordInfo.setColorEmpty()
        self.onRecordInfo.changeColorToActive()

        Tk.update(self)


    def setNoRecordColor(self):
        self.onRecordInfo.setColorEmpty()
        self.offRecordInfo.setColoroDefault()

        Tk.update(self)



    def recording(self):
        self.setRecordColor()

        sounde = Sounds.SOUND_RECORD[mg.MyLabelListElem.textElem]
        sounde.addNewRecord()
       # print(sounde)
        self.setNoRecordColor()


    def createWidgetAddNewRecord(self):

        self.addNewRecordText = mg.MyLabel(self, text="Add new record \n", anchor='w')
        self.addNewRecordText.grid(column=1, row=0, columnspan=10)
        self.empty=mg.EmptyLabel(self)
        self.empty.grid(column=0,row=5,padx=3)

        self.empty2 = mg.EmptyLabel(self)
        self.empty2.grid(column=1, row=5,padx=3)

        self.empty3 = mg.EmptyLabel(self)
        self.empty3.grid(column=2, row=5,padx=3)

        self.empty4 = mg.EmptyLabel(self)
        self.empty4.grid(column=3, row=5,padx=3)

        self.empty5 = mg.EmptyLabel(self)
        self.empty5.grid(column=4, row=5,padx=3)

        self.empty6 = mg.EmptyLabel(self)
        self.empty6.grid(column=5, row=5,padx=3)

        self.empty7 = mg.EmptyLabel(self)
        self.empty7.grid(column=6, row=5,padx=3)

        self.empty8 = mg.EmptyLabel(self)
        self.empty8.grid(column=7, row=5,padx=3)

        self.returnMenulLabelOfNewRecord = mg.MyLabelReturnMenu(self)
        self.returnMenulLabelOfNewRecord.grid(column=0, row=0, sticky='wn',padx=10,pady=5)



        self.returnMenulLabelOfNewRecord.bind("<Button-1>", lambda x: (self.createWidget()))

        self.inputNameSound=mg.MyEntry(self)

        self.inputNameSound.grid(column=3,row=2,columnspan=4,padx=10,sticky="w")

        self.infoMessage=mg.MyLabelInfo(self)
        self.infoMessage.grid(column=3,row=3,columnspan=4,sticky="w",padx=10)

        self.addNewRecordText=mg.MyButton(self,text="Add new record",command=self.addNewRecordUntilRecording)
        self.addNewRecordText.grid(column=3,row=4,columnspan=4,padx=10,sticky="w")
        self.addNewRecordText.configure(width=19)


    def modifyNameRecordToFormat(self,nameSound):
        changeTextFormat = lambda s: s[:1].upper() + s[1:].lower() if s else ''
        return changeTextFormat(nameSound)

    def addNewRecordUntilRecording(self):

        if(self.inputNameSound.checkValidateName()):
            self.infoMessage.setInfoMessage(self.inputNameSound.getInfoMessageAfterClickAddRecord())
            self.addNewRecordToFile(self.modifyNameRecordToFormat(self.inputNameSound.get()))
            self.createCatalogStructure(self.modifyNameRecordToFormat(self.inputNameSound.get()))
            self.readOptionToRecordFromFile()

        else:
            self.infoMessage.setErrorMessage(self.inputNameSound.getInfoMessageAfterClickAddRecord())

    def addNewRecordToFile(self,nameNew):

        records = open(resource_path("records.txt"),"a+",encoding="utf-8")
        records.write(nameNew+"\n")
        records.close()

    def createCatalogStructure(self,nameSound):
        os.mkdir(resource_path("StatisticsOfRecordSound\\Sound_"+nameSound))
        self.createConfigurationSound(nameSound)
        self.createFolderWithSampleSound(nameSound)

    def createConfigurationSound(self,nameSound):
        learnSet = open(resource_path("StatisticsOfRecordSound\\Sound_"+nameSound+'\\LearnSet.txt'), 'w+')
        testSet = open(resource_path("StatisticsOfRecordSound\\Sound_"+nameSound+'\\TestSet.txt'), 'w+')
        learnSet.write("0"+"\n")
        testSet.write("0"+"\n")
        learnSet.close()
        testSet.close()

    def createFolderWithSampleSound(self,nameSound):
        os.mkdir(resource_path("Record\\Sound" + nameSound))
        os.mkdir(resource_path("Record\\Sound" + nameSound+"\\Learn"))
        os.mkdir(resource_path("Record\\Sound" + nameSound + "\\Test"))




    def sprawdzCzyPoprawnyLoginIWyslijSMS(self):

        if(sl.czyWBazieJestTakiLogin(self.wprowadzLogin.get())==False):
            self.informacjaOPodanieLoginu["text"]="Błedny login"
        else:
            self.informacjaOPodanieLoginu["text"] = "Wysłano SMS"
            sms.wyslijSMS(sl.sprawdzJakiJestNumerTelefonuUsera(self.wprowadzLogin.get()),str(kod.zwrocKodDostepu()))


    def clearGraphicInterface(self):

        for widget in self.winfo_children():
            widget.destroy()











    def wprowadzPodpisMetoda(self):
        from tkinter import filedialog
        self.file_path = filedialog.askopenfilename()



    def wyslijetap2(self):

        import cv2
        import numpy as np
        # img = cv2.imread(self.wprowadzPodpis.get(), cv2.IMREAD_GRAYSCALE)

        img = cv2.imread(self.file_path, cv2.IMREAD_GRAYSCALE)

        img = cv2.resize(img, (60, 15))

        img = img.flatten()


        tab = [img]

        self.imgNumpay = np.array(tab)



        if (TS.sprawdzCzyToAudentycznyPodpis(self.imgNumpay) and GS.sprawdzCzyPodpisAudentyczny(self.imgNumpay)):

            self.czyscInterfejs()

            self.informacjaOAutoryzacji = tk.Label(self, height=3, width=30, font="Helvetica 20 bold")

            self.informacjaOAutoryzacji["text"] = "Udana Autoryzacja \n"
            self.informacjaOAutoryzacji.configure(background='LightYellow2')

            self.informacjaOAutoryzacji.grid(row=0, columnspan=2)

            blokadaNotatnika.x=True
        else:
            self.informacjaOpodanieZdjecia["text"] = "Błędny podpis \n"


    def tworzInterfejsEtap_2(self):

        self.configure(background='LightYellow2')
        self.informacjaOpodanieZdjecia = tk.Label(self, height=3, width=20, font="Helvetica 20 bold")
        self.informacjaOpodanieZdjecia["text"] = "Wprowadź swój podpis \n"
        self.informacjaOpodanieZdjecia.grid(row=0, columnspan=2,padx=20)
        self.informacjaOpodanieZdjecia.configure(background='LightYellow2')
        self.wprowadzPodpis = tk.Button(self, text="Prześlij podpis", fg="black",
                              command=self.wprowadzPodpisMetoda, height=1, width=20, font="Helvetica 20 bold",cursor="hand1")
        self.wprowadzPodpis.bind("<Enter>", self.on_enter3)
        self.wprowadzPodpis.bind("<Leave>", self.on_leave3)
        self.wprowadzPodpis.grid(row=1, column=1,padx=20,pady=20)

        self.zaloguj_2etap = tk.Button(self, text="Zaloguj", fg="black",
                               command=self.wyslijetap2, height=1, width=20, font="Helvetica 20 bold",cursor="hand1")

        self.zaloguj_2etap.bind("<Enter>", self.on_enter4)
        self.zaloguj_2etap.bind("<Leave>", self.on_leave4)

        self.zaloguj_2etap.grid(row=2, column=1,padx=20)
        self.configure(background='LightYellow2')


    def uwierzytelniketap_1(self):
        trescTokenuPodanaPrzezUzytkownika=self.wprowadzToken.get()

        print(kod.zwrocKodDostepu())
        if(trescTokenuPodanaPrzezUzytkownika==str(kod.zwrocKodDostepu())):
           self.czyscInterfejs()
           self.tworzInterfejsEtap_2()




        else:

            self.informacjaOPodanieTokenu["text"]="Błedny kod"




root = tk.Tk()
#root.iconbitmap('C:\\Users\\polsk\\PycharmProjects\\Sound\\img\\micro.ico')
root.title("Emma Sound Record")
root.geometry("1440x750")
root.configure(background='LightYellow2')
root.resizable(False, False)

root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
app = Application(master=root)
app.mainloop()

ss=input("ww")