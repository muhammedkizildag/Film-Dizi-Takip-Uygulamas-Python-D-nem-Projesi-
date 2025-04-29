import customtkinter as cTk
from views.filmListView import FilmListView
from views.homePageView import HomePageView


class LeftMenuView(cTk.CTkFrame):
    def __init__(self, master ,  **kwargs):
        super().__init__(master, **kwargs, bg_color="#101014", fg_color="#101014")
        font = ("Roboto", 16)
        self.homePageButton = cTk.CTkButton(self,text="Anasayfa" , width=180, height=48, corner_radius=6, bg_color="#101014", fg_color="#343437", font=font, hover_color="#343437", command= lambda : self.updateState(HomePageView, self.homePageButton))
        self.homePageButton.configure(cursor="hand2")
        self.homePageButton.configure()
        self.homePageButton.place(x=10, y=10)

        self.libraryPageButton = cTk.CTkButton(self,text="Kütüphane" , width=180, height=48, corner_radius=6, bg_color="#101014", fg_color="#101014", font=font, hover_color="#343437", command= lambda : self.updateState(FilmListView, self.libraryPageButton))
        self.libraryPageButton.configure(cursor="hand2")
        self.libraryPageButton.place(x=10, y=68)

    def updateState(self, newView, w):
        for e in self.master.children["!ctkframe"].winfo_children():
            e.destroy()

        newView(self.master.children["!ctkframe"]).place(x=0, y=0)

        for e in self.children:
            if e != "!ctkcanvas":
                self.children[e].configure(fg_color="#101014")

        w.configure(fg_color="#343437")



                
