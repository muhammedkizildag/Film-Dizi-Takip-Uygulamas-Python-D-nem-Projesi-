import tkinter as tk
import customtkinter as cTk
from PIL import Image
import threading
from services.request import SearchData, FetchData


class AddFormView(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=960, height=500, bg_color="#101014", fg_color="#101014", **kwargs)

        font = ("Roboto", 16)
        self.typeVariable = cTk.StringVar(value="Film")
        self.directorVariable = cTk.StringVar()
        self.yearVariable = cTk.StringVar()

        nameLabel = cTk.CTkLabel(self,text="Ad" ,height=40, text_color="white", font=font)
        nameLabel.place(x=10, y=0)
        nameEntry = nameEntryFrame(self)
        nameEntry.place(x=10, y=40)

        typeLabel = cTk.CTkLabel(self, text="Tür", height=40, text_color="white", font=font)
        typeLabel.place(x=10, y=100)
        typeSegmentedButton = cTk.CTkSegmentedButton(self, height=40, values=["Film", "Dizi"], variable=self.typeVariable,fg_color="#101014", font=font, selected_color="#343437", unselected_color="#101014", unselected_hover_color="#343437", selected_hover_color="#343437")
        typeSegmentedButton.place(x=10, y=140)

        directorLabel = cTk.CTkLabel(self, text="Yönetmen", height=40, text_color="white", font=font)
        directorLabel.place(x=10, y=200)
        directorEntry = cTk.CTkEntry(self, height=40, width=250, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.directorVariable)
        directorEntry.place(x=10, y=240)

        yearLabel = cTk.CTkLabel(self, text="Yıl", height=40, text_color="white", font=font)
        yearLabel.place(x=10, y=300)
        yearEntry = cTk.CTkEntry(self, height=40, width=60, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.yearVariable)
        yearEntry.place(x=10, y=340)

        self.posterLabel = cTk.CTkLabel(self, text="", width=160, height=240, corner_radius=6, text_color="white")
        self.posterLabel.place(x=500, y=0)

        nameEntry.lift()


class nameEntryFrame(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=300, height=40, fg_color="#101014", **kwargs)
        self.nameToggleVariable = cTk.StringVar(value="on")
        self.nameVariable = tk.StringVar()
        self.nameVariable.trace("w", self.showSearchDataThread)

        self.nameEntry = cTk.CTkEntry(self, width=250, height=40, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.nameVariable)
        self.nameEntry.place(x=0, y=0)

        self.nameToggle = cTk.CTkSwitch(self, text="", variable=self.nameToggleVariable, onvalue="on", offvalue="off",)
        self.nameToggle.place(x= 250, y=10)

        self.searchFrame = cTk.CTkFrame(self, width=250, height=100, bg_color="white", fg_color="white")
        self.searchFrame.place(x=0, y=50)

    def showSearchData(self, *args):
        if self.nameToggleVariable.get() == "on":
            text = self.nameVariable.get()
            if text != "":
                y = 10
                data = SearchData(query=text)
                if text == self.nameVariable.get():
                    for e in data.results:
                        item = cTk.CTkFrame(self.searchFrame, height=54, width=250, fg_color="white")
                        item.place(x=0, y=y)

                        img = Image.open(e["Pic"])
                        img.resize((36, 54))

                        itemImg = cTk.CTkLabel(item, width=36, height=54 ,text="",image=cTk.CTkImage(img, size=(36, 54)))
                        itemImg.place(x=0, y=0)
                        nameLabel = cTk.CTkLabel(item, height=54, width=210,text=e["Name"], bg_color="white", text_color="black")
                        nameLabel.place(x=40, y=0)
                        y += 54

                        print(e)
                        item.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))
                        itemImg.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))
                        nameLabel.bind("<Button-1>", lambda event, URL=e["URL"], _type=e["Type"]: self.getData(URL, _type))


                    self.searchFrame.configure(height=y)
                    self.configure(height=y+90)

            else:
                self.searchFrame.configure(height=0)
                self.configure(height=40)

    def showSearchDataThread(self, *args):
        threading.Thread(target=self.showSearchData, daemon=True).start()

    def getData(self, URL, _type):
        print(URL)
        data = FetchData(URL)

        self.nameVariable.set(data.result["name"])
        self.master.typeVariable.set(_type)
        self.master.directorVariable.set(data.result["director"])
        self.master.yearVariable.set(data.result["year"])

        _image = Image.open(data.pic)
        _image.resize((160, 240))

        self.master.posterLabel.configure(image= cTk.CTkImage(_image, size=(160, 240)))
        self.nameToggleVariable.set("off")
        self.searchFrame.configure(height=0)
        self.configure(height=40)


