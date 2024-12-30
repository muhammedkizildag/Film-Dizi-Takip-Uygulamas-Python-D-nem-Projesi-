import customtkinter as cTk
from PIL import Image, ImageDraw


class FilmCard(cTk.CTkFrame):

    def __init__(self, master, filmModel,**kwargs):
        super().__init__(master, width=160, height=240, bg_color="#101014",fg_color="#101014", **kwargs)

        label = cTk.CTkLabel(self, text="", image=self._image(f"./database/pics/{filmModel.picPath}"))
        label.place(x=0, y=0)

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