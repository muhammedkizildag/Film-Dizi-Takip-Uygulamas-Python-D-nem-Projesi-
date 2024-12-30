import customtkinter as cTk
from views.filmListView import FilmListView
from views.leftMenuView import LeftMenuView
from views.topMenuView import TopMenuView

root = cTk.CTk()
root.geometry("1200x625")
root.config(bg="#101014")
root.resizable(width=False, height=False)

topMenu = TopMenuView(root, width=1200, height=120)
topMenu.place(x=0, y=0)

leftMenuView = LeftMenuView(root, width=240, height=900)
leftMenuView.place(x=0, y=120)

mainFrameView = cTk.CTkFrame(root, width=960, height=500, bg_color="#101014", fg_color="#101014")
mainFrameView.place(x=240, y=120)

filmListView = FilmListView(mainFrameView)
filmListView.place(x=0, y=0)


root.mainloop()
