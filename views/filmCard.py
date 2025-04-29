import customtkinter as cTk
from PIL import Image, ImageDraw
from services.database import Database
from views.editFormView import EditFormView


class FilmCard(cTk.CTkFrame):

    def __init__(self, master, filmModel, page, **kwargs):
        super().__init__(master, width=160, height=360, bg_color="#101014",fg_color="#101014", **kwargs)

        font = ("Roboto", 12, "bold")
        self.point = filmModel.point

        self.page = page

        self.images = self._image(f"./database/pics/{filmModel.picPath}")
        self.imgLabel = cTk.CTkLabel(self, text="", image=self.images[0])
        self.imgLabel.place(x=0, y=0)

        self.imgLabel.bind("<Enter>", self.enterEvent)
        self.imgLabel.bind("<Leave>", self.leaveEvent)
        self.imgLabel.bind("<Motion>", self.motionEvent)
        self.imgLabel.bind("<Button-1>", lambda e: self.clickEvent(event=e, filmModel=filmModel))

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

        _image_ = _image.copy()

        deleteIcon = Image.open("./database/pics/deleteicon.png").convert("RGBA").resize((22, 25))
        _image_.paste(deleteIcon, (10, 200), deleteIcon)

        stars = self.stars()
        _image_.paste(stars, (10, 10), stars)

        editIcon = Image.open("./database/pics/editicon.png").resize((30, 30))
        _image_.paste(editIcon, (125, 200), editIcon)

        imageList = [cTk.CTkImage(_image, size=(width, heigth)), cTk.CTkImage(_image_, size=(width, heigth))]

        return imageList


    def stars(self):
        star = Image.open("./database/pics/star.png").resize((20, 20))
        starOutlined = Image.open("./database/pics/star-outlined.png").resize((20, 20))

        img = Image.new("RGBA", (125, 20))
        for i in range(self.point):
            e = i
            img.paste(star, (25*e, 0), star)
        for i in range(5-self.point):
            e = i
            img.paste(starOutlined, (25*e + self.point*25, 0), starOutlined)

        return img


    def enterEvent(self, *args):
        self.imgLabel.configure(image=self.images[1])

    def leaveEvent(self, *args):
        self.imgLabel.configure(image=self.images[0])


    def motionEvent(self, event):
        if (10 <= event.x <= 45) and (250 <= event.y <= 285):
            self.imgLabel.configure(cursor="hand2")

        elif (155 <= event.x <= 190) and (250 <= event.y <= 285):
            self.imgLabel.configure(cursor="hand2")

        else:
            self.imgLabel.configure(cursor="arrow")


    def clickEvent(self, event, filmModel):
        if (155 <= event.x <= 190) and (250 <= event.y <= 285):
            if self.page == "list":
                for e in self.master.master.master.master.master.children["!ctkframe"].winfo_children():
                    e.destroy()

                EditFormView(self.master.master.master.master.master.children["!ctkframe"], filmModel).place(x=0, y=0)
            elif self.page == "":
                for e in self.master.master.master.master.master.master.master.master.children["!ctkframe"].winfo_children():
                    e.destroy()

                EditFormView(self.master.master.master.master.master.master.master.master.children["!ctkframe"], filmModel).place(x=0, y=0)


        elif (10 <= event.x <= 45) and (250 <= event.y <= 285):
            self.deleteMenu = cTk.CTkFrame(self, width=160, height=240, fg_color="#222222", corner_radius=6)
            self.deleteMenu.place(x=0, y=0)

            btn1 = cTk.CTkButton(self.deleteMenu, width=80, height=40, text="Sil",fg_color="black", hover_color="black", command=lambda: self.delete(filmModel.id))
            btn2 = cTk.CTkButton(self.deleteMenu, width=80, height=40, text="Vazgeç",fg_color="black", hover_color="black",command=lambda: self.deleteMenu.destroy())

            btn1.place(y=75, x=40)
            btn2.place(y=125, x=40)


    def delete(self, id):
        from views.filmListView import FilmListView
        from views.homePageView import HomePageView

        Database().delete(id)

        frame = self.winfo_toplevel().children["!ctkframe"]

        for e in frame.winfo_children():
            try:
                e.destroy()
            except:
                continue

        if self.page == "list":
            FilmListView(frame).place(x=0, y=0)

        else:
            HomePageView(frame).place(x=0, y=0)




