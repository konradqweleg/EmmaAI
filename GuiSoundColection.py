import tkinter as tk
import MyGUIElem as mg
import PIL
from PIL import ImageTk, Image
import MyGUIFrame as myFrame
import tkinter, sys
from tkinter import *
import tkinter.messagebox as messagebox



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()
        self.createWidget()
        self.configure(background='LightYellow2')


    def createWidget(self):



        self.descriptionApp = mg.MyLabel(self,text="Emma Sound Collections \n")


        self.imageRecordSound = mg.MyLabelPhoto(self, height=64, width=64)
        self.imageRecordSound.addPhotoRecordSound()
        self.recordSoundButton = mg.MyButton(self, text="Record sound",
                                             command=self.setFrameRecordSound)


        self.imageAddNewRecord=mg.MyLabelPhoto(self,height=64,width=64)
        self.imageAddNewRecord.addPhotoNewRecord()
        self.addNewRecordButton = mg.MyButton(self, text="Add new record" )


        self.imageSettingsAndInfo = mg.MyLabelPhoto(self, height=64, width=64)
        self.imageSettingsAndInfo.addPhotoSettingsAndInfo()
        self.settingsAndInfoButton = mg.MyButton(self, text="Settings & info")



        self.descriptionApp.grid(row=1, columnspan=3)

        self.imageRecordSound.grid(row=2, column=0, padx=20, pady=20)
        self.recordSoundButton.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        self.imageAddNewRecord.grid(row=3, column=0)
        self.addNewRecordButton.grid(row=3,column=2,columnspan=2,padx=20,pady=20)

        self.imageSettingsAndInfo.grid(row=4, column=0)
        self.settingsAndInfoButton.grid(row=4, column=1, columnspan=2, padx=20, pady=20)



        self.backgroundPhoto = mg.MyLabelPhoto()
        self.backgroundPhoto.addBackgroundImage()



        self.backgroundPhoto.pack(pady=20)



    def setFrameRecordSound(self):
        self.clearGraphicInterface()
        self.createWidgetTwoPart()



    def createWidgetTwoPart(self):
        from tkinter import font

        self.recordSoundText = mg.MyLabel(self, text="Record Sound \n")
        self.recordSoundText.grid(column=0,row=0,columnspan=3)
        small_font = font.Font(size=25)  #
        self.recordButton = mg.MyButton(self, text="Recording")
        self.recordButton.configure(width=26)
        self.recordButton.grid(row=4,column=0,columnspan=3,pady=10)


        self.on=mg.MyLabelStartRecord(self,text="Off")
        self.on.grid(row=3,column=0)
#        self.on.setColoroActive()

        self.on2 = mg.MyLabelStartRecord(self, text="On")
        self.on2.grid(row=3, column=1)
 #       self.on2.setColoroActive()

        self.opis=mg.MyLabelListElem(self,text="Emma")
        self.opis.grid(row=1,column=0)
        self.opis.setColoroActive()
        self.opisp = mg.MyLabelListElem(self, text="Pogoda")
        self.opisp.grid(row=2, column=0)

        #self.Lb1 = Listbox(self,height=2,width=10,background='LightYellow2',font=small_font)
        #self.buton=mg.MyButton(text="ww")
        #self.Lb1.insert(1, "Emma")
        #self.Lb1.insert(2, "Pogoda")
        #self.Lb1.insert(3, "C")
        #self.Lb1.insert(4, "PHP")
       # self.Lb1.insert(5, "JSP")
        #self.Lb1.insert(6, self.button)

       # self.Lb1.grid(row=1,column=0)


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
root.iconbitmap('C:\\Users\\polsk\\PycharmProjects\\Sound\\img\\micro.ico')
root.title("Emma Sound Record")
root.geometry("500x750")
root.configure(background='LightYellow2')
root.resizable(False, False)
app = Application(master=root)

app.mainloop()

