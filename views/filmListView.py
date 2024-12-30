import customtkinter as cTk
from PIL import Image

from services.database import Database
from views.addFormView import AddFormView
from views.filmCard import FilmCard


class FilmListView(cTk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=960, height=500, bg_color="#101014", fg_color="#101014",**kwargs)

        lastIndex = 0
        columns = 4
        for index, e in enumerate(Database().list):
            row = index // columns
            column = index % columns
            FilmCard(self, filmModel=e).grid(row=row, column=column, padx=25, pady=0)
            lastIndex = index

        lastIndex += 1

        addFilmLabel = cTk.CTkLabel(self, text="", width=160, height=360, cursor="hand2",image=cTk.CTkImage(Image.open("./database/pics/addFilmButton.png"), size=(160, 240)), anchor="n")
        addFilmLabel.grid(row= lastIndex // columns, column=lastIndex % columns, padx=25, pady=0)
        addFilmLabel.bind("<Button-1>", self.updateState)

    def updateState(self, *args):
        for e in self.master.master.master.master.children["!ctkframe"].winfo_children():
            e.destroy()

        AddFormView(self.master.master.master.master.children["!ctkframe"]).place(x=0, y=0)

