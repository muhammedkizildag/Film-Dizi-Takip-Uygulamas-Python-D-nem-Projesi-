class FilmModel():
    def __init__(self, id, name, year, type, director, state, picPath, note,point=False):
        self.id = int(id)
        self.name = name
        self.year = year
        self.type = type
        self.director = director
        self.state = state
        self.point = point
        self.note = note
        self.picPath = picPath