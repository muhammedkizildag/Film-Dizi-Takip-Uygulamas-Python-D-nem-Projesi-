import random
import customtkinter as cTk
from services.database import Database
from views.filmCard import FilmCard

class HomePageView(cTk.CTkScrollableFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, width=960, height=500, bg_color="#101014", fg_color="#101014", **kwargs)

        frame = cTk.CTkFrame(self, width=960, height=1000, bg_color="#101014", fg_color="#101014")
        frame.pack()
        filmList = Database().list
        watchedList = [e for e in filmList if e.state == "İzlendi"]
        watchingList = [e for e in filmList if e.state == "İzleniyor"]
        willwatchList = [e for e in filmList if e.state == "İzlenecek"]

        font = ("Roboto", 24, "bold")


        if len(watchedList) != 0:
            watchedFrame = cTk.CTkFrame(frame, width=960, height=384, bg_color="#101014", fg_color="#101014")
            watchedFrame.pack()
            watchedLabel = cTk.CTkLabel(watchedFrame, text="İzlediklerim", font=font, width=20, height=24)
            watchedLabel.place(x=0, y=0)
            watchedCardFrame = cTk.CTkFrame(watchedFrame, height=360, width=960, bg_color="#101014", fg_color="#101014")
            watchedCardFrame.place(x=0, y=34)
            length = 4 if len(watchedList) >= 4 else len(watchedList)

            for index, e in enumerate(random.sample(watchedList, length)):
                FilmCard(watchedCardFrame, e, page="").grid(row=0, column=index, padx=25, pady=0)

        if len(watchingList) != 0:
            watchingFrame = cTk.CTkFrame(frame, width=960, height=384, bg_color="#101014", fg_color="#101014")
            watchingFrame.pack()
            watchingLabel = cTk.CTkLabel(watchingFrame, text="İzliyorum", font=font, width=20, height=24)
            watchingLabel.place(x=0, y=0)
            watchingCardFrame = cTk.CTkFrame(watchingFrame, height=360, width=960, bg_color="#101014", fg_color="#101014")
            watchingCardFrame.place(x=0, y=34)
            length = 4 if len(watchingList) >= 4 else len(watchingList)

            for index, e in enumerate(random.sample(watchingList, length)):
                FilmCard(watchingCardFrame, e, page="").grid(row=0, column=index, padx=25, pady=0)

        if len(willwatchList) != 0:
            willwatchFrame = cTk.CTkFrame(frame, width=960, height=384, bg_color="#101014", fg_color="#101014")
            willwatchFrame.pack()
            willwatchLabel = cTk.CTkLabel(willwatchFrame, text="İzleyeceklerim", font=font, width=20, height=24)
            willwatchLabel.place(x=10, y=0)
            willwatchCardFrame = cTk.CTkFrame(willwatchFrame, height=360, width=960, bg_color="#101014", fg_color="#101014")
            willwatchCardFrame.place(x=0, y=34)
            length = 4 if len(willwatchList) >= 4 else len(willwatchList)

            for index, e in enumerate(random.sample(willwatchList, length)):
                FilmCard(willwatchCardFrame, e, page="").grid(row=0, column=index, padx=25, pady=0)





