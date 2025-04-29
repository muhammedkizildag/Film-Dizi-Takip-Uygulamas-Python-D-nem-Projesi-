import customtkinter as cTk
from views.homePageView import HomePageView
from views.leftMenuView import LeftMenuView
from views.topMenuView import TopMenuView


class App(cTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x625")
        self.config(bg="#101014")
        self.resizable(width=False, height=False)
        self.title("MOOVIE")
        self.iconbitmap("./database/pics/moovie3.ico")

        topMenu = TopMenuView(self, width=1200, height=120)
        topMenu.place(x=0, y=0)

        leftMenuView = LeftMenuView(self, width=240, height=900)
        leftMenuView.place(x=0, y=120)

        mainFrameView = cTk.CTkFrame(self, width=960, height=500, bg_color="#101014", fg_color="#101014")
        mainFrameView.place(x=240, y=120)

        filmListView = HomePageView(mainFrameView)
        filmListView.place(x=0, y=0)

        self.mainloop()

App()
