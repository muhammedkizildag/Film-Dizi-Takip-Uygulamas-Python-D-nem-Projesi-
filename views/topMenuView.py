import tkinter
from tkinter import ttk
import customtkinter as cTk
from PIL import Image


class TopMenuView(cTk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, bg_color="#101014", fg_color="#101014")
        image = Image.open("./database/pics/moovie3.png")
        image = image.resize((100, 100))
        photo = cTk.CTkImage(image, size=(100, 100))
        photo_label = cTk.CTkLabel(self, image=photo, text="")
        photo_label.place(x=56, y=10)

