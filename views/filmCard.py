import tkinter

import customtkinter as cTk
from PIL import Image, ImageDraw



class FilmCard(cTk.CTkFrame):

    def __init__(self, master, filmModel,**kwargs):
        super().__init__(master, width=160, height=360, bg_color="#101014",fg_color="#101014", **kwargs)

        font = ("Roboto", 12, "bold")

        imgLabel = cTk.CTkLabel(self, text="", image=self._image(f"./database/pics/{filmModel.picPath}"))
        imgLabel.place(x=0, y=0)

        deleteLabel = cTk.CTkLabel(self,text="", image=cTk.CTkImage(Image.open("./database/pics/deleteicon.png").convert("RGBA"), size=(22, 25)), fg_color="transparent", bg_color="transparent")
        deleteLabel.place(x=10, y=10)

        infoFrame = cTk.CTkFrame(self, width=160, fg_color="transparent")
        infoFrame.place(x=0, y=241)

        nameLabel = cTk.CTkLabel(infoFrame, text=filmModel.name, font=font, text_color="white", wraplength=160, width=160,anchor="center")
        nameLabel.pack(anchor="center")

        directorLabel = cTk.CTkLabel(infoFrame, text=filmModel.director, font=font, text_color="#aaaaaa", height=14, wraplength=160)
        directorLabel.pack(anchor="w")

        yearLabel = cTk.CTkLabel(infoFrame, text=filmModel.year, font=font, text_color="#aaaaaa", height=14)
        yearLabel.pack(anchor="w")







    def _image(self, path):
        width = 160
        heigth = 240
        image = Image.open(path).convert("RGBA")
        image = image.resize((width, heigth))

        mask = Image.new("L", (width, heigth), 0)
        draw = ImageDraw.Draw(mask)

        draw.rounded_rectangle((0, 0, width, heigth), radius=6, fill=255)

        _image = Image.new("RGBA", (width, heigth))
        _image.paste(image, (0, 0), mask=mask)
        return cTk.CTkImage(_image, size=(width, heigth))