import tkinter as tk
from tkinter import ttk
import customtkinter as cTk
from PIL import Image, ImageTk, ImageDraw

from services.database import Database
from views.filmView import FilmView


class FilmListView(cTk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=960, height=500, bg_color="#101014", fg_color="#101014",**kwargs)

        for e in Database().list:
            FilmView(self, filmModel=e).grid()


    def _image(self, path):
        width = 200
        heigth = 300
        image = Image.open(path).convert("RGBA")
        image = image.resize((width, heigth))

        mask = Image.new("L", (width, heigth), 0)
        draw = ImageDraw.Draw(mask)


        draw.rounded_rectangle((0, 0, width, heigth), radius=6, fill=255)


        _image = Image.new("RGBA", (width, heigth))
        _image.paste(image, (0, 0), mask=mask)

        return ImageTk.PhotoImage(_image)






