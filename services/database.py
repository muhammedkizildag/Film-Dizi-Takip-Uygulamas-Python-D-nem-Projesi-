import json

from models.filmModel import FilmModel


class Database():

    def __init__(self):
        with open("./database/database.json", "r") as f:
            self._data = json.load(f)

        self.list = [FilmModel(id=k, name=v["name"], year=v["year"], type=v["type"], director=v["director"], state=v["state"], picPath=v["picPath"],point=v["point"]) for k, v in self._data.items()]





