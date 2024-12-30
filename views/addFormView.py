import tkinter as tk
from io import BytesIO

import customtkinter as cTk
from PIL import Image
import threading
from services.database import Database
from services.request import SearchData, FetchData


class AddFormView(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=960, height=500, bg_color="#101014", fg_color="#101014", **kwargs)

        font = ("Roboto", 16)
        self.nameVariable = tk.StringVar()
        self.typeVariable = cTk.StringVar(value="Film")
        self.stateVariable = cTk.StringVar(value="İzlendi")
        self.directorVariable = cTk.StringVar()
        self.yearVariable = cTk.StringVar()
        self.pointVariable = cTk.IntVar(value=0)

        self.posterBytesIO = BytesIO()

        nameLabel = cTk.CTkLabel(self,text="Ad" ,height=40, text_color="white", font=font)
        nameLabel.place(x=10, y=0)
        nameEntry = nameEntryFrame(self)
        nameEntry.place(x=10, y=40)

        typeLabel = cTk.CTkLabel(self, text="Tür", height=40, text_color="white", font=font)
        typeLabel.place(x=10, y=100)
        typeSegmentedButton = cTk.CTkSegmentedButton(self, height=40, values=["Film", "Dizi"], variable=self.typeVariable,fg_color="#101014", font=font, selected_color="#343437", unselected_color="#101014", unselected_hover_color="#343437", selected_hover_color="#343437")
        typeSegmentedButton.place(x=10, y=140)

        stateLabel = cTk.CTkLabel(self, text="Durum", height=40, text_color="white", font=font)
        stateLabel.place(x= 120, y=100)
        stateSegmentedButton = cTk.CTkSegmentedButton(self, height=40, values=["İzlendi", "İzleniyor", "İzlenecek"], variable=self.stateVariable,fg_color="#101014", font=font, selected_color="#343437", unselected_color="#101014", unselected_hover_color="#343437", selected_hover_color="#343437")
        stateSegmentedButton.place(x=120, y=140)

        directorLabel = cTk.CTkLabel(self, text="Yönetmen", height=40, text_color="white", font=font)
        directorLabel.place(x=10, y=200)
        self.directorEntry = cTk.CTkEntry(self, height=40, width=250, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.directorVariable)
        self.directorEntry.place(x=10, y=240)

        yearLabel = cTk.CTkLabel(self, text="Yıl", height=40, text_color="white", font=font)
        yearLabel.place(x=10, y=300)
        self.yearEntry = cTk.CTkEntry(self, height=40, width=60, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.yearVariable)
        self.yearEntry.place(x=10, y=340)

        self.PointFrame = StarPointFrame(self)
        self.PointFrame.place(x=700, y=0)

        self.posterLabel = cTk.CTkLabel(self, text="", width=160, height=240, corner_radius=6, text_color="white")
        self.posterLabel.place(x=700, y=100)

        self.saveButton = cTk.CTkButton(self, text="Kaydet", width=90, height=40, fg_color="#101014", command= self.save, border_color="red", hover_color="red", border_width=2)
        self.saveButton.place(x=730, y=380)
        nameEntry.lift()

    def save(self):
        x = False

        name = self.nameVariable.get()
        year = self.yearVariable.get()
        type = self.typeVariable.get()
        director = self.directorVariable.get()
        state = self.stateVariable.get()
        point = self.pointVariable.get()

        if name == "":
            self.children["!nameentryframe"].children["!ctkentry"].configure(border_color="red")
            x = True
        if year == "":
            self.yearEntry.configure(border_color="red")
            x = True

        if director == "":
            self.directorEntry.configure(border_color="red")
            x = True

        if point == 0:
             self.PointFrame.configure(border_color="red")

        if not x:
            Database().save(name=name, year=year, type=type, director=director, state=state, point=point, pic=self.posterBytesIO)


class nameEntryFrame(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=300, height=40, fg_color="#101014", **kwargs)
        self.nameToggleVariable = cTk.StringVar(value="on")
        self.master.nameVariable.trace("w", self.showSearchDataThread)

        self.nameEntry = cTk.CTkEntry(self, width=250, height=40, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.master.nameVariable)
        self.nameEntry.place(x=0, y=0)

        self.nameToggle = cTk.CTkSwitch(self, text="", variable=self.nameToggleVariable, onvalue="on", offvalue="off", command=self.toggleEvent)
        self.nameToggle.place(x= 250, y=10)

        self.searchFrame = cTk.CTkFrame(self, width=300, height=100, bg_color="transparent", fg_color="white", corner_radius=6)
        self.searchFrame.place(x=0, y=50)

    def showSearchData(self, *args):
        if self.nameToggleVariable.get() == "on":
            text = self.master.nameVariable.get()
            if text != "":
                y = 10
                data = SearchData(query=text)
                if text == self.master.nameVariable.get():
                    for e in data.results:
                        item = cTk.CTkFrame(self.searchFrame, height=54, width=298, fg_color="white", cursor="hand2")
                        item.place(x=0, y=y)

                        img = Image.open(e["Pic"])
                        img.resize((36, 54))

                        itemImg = cTk.CTkLabel(item, width=36, height=54 ,text="",image=cTk.CTkImage(img, size=(36, 54)), cursor="hand2")
                        itemImg.place(x=0, y=0)
                        nameLabel = cTk.CTkLabel(item, height=54, width=250,text=e["Name"], bg_color="white", text_color="black", cursor="hand2")
                        nameLabel.place(x=40, y=0)
                        y += 54

                        item.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))
                        itemImg.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))
                        nameLabel.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))




                    self.searchFrame.configure(height=y)
                    self.configure(height=y+50)

            else:
                self.searchFrame.configure(height=0)
                self.configure(height=40)

    def showSearchDataThread(self, *args):
        threading.Thread(target=self.showSearchData, daemon=True).start()

    def getData(self, URL, _type):
        data = FetchData(URL)

        self.master.nameVariable.set(data.result["name"])
        self.master.typeVariable.set(_type)
        self.master.directorVariable.set(data.result["director"])
        self.master.yearVariable.set(data.result["year"])

        _image = Image.open(data.pic)
        _image.resize((160, 240))

        self.master.posterBytesIO = data.pic
        self.master.posterLabel.configure(image= cTk.CTkImage(_image, size=(160, 240)))
        self.nameToggleVariable.set("off")
        self.searchFrame.configure(height=0)
        self.configure(height=40)

    def toggleEvent(self):
        if self.nameToggleVariable.get() == "off":
            self.searchFrame.configure(height=0)
            self.configure(height=40)
        else:
            self.showSearchDataThread()


class StarPointFrame(cTk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master, height=25, width=125, fg_color="transparent")

        self.starImgOutlined = cTk.CTkImage(Image.open("./database/pics/star-outlined.png"), size=(20,20))
        self.starImg = cTk.CTkImage(Image.open("./database/pics/star.png"), size=(20, 20))

        self.starLabels = [cTk.CTkLabel(self, image=self.starImgOutlined, width=20, height=20, text="", cursor="hand2") for x in range(5)]

        for index, item in enumerate(self.starLabels):
            item.place(y=0, x=index*25)
            item.bind("<Enter>", lambda e, _index=index: self.enterEvent(_index))
            item.bind("<Leave>", self.leaveEvent)
            item.bind("<Button-1>", lambda e, _index=index: self.clickEvent(_index))

    def enterEvent(self, index):

        for e in self.starLabels[:index+1]:
            e.configure(image=self.starImg)

    def leaveEvent(self, *args):
        for e in self.starLabels[self.master.pointVariable.get():]:
            e.configure(image=self.starImgOutlined)


    def clickEvent(self, index):
        self.master.pointVariable.set(index+1)

        for e in self.starLabels[:index+1]:
            e.configure(image=self.starImg)

        for e in self.starLabels[self.master.pointVariable.get():]:
            e.configure(image=self.starImgOutlined)


