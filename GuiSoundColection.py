import tkinter as tk

import PIL


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.pack()

        self.tworzWidzety_1()
        self.configure(background='LightYellow2')

    def on_enter(self,e):
        self.przyciskWyslijLogin['background'] = 'lavender'


    def on_leave(self,e):
        self.przyciskWyslijLogin['background'] = 'SystemButtonFace'

    def on_enter2(self, e):
        self.uwierzytelnijEtap_1['background'] = 'lavender'

    def on_leave2(self, e):
        self.uwierzytelnijEtap_1['background'] = 'SystemButtonFace'

    def on_enter3(self, e):
        self.wprowadzPodpis['background'] = 'lavender'

    def on_leave3(self, e):
        self.wprowadzPodpis['background'] = 'SystemButtonFace'

    def on_enter4(self, e):
        self.zaloguj_2etap['background'] = 'lavender'

    def on_leave4(self, e):
        self.zaloguj_2etap['background'] = 'SystemButtonFace'

    def tworzWidzety_1(self):

        from PIL import ImageTk, Image
        from PIL import ImageTk, Image
        self.informacjaOPodanieLoginu = tk.Label(self, height=3, width=20, font="Helvetica 20 bold")
        self.informacjaOPodanieLoginu["text"] = "Emma Sound Collections \n"
        self.informacjaOPodanieLoginu.configure(background='LightYellow2')
        self.informacjaOPodanieLoginu.grid(row=1, columnspan=3)

        self.photo = ImageTk.PhotoImage(Image.open("img/klient.png"))
       # self.photo= ImageTk.PhotoImage(image=PIL.Image.fromarray("img/klienty.png"))
        self.b = tk.Label(self, image=self.photo, height=64, width=64)

        self.b.grid(row=2, column=0,padx=20, pady=20)
        self.b.configure(background='LightYellow2')
        self.configure(background='LightYellow2')


      #  self.wprowadzLogin = tk.Entry(self, width=10, justify="center", font="Helvetica 20 bold")

     #   self.wprowadzLogin.grid(row=2, column=1)


        self.przyciskWyslijLogin = tk.Button(self, text="Record sound", fg="black",borderwidth=6,
                             command=self.sprawdzCzyPoprawnyLoginIWyslijSMS, height=1, width=15, font="Helvetica 20 bold",cursor="hand1")
        self.przyciskWyslijLogin.bind("<Enter>", self.on_enter)
        self.przyciskWyslijLogin.bind("<Leave>", self.on_leave)
        self.przyciskWyslijLogin.grid(row=2,column=1,columnspan=2,padx=20, pady=20)



      #  self.informacjaOPodanieTokenu = tk.Label(self,height = 3, width = 20,font = "Helvetica 20 bold")
       # self.informacjaOPodanieTokenu["text"] = "Wprowadź kod dostępu \n"
       # self.informacjaOPodanieTokenu.grid(row=3,columnspan=3)
        #self.informacjaOPodanieTokenu.configure(background='LightYellow2')

        self.photo2 = ImageTk.PhotoImage(file="img/dodaj.png")
        self.b2 = tk.Label(self, image=self.photo2, height=64, width=64)
        self.b2.configure(background='LightYellow2')


        self.b2.grid(row=3, column=0)

        #self.wprowadzToken=tk.Entry(self,width = 10, justify="center",show="*",font = "Helvetica 20 bold")
        #self.wprowadzToken.grid(row=3,column=1)

        self.uwierzytelnijEtap_1 = tk.Button(self, text="Add new record", fg="black",
                             command=self.uwierzytelniketap_1,height = 1, width = 15,font = "Helvetica 20 bold",cursor="hand1",borderwidth=6,)
        self.uwierzytelnijEtap_1.grid(row=3,column=2,columnspan=2,padx=20,pady=20)

        self.uwierzytelnijEtap_1.bind("<Enter>", self.on_enter2)
        self.uwierzytelnijEtap_1.bind("<Leave>", self.on_leave2)

        self.photo3 = ImageTk.PhotoImage(file="img/ustawienia.png")
        self.b3 = tk.Label(self, image=self.photo3, height=64, width=64)
        self.b3.configure(background='LightYellow2')

        self.b3.grid(row=4, column=0)

        self.przyciskWyslijLogin2 = tk.Button(self, text="Settings & info", fg="black", borderwidth=6,
                                             command=self.sprawdzCzyPoprawnyLoginIWyslijSMS, height=1, width=15,
                                             font="Helvetica 20 bold", cursor="hand1")
        self.przyciskWyslijLogin2.bind("<Enter>", self.on_enter)
        self.przyciskWyslijLogin2.bind("<Leave>", self.on_leave)
        self.przyciskWyslijLogin2.grid(row=4, column=1, columnspan=2, padx=20, pady=20)










        path = 'img/sd.png'
        image = Image.open(path)




        photo = ImageTk.PhotoImage(image)

        self.label = tk.Label(image=photo)
        self.label.image = photo
        self.label.configure(background='LightYellow2')
        self.configure(background='LightYellow2')
        #self.label.grid(row=5,columnspan=3)
        self.label.pack(pady=20)



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

