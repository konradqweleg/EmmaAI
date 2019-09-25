import tkinter as tk
import MyGUIElem as mg
import PIL
from PIL import ImageTk, Image
import MyGUIFrame as myFrame




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
        pass

    def sprawdzCzyPoprawnyLoginIWyslijSMS(self):

        if(sl.czyWBazieJestTakiLogin(self.wprowadzLogin.get())==False):
            self.informacjaOPodanieLoginu["text"]="Błedny login"
        else:
            self.informacjaOPodanieLoginu["text"] = "Wysłano SMS"
            sms.wyslijSMS(sl.sprawdzJakiJestNumerTelefonuUsera(self.wprowadzLogin.get()),str(kod.zwrocKodDostepu()))


    def czyscInterfejs(self):
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

