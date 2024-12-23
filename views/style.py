from tkinter import ttk
from tkinter.font import Font


font = ("Roboto Medium", 16)


def style():

    style = ttk.Style()
    style.configure("LeftMenu.TFrame", background="red")
    style.configure("LeftMenuButton.TLabel", background="#343437", foreground="#ffffff", anchor="center", justify="center")
