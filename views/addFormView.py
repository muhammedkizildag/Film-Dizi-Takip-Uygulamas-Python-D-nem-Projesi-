import tkinter as tk
import customtkinter as cTk
from PIL import ImageDraw, Image, ImageTk

from services.request import SearchData


class AddFormView(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=960, height=500, bg_color="#101014", fg_color="#101014", **kwargs)

   
        font = ("Roboto", 16)
        typeVariable = cTk.StringVar(value="Film")


        nameLabel = cTk.CTkLabel(self,text="Ad" ,height=40, text_color="white", font=font)
        nameLabel.place(x=10, y=0)
        nameEntry = nameEntryFrame(self)
        nameEntry.place(x=10, y=40)


        typeLabel = cTk.CTkLabel(self, text="Tür", height=40, text_color="white", font=font)
        typeLabel.place(x=10, y=100)
        typeSegmentedButton = cTk.CTkSegmentedButton(self, height=40, values=["Film", "Dizi"], variable=typeVariable,fg_color="#101014", font=font, selected_color="#343437", unselected_color="#101014", unselected_hover_color="#343437", selected_hover_color="#343437")
        typeSegmentedButton.place(x=10, y=140)
        nameEntry.lift()
        
class nameEntryFrame(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=250, height=40, fg_color="#101014", **kwargs)

        self.entryVariable = tk.StringVar()
        self.entryVariable.trace("w", self.showSearchData)

        self.nameEntry = cTk.CTkEntry(self, width=250, height=40, corner_radius=6, fg_color="#101014", text_color="white", textvariable=self.entryVariable)
        self.nameEntry.place(x=0, y=0)

        self.searchFrame = cTk.CTkFrame(self, width=250, height=100)
        self.searchFrame.place(x=0, y=50)





    def showSearchData(self, *args):
        text = self.entryVariable.get()

        if text != "":
            y = 10
            data = SearchData(query=text)
            for e in data.results:
                item = cTk.CTkLabel(self.searchFrame ,text=e["Name"], height=40, width=250)
                item.place(x=0, y=y)
                y += 40

            self.searchFrame.configure(height=y+40)
            self.configure(height=y+90)

        else:
            self.searchFrame.configure(height=0)
            self.configure(height=40)



