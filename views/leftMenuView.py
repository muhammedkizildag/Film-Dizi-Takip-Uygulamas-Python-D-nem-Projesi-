import customtkinter
from tkinter import ttk
import customtkinter as cTk

from state import mainFrameState
from views.addFormView import AddFormView
from views.filmListView import FilmListView
from views.style import font



class LeftMenuView(cTk.CTkFrame):



    def __init__(self, master ,  **kwargs):
        super().__init__(master, **kwargs, bg_color="#101014", fg_color="#101014")

        self.homePageButton = cTk.CTkButton(self,text="Anasayfa" , width=180, height=48, corner_radius=6, bg_color="#101014", fg_color="#343437", font=font, hover_color="#343437", command= lambda : self.updateState(FilmListView, self.homePageButton))
        self.homePageButton.configure(cursor="hand2")
        self.homePageButton.configure()
        self.homePageButton.place(x=10, y=10)


        self.watchedPageButton = cTk.CTkButton(self,text="İzlediklerim" , width=180, height=48, corner_radius=6, bg_color="#101014", fg_color="#101014", font=font, hover_color="#343437", command= lambda : self.updateState(AddFormView, self.watchedPageButton))
        self.watchedPageButton.configure(cursor="hand2")
        self.watchedPageButton.place(x=10, y=68)

    def updateState(self, newView, w):
        for e in self.master.children["!ctkframe"].winfo_children():
            e.destroy()

        newView(self.master.children["!ctkframe"]).place(x=0, y=0)

        for e in self.children:
            if e != "!ctkcanvas":
                self.children[e].configure(fg_color="#101014")

        w.configure(fg_color="#343437")



                









